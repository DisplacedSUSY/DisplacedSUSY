#!/usr/bin/env python

import sys
import os
import re
from array import array
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from ROOT import TFile, TF1, TCanvas, Double, gStyle, gROOT, TLine, TGraphAsymmErrors, TMultiGraph

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
gStyle.SetOptFit(1)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetTextFont(42)
gStyle.SetPaintTextFormat('6.4f')
gStyle.SetStatFormat('6.4f')
gStyle.SetFitFormat('6.4f')
gROOT.ForceStyle()

out_file = TFile(output_path + "improved_abcd_results.root", "recreate")
fit_results = {}
c_yields = {}

for sample in samples:
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
    b_over_a_hist = TGraphAsymmErrors(in_hists['b'], in_hists['a'], "pois")
    d_over_c_hist = TGraphAsymmErrors(in_hists['d'], in_hists['c'], "pois")

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

    b_over_a_hist.Fit(fit_func, "", "", fit_range[0], fit_range[1])
    fit = b_over_a_hist.GetFunction(sample+"_fit")
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
    print "estimate:", round(d_estimate_hist.IntegralAndError(0, d_estimate_hist.GetNbinsX(), error),2), "+-", round(error,2)
    if arguments.unblind:
        print "actual:", round(in_hists["d"].IntegralAndError(0, in_hists["d"].GetNbinsX(), error),2), "+-", round(error,2)
    else:
        print "actual: BLINDED"

    # Save plots
    out_file.cd()
    # transfer factor plots
    transfer_factor_hist.SetTitle(sample + "_tf")
    transfer_factor_hist.SetName(sample + "_tf")
    transfer_factor_hist.Write()
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
    # estimated and actual pT distributions in region D
    d_canvas = TCanvas(sample+"_d", sample+"_d", 100, 100, 700, 600)
    d_estimate_hist.SetTitle(sample + " d estimate and actual")
    d_estimate_hist.SetName(sample + " d estimate and actual")
    d_estimate_hist.SetLineColor(2)
    d_estimate_hist.Draw()
    if arguments.unblind:
        in_hists['d'].Draw("sames")
    d_canvas.Write()
    # fits and combined B/A and D/C plots
    fit_canvas = TCanvas(sample + " fit", sample + " fit", 100, 100, 700, 600)
    b_over_a_hist.PaintStats(fit)
    badc_mg = TMultiGraph()
    badc_mg.Add(b_over_a_hist)
    if arguments.unblind:
        badc_mg.Add(d_over_c_hist)
    badc_mg.Draw("AP")
    badc_mg.SetTitle(sample + " fit")
    badc_mg.SetName(sample + " fit")
    if "QCD" in sample:
        y_range = 0.5
    else:
        y_range = 0.005
    badc_mg.GetYaxis().SetRangeUser(0, y_range)
    badc_mg.GetYaxis().SetTitle("B/A or D/C")
    badc_mg.GetYaxis().SetTitleOffset(1.4)
    badc_mg.GetYaxis().SetLabelSize(0.025)
    fit.SetRange(0, 500)
    line = TLine()
    line.SetLineWidth(2)
    line.SetLineColor(4)
    line.SetLineStyle(9)
    line.DrawLine(fit_range[0], 0, fit_range[0], y_range)
    line.DrawLine(fit_range[1], 0, fit_range[1], y_range)
    fit_canvas.Write()
    #fit_canvas.SaveAs(sample+"_fit.pdf")

out_file.Close()
