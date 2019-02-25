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
    A0 = RooRealVar("A0", "A0", 50, 40, 100)
    A1 = RooRealVar("A1", "A1", -0.05, -0.1, 0.1)
    B0 = RooRealVar("B0", "B0", 50, 40, 100)
    B1 = RooRealVar("B1", "B1", -0.05, -0.1, 0.1)
    polyA = RooPolynomial("polyA", "polyA", x, RooArgList(A0, A1), 0)
    polyB = RooPolynomial("polyB", "polyB", x, RooArgList(B0, B1), 0)

    fit_rangeA = d['fit_rangeA'] if 'fit_rangeA' in d else (var_range_lo, var_range_hi)
    fit_rangeB = d['fit_rangeB'] if 'fit_rangeB' in d else (var_range_lo, var_range_hi)
    polyA.fitTo(hist, RooFit.Range(fit_rangeA[0], fit_rangeA[1]))
    polyB.fitTo(hist, RooFit.Range(fit_rangeB[0], fit_rangeB[1]))

    # plot everything
    out_file.cd()
    c = TCanvas(d['name'], d['name'], 800, 700)
    c.SetLeftMargin(0.13)
    f = x.frame()
    f.SetName(d['name'])
    f.SetTitle(d['name'])
    hist.plotOn(f)
    polyA.plotOn(f)
    polyB.plotOn(f)
    polyA.paramOn(f, RooFit.Layout(.3, 0.6, .87))
    polyB.paramOn(f, RooFit.Layout(.6, 0.9, .87))
    f.Draw()
    c.Write()
    if arguments.savePDFs:
        c.SaveAs("linear_fit_" + d["name"] + ".pdf", "recreate")
