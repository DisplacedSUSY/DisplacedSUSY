#!/usr/bin/env python
import sys
import os
import re
import numpy
from optparse import OptionParser
from ROOT import TFile, TCanvas, TGraphAsymmErrors, TMultiGraph, TLegend, Double, gROOT

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

gROOT.SetBatch()

# pick good TColors
colors = [1,2,3,4,6,7,8,9,11,29,33,36,38,40,45,48]
color_ix = 0

def makeEfficiencyHist(in_hist):
    last_bin = in_hist.GetXaxis().GetLast()
    total_error = Double(0.0)
    n_total = in_hist.IntegralAndError(0, last_bin, total_error)

    total_hist = in_hist.Clone()
    pass_hist  = in_hist.Clone()

    for d0_bin in range(0, last_bin+1):
        total_hist.SetBinContent(d0_bin, n_total)
        total_hist.SetBinError(d0_bin, total_error)

        pass_error = Double(0.0)
        n_pass = in_hist.IntegralAndError(d0_bin, last_bin, pass_error)

        # if no events pass d0 cut, use last non-zero value
        if n_pass == 0.0:
            n_pass = last_n_pass
            pass_error = last_pass_error

        last_n_pass = n_pass
        last_pass_error = pass_error

        pass_hist.SetBinContent(d0_bin, n_pass)
        pass_hist.SetBinError(d0_bin, pass_error)

    return TGraphAsymmErrors(pass_hist, total_hist)

def get_yields(x_eff, y_eff):
    last_bin = in_hist.GetXaxis().GetLast()
    total_error = Double(0.0)
    n_total = in_hist.IntegralAndError(0, last_bin, total_error)
    yield_estimation = x_eff * y_eff * total
    return yield_estimation

###############################################################################

x_multigraph = TMultiGraph()
y_multigraph = TMultiGraph()
x_legend = TLegend(0.6, 0.6, 0.8, 0.8)
y_legend = TLegend(0.6, 0.6, 0.8, 0.8)

for x_lo, x_hi in zip(bins_x[:-1], bins_x[1:]):
    in_file = TFile(output_path+sample+".root")
    in_hist = in_file.Get(plot)

    x_bin_lo = in_hist.GetXaxis().FindBin(x_lo)
    x_bin_hi = in_hist.GetXaxis().FindBin(x_hi)-1

    for y_lo, y_hi in zip(bins_y[:-1], bins_y[1:]):
        y_bin_lo = in_hist.GetYaxis().FindBin(y_lo)
        y_bin_hi = in_hist.GetYaxis().FindBin(y_hi)-1

        for sample in samples:
            #in_file = TFile(output_path+sample+".root")
            #in_hist = in_file.Get(plot)

            x_eff_hist = makeEfficiencyHist(in_hist.ProjectionX().Clone())
            y_eff_hist = makeEfficiencyHist(in_hist.ProjectionY().Clone())
            x_eff_hist.SetLineColor(colors[color_ix])
            y_eff_hist.SetLineColor(colors[color_ix])
            color_ix += 1

            total_error = Double(0.0)
            x_eff = x_eff_hist.IntegralAndError(x_lo, x_hi, error)
            y_eff = y_eff_hist.IntegralAndError(y_lo, y_hi, error)

            x_multigraph.Add(x_eff_hist)
            y_multigraph.Add(y_eff_hist)
            x_multigraph.SetTitle(";"+in_hist.GetXaxis().GetTitle()+";Efficiency")
            y_multigraph.SetTitle(";"+in_hist.GetYaxis().GetTitle()+";Efficiency")

            x_legend.AddEntry(x_eff_hist, sample, "elp")

    estimation = get_yields(x_eff, y_eff)

# plot everything and make output file
out_file = TFile(output_path+"nonQcdBgEstimate.root", "recreate")
x_canvas = TCanvas("x", "x", 100, 100, 700, 700)
x_canvas.SetLogy()
x_multigraph.Draw("ap")
x_multigraph.GetXaxis().SetRangeUser(0, 500)
x_multigraph.GetYaxis().SetRangeUser(0.00001, 2)
x_legend.Draw()
x_canvas.Write()
y_canvas = TCanvas("y", "y", 100, 100, 700, 700)
y_canvas.SetLogy()
y_multigraph.Draw("ap")
y_multigraph.GetXaxis().SetRangeUser(0, 500)
y_multigraph.GetYaxis().SetRangeUser(0.00001, 2)
y_legend.Draw()
y_canvas.Write()
