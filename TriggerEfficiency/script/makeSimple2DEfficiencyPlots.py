#!/usr/bin/env python
import sys
import os
import re
from array import array
from optparse import OptionParser
from ROOT import TFile, TH1, TGraphAsymmErrors

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")

output_file = TFile(output_file_name, "RECREATE")

for f in input_files:
    input_file = TFile(f["input_file"])
    for pair in f["hist_pairs"]:
        pass_hist = input_file.Get(pair["pass_hist"]).Clone()
        total_hist = input_file.Get(pair["total_hist"]).Clone()
        pass_hist.Rebin2D(5,5)
        total_hist.Rebin2D(5,5)

        eff_hist = pass_hist.Clone()
        eff_hist.Divide(total_hist)
        eff_hist.SetTitle(pair["eff_plot_title"])
        eff_hist.GetXaxis().SetTitle(pair["x_axis_title"])
        eff_hist.GetYaxis().SetTitle(pair["y_axis_title"])

        sub_hist = total_hist.Clone()
        sub_hist.Add(pass_hist, -1)
        sub_hist.SetTitle(pair["eff_plot_title"])
        sub_hist.GetXaxis().SetTitle(pair["x_axis_title"])
        sub_hist.GetYaxis().SetTitle(pair["y_axis_title"])

        output_file.cd()
        total_hist.Write("total")
        eff_hist.Write(pair["eff_plot_title"])
        sub_hist.Write(pair["eff_plot_title"] + " Subtraction")

output_file.Close()
input_file.Close()

