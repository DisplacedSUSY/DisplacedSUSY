#!/usr/bin/env python

# Given a 2D histogram and a set of x and y bin edges, this script will estimate
# the number of events in the given target regions using an abcd method.
#
# usage: abcd_from2dHist.py -l CONFIG -w CONDOR_DIR
# sample config: EEChannel/test/abcd_from2dHist_cfg.py

import sys
import os
import re
from array import array
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from ROOT import TFile, TCanvas, TH2F, gROOT, Double, gStyle

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")
parser.add_option("-c", "--doClosureTest", action="store_true", dest="doClosureTest",
                  default=False, help="perform closure test; DON'T RUN OVER DATA IF BLINDED!")
parser.add_option("-t", "--makeTables", action="store_true", dest="makeTables",
                  default=False, help="print table of abcd and counting yields; table is formatted for elog; must be used with '-c'")

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
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetTextFont(42)
gStyle.SetPaintTextFormat('.2f')
gROOT.ForceStyle()


def get_yields_and_errors(h, x_bin_lo, x_bin_hi, y_bin_lo, y_bin_hi, variable_bins):
    error = Double(0.0)
    integral = h.IntegralAndError(x_bin_lo, x_bin_hi, y_bin_lo, y_bin_hi, error)
    # multiply by area of last bin if histogram was made with variable-width bins
    # assume input histograms have symmetric binning
    if variable_bins:
        nBins = h.GetXaxis().GetNbins()
        area = h.GetXaxis().GetBinWidth(nBins) ** 2
        integral *= area
        error *= area
    return (integral, error)


in_file = TFile(input_file)
in_hist = in_file.Get(input_hist).Clone()
title = lambda x: output_file.replace(".root", " "+x)
abcd_hist  = TH2F(title("ABCD Estimates"), title("ABCD Estimates"), len(bins_x)-1,
                  array('d',bins_x), len(bins_y)-1, array('d',bins_y) )
count_hist = TH2F(title("Counting Yields"), title("Counting Yields"), len(bins_x)-1,
                  array('d',bins_x), len(bins_y)-1, array('d',bins_y) )
comp_hist  = TH2F(title("Consistency"), title("Consistency"),  len(bins_x)-1,
                  array('d',bins_x), len(bins_y)-1, array('d',bins_y) )
ratio_hist  = TH2F(title("Ratio"), title("Ratio"),  len(bins_x)-1,
                  array('d',bins_x), len(bins_y)-1, array('d',bins_y) )

# Get yield and error in prompt region
prompt_bin_x_lo = in_hist.GetXaxis().FindBin(bins_x[0])
prompt_bin_x_hi = in_hist.GetXaxis().FindBin(bins_x[1])-1
prompt_bin_y_lo = in_hist.GetYaxis().FindBin(bins_y[0])
prompt_bin_y_hi = in_hist.GetYaxis().FindBin(bins_y[1])-1

(prompt_yield, prompt_error) = get_yields_and_errors(in_hist, prompt_bin_x_lo, prompt_bin_x_hi,
                                                     prompt_bin_y_lo, prompt_bin_y_hi, variable_bins)

if arguments.makeTables:
    print "[B]", title(""), "[/B]"
    print '[TABLE border="1"]'
    print "mu d0 range (#mum)|e d0 range (#mum)|A|B|C|D Estimate|D Actual|D Actual/Estimate"

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

        # get counting yields in signal region and calculate consistency between abcd and counting
        if arguments.doClosureTest:
            (count_yield, count_error) = get_yields_and_errors(in_hist, x_bin_lo, x_bin_hi,
                                                               y_bin_lo, y_bin_hi, variable_bins)
            count_hist.SetBinContent(out_bin, count_yield)
            count_hist.SetBinError(out_bin, count_error)

            try:
                ratio_hist.SetBinContent(out_bin, abcd_yield/count_yield)
            except ZeroDivisionError:
                ratio_hist.SetBinContent(out_bin, 2)
                print "count yield is 0, setting ratio to 2"

            yield_diff = round(abs(abcd_yield - count_yield), 5)
            total_error  = abcd_error + count_error
            try:
                consistency = yield_diff / total_error
            except ZeroDivisionError:
                if yield_diff == 0:
                    consistency = 0
                else:
                    print "Total error is 0 while yields are > 0. Something is wrong with your input histogram"
            comp_hist.SetBinContent(out_bin, consistency)

            if arguments.makeTables and x_bin_lo != prompt_bin_x_lo and y_bin_lo != prompt_bin_y_lo:
                format_string = "{:d}-{:d} | {:d}-{:d}" + 3 * " | {:.0f}" + " | {:.2f}+-{:.2f}" + " | {:.0f}" + " | {:.2f}"
                print "|-"
                print format_string.format(x_lo, x_hi, y_lo, y_hi, prompt_yield, x_yield, y_yield,
                                           abcd_yield, abcd_error, count_yield, count_yield/abcd_yield)

if arguments.makeTables:
    print "[/TABLE]"

    # Get yield and error in inclusive signal regions
    abcd_yields_and_errors  = []
    count_yields_and_errors = []
    last_x_bin = abcd_hist.GetXaxis().FindBin(bins_x[-1])
    last_y_bin = abcd_hist.GetYaxis().FindBin(bins_y[-1])
    for x, y in zip(bins_x[1:], bins_y[1:]):
        x_bin = abcd_hist.GetXaxis().FindBin(x)
        y_bin = abcd_hist.GetYaxis().FindBin(y)
        abcd_yields_and_errors.append(get_yields_and_errors(abcd_hist, x_bin, last_x_bin,
                                                            y_bin, last_y_bin, False))
        count_yields_and_errors.append(get_yields_and_errors(count_hist, x_bin, last_x_bin,
                                                            y_bin, last_y_bin, False))

    # subtract each yield from more inclusive yield to create non-overlapping regions
    abcd_yields_and_errors  = [ propagateError("sum", y1, e1, -1*y2, e2) for (y1,e1), (y2,e2) in
                              zip(abcd_yields_and_errors[:-1], abcd_yields_and_errors[1:]) ]
    count_yields_and_errors = [ propagateError("sum", y1, e1, -1*y2, e2) for (y1,e1), (y2,e2) in
                              zip(count_yields_and_errors[:-1], count_yields_and_errors[1:]) ]


    # print summary table
    print '[TABLE border="1"]'
    print "Signal Region|Estimate|Actual"
    for region, (abcd_yield, abcd_error), (count_yield, count_error) in zip(
        range(1, len(abcd_yields_and_errors)+1), abcd_yields_and_errors, count_yields_and_errors):
        print "|-"
        print "Region {} | {:.1e}+-{:.1e} | {:.1e}+-{:.1e}".format(
            region, abcd_yield, abcd_error, count_yield, count_error)
    print "[/TABLE]"


out_file = TFile(output_path + output_file, "recreate")

abcd_hist.SetMarkerSize(0.75)
abcd_hist.SetOption("colz text45 e")
abcd_hist.GetXaxis().SetTitle(x_axis_title)
abcd_hist.GetYaxis().SetTitle(y_axis_title)
abcd_hist.GetXaxis().SetTitleOffset(1.2)
abcd_hist.GetYaxis().SetTitleOffset(1.1)
abcd_hist.Write()
CanvasAbcd = TCanvas( "CanvasAbcd", "CanvasAbcd", 100, 100, 700, 600 )
#CanvasAbcd.SetLogx()
#CanvasAbcd.SetLogy()
CanvasAbcd.SetLogz()
CanvasAbcd.cd()
abcd_hist.Draw("colz text45 e")
CanvasAbcd.SaveAs(output_path+output_file.replace(".root", "_abcd.pdf"))
CanvasAbcd.SaveAs(output_path+output_file.replace(".root", "_abcd.png"))

if arguments.doClosureTest:
    count_hist.SetMarkerSize(0.75)
    count_hist.SetOption("colz text45 e")
    count_hist.GetXaxis().SetTitle(x_axis_title)
    count_hist.GetYaxis().SetTitle(y_axis_title)
    count_hist.GetXaxis().SetTitleOffset(1.2)
    count_hist.GetYaxis().SetTitleOffset(1.1)
    count_hist.Write()
    CanvasCount = TCanvas( "CanvasCount", "CanvasCount", 100, 100, 700, 600 )
    #CanvasCount.SetLogx()
    #CanvasCount.SetLogy()
    CanvasCount.SetLogz()
    CanvasCount.cd()
    count_hist.Draw("colz text45 e")
    CanvasCount.SaveAs(output_path+output_file.replace(".root", "_count.pdf"))
    CanvasCount.SaveAs(output_path+output_file.replace(".root", "_count.png"))

    comp_hist.SetMarkerSize(0.75)
    comp_hist.SetOption("colz text45")
    comp_hist.GetXaxis().SetTitle(x_axis_title)
    comp_hist.GetYaxis().SetTitle(y_axis_title)
    comp_hist.GetXaxis().SetTitleOffset(1.2)
    comp_hist.GetYaxis().SetTitleOffset(1.1)
    comp_hist.Write()
    CanvasComp = TCanvas( "CanvasComp", "CanvasComp", 100, 100, 700, 600 )
    #CanvasComp.SetLogx()
    #CanvasComp.SetLogy()
    CanvasComp.cd()
    comp_hist.Draw("colz text45")
    CanvasComp.SaveAs(output_path+output_file.replace(".root", "_comp.pdf"))
    CanvasComp.SaveAs(output_path+output_file.replace(".root", "_comp.png"))

    ratio_hist.SetMarkerSize(0.75)
    ratio_hist.SetOption("colz text45")
    ratio_hist.GetXaxis().SetTitle(x_axis_title)
    ratio_hist.GetYaxis().SetTitle(y_axis_title)
    ratio_hist.GetXaxis().SetTitleOffset(1.2)
    ratio_hist.GetYaxis().SetTitleOffset(1.1)
    ratio_hist.Write()
    CanvasRatio = TCanvas( "CanvasRatio", "CanvasRatio", 100, 100, 700, 600 )
    #CanvasRatio.SetLogx()
    #CanvasRatio.SetLogy()
    CanvasRatio.cd()
    ratio_hist.Draw("colz text45")
    CanvasRatio.SaveAs(output_path+output_file.replace(".root", "_ratio.pdf"))
    CanvasRatio.SaveAs(output_path+output_file.replace(".root", "_ratio.png"))

out_file.Close()
