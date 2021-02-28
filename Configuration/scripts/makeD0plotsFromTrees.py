#!/usr/bin/env python

# data trees made from events that pass the Preselection

import sys
import os
import re
import math
from array import *
from decimal import *
from optparse import OptionParser
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *
from OSUT3Analysis.Configuration.cutUtilities import *

### parse the command-line options

parser = OptionParser()
#parser = set_commandline_arguments(parser)
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")
parser.add_option("-d", "--diagramPlot", action="store_true", dest="diagramPlot", default=False,
                  help="make diagram version of d0-d0 plot")
parser.add_option("-m", "--mc", action="store_true", dest="mc", default=False,
                  help="make MC simulation version of d0-d0 plot")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "you forgot to specify a config file with -l"
    sys.exit(1)

if not arguments.condorDir:
    print "you forgot to specify a condor directory with -w"
    sys.exit(1)
else:
    condirDir = arguments.condorDir


from ROOT import gROOT, gStyle, TFile, TCanvas, TH2F, TPaveLabel

gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetCanvasDefH(600)
gStyle.SetCanvasDefW(600)
gStyle.SetCanvasDefX(0)
gStyle.SetCanvasDefY(0)
gStyle.SetPadTopMargin(0.15)
gStyle.SetPadBottomMargin(0.15)
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadRightMargin(0.15)
gStyle.SetTitleColor(1, "XYZ")
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.05, "XYZ")
gStyle.SetTitleXSize(0.04)
gStyle.SetTitleXOffset(1.25)
gStyle.SetTitleYSize(0.04)
gStyle.SetTitleYOffset(1.5)
gStyle.SetTextAlign(12)
gStyle.SetLabelColor(1, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelOffset(0.005, "XYZ")
gStyle.SetLabelSize(0.04, "XYZ")
gStyle.SetAxisColor(1, "XYZ")
gStyle.SetStripDecimals(True)
gStyle.SetTickLength(0.03, "XYZ")
gStyle.SetNdivisions(505, "XYZ")
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gROOT.ForceStyle()

#bestest place for lumi. label, in top left corner
topLeft_x_left    = 0.15
y_bottom  = 0.85
topLeft_x_right   = 0.50
y_top     = 0.9

#position for header
header_x_left    = 0.55
header_x_right   = 0.91

#position for A region (user coord)
A_x_left = 1
A_y_bottom = 1
A_x_right = 100
A_y_top = 100

#position for B region (user coord)
B_x_left = 1
B_y_bottom = 100
B_x_right = 100
B_y_top = 100000

#position for C region (user coord)
C_x_left = 100
C_y_bottom = 1
C_x_right = 100000
C_y_top = 100

#position for SR I (user coord)
I_x_left = 100
I_y_bottom = 100
I_x_right = 500
I_y_top = 500

#position for SR II (user coord)
II_x_left = 500
II_y_bottom = 100
II_x_right = 100000
II_y_top = 500

#position for SR III (user coord)
III_x_left = 100
III_y_bottom = 500
III_x_right = 500
III_y_top = 100000

#position for SR IV (user coord)
IV_x_left = 500
IV_y_bottom = 500
IV_x_right = 100000
IV_y_top = 100000


LumiInFb = intLumi/1000.
#LumiText = str.format('{0:.1f}', LumiInFb) + " fb^{-1}"
LumiText = "{:d} fb^{{-1}}".format(int(round(LumiInFb)))
if arguments.mc or arguments.diagramPlot:
    HeaderText = "(13 TeV)"
else:
    HeaderText = LumiText + " (13 TeV)"

HeaderLabel = TPaveLabel(header_x_left,y_bottom,header_x_right,y_top,HeaderText,"NDC")
HeaderLabel.SetTextAlign(32)
HeaderLabel.SetTextFont(42)
HeaderLabel.SetTextSize(0.697674)
HeaderLabel.SetBorderSize(0)
HeaderLabel.SetFillColor(0)
HeaderLabel.SetFillStyle(0)

if arguments.mc or arguments.diagramPlot:
    LumiLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS Simulation","NDC")
else:
    LumiLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS","NDC")
LumiLabel.SetTextFont(62)
LumiLabel.SetTextSize(0.8)
LumiLabel.SetTextAlign(12)
LumiLabel.SetBorderSize(0)
LumiLabel.SetFillColor(0)
LumiLabel.SetFillStyle(0)

if arguments.mc or arguments.diagramPlot:
    LumiPrelimLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS Simulation Preliminary","NDC")
else:
    LumiPrelimLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS Preliminary","NDC")
LumiPrelimLabel.SetTextFont(62)
LumiPrelimLabel.SetTextSize(0.8)
LumiPrelimLabel.SetTextAlign(12)
LumiPrelimLabel.SetBorderSize(0)
LumiPrelimLabel.SetFillColor(0)
LumiPrelimLabel.SetFillStyle(0)

ABox = TPaveLabel(A_x_left,A_y_bottom,A_x_right,A_y_top,"A","nb")
ABox.SetTextFont(62)
ABox.SetTextSize(0.3)
ABox.SetTextAlign(22)
ABox.SetBorderSize(4)
ABox.SetLineWidth(4)
ABox.SetFillColor(0)
ABox.SetFillStyle(0)

BBox = TPaveLabel(B_x_left,B_y_bottom,B_x_right,B_y_top,"B","nb")
BBox.SetTextFont(62)
BBox.SetTextSize(0.2)
BBox.SetTextAlign(22)
BBox.SetBorderSize(4)
BBox.SetLineWidth(4)
BBox.SetFillColor(0)
BBox.SetFillStyle(0)

CBox = TPaveLabel(C_x_left,C_y_bottom,C_x_right,C_y_top,"C","nb")
CBox.SetTextFont(62)
CBox.SetTextSize(0.3)
CBox.SetTextAlign(22)
CBox.SetBorderSize(4)
CBox.SetLineWidth(4)
CBox.SetFillColor(0)
CBox.SetFillStyle(0)

IBox = TPaveLabel(I_x_left,I_y_bottom,I_x_right,I_y_top,"SR I","nb")
IBox.SetTextFont(62)
IBox.SetTextSize(0.4)
IBox.SetTextAlign(22)
IBox.SetBorderSize(4)
IBox.SetLineWidth(4)
IBox.SetFillColor(0)
IBox.SetFillStyle(0)

IIBox = TPaveLabel(II_x_left,II_y_bottom,II_x_right,II_y_top,"SR II","nb")
IIBox.SetTextFont(62)
IIBox.SetTextSize(0.6)
IIBox.SetTextAlign(22)
IIBox.SetBorderSize(4)
IIBox.SetLineWidth(4)
IIBox.SetFillColor(0)
IIBox.SetFillStyle(0)

IIIBox = TPaveLabel(III_x_left,III_y_bottom,III_x_right,III_y_top,"SR III","nb")
IIIBox.SetTextFont(62)
IIIBox.SetTextSize(0.1)
IIIBox.SetTextAlign(22)
IIIBox.SetBorderSize(4)
IIIBox.SetLineWidth(4)
IIIBox.SetFillColor(0)
IIIBox.SetFillStyle(0)

IVBox = TPaveLabel(IV_x_left,IV_y_bottom,IV_x_right,IV_y_top,"SR IV","nb")
IVBox.SetTextFont(62)
IVBox.SetTextSize(0.2)
IVBox.SetTextAlign(22)
IVBox.SetBorderSize(4)
IVBox.SetLineWidth(4)
IVBox.SetFillColor(0)
IVBox.SetFillStyle(0)

if analysisChannel == "mumu":
    var1 = "muon_beamspot_absD0Muon1"
    var2 = "muon_beamspot_absD0Muon0"
    xTitle = "Subleading muon |d_{0}| [#mum]"
    yTitle = "Leading muon |d_{0}| [#mum]"
elif analysisChannel == "emu":
    var1 = "muon_beamspot_absD0Muon0"
    var2 = "electron_beamspot_absD0Electron0"
    if(arguments.diagramPlot):
        xTitle = "|d^{b}_{0}| [#mum]"
        yTitle = "|d^{a}_{0}| [#mum]"
    else:
        xTitle = "Leading muon |d_{0}| [#mum]"
        yTitle = "Leading electron |d_{0}| [#mum]"
elif analysisChannel == "ee":
    var1 = "electron_beamspot_absD0Electron1"
    var2 = "electron_beamspot_absD0Electron0"
    xTitle = "Subleading electron |d_{0}| [#mum]"
    yTitle = "Leading electron |d_{0}| [#mum]"

Canvas = TCanvas("canvas","")
Canvas.SetHighLightColor(2)
Canvas.Range(-72.16495,-10.50091,516.9367,82.84142)
Canvas.SetFillColor(0)
Canvas.SetBorderMode(0)
Canvas.SetBorderSize(2)
Canvas.SetTickx(1)
Canvas.SetTicky(1)
Canvas.SetFrameBorderMode(0)
Canvas.SetFrameBorderMode(0)
Canvas.SetLogx()
Canvas.SetLogy()
Canvas.SetLogz()

CanvasPrelim = TCanvas("canvasPreliminary","")
CanvasPrelim.SetHighLightColor(2)
CanvasPrelim.Range(-72.16495,-10.50091,516.9367,82.84142)
CanvasPrelim.SetFillColor(0)
CanvasPrelim.SetBorderMode(0)
CanvasPrelim.SetBorderSize(2)
CanvasPrelim.SetTickx(1)
CanvasPrelim.SetTicky(1)
CanvasPrelim.SetFrameBorderMode(0)
CanvasPrelim.SetFrameBorderMode(0)
CanvasPrelim.SetLogx()
CanvasPrelim.SetLogy()
CanvasPrelim.SetLogz()

log_100000um_bins = [1,10,100,500,1000,5000,10000,50000,100000]
nbins = int(len(log_100000um_bins)-1)
h = TH2F("h","",nbins,array('d',log_100000um_bins),nbins,array('d',log_100000um_bins))
h.SetTitle(";"+xTitle+";"+yTitle)

fileName = "condor/%s/mergeOutputHadd/%s.root" % (arguments.condorDir,dataset)
inputFile = TFile(fileName)
if(inputFile.IsZombie()):
    print "input file is zombie"
    sys.exit(1)
inputFile.cd()
keys = []
for key in inputFile.GetListOfKeys():
    keys.append(key.GetName())
    if (key.GetClassName() != "TDirectoryFile"):
        print "no TDirectoryFile"
        sys.exit(1)
if not "PreselectionTreeMaker" in keys:
    print "no Tree, setting getMeanEfficiency to -1"
    sys.exit(1)
tree = inputFile.Get("PreselectionTreeMaker/Tree")

for iEntry in tree:
    d01 = getattr(iEntry,var1)
    d02 = getattr(iEntry,var2)
    if d01<1.:
        d01 = 1.1
    if d02<1.:
        d02 = 1.1
    #print "d01 is: " + str(d01) + " d02 is: " + str(d02)
    h.Fill(d01,d02)

inputFile.Close()


Canvas.cd()
h.Draw("colz")
LumiLabel.Draw()
HeaderLabel.Draw()
if(arguments.diagramPlot):
    ABox.Draw()
    BBox.Draw()
    CBox.Draw()
    IBox.Draw()
    IIBox.Draw()
    IIIBox.Draw()
    IVBox.Draw()
    Canvas.SaveAs("./abcdMethod.pdf")
else:
    Canvas.SaveAs("./d0vsd0_" + analysisChannel + ".pdf")

CanvasPrelim.cd()
h.Draw("colz")
LumiPrelimLabel.Draw()
HeaderLabel.Draw()
if(arguments.diagramPlot):
    ABox.Draw()
    BBox.Draw()
    CBox.Draw()
    IBox.Draw()
    IIBox.Draw()
    IIIBox.Draw()
    IVBox.Draw()
    CanvasPrelim.SaveAs("./abcdMethod_CMSPreliminary.pdf")
else:
    CanvasPrelim.SaveAs("./d0vsd0_" + analysisChannel + "_CMSPreliminary.pdf")
