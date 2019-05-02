#!/usr/bin/env python

import sys
import os
import re
from array import array
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from ROOT import TFile, TF1, TCanvas, Double, gStyle, gPad, gROOT, TLine, TGraphAsymmErrors, TMultiGraph, TLegend

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")
parser.add_option("-u", "--unblind", action="store_true", dest="unblind",
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

###################################################################################################

gROOT.SetBatch(True)
gStyle.SetOptStat(1)
gStyle.SetOptFit(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetTextFont(42)
gStyle.SetPaintTextFormat('6.4f')
gStyle.SetStatFormat('6.4f')
gStyle.SetFitFormat('6.4f')
gROOT.ForceStyle()
# select high contrast TColors for summary plots
colors = [x for x in range(1, 10)] + [11, 12, 28, 29, 33, 38, 41, 42, 43, 45, 46]

out_file = TFile(output_path + "improved_abcd_results.root", "recreate")
fit_results = {}
c_yields = {}

for sample in samples:
    color_ix = 0
    fit_summary_plot = TMultiGraph()
    fit_legend = TLegend(0.4, 0.5, 0.89, 0.89)
    for fit_range in fit_ranges:
        print "\n" + sample
        in_hists = {}
        in_file = TFile(output_path + sample + ".root")

        # get histograms and statistical uncertainties for all regions
        for region, channel in channels.iteritems():
            in_hists[region] = in_file.Get(channel + "Plotter/" + input_hist)
            in_hists[region] = in_hists[region].Rebin(len(bin_edges)-1, in_hists[region].GetName(), array('d', bin_edges))
            if not in_hists[region]:
                print "Warning: could not load histogram"

        # plot A/B and C/D
        b_over_a_plot = TGraphAsymmErrors(in_hists['b'], in_hists['a'], "pois")
        d_over_c_plot = TGraphAsymmErrors(in_hists['d'], in_hists['c'], "pois")

        # fit A/B
        composite = sample in composite_samples
        model = composite_model if composite else component_model
        fit_func = TF1(sample + "_fit", model, 0, in_hists['a'].GetXaxis().GetXmax())
        if composite:
            components = composite_samples[sample]
            print "Fitting composite dataset:"
            print "model:", model
            print "[1] and [2] correspond to " + components[0]
            print "[3] and [4] correspond to " + components[1]
            #fit_func.SetParLimits(0, 0, 1) # let weights float
            fit_func.FixParameter(0, c_yields[components[0]] / (c_yields[components[0]]+c_yields[components[1]])) # fix weights to ratio of events in region c
            fit_func.FixParameter(1, fit_results[components[0]].GetParameter(0))
            fit_func.FixParameter(2, fit_results[components[0]].GetParameter(1))
            fit_func.FixParameter(3, fit_results[components[1]].GetParameter(0))
            fit_func.FixParameter(4, fit_results[components[1]].GetParameter(1))
        else:
            print "Fitting component dataset:"
            print "model:", model
            fit_func.SetParLimits(0, 0, 100)
            fit_func.SetParLimits(1, 0, 100)

        b_over_a_plot.Fit(fit_func, "", "", fit_range[0], fit_range[1])
        fit = b_over_a_plot.GetFunction(sample+"_fit")
        fit_results[sample] = fit.Clone()
        c_yields[sample] = in_hists["c"].Integral()

        # calculate d(pT) = c(pT) * model(pT)
        transfer_factor_hist = in_hists['c'].Clone()
        for b in range(1, in_hists["c"].GetNbinsX()+1):
            transfer_factor_hist.SetBinContent(b, fit.Eval(transfer_factor_hist.GetBinCenter(b)))
            transfer_factor_hist.SetBinError(b, 0) # fixme: account for fit uncertainty
        d_estimate_hist = in_hists['c'].Clone()
        d_estimate_hist.Multiply(transfer_factor_hist)

        # print closure test results
        # fixme: need to account for overflow bin
        error = Double()
        estimate = d_estimate_hist.IntegralAndError(0, d_estimate_hist.GetNbinsX(), error)
        print "estimate:", round(estimate, 2), "+-", round(error, 2)
        if arguments.unblind:
            actual_yield = in_hists["d"].IntegralAndError(0, in_hists["d"].GetNbinsX(), error)
            actual_error = error
            print "actual:", round(actual_yield, 2), "+-", round(error, 2)
        else:
            print "actual: BLINDED"

        # Save once-per-fit plots
        out_file.cd()
        sample_and_range = sample + "_" + str(fit_range[0])
        # estimated and actual pT distributions in region D
        d_canvas = TCanvas(sample_and_range+"_d", sample_and_range+"_d", 100, 100, 700, 600)
        d_estimate_hist.SetTitle(sample_and_range + " d estimate and actual")
        d_estimate_hist.SetName(sample_and_range + " d estimate and actual")
        d_estimate_hist.SetLineColor(2)
        d_estimate_hist.Draw()
        if arguments.unblind:
            in_hists['d'].Draw("sames")
        d_canvas.Write()
        # fits and combined B/A and D/C plots
        fit_canvas = TCanvas(sample_and_range+"_fit", sample_and_range+"_fit", 100, 100, 700, 600)
        b_over_a_plot.PaintStats(fit)
        fit_plot = TMultiGraph()
        fit_plot.Add(b_over_a_plot, "P")
        if arguments.unblind:
            fit_plot.Add(d_over_c_plot, "P")
        fit_plot.Draw("A")
        fit_plot.SetTitle(sample_and_range + " fit")
        fit_plot.SetName(sample_and_range + " fit")
        fit_plot.GetXaxis().SetTitle(str(d_estimate_hist.GetXaxis().GetTitle()))
        fit_plot.GetYaxis().SetTitle("B/A or D/C")
        fit_plot.GetYaxis().SetTitleOffset(1.4)
        fit_plot.GetYaxis().SetLabelSize(0.025)
        fit.SetRange(0, 500)
        line = TLine()
        line.SetLineWidth(2)
        line.SetLineColor(4)
        line.SetLineStyle(9)
        gPad.Update()
        line.DrawLine(fit_range[0], 0, fit_range[0], gPad.GetUymax())
        line.DrawLine(fit_range[1], 0, fit_range[1], gPad.GetUymax())
        fit_canvas.Write()
        # add fit plots to summary plot
        fit.SetLineColor(colors[color_ix])
        b_over_a_clone = b_over_a_plot.Clone() # clone plots to please pyroot
        b_over_a_clone.SetMarkerStyle(6)
        b_over_a_clone.SetMarkerColor(colors[color_ix])
        b_over_a_clone.SetLineColor(colors[color_ix])
        fit_summary_plot.Add(b_over_a_clone, "PX")
        fit_legend.AddEntry(b_over_a_clone, str(fit_range[0]) + " GeV --> " +
                                           str(round(estimate, 2)) + " events")
        if arguments.unblind:
            d_over_c_clone = d_over_c_plot.Clone()
            d_over_c_clone.SetMarkerStyle(6)
            d_over_c_clone.SetMarkerColor(colors[color_ix])
            d_over_c_clone.SetLineColor(colors[color_ix])
            fit_summary_plot.Add(d_over_c_clone, "PX")
        color_ix = (color_ix + 1) % len(colors)

    # save once-per-sample plots
    # input hists
    a_canvas = TCanvas(sample+"_a", sample+"_a", 100, 100, 700, 600)
    in_hists['a'].Draw()
    a_canvas.Write()
    b_canvas = TCanvas(sample+"_b", sample+"_b", 100, 100, 700, 600)
    in_hists['b'].Draw()
    b_canvas.Write()
    c_canvas = TCanvas(sample+"_c", sample+"_c", 100, 100, 700, 600)
    in_hists['c'].Draw()
    c_canvas.Write()
    # fit summary plot
    fit_summary_canvas = TCanvas(sample+"_fit_summary", sample+"_fit_summary", 100, 100, 700, 600)
    fit_summary_plot.Draw("A")
    fit_summary_plot.SetTitle(sample + " fit summary")
    fit_summary_plot.SetName(sample + " fit summary")
    fit_summary_plot.GetXaxis().SetTitle(str(d_estimate_hist.GetXaxis().GetTitle()))
    fit_summary_plot.GetYaxis().SetTitle("B/A or D/C")
    fit_summary_plot.GetYaxis().SetTitleOffset(1.4)
    fit_summary_plot.GetYaxis().SetLabelSize(0.025)
    fit_legend.SetHeader("#splitline{Fit Range Lower Bound --> Corresponding BG Estimate}{(Actual yield is "
                     + str(round(actual_yield, 2)) + " +- " + str(round(actual_error, 2)) + ")}")
    fit_legend.SetTextSize(0.025)
    fit_legend.SetBorderSize(0)
    fit_legend.Draw()
    line.DrawLine(fit_range[1], 0, fit_range[1], gPad.GetUymax())
    fit_summary_canvas.Write()

out_file.Close()
