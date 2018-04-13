#!/usr/bin/env python
import sys
import os
import re
from array import array
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from ROOT import TFile, TCanvas, TH2F, gROOT, Double

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")

(arguments, args) = parser.parse_args()
if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "you forgot to specify a config file with -l"
    sys.exit(1)

if arguments.condorDir:
    output_path = "condor/" + arguments.condorDir + "/"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
else:
    print "you forgot to specify a condor directory with -w"
    sys.exit(1)


def get_yields_and_errors(h, x_bin_lo, x_bin_hi, y_bin_lo, y_bin_hi, variable_bins):
    error = Double(0.0)
    integral = h.IntegralAndError(x_bin_lo, x_bin_hi, y_bin_lo, y_bin_hi, error)
    # multiply by area of last bin if histogram was made with variable-width bins
    # assume input histograms have symmetric binning 
    if variable_bins:
        nBins = h.GetXaxis().GetNbins()
        lastBin = h.GetXaxis().FindBin(nBins)
        area = h.GetXaxis().GetBinWidth(lastBin) ** 2
        integral *= area
        error *= area
    return (integral, error)


gROOT.SetBatch()
x_yields_and_errors = {}
y_yields_and_errors = {}

in_file = TFile(input_file)
x_hist = in_file.Get(hist_x).Clone()
y_hist = in_file.Get(hist_y).Clone()

# get x-axis sideband yields and errors
for edge_low, edge_high in zip(bin_edges_x[:-1], bin_edges_x[1:]):
    x_yields_and_errors[edge_low] = get_yields_and_errors(
                            x_hist,
                            x_hist.GetXaxis().FindBin(edge_low),
                            x_hist.GetXaxis().FindBin(edge_high)-1,
                            0,
                            x_hist.GetYaxis().FindBin(bin_edges_y[1])-1,
                            x_variable_bins )

# get y-axis sideband yields and errors
for edge_low, edge_high in zip(bin_edges_y[:-1], bin_edges_y[1:]):
    y_yields_and_errors[edge_low] = get_yields_and_errors(
                            y_hist,
                            0,
                            y_hist.GetXaxis().FindBin(bin_edges_x[1])-1,
                            y_hist.GetYaxis().FindBin(edge_low),
                            y_hist.GetYaxis().FindBin(edge_high)-1,
                            y_variable_bins )

out_hist = TH2F(out_hist, out_hist,len(bin_edges_x)-1, array('d',bin_edges_x),
                len(bin_edges_y)-1, array('d',bin_edges_y))

# get yield in prompt region
if y_yields_and_errors[bin_edges_y[0]] != x_yields_and_errors[bin_edges_x[0]]:
    print "x and y sideband yields don't match in 'a' (prompt) region"
    print "using x yield in 'a' region, but you should make sure this behavior is expected"
(a_yield, a_error) = x_yields_and_errors[bin_edges_x[0]]

# fill TH2 using abcd method
for x_d0, (x_yield, x_error) in x_yields_and_errors.iteritems():
    for y_d0, (y_yield, y_error) in y_yields_and_errors.iteritems():
        bin_num = out_hist.FindBin(x_d0, y_d0)

        if x_d0 is bin_edges_x[0] and y_d0 is bin_edges_y[0]: # prompt region; use input yield
            yield_temp = a_yield
            error_temp = a_error
        elif y_d0 is bin_edges_y[0]: # x-axis sideband; use input yield
            yield_temp = x_yield
            error_temp = x_error
        elif x_d0 is bin_edges_x[0]: # y-axis sideband; use input yield
            yield_temp = y_yield
            error_temp = y_error
        else: # signal region; use d = c*b/a
            if x_yield == 0 or y_yield == 0:
                yield_temp = 0
                error_temp = 0
            else:
                (cb_yield, cb_error) = propagateError("product", x_yield, x_error, y_yield, y_error)
                (yield_temp, error_temp) = propagateError("quotient", cb_yield, cb_error, a_yield, a_error)

        out_hist.SetBinContent(bin_num, yield_temp)
        out_hist.SetBinError(bin_num, error_temp)

out_file = TFile(output_path + out_file, "recreate")
out_hist.SetOption("colz texte")
out_hist.GetXaxis().SetTitle(x_axis_title)
out_hist.GetYaxis().SetTitle(y_axis_title)
out_hist.SetTitle("")
out_hist.Draw()
out_hist.Write()
out_file.Close()
