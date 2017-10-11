#!/usr/bin/env python
import sys
import os
import re
from array import array
from optparse import OptionParser
from ROOT import TFile, TCanvas, gPad, TH1, TGraphAsymmErrors, TMultiGraph, TLegend

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")


for plot in plots:

    input_file = TFile(plot["input_file"])
    combined_plot = TMultiGraph();
    combined_plot.SetTitle(";"+plot["x_axis_title"]+";Efficiency")
    legend = TLegend(0.35,0.35,0.85,0.5)

    for pair in plot["hist_pairs"]:
        pass_hist = input_file.Get(pair["pass_hist"]).Clone()
        total_hist = input_file.Get(pair["total_hist"]).Clone()

        bins_array = array('d',plot["bins"])
        rebinned_pass  = pass_hist.Rebin(len(bins_array)-1, "Rebinned pass hist", bins_array)
        rebinned_total = total_hist.Rebin(len(bins_array)-1, "Rebinned total hist", bins_array)

        eff_plot = TGraphAsymmErrors(rebinned_pass, rebinned_total)
        eff_plot.SetLineColor(pair["color"])

        combined_plot.Add(eff_plot)
        legend.AddEntry(eff_plot, pair["label"])

    canvas = TCanvas(plot["channel"], plot["channel"], 700, 700)
    combined_plot.Draw("ALP")
    combined_plot.SetMinimum(0.)
    combined_plot.SetMaximum(1.)
    legend.Draw()
    canvas.Update()
    canvas.SaveAs(plot["channel"]+".png")

input_file.Close()

