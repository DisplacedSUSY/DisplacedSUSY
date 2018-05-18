#!/usr/bin/env python
import sys
import os
import re
import math
from array import array
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from ROOT import TFile, TCanvas, gPad, gROOT, TH1, TGraphAsymmErrors, TMultiGraph, TLegend, Double

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-r", "--rebin", action="store_true", dest="rebin", default=False,
                  help="local configuration file")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")

gROOT.SetBatch()

out_file = TFile(output_file_name, "recreate")

for plot in plots:
    combined_plot = TMultiGraph();
    combined_plot.SetTitle(";"+plot["x_axis_title"]+";Efficiency")
    legend = TLegend(0.35,0.35,0.85,0.5)
    eff_and_err = {}

    for pair in plot["hist_pairs"]:
        in_file = TFile(pair["input_file"])
        pass_hist = in_file.Get(pair["pass_hist"]).Clone()
        total_hist = in_file.Get(pair["total_hist"]).Clone()

        bins_array = array('d',plot["bins"])
        rebinned_pass  = pass_hist.Rebin(len(bins_array)-1, "Rebinned pass hist", bins_array)
        rebinned_total = total_hist.Rebin(len(bins_array)-1, "Rebinned total hist", bins_array)

        if arguments.rebin:
            eff_plot = TGraphAsymmErrors(rebinned_pass, rebinned_total)
        else:
            eff_plot = TGraphAsymmErrors(pass_hist, total_hist)
        eff_plot.SetLineColor(pair["color"])
        eff_plot.SetLineWidth(1)
        eff_plot.SetMarkerStyle(21)
        eff_plot.SetMarkerColor(pair["color"])
        eff_plot.SetMarkerSize(1)

        # Record efficiency and error of last bin
        x, y = Double(0.0), Double(0.0)
        eff_plot.GetPoint(eff_plot.GetN()-1, x, y)
        y_err = eff_plot.GetErrorY(eff_plot.GetN()-1)
        eff_and_err[pair["type"]] = {"eff" : y, "err" : y_err}
	
        # eff_plot.Fit("pol1","","",65,500)
        combined_plot.Add(eff_plot)
        legend.AddEntry(eff_plot, pair["label"])

    (sf, sf_err) = propagateError("quotient", eff_and_err['data']["eff"], eff_and_err['data']["err"],
                                              eff_and_err['mc']["eff"], eff_and_err['mc']["err"])
    print plot["channel"], "-- scaleFactor: ", sf, "-- scaleFactorError: ", sf_err


    canvas = TCanvas(plot["channel"], plot["channel"], 700, 700)
    combined_plot.Draw("ALP")
    combined_plot.SetMinimum(0.)
    combined_plot.SetMaximum(1.)
    legend.Draw()
    canvas.Update()
    #canvas.SaveAs(plot["channel"]+".png")
    out_file.cd()
    canvas.Write()

in_file.Close()
out_file.Close()
