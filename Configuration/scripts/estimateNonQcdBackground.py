#!/usr/bin/env python
import sys
import os
import re
from optparse import OptionParser
from ROOT import TFile, TCanvas, TGraphAsymmErrors, TMultiGraph, TLegend, Double, gROOT

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
    output_path = "condor/" + arguments.condorDir + "/"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
else:
    print "you forgot to specify a condor directory with -w"
    sys.exit(1)

gROOT.SetBatch()

# pick good TColors
colors = [1,2,3,4,6,7,8,9,11,29,33,36,38,40,45,48]
color_ix = 0

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

x_multigraph = TMultiGraph()
y_multigraph = TMultiGraph()
x_legend = TLegend()
y_legend = TLegend()

for sample in samples:
    in_file = TFile(output_path+sample+".root")
    in_hist = in_file.Get(plot)

    x_eff_hist = makeEfficiencyHist(in_hist.ProjectionX().Clone())
    y_eff_hist = makeEfficiencyHist(in_hist.ProjectionY().Clone())
    x_eff_hist.SetLineColor(colors[color_ix])
    y_eff_hist.SetLineColor(colors[color_ix])
    color_ix += 1

    x_multigraph.Add(x_eff_hist)
    y_multigraph.Add(y_eff_hist)
    x_multigraph.SetTitle(";"+in_hist.GetXaxis().GetTitle()+";Efficiency")
    y_multigraph.SetTitle(";"+in_hist.GetYaxis().GetTitle()+";Efficiency")

    x_legend.AddEntry(x_eff_hist, sample, "elp")
    y_legend.AddEntry(y_eff_hist, sample, "elp")


# plot everything and make output file
out_file = TFile(output_path+"nonQcdBgEstimate.root", "recreate")
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
