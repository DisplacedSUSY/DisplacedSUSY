#!/usr/bin/env python

import sys
import os
import re
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from ROOT import TFile, TH1F, TF1, TCanvas, Double, gStyle, gROOT, TLine

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
out_file = TFile(output_path + "improved_abcd_results.root", "recreate")

for sample in samples:
    print "\n" + sample
    in_hists = {}
    in_file = TFile(output_path + sample + ".root")

    # get histograms and statistical uncertainties for all regions
    for region, channel in channels.iteritems():
        # fixme: set plot in cfg
        in_hists[region] = in_file.Get(channel + "Plotter/" + input_hist)
        if not in_hists[region]:
            print "Warning: could not load histogram"

    # plot A/B and perform fit
    fit_func = TF1("fit", fit_function, 0, in_hists['a'].GetXaxis().GetXmax())
    fit_func.SetParLimits(0, 0, 1)
    fit_func.SetParLimits(1, -1, 1)
    b_over_a_hist = in_hists['b'].Clone()
    d_over_c_hist = in_hists['d'].Clone()
    b_over_a_hist.Divide(in_hists['a'])
    d_over_c_hist.Divide(in_hists['c'])
    b_over_a_hist.Fit(fit_func, "WL", "", fit_range[0], fit_range[1])
    gStyle.SetOptFit(1111)
    fit = b_over_a_hist.GetFunction("fit")

    # calculate d(pT) = c(pT) * fit_function(pT)
    transfer_factor_hist = in_hists['c'].Clone()
    for b in range(1, in_hists["c"].GetNbinsX()+1):
        transfer_factor_hist.SetBinContent(b, fit.Eval(transfer_factor_hist.GetBinCenter(b)))
        transfer_factor_hist.SetBinError(b, 0) # fixme: account for fit uncertainty
    d_estimate_hist = in_hists['c'].Clone()
    d_estimate_hist.Multiply(transfer_factor_hist)

    # print closure test results
    # fixme: need to account for overflow bin
    error = Double()
    print "estimate:", d_estimate_hist.IntegralAndError(0, d_estimate_hist.GetNbinsX(), error), "+-", error
    if arguments.unblind:
        print "actual:", in_hists["d"].IntegralAndError(0, in_hists["c"].GetNbinsX(), error), "+-", error
    else:
        print "actual: BLINDED"

    # Save plots
    out_file.cd()
    # transfer factor plots
    transfer_factor_hist.SetTitle(sample + "_tf")
    transfer_factor_hist.SetName(sample + "_tf")
    transfer_factor_hist.Write()
    # estimated and actual pT distributions in region D
    d_canvas = TCanvas(sample+"_d", sample+"_d", 100, 100, 700, 600 )
    d_estimate_hist.SetTitle(sample + " d estimate and actual")
    d_estimate_hist.SetName(sample + " d estimate and actual")
    d_estimate_hist.SetLineColor(2)
    d_estimate_hist.Draw()
    if arguments.unblind:
        in_hists['d'].Draw("sames")
    d_canvas.Write()
    # fits and combined B/A and D/C plots
    fit_canvas = TCanvas(sample + " fit", sample + " fit", 100, 100, 700, 600 )
    b_over_a_hist.Draw()
    b_over_a_hist.SetTitle(sample + " fit")
    b_over_a_hist.SetName(sample + " fit")
    b_over_a_hist.GetYaxis().SetRangeUser(0, 0.005)
    b_over_a_hist.GetYaxis().SetTitle("B/A or D/C")
    b_over_a_hist.GetYaxis().SetTitleOffset(1.4)
    b_over_a_hist.GetYaxis().SetLabelSize(0.025)
    if arguments.unblind:
        d_over_c_hist.Draw("same")
    fit.SetRange(0, 500)
    fit.Draw("same")
    line = TLine()
    line.SetLineWidth(2)
    line.SetLineColor(4)
    line.SetLineStyle(9)
    line.DrawLine(40, 0, 40, 0.005)
    line.DrawLine(100, 0, 100, 0.005)
    fit_canvas.Write()

out_file.Close()
