#!/usr/bin/env python

# Written to fit data and MC d0 distributions in the prompt control region to extract the
# d0 resolutions so that the MC d0 can be smeared to match the data d0. Can be used to
# fit any set of distributions with gaussians. Takes in an arbitrary number of plots, fits
# them, and plots the distributions, fits, and fit parameters on individual canvases.

# usage: fitGaussian.py -l CONFIG
# sample config: EEChannel/test/fitGaussian_cfg.py

import sys
import re
import os
from optparse import OptionParser
from ROOT import gPad, gROOT, TFile, TF1, TCanvas, RooFit, RooRealVar, RooGaussian, RooPlot, RooDataHist, RooArgList

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig", help="local configuration file")
parser.add_option("-p", "--savePDFs", dest="savePDFs", action="store_true", default=False, help="save PDFs of each plot")

(arguments, args) = parser.parse_args()
if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "you forgot to specify a config file with -l"
    sys.exit(1)


gROOT.SetBatch()
out_file = TFile("gaussian_fit.root", "recreate")

for d in distributions:
    in_file = TFile(d['file'])
    in_hist = in_file.Get(d['hist']).Clone()

    var_name = in_hist.GetXaxis().GetTitle()
    var_range_lo = in_hist.GetXaxis().GetXmin()
    var_range_hi = in_hist.GetXaxis().GetXmax()

    x = RooRealVar(var_name, var_name, var_range_lo, var_range_hi)
    hist = RooDataHist(d['name'], d['name'], RooArgList(x), in_hist)

    # build gaussian model and fit hist
    mean = RooRealVar("mean", "mean", (var_range_lo+var_range_hi)/2., var_range_lo, var_range_hi)
    sigma = RooRealVar("sigma", "sigma", var_range_hi/10, 0, var_range_hi*10)
    gauss = RooGaussian("gauss", "gauss", x, mean, sigma)

    fit_range = d['fit_range'] if 'fit_range' in d else (var_range_lo, var_range_hi)
    gauss.fitTo(hist, RooFit.Range(fit_range[0], fit_range[1]))

    # plot everything
    out_file.cd()
    c = TCanvas(d['name'], d['name'], 800, 700)
    c.SetLeftMargin(0.13)
    f = x.frame()
    f.SetName(d['name'])
    f.SetTitle(d['name'])
    hist.plotOn(f)
    gauss.plotOn(f)
    gauss.paramOn(f, RooFit.Layout(.62, 0.99, .87))
    f.Draw()
    c.Write()
    if arguments.savePDFs:
        c.SaveAs("gaussian_fit_" + d["name"] + ".pdf", "recreate")
