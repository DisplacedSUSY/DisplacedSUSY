#!/usr/bin/env python
import sys
import os
import re
from array import array
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
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
    sys.exit(1)

if arguments.condorDir:
    output_path = "condor/" + arguments.condorDir
    if not os.path.exists(output_path):
        os.makedirs(output_path)
else:
    print "you forgot to specify a condor directory with -w"
    sys.exit(1)


def convertToDataHist(hist, name, var, bins):
    rebinned_hist = hist.Rebin(len(bins)-1, "Rebinned hist", bins)
    datahist = RooDataHist(name,name,RooArgList(var),rebinned_hist)
    return datahist

gROOT.SetBatch()
output_file = TFile(output_path + "/SidebandFit.root", "recreate")
bins_x = array('d', sidebands["x"]["bins"])
bins_y = array('d', sidebands["y"]["bins"])
model_th2 = TH2F(th2_name, th2_name, len(bins_x)-1, bins_x, len(bins_y)-1, bins_y)

for axis, s in sidebands.iteritems():
    prompt_file    = TFile(s["prompt"]["file"])
    displaced_file = TFile(s["displaced"]["file"])
    sideband_file  = TFile(s["sideband"]["file"])

    prompt_hist    = prompt_file.Get(s["prompt"]["hist"]).Clone()
    displaced_hist = displaced_file.Get(s["displaced"]["hist"]).Clone()
    sideband_th2   = sideband_file.Get(s["sideband"]["hist"]).Clone()

    if axis == "x":
        h_bin = sideband_th2.GetXaxis().FindBin(s["depth"])
        sideband_hist = sideband_th2.ProjectionX("Muon Sideband",0,h_bin,"e")
    elif axis == "y":
        h_bin = sideband_th2.GetYaxis().FindBin(s["depth"])
        sideband_hist = sideband_th2.ProjectionY("Electron Sideband",0,h_bin,"e")
    else:
        print "Unrecognized axis name"

    d0 = RooRealVar(s["name"]+" d0", s["name"]+" d0", 0, 10.0, s["unit"])
    d0_set = RooArgSet(RooArgList(d0))
    bin_array = array('d', s["bins"])

    prompt_datahist    = convertToDataHist(prompt_hist,    s["prompt"]["name"],    d0, bin_array)
    displaced_datahist = convertToDataHist(displaced_hist, s["displaced"]["name"], d0, bin_array)
    sideband_datahist  = convertToDataHist(sideband_hist,  s["sideband"]["name"],  d0, bin_array)

    prompt_pdf    = RooHistPdf(s["prompt"]["name"],    s["prompt"]["name"],    d0_set, prompt_datahist)
    displaced_pdf = RooHistPdf(s["displaced"]["name"], s["displaced"]["name"], d0_set, displaced_datahist)
    bg_components = RooArgList(prompt_pdf, displaced_pdf)

    n_prompt    = RooRealVar("n_prompt","number of prompt bg events",0,10000000)
    n_displaced = RooRealVar("n_displaced","number of displaced bg events",0,10000000)
    bg_norms    = RooArgList(n_prompt,n_displaced)

    model = RooAddPdf("model","model", bg_components, bg_norms)
    model.fitTo(sideband_datahist)
    n_model = n_prompt.getVal() + n_displaced.getVal()

    # make TH1s of each sideband fit 
    frame = d0.frame()
    frame.SetName(s["name"]+" sideband")
    frame.SetTitle(s["name"]+" sideband")
    sideband_datahist.plotOn(frame, RooFit.Name("sideband"))
    model.plotOn(frame, RooFit.Name("model"))
    model.plotOn(frame, RooFit.Name("prompt"),    RooFit.Components(s["prompt"]["name"]),    RooFit.LineColor(1))
    model.plotOn(frame, RooFit.Name("displaced"), RooFit.Components(s["displaced"]["name"]), RooFit.LineColor(2))
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
    output_file.cd()
    gPad.SetLogy()
    gPad.Update()
    gPad.Modified()
    canvas.Write()

    # fill TH2 with fit yields in sideband regions
    for l_edge, h_edge in zip(s["bins"][:-1], s["bins"][1:]):
        if axis == "x":
            bin_num = model_th2.FindBin(l_edge, 0.0)
        elif axis == "y":
            bin_num = model_th2.FindBin(0.0, l_edge)

        # get yields and fill TH2
        d0.setRange(str(l_edge), l_edge, h_edge)
        yield_frac = model.createIntegral(d0_set, d0_set, str(l_edge))
        model_th2.SetBinContent(bin_num, yield_frac.getVal() * n_model)

        # get values to calculate error on model yield
        error = Double(0.0)
        l_bin = sideband_hist.FindBin(l_edge)
        h_bin = sideband_hist.FindBin(h_edge)-1

        prompt_yield = prompt_hist.IntegralAndError(l_bin, h_bin, error)
        prompt_err = error
        prompt_total = prompt_hist.IntegralAndError(1, prompt_hist.GetNbinsX(), error)
        prompt_total_err = error
        (prompt_norm, prompt_norm_err) = propagateError("quotient", n_prompt.getVal(),
                                                        n_prompt.errorVar().getVal(),
                                                        prompt_total, prompt_total_err)

        displaced_yield = displaced_hist.IntegralAndError(l_bin, h_bin, error)
        displaced_err = error
        displaced_total = displaced_hist.IntegralAndError(1, displaced_hist.GetNbinsX(), error)
        displaced_total_err = error
        (displaced_norm, displaced_norm_err) = propagateError("quotient", n_displaced.getVal(),
                                                              n_displaced.errorVar().getVal(),
                                                              displaced_total, displaced_total_err)

        # calulate error and fill TH2
        # account for both statistical and fit uncertainty
        (scaled_prompt, scaled_prompt_err) = propagateError("product", prompt_yield, prompt_err,
                                                            prompt_norm, prompt_norm_err)
        (scaled_displaced, scaled_displaced_err) = propagateError("product", displaced_yield, displaced_err,
                                                                 displaced_norm, displaced_norm_err)
        (_, model_error) = propagateError("sum", scaled_prompt, scaled_prompt_err,
                                          scaled_displaced, scaled_displaced_err)
        model_th2.SetBinError(bin_num, model_error)

model_th2.SetOption("colz texte")
model_th2.GetXaxis().SetTitle(sidebands["x"]["name"])
model_th2.GetYaxis().SetTitle(sidebands["y"]["name"])
model_th2.Draw()
model_th2.Write()

output_file.Close()
