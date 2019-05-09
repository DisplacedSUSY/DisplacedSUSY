#!/usr/bin/env python

import sys
import os
import re
from array import array
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from ROOT import TFile, TF1, TCanvas, Double, gStyle, gPad, gROOT, TLine, TGraph, TGraphErrors, TGraphAsymmErrors, TMultiGraph, TLegend, TPaveText

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

gROOT.SetBatch(True)
gStyle.SetOptStat(1)
gStyle.SetOptFit(0) # fixme: ideally this would be set on a plot-by-plot basis
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

def make_estimate_hist(c_hist, fit):
    transfer_factor_hist = c_hist.Clone()
    for b in range(1, transfer_factor_hist.GetNbinsX()+1):
        transfer_factor_hist.SetBinContent(b, fit.Eval(transfer_factor_hist.GetBinCenter(b)))
        transfer_factor_hist.SetBinError(b, 0) # fixme: account for fit uncertainty
    d_estimate_hist = c_hist.Clone()
    d_estimate_hist.Multiply(transfer_factor_hist)
    return d_estimate_hist

def do_closure_test(estimate_hist, d_hist):
    estimate = estimate_hist.Integral(0, estimate_hist.GetNbinsX())
    print "estimate:", round(estimate, 2)
    if arguments.unblind:
        actual_error = Double()
        actual_yield = d_hist.IntegralAndError(0, d_hist.GetNbinsX(), actual_error)
        print "actual:", round(actual_yield, 2), "+-", round(actual_error, 2)
    else:
        print "actual: BLINDED"
        actual_yield = actual_error = 0.0
    return (estimate, actual_yield, actual_error)

def setup_plot(plot, title, x_title, y_title):
    plot.SetTitle(title)
    plot.SetName(title)
    plot.GetXaxis().SetTitle(x_title)
    plot.GetYaxis().SetTitle(y_title)
    plot.GetYaxis().SetTitleOffset(1.4)
    plot.GetYaxis().SetLabelSize(0.025)

def draw_lines(x_values):
    line = TLine()
    line.SetLineWidth(2)
    line.SetLineColor(4)
    line.SetLineStyle(9)
    gPad.Update()
    for x in x_values:
        line.DrawLine(x, 0, x, gPad.GetUymax())

####################################################################################################

out_file = TFile(output_path + "improved_abcd_results.root", "recreate")
mean_fit_results = {}
c_yields = {}

for sample in samples:
    fit_summary_plot = TMultiGraph()
    fit_summary_legend = TLegend(0.4, 0.5, 0.89, 0.89)
    fit_parameters_plot = TGraph()
    color_ix = 0
    print "\n" + sample

    # get histograms and statistical uncertainties for all regions
    in_hists = {}
    in_file = TFile(output_path + sample + ".root")
    for region, channel in channels.iteritems():
        in_hists[region] = in_file.Get(channel + "Plotter/" + input_hist)
        in_hists[region] = in_hists[region].Rebin(len(bin_edges)-1, in_hists[region].GetName(),
                                                  array('d', bin_edges))
        if not in_hists[region]:
            print "Warning: could not load " + channel + "Plotter/" + input_hist

    # set up fit model
    composite = sample in composite_samples
    model = composite_model if composite else component_model
    fit_func = TF1(sample + "_fit", model, 0, in_hists['a'].GetXaxis().GetXmax())
    c_yields[sample] = in_hists["c"].Integral()
    if composite:
        components = composite_samples[sample]
        print "Fitting composite dataset:"
        print "model:", model
        print "[1] and [2] correspond to " + components[0]
        print "[3] and [4] correspond to " + components[1]
        #fit_func.SetParLimits(0, 0, 1) # let weights float
        # fix weights to ratio of events in region c
        fit_func.FixParameter(0, c_yields[components[0]] /
                              (c_yields[components[0]]+c_yields[components[1]]))
        fit_func.FixParameter(1, mean_fit_results[components[0]].GetParameter(0))
        fit_func.FixParameter(2, mean_fit_results[components[0]].GetParameter(1))
        fit_func.FixParameter(3, mean_fit_results[components[1]].GetParameter(0))
        fit_func.FixParameter(4, mean_fit_results[components[1]].GetParameter(1))
    else:
        print "Fitting component dataset:"
        print "model:", model
        fit_func.SetParLimits(0, 0, 100)
        fit_func.SetParLimits(1, 0, 100)

    estimates = {}
    fits = {}
    # fit B/A once per fit range
    for fit_range in fit_ranges:
        b_over_a_plot = TGraphAsymmErrors(in_hists['b'], in_hists['a'], "pois")
        b_over_a_plot.Fit(fit_func, "", "", fit_range[0], fit_range[1])
        fit = b_over_a_plot.GetFunction(sample+"_fit")

        # calculate d(pT) = c(pT) * model(pT) and do closure test
        d_estimate_hist = make_estimate_hist(in_hists['c'].Clone(), fit)
        estimate, actual_yield, actual_error = do_closure_test(d_estimate_hist, in_hists['d'])

        # save max and min estimate and corresponding fits
        if fit_range == fit_ranges[0]:
            estimates['max'] = estimates['min'] = estimate
            fits['max'] = fits['min'] = fit.Clone()
        else:
            if estimate > estimates['max']:
                estimates['max'] = estimate
                fits['max'] = fit.Clone()
            elif estimate < estimates['min']:
                estimates['min'] = estimate
                fits['min'] = fit.Clone()

        # save once-per-fit plots
        out_file.cd()
        sample_and_range = sample + "_" + str(fit_range[0])

        # estimated and actual pT distribution in region D
        d_canvas = TCanvas(sample_and_range+"_d", sample_and_range+"_d", 100, 100, 700, 600)
        d_estimate_hist.SetTitle(sample_and_range + " d estimate and actual")
        d_estimate_hist.SetName(sample_and_range + " d estimate and actual")
        d_estimate_hist.SetLineColor(2)
        d_estimate_hist.Draw()
        if arguments.unblind:
            in_hists['d'].Draw("sames")
        d_canvas.Write()

        # fits and combined B/A and D/C plot
        fit_canvas = TCanvas(sample_and_range+"_fit", sample_and_range+"_fit", 100, 100, 700, 600)
        b_over_a_plot.PaintStats(fit)
        fit_plot = TMultiGraph()
        fit_plot.Add(b_over_a_plot, "P")
        if arguments.unblind:
            d_over_c_plot = TGraphAsymmErrors(in_hists['d'], in_hists['c'], "pois")
            fit_plot.Add(d_over_c_plot, "P")
        fit_plot.Draw("A")
        setup_plot(fit_plot, sample_and_range+" fit",
                    str(d_estimate_hist.GetXaxis().GetTitle()), "B/A or D/C")
        fit.SetRange(0, 500)
        draw_lines([fit_range[0], fit_range[1]])
        fit_canvas.Write()

        # add fit plots to fit summary plot
        fit.SetLineColor(colors[color_ix])
        b_over_a_clone = b_over_a_plot.Clone() # clone plots to please pyroot
        b_over_a_clone.SetMarkerStyle(6)
        b_over_a_clone.SetMarkerColor(colors[color_ix])
        b_over_a_clone.SetLineColor(colors[color_ix])
        fit_summary_plot.Add(b_over_a_clone, "PX")
        fit_summary_legend.AddEntry(b_over_a_clone, str(fit_range[0]) + " GeV --> " +
                                    str(round(estimate, 2)) + " events")
        if arguments.unblind:
            d_over_c_clone = d_over_c_plot.Clone() # clone plots to please pyroot
            d_over_c_clone.SetMarkerStyle(6)
            d_over_c_clone.SetMarkerColor(colors[color_ix])
            d_over_c_clone.SetLineColor(colors[color_ix])
            fit_summary_plot.Add(d_over_c_clone, "PX")
        color_ix = (color_ix + 1) % len(colors)

        # add point to fit parameter plot
        fit_parameters_plot.SetMarkerStyle(8)
        fit_parameters_plot.SetPoint(fit_parameters_plot.GetN(),
                                    fit.GetParameter(0), fit.GetParameter(1))

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
    setup_plot(fit_summary_plot, sample+" fit summary",
               str(d_estimate_hist.GetXaxis().GetTitle()), "B/A or D/C")
    fit_summary_legend.SetHeader(
        "#splitline{Fit Range Lower Bound --> Corresponding BG Estimate}{(Actual yield is "
        + str(round(actual_yield, 2)) + " +- " + str(round(actual_error, 2)) + ")}")
    fit_summary_legend.SetTextSize(0.025)
    fit_summary_legend.SetBorderSize(0)
    fit_summary_legend.Draw()
    draw_lines([fit_range[1]])
    fit_summary_canvas.Write()

    # fit parameters plot
    fit_parameters_canvas = TCanvas(sample+"_fit_pars", sample+"_fit_pars", 100, 100, 700, 600)
    par_0_mean = fit_parameters_plot.GetMean(1)
    par_0_rms  = fit_parameters_plot.GetRMS(1)
    par_1_mean = fit_parameters_plot.GetMean(2)
    par_1_rms  = fit_parameters_plot.GetRMS(2)
    fit_parameters_mean = TGraphErrors()
    fit_parameters_mean.SetLineColor(4)
    fit_parameters_mean.SetMarkerColor(4)
    fit_parameters_mean.SetMarkerStyle(8)
    fit_parameters_mean.SetPoint(0, par_0_mean, par_1_mean)
    fit_parameters_mean.SetPointError(0, par_0_rms, par_1_rms)
    fit_parameters_min = TGraph()
    fit_parameters_max = TGraph()
    fit_parameters_min.SetMarkerStyle(8)
    fit_parameters_max.SetMarkerStyle(8)
    fit_parameters_min.SetMarkerColor(8)
    fit_parameters_max.SetMarkerColor(46)
    fit_parameters_min.SetPoint(0, fits['min'].GetParameter(0), fits['min'].GetParameter(1))
    fit_parameters_max.SetPoint(0, fits['max'].GetParameter(0), fits['max'].GetParameter(1))
    par_mg = TMultiGraph()
    par_mg.Add(fit_parameters_plot, "P")
    par_mg.Add(fit_parameters_mean, "P")
    par_mg.Add(fit_parameters_min, "P")
    par_mg.Add(fit_parameters_max, "P")
    par_mg.Draw("A")
    setup_plot(par_mg, "Fit parameters for "+model, "Parameter [0]", "Parameter [1]")
    par_legend = TLegend(0.5, 0.7, 0.89, 0.89)
    par_legend.AddEntry(fit_parameters_plot, "Individual fit parameters", "P")
    par_legend.AddEntry(fit_parameters_mean, "Mean fit parameters (RMS errors)", "LEP")
    par_legend.AddEntry(fit_parameters_min, "Fit parameters yielding lowest estimate", "P")
    par_legend.AddEntry(fit_parameters_max, "Fit parameters yielding highest estimate", "P")
    par_legend.SetBorderSize(0)
    par_legend.Draw()
    fit_parameters_canvas.Write()

    # mean fit plot
    # constrain fit parameters to mean values
    fit_func.FixParameter(0, par_0_mean)
    fit_func.FixParameter(1, par_1_mean)
    b_over_a_clone = b_over_a_plot.Clone() # clone plots to please pyroot
    b_over_a_clone.Fit(fit_func, "", "", fit_ranges[0][0], fit_ranges[0][1]) # use initial fit range
    mean_fit = b_over_a_clone.GetFunction(sample+"_fit")
    mean_fit_results[sample] = mean_fit.Clone()
    # estimate background from mean fit
    mean_estimate_hist = make_estimate_hist(in_hists['c'].Clone(), mean_fit)
    estimate, actual_yield, actual_error = do_closure_test(mean_estimate_hist, in_hists['d'])
    # make plot
    mean_fit_canvas = TCanvas(sample+"_mean_fit", sample+"_mean_fit", 100, 100, 700, 600)
    mean_fit_plot = TMultiGraph()
    mean_fit_plot.Add(b_over_a_clone, "P")
    if arguments.unblind:
        d_over_c_clone = d_over_c_plot.Clone() # clone plots to please pyroot
        mean_fit_plot.Add(d_over_c_clone, "P")
    mean_fit_plot.Draw("A")
    setup_plot(mean_fit_plot, sample+" mean fit",
               str(d_estimate_hist.GetXaxis().GetTitle()), "B/A or D/C")
    mean_fit.SetRange(0, 500)
    fits['min'].Draw("same")
    fits['max'].Draw("same")
    fits['min'].SetRange(fit_ranges[0][1], d_estimate_hist.GetXaxis().GetXmax())
    fits['max'].SetRange(fit_ranges[0][1], d_estimate_hist.GetXaxis().GetXmax())
    draw_lines([fit_ranges[0][0], fit_ranges[0][1]])
    results_pave = TPaveText(0.5, 0.7, 0.8, 0.8, "NDC")
    results_pave.AddText("Actual yield: " + str(round(actual_yield, 2))
                         + " +- " + str(round(actual_error, 2)) + " events")
    results_pave.AddText("Mean estimated yield: " + str(round(estimate, 2)) + " events")
    results_pave.AddText("Minimum estimated yield: " + str(round(estimates['min'], 2)) + " events")
    results_pave.AddText("Maximum estimated yield: " + str(round(estimates['max'], 2)) + " events")
    results_pave.SetTextSize(0.025)
    results_pave.SetFillColor(0)
    results_pave.SetBorderSize(0)
    results_pave.SetTextAlign(11)
    results_pave.Draw()
    mean_fit_canvas.Write()

out_file.Close()
