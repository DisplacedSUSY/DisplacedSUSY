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
parser.add_option("-c", "--doClosureTest", action="store_true", dest="doClosureTest",
                  default=False, help="perform closure test; DON'T RUN OVER DATA IF BLINDED!")

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
in_file = TFile(input_file)
in_hist = in_file.Get(input_hist).Clone()
abcd_hist  = TH2F("abcd", "abcd", len(bins_x)-1, array('d',bins_x), len(bins_y)-1, array('d',bins_y) )
count_hist = TH2F("count", "count", len(bins_x)-1, array('d',bins_x), len(bins_y)-1, array('d',bins_y) )
comp_hist  = TH2F("diff", "diff",  len(bins_x)-1, array('d',bins_x), len(bins_y)-1, array('d',bins_y) )

# Get yield and error in prompt region
prompt_bin_x_lo = in_hist.GetXaxis().FindBin(bins_x[0])
prompt_bin_x_hi = in_hist.GetXaxis().FindBin(bins_x[1])-1
prompt_bin_y_lo = in_hist.GetYaxis().FindBin(bins_y[0])
prompt_bin_y_hi = in_hist.GetYaxis().FindBin(bins_y[1])-1

(prompt_yield, prompt_error) = get_yields_and_errors(in_hist, prompt_bin_x_lo, prompt_bin_x_hi,
                                                     prompt_bin_y_lo, prompt_bin_y_hi, variable_bins)

for x_lo, x_hi in zip(bins_x[:-1], bins_x[1:]):
    x_bin_lo = in_hist.GetXaxis().FindBin(x_lo)
    x_bin_hi = in_hist.GetXaxis().FindBin(x_hi)-1

    # Get yield and error in x sideband
    (x_yield, x_error) = get_yields_and_errors(in_hist, x_bin_lo, x_bin_hi, prompt_bin_y_lo,
                                               prompt_bin_y_hi, variable_bins)

    for y_lo, y_hi in zip(bins_y[:-1], bins_y[1:]):
        y_bin_lo = in_hist.GetYaxis().FindBin(y_lo)
        y_bin_hi = in_hist.GetYaxis().FindBin(y_hi)-1
        out_bin = count_hist.FindBin(x_lo, y_lo)

        # Get yield and error in y sideband
        (y_yield, y_error) = get_yields_and_errors(in_hist, prompt_bin_x_lo, prompt_bin_x_hi,
                                                   y_bin_lo, y_bin_hi, variable_bins)

        # calculate abcd yield as d = c * b / a
        if x_yield == 0 or y_yield == 0:
            abcd_yield = 0
            abcd_error = 0
        else:
            (cb_yield, cb_error) = propagateError("product", x_yield, x_error, y_yield, y_error)
            (abcd_yield, abcd_error) = propagateError("quotient", cb_yield, cb_error, prompt_yield, prompt_error)
        abcd_hist.SetBinContent(out_bin, abcd_yield)
        abcd_hist.SetBinError(out_bin, abcd_error)

        # get couting yields in signal region and calculate consistency between abcd and counting
        if arguments.doClosureTest:
            (count_yield, count_error) = get_yields_and_errors(in_hist, x_bin_lo, x_bin_hi,
                                                               y_bin_lo, y_bin_hi, variable_bins)
            count_hist.SetBinContent(out_bin, count_yield)
            count_hist.SetBinError(out_bin, count_error)

            yield_diff = round(abs(abcd_yield - count_yield), 5)
            total_error  = abcd_error + count_error
            consistency = yield_diff / total_error
            comp_hist.SetBinContent(out_bin, consistency)

out_file = TFile(output_path + out_file, "recreate")
count_hist.SetMarkerSize(0.75)
count_hist.SetOption("colz text45 e")
count_hist.GetXaxis().SetTitle(x_axis_title)
count_hist.GetYaxis().SetTitle(y_axis_title)
count_hist.Write()
abcd_hist.SetMarkerSize(0.75)
abcd_hist.SetOption("colz text45 e")
abcd_hist.GetXaxis().SetTitle(x_axis_title)
abcd_hist.GetYaxis().SetTitle(y_axis_title)
abcd_hist.Write()
comp_hist.SetMarkerSize(0.75)
comp_hist.SetOption("colz text45")
comp_hist.GetXaxis().SetTitle(x_axis_title)
comp_hist.GetYaxis().SetTitle(y_axis_title)
comp_hist.Write()
out_file.Close()
