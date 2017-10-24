#!/usr/bin/env python
import sys
import os
import re
from array import array
from optparse import OptionParser
from ROOT import TFile, TCanvas, gPad, TH1, TGraphAsymmErrors, TMultiGraph, TLegend, Double

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")


for plot in plots:
    combined_plot = TMultiGraph();
    combined_plot.SetTitle(";"+plot["x_axis_title"]+";Efficiency")
    legend = TLegend(0.35,0.35,0.85,0.5)
    efficiencies = []

    for pair in plot["hist_pairs"]:
        input_file = TFile(pair["input_file"])
        pass_hist = input_file.Get(pair["pass_hist"]).Clone()
        total_hist = input_file.Get(pair["total_hist"]).Clone()

        bins_array = array('d',plot["bins"])
        rebinned_pass  = pass_hist.Rebin(len(bins_array)-1, "Rebinned pass hist", bins_array)
        rebinned_total = total_hist.Rebin(len(bins_array)-1, "Rebinned total hist", bins_array)

        eff_plot = TGraphAsymmErrors(rebinned_pass, rebinned_total)
        eff_plot.SetLineColor(pair["color"])
        eff_plot.SetLineWidth(1)
        eff_plot.SetMarkerStyle(21)
        eff_plot.SetMarkerColor(pair["color"])
        eff_plot.SetMarkerSize(1)

        # Record efficiency of last bin
        x, y = Double(0.0), Double(0.0)
        eff_plot.GetPoint(eff_plot.GetN()-1, x, y)
        efficiencies.append(y)

        combined_plot.Add(eff_plot)
        legend.AddEntry(eff_plot, pair["label"])

    #print plot["channel"]
    #print efficiencies[0]/efficiencies[1]
    canvas = TCanvas(plot["channel"], plot["channel"], 700, 700)
    combined_plot.Draw("ALP")
    combined_plot.SetMinimum(0.)
    combined_plot.SetMaximum(1.)
    legend.Draw()
    canvas.Update()
    canvas.SaveAs(plot["channel"]+".png")

input_file.Close()

