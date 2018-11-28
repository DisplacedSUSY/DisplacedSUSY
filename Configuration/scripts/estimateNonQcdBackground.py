#!/usr/bin/env python
import sys
import os
import re
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from ROOT import TFile, TCanvas, TGraphAsymmErrors, TMultiGraph, TLegend, Double, gROOT, gStyle

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")
parser.add_option("-t", "--makeTables", action="store_true", dest="makeTables",
                  default=False, help="print tables of non-qcd background estimations and direct counting yields; table is formatted for elog")

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
    total_err = Double(0.0)
    n_total = in_hist.IntegralAndError(0, last_bin, total_err)

    total_hist = in_hist.Clone()
    pass_hist  = in_hist.Clone()

    for d0_bin in range(0, last_bin+1):
        total_hist.SetBinContent(d0_bin, n_total)
        total_hist.SetBinError(d0_bin, total_err)

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

###############################################################################

x_multigraph = TMultiGraph()
y_multigraph = TMultiGraph()
x_legend = TLegend(0.6, 0.6, 0.8, 0.8)
y_legend = TLegend(0.6, 0.6, 0.8, 0.8)

for sample in samples:
    in_file = TFile(output_path+sample+".root")
    try:
        in_hist = in_file.Get(plot).Clone()
    except ReferenceError:
        print "Could not find input histogram for", sample
        continue

    # make efficiency plots
    x_eff_hist = makeEfficiencyHist(in_hist.ProjectionX().Clone())
    y_eff_hist = makeEfficiencyHist(in_hist.ProjectionY().Clone())
    x_eff_hist.SetLineColor(colors[color_ix])
    y_eff_hist.SetLineColor(colors[color_ix])
    color_ix += 1

    # add efficiency plots to summary plot for all samples
    x_multigraph.Add(x_eff_hist)
    y_multigraph.Add(y_eff_hist)
    x_multigraph.SetTitle(";"+in_hist.GetXaxis().GetTitle()+";Efficiency")
    y_multigraph.SetTitle(";"+in_hist.GetYaxis().GetTitle()+";Efficiency")
    x_legend.AddEntry(x_eff_hist, sample, "elp")
    y_legend.AddEntry(y_eff_hist, sample, "elp")

    # use efficiencies to estimate background
    last_x_bin = in_hist.GetXaxis().GetLast()
    last_y_bin = in_hist.GetYaxis().GetLast()
    total_err = Double(0.0)
    total_yield = in_hist.IntegralAndError(0, last_x_bin, 0, last_y_bin, total_err)
    if variable_bins:
        total_yield *= in_hist.GetXaxis().GetBinWidth(last_x_bin) ** 2
        total_err *= in_hist.GetXaxis().GetBinWidth(last_x_bin) ** 2

    x_eff_lo = Double(0.0)
    x_eff_hi = Double(0.0)
    y_eff_lo = Double(0.0)
    y_eff_hi = Double(0.0)
    _ = Double(0.0) # dummy variable for GetPoint method

    # start elog table
    if arguments.makeTables:
        print "[B]", sample, "[/B]"
        print '[TABLE border="1"]'
        print "d0 region | Estimate | Direct Counting"

    for lo, hi in closure_test_bins:
        lo_bin = in_hist.GetXaxis().FindBin(lo)
        hi_bin = in_hist.GetXaxis().FindBin(hi)
        x_eff_hist.GetPoint(lo_bin-1, _, x_eff_lo)
        x_eff_hist.GetPoint(hi_bin-1, _, x_eff_hi)
        y_eff_hist.GetPoint(lo_bin-1, _, y_eff_lo)
        y_eff_hist.GetPoint(hi_bin-1, _, y_eff_hi)
        # gloss over asymmetric uncertainty for now for ease of comparison
        x_eff_lo_err = x_eff_hist.GetErrorY(lo_bin)
        x_eff_hi_err = x_eff_hist.GetErrorY(hi_bin)
        y_eff_lo_err = y_eff_hist.GetErrorY(lo_bin)
        y_eff_hi_err = y_eff_hist.GetErrorY(hi_bin)

        (x_eff, x_err) = propagateError("sum", -1*x_eff_hi, x_eff_hi_err, x_eff_lo, x_eff_lo_err)
        (y_eff, y_err) = propagateError("sum", -1*y_eff_hi, y_eff_hi_err, y_eff_lo, y_eff_lo_err)
        (overall_eff, overall_eff_err) = propagateError("product", x_eff, x_err, y_eff, y_err)
        (estimate, estimate_err) = propagateError("product", overall_eff, overall_eff_err, total_yield, total_err)

        count_err = Double(0.0)
        count_yield = in_hist.IntegralAndError(lo_bin, hi_bin-1, lo_bin, hi_bin-1, count_err)
        if variable_bins:
            count_yield *= in_hist.GetXaxis().GetBinWidth(last_x_bin) ** 2
            count_err *= in_hist.GetXaxis().GetBinWidth(last_x_bin) ** 2


        # elog table content
        if arguments.makeTables:
            format_string = "{:d}-{:d} | {:.2f}+-{:.2f} | {:.2f}+-{:.2f}"
            print '|-'
            print format_string.format(lo, hi, estimate, estimate_err, count_yield, count_err)

    # end elog table
    if arguments.makeTables:
        print "[/TABLE]"

# plot everything and make output file
out_file = TFile("nonQcdBgEstimate.root", "recreate")
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
