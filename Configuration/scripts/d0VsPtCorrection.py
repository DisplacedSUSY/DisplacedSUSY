#!/usr/bin/env python

# Fits profile plots (mean |d0| vs pt, each background MC) with linear functions
# Uses this linear function as a correction to |d0| vs pt plot in 4 regions

# Written to fit data and MC d0 distributions in the prompt control region to extract the
# d0 resolutions so that the MC d0 can be smeared to match the data d0. Can be used to
# fit any set of distributions with gaussians. Takes in an arbitrary number of plots, fits
# them, and plots the distributions, fits, and fit parameters on individual canvases.

# usage: d0VsPtCorrection.py -l CONFIG
# sample config: StandardAnalysis/test/d0VsPtCorrection_cfg.py

import sys
import re
import os
from optparse import OptionParser
from ROOT import gPad, gROOT, TFile, TF1, TH1D, TCanvas, RooFit, RooRealVar, RooGaussian, RooPolynomial, RooPlot, RooDataHist, RooArgList, RooArgSet

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig", help="local configuration file")
parser.add_option("-p", "--savePDFs", dest="savePDFs", action="store_true", default=False, help="save PDFs of each plot")

(arguments, args) = parser.parse_args()
if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "you forgot to specify a config file with -l"
    sys.exit(-1)


gROOT.SetBatch()
out_file = TFile("linear_fit.root", "recreate")

for d in distributions:
    #get 2D distributions
    in_file = TFile(d['file'])
    in_hist = in_file.Get(d['hist']).Clone()

    #make profiles
    rawProfileX = in_hist.ProfileX()
    rawProfileY = in_hist.ProfileY()

    profileX = TH1D(rawProfileX.GetName(),
                    rawProfileX.GetTitle(),
                    in_hist.GetNbinsX(),
                    in_hist.GetXaxis().GetBinLowEdge(1),
                    in_hist.GetXaxis().GetBinUpEdge(in_hist.GetNbinsX())
                    )
    profileX.Sumw2()
    profileX.SetDirectory(0)

    for bin in range(1,profileX.GetNbinsX()):
        profileX.SetBinContent(bin, rawProfileX.GetBinContent(bin))
        profileX.SetBinError(bin,rawProfileX.GetBinError(bin))

        profileY = TH1D(rawProfileY.GetName(),
                        rawProfileY.GetTitle(),
                        in_hist.GetNbinsY(),
                        in_hist.GetYaxis().GetBinLowEdge(1),
                        in_hist.GetYaxis().GetBinUpEdge(in_hist.GetNbinsY())
                        )
        profileY.Sumw2()
        profileY.SetDirectory(0)

        for bin in range(1,profileY.GetNbinsX()):
            profileY.SetBinContent(bin, rawProfileY.GetBinContent(bin))
            profileY.SetBinError(bin,rawProfileY.GetBinError(bin))

    #start roofit for profileX
    var_name = profileX.GetXaxis().GetTitle()
    var_range_lo = profileX.GetXaxis().GetXmin()
    var_range_hi = profileX.GetXaxis().GetXmax()

    x = RooRealVar(var_name, var_name, var_range_lo, var_range_hi)
    hist = RooDataHist(d['name'], d['name'], RooArgList(x), profileX)

    # build linear model and fit hist
    # poly(x) = c0 + c1*x
    c0 = RooRealVar("c0", "c0", 50, 0, 100)
    c1 = RooRealVar("c1", "c1", -0.05, -2, 1)
    poly = RooPolynomial("poly", "poly", x, RooArgList(c0, c1), 0)

    fit_range = d['fit_range'] if 'fit_range' in d else (var_range_lo, var_range_hi)
    poly.fitTo(hist, RooFit.Range(fit_range[0], fit_range[1]))

    # plot everything
    out_file.cd()
    c = TCanvas(d['name'], d['name'], 800, 700)
    c.SetLeftMargin(0.13)
    f = x.frame()
    f.SetName(d['name'])
    f.SetTitle(d['name'])
    hist.plotOn(f)
    poly.plotOn(f)
    poly.paramOn(f, RooFit.Layout(.62, 0.99, .87))
    f.Draw()
    c.Write()
    if arguments.savePDFs:
        c.SaveAs("linear_fit_" + d["name"] + ".pdf", "recreate")
