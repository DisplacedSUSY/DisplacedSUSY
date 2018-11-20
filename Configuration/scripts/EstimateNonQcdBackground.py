#!/usr/bin/env python

import time
from ROOT import TFile, TCanvas, TGraphAsymmErrors, TMultiGraph, TLegend, Double, gPad

#condor_dir = "EEPreselection_2017Analysis_26July2018"
condor_dir = "EMuPreselection_2017Analysis_28July2018"

#plot = "PreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_500um"
plot = "PreselectionPlotter/Electron-muon-beamspot Plots/electronAbsD0_vs_muonAbsD0_500um"

samples = [
    'DYJetsToLL',
    'TTJets_inclusive',
    'SingleTop',
    'Diboson',
]



def makeEfficiencyHist(in_hist):
    last_bin = in_hist.GetXaxis().GetLast()
    total_error = Double(0.0)
    n_total = in_hist.IntegralAndError(0, last_bin, total_error)

    total_hist = in_hist.Clone()
    pass_hist  = in_hist.Clone()

    for d0_bin in range(0, last_bin):
        total_hist.SetBinContent(d0_bin, n_total)
        total_hist.SetBinError(d0_bin, total_error)

        pass_error = Double(0.0)
        n_pass = in_hist.IntegralAndError(d0_bin, last_bin, pass_error)

        # if no events pass d0 cut, use last non-zero value
        if n_pass == 0.0:
            n_pass = last_n_pass
            pass_error = last_pass_error

        last_n_pass = n_pass
        last_pass_error = pass_error

        pass_hist.SetBinContent(d0_bin, n_pass)
        pass_hist.SetBinError(d0_bin, pass_error)

    return TGraphAsymmErrors(pass_hist, total_hist)

###############################################################################

colors = [1,2,3,4,6,7,8,9,11,29,33,36,38,40,45,48]
color_ix = 0

x_multigraph = TMultiGraph()
y_multigraph = TMultiGraph()
x_legend = TLegend()
y_legend = TLegend()

for sample in samples:
    in_file = TFile("condor/"+condor_dir+"/"+sample+".root")
    in_hist = in_file.Get(plot)

    x_eff_hist = makeEfficiencyHist(in_hist.ProjectionX().Clone())
    y_eff_hist = makeEfficiencyHist(in_hist.ProjectionY().Clone())

    x_eff_hist.SetLineColor(colors[color_ix])
    y_eff_hist.SetLineColor(colors[color_ix])
    color_ix += 1

    x_multigraph.Add(x_eff_hist)
    y_multigraph.Add(y_eff_hist)

    x_legend.AddEntry(x_eff_hist, sample, "elp")
    y_legend.AddEntry(y_eff_hist, sample, "elp")

    x_multigraph.SetTitle(";"+in_hist.GetXaxis().GetTitle()+";Efficiency")
    y_multigraph.SetTitle(";"+in_hist.GetYaxis().GetTitle()+";Efficiency")

out_file = TFile("nonQcdBgEstimate.root", "recreate")
x_canvas = TCanvas("x", "x", 100, 100, 700, 700)
x_canvas.SetLogy()
x_multigraph.Draw("ap")
x_legend.Draw()
x_canvas.Write()
y_canvas = TCanvas("y", "y", 100, 100, 700, 700)
y_canvas.SetLogy()
y_multigraph.Draw("ap")
y_legend.Draw()
y_canvas.Write()
