#!/usr/bin/env python
import sys
import os
import re
import math
from array import array
from sets import Set
from numpy import arange, concatenate, empty
from optparse import OptionParser
from ROOT import TFile, TCanvas, TH2F, TLegend, gROOT, gPad, gDirectory, Double, RooFit, RooRealVar, RooDataHist, RooHistPdf, RooArgList, RooArgSet, RooAddPdf, RooPlot

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

if arguments.condorDir:
    output_path = "condor/" + arguments.condorDir
    if not os.path.exists(output_path):
        os.makedirs(output_path)
else:
    print "you forgot to specify a condor directory with -w"


def makeBins(regions, coarse):
    bins = [0.00]
    for low, high, num in regions.itervalues():
        if coarse:
            num = 1
        width = (high - low) / num
        for i in range(1, num+1):
            edge = round(low + i * width, 5)
            bins.append(edge)
    bins.sort()
    return array('d', bins)

def convertToDataHist(input_file, hist, name, var, bins):
    histogram = input_file.Get(hist).Clone()
    rebinned_histogram = histogram.Rebin(len(bins)-1, "Rebinned hist", bins)
    datahist = RooDataHist(name,name,RooArgList(var),rebinned_histogram)
    return datahist

# set up a few things
gROOT.SetBatch()
output_file = TFile(output_path + "/SidebandFit.root", "recreate")
output_file.mkdir(channel)
output_file.cd(channel)
gDirectory.mkdir(emu_dir)
gDirectory.mkdir(fit_dir)
yields = {}
bin_array = makeBins(regions, False)
bin_array_coarse = makeBins(regions, True)

for s in sidebands:
    prompt_file    = TFile(s["prompt"]["file"])
    displaced_file = TFile(s["displaced"]["file"])
    sideband_file  = TFile(s["sideband"]["file"])
    prompt_hist    = s["prompt"]["hist"]
    displaced_hist = s["displaced"]["hist"]
    sideband_hist  = s["sideband"]["hist"]
    prompt_name    = s["prompt"]["name"]
    displaced_name = s["displaced"]["name"]
    sideband_name  = s["sideband"]["name"]
    d0 = RooRealVar(s["name"]+" d0", s["name"]+" d0", 0, bin_array[-1], "um")
    d0_set = RooArgSet(RooArgList(d0))

    # make datahists and histpdfs to please roofit
    prompt_datahist    = convertToDataHist(prompt_file, prompt_hist, prompt_name, d0, bin_array)
    displaced_datahist = convertToDataHist(displaced_file, displaced_hist, displaced_name, d0, bin_array)
    sideband_datahist  = convertToDataHist(sideband_file, sideband_hist, sideband_name, d0, bin_array)

    prompt_pdf    = RooHistPdf(prompt_name, prompt_name, d0_set, prompt_datahist)
    displaced_pdf = RooHistPdf(displaced_name, displaced_name, d0_set, displaced_datahist)
    bg_components = RooArgList(prompt_pdf, displaced_pdf)

    n_prompt    = RooRealVar("n_prompt","number of prompt bg events",0,10000000)
    n_displaced = RooRealVar("n_displaced","number of displaced bg events",0,10000000)
    bg_norms    = RooArgList(n_prompt,n_displaced)

    model = RooAddPdf("model","model", bg_components, bg_norms)
    model.fitTo(sideband_datahist)
    n_model = n_prompt.getVal() + n_displaced.getVal()

    # Get model yields in sideband regions
    for range_name, bounds in regions.iteritems():
        d0.setRange(range_name, bounds[0], bounds[1])
        yield_frac = model.createIntegral(d0_set,d0_set,range_name)
        yields[s["name"]+" "+range_name] = yield_frac.getVal() * n_model

    # plot background components, sidebands, and fits
    frame = d0.frame()
    frame.SetName(s["name"]+" sideband")
    frame.SetTitle(s["name"]+" sideband")
    sideband_datahist.plotOn(frame, RooFit.Name("sideband"))
    model.plotOn(frame, RooFit.Name("model"))
    model.plotOn(frame, RooFit.Name("prompt"), RooFit.Components(prompt_name), RooFit.LineColor(1))
    model.plotOn(frame, RooFit.Name("displaced"), RooFit.Components(displaced_name), RooFit.LineColor(2))
    frame.SetMinimum(0.01)
    frame.SetMaximum(1000*sideband_datahist.weight(sideband_datahist.get(0)))
    canvas = TCanvas(s["name"],s["name"],700,700)
    frame.Draw()
    legend = TLegend(0.52,0.76,0.83,0.87)
    legend.AddEntry("sideband" , "Sideband Data"         , "LP")
    legend.AddEntry("model"    , "Prompt + Displaced Fit", "LP")
    legend.AddEntry("prompt"   , "Prompt Background"     , "LP")
    legend.AddEntry("displaced", "Displaced Background"  , "LP")
    legend.Draw()
    output_file.cd(channel)
    gDirectory.cd(fit_dir)
    gPad.SetLogy()
    gPad.Update()
    gPad.Modified()
    canvas.Write()

    prompt_file.Close()
    displaced_file.Close()
    sideband_file.Close()

# Make bg estimate TH2
n_bins_coarse = len(bin_array_coarse)-1
bg_2D_hist = TH2F(th2_name, th2_name, n_bins_coarse, bin_array_coarse, n_bins_coarse, bin_array_coarse)
prompt_avg = 0.5 * (yields["electron prompt"] + yields["muon prompt"])

for mu_range, mu_bounds in regions.iteritems():
    for e_range, e_bounds in regions.iteritems():

        mu_d0 = mu_bounds[0]
        e_d0  = e_bounds[0]
        bin_num = bg_2D_hist.FindBin(mu_d0, e_d0)
        mu_yield = yields["muon "+mu_range]
        e_yield  = yields["electron "+e_range]

        if mu_range is "prompt" and e_range is "prompt":
            bg_2D_hist.SetBinContent(bin_num, prompt_avg)
        elif mu_range is "prompt": # fill electron sideband
            bg_2D_hist.SetBinContent(bin_num, e_yield)
        elif e_range is "prompt": # fill muon sideband
            bg_2D_hist.SetBinContent(bin_num, mu_yield)
        else: # use ABCD to fill signal regions
            bg_2D_hist.SetBinContent(bin_num, mu_yield*e_yield/prompt_avg)

bg_2D_hist.SetOption("colz")
bg_2D_hist.Draw()
output_file.cd(channel)
gDirectory.cd(emu_dir)
bg_2D_hist.Write()

output_file.Close()

