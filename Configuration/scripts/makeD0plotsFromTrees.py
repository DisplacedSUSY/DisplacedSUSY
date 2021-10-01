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
                  help="make bkg MC simulation version of d0-d0 plot")
parser.add_option("-s", "--signal", action="store_true", dest="signal", default=False,
                  help="add signal to data d0-d0 plot")


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


from ROOT import gROOT, gStyle, TFile, TCanvas, TH2F, TPaveLabel, TLegend, TColor, TLine

gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
if arguments.signal:
    gStyle.SetCanvasDefH(675)
else:
    gStyle.SetCanvasDefH(600)
gStyle.SetCanvasDefW(600)
gStyle.SetCanvasDefX(0)
gStyle.SetCanvasDefY(0)
gStyle.SetPadTopMargin(0.2)
gStyle.SetPadBottomMargin(0.2)
gStyle.SetPadLeftMargin(0.2)
gStyle.SetPadRightMargin(0.2)
gStyle.SetTitleColor(1, "XYZ")
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.05, "XYZ")
gStyle.SetTitleXSize(0.04)
gStyle.SetTitleXOffset(1.25)
gStyle.SetTitleYSize(0.04)
gStyle.SetTitleYOffset(1.5)
gStyle.SetTitleOffset(1.25,"Z")
gStyle.SetTextAlign(12)
gStyle.SetLabelColor(1, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelOffset(0.005, "XZ")
gStyle.SetLabelOffset(0.01, "Y")
gStyle.SetLabelSize(0.04, "XYZ")
gStyle.SetAxisColor(1, "XYZ")
gStyle.SetStripDecimals(True)
gStyle.SetTickLength(0.03, "XYZ")
gStyle.SetNdivisions(505, "XYZ")
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

#make colz in shades of blue (near-white to blue)
nContours = 500
stops = [0, 1]
red =   [0.9, 0]
green = [1, 0.4]
blue =  [1, 1]

s = array('d', stops)
r = array('d', red)
g = array('d', green)
b = array('d', blue)

length = len(s)
TColor.CreateGradientColorTable(length, s, r, g, b, nContours)
gStyle.SetNumberContours(nContours)

gROOT.ForceStyle()

#bestest place for lumi. label, in top left corner
topLeft_x_left    = 0.2
y_bottom  = 0.8
topLeft_x_right   = 0.6
y_top     = 0.85

#position for header
header_x_left    = 0.50
header_x_right   = 0.86

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
if arguments.mc or arguments.diagramPlot or arguments.signal:
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


if arguments.diagramPlot:
    LumiLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS #bf{#it{Simulation}}","NDC")
    LumiLabel.SetTextSize(0.8)
elif arguments.mc:
    LumiLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS #bf{#it{Simulation Supplementary}}","NDC")
    LumiLabel.SetTextSize(0.78)
else:
    LumiLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS #bf{#it{Supplementary}}","NDC")
    LumiLabel.SetTextSize(0.8)
LumiLabel.SetTextFont(62)
LumiLabel.SetTextAlign(12)
LumiLabel.SetBorderSize(0)
LumiLabel.SetFillColor(0)
LumiLabel.SetFillStyle(0)

if arguments.mc or arguments.diagramPlot:
    LumiPrelimLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS #bf{#it{Simulation Preliminary}}","NDC")
else:
    LumiPrelimLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS #bf{#it{Preliminary}}","NDC")
LumiPrelimLabel.SetTextFont(62)
LumiPrelimLabel.SetTextSize(0.8)
LumiPrelimLabel.SetTextAlign(12)
LumiPrelimLabel.SetBorderSize(0)
LumiPrelimLabel.SetFillColor(0)
LumiPrelimLabel.SetFillStyle(0)

break_left = A_x_left*1.3
break_right = A_x_left*1.6
break_bottom = A_y_bottom*1.3
break_top = A_y_bottom*1.6

xAxisBreak = TLine(break_left,A_y_bottom-0.01,break_right,A_y_bottom-0.01)
xAxisBreak.SetLineColor(0)
xAxisBreak.SetLineWidth(5)

xAxisBreakDiag1 = TLine(break_left*0.95,A_y_bottom*0.8,break_left*1.05,A_y_bottom*1.2)
xAxisBreakDiag1.SetLineColor(1)
xAxisBreakDiag1.SetLineWidth(4)

xAxisBreakDiag2 = TLine(break_right*0.95,A_y_bottom*0.8,break_right*1.05,A_y_bottom*1.2)
xAxisBreakDiag2.SetLineColor(1)
xAxisBreakDiag2.SetLineWidth(4)

yAxisBreak = TLine(A_x_left-0.01,break_bottom,A_x_left-0.01,break_top)
yAxisBreak.SetLineColor(0)
yAxisBreak.SetLineWidth(5)

yAxisBreakDiag1 = TLine(A_x_left*0.8,break_bottom*1.05,A_x_left*1.2,break_bottom*0.95)
yAxisBreakDiag1.SetLineColor(1)
yAxisBreakDiag1.SetLineWidth(4)

yAxisBreakDiag2 = TLine(A_x_left*0.8,break_top*1.05,A_x_left*1.2,break_top*0.95)
yAxisBreakDiag2.SetLineColor(1)
yAxisBreakDiag2.SetLineWidth(4)

zeroLabelx = TPaveLabel(A_x_left*0.8,0.35,A_x_left*1.4,0.75,"0","nb")
zeroLabelx.SetTextFont(42)
zeroLabelx.SetTextSize(1)
zeroLabelx.SetTextAlign(22)
zeroLabelx.SetBorderSize(0)
zeroLabelx.SetLineWidth(0)
zeroLabelx.SetFillColor(0)
zeroLabelx.SetFillStyle(1001)

zeroLabely = TPaveLabel(0.5,A_y_bottom*0.65,0.9,A_y_bottom*1.45,"0","nb")
zeroLabely.SetTextFont(42)
zeroLabely.SetTextSize(0.98)
zeroLabely.SetTextAlign(22)
zeroLabely.SetBorderSize(0)
zeroLabely.SetLineWidth(0)
zeroLabely.SetFillColor(0)
zeroLabely.SetFillStyle(1001)

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
        xTitle = "|d^{#kern[0.2]{b}}_{#kern[0.2]{0}}| [#mum]" #kern puts a bit of extra space
        yTitle = "|d^{#kern[0.2]{a}}_{#kern[0.2]{0}}| [#mum]"
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

log_100000um_bins = [1,10,100,500,1000,5000,10000,100000]
y_log_100000um_bins = [1,10,100,500,1000,5000,10000,100000,300000]
nbins = int(len(log_100000um_bins)-1)
nbinsY = int(len(y_log_100000um_bins)-1)
if arguments.signal:
    h = TH2F("h","",nbins,array('d',log_100000um_bins),nbinsY,array('d',y_log_100000um_bins))
else:
    h = TH2F("h","",nbins,array('d',log_100000um_bins),nbins,array('d',log_100000um_bins))
h.SetTitle(";"+xTitle+";"+yTitle+";Events / #mum^{2}")
h.SetFillColor(4)
h.SetLineWidth(0)
totalCount = 0
srCount = 0

hSignal = TH2F("hSignal","",nbins,array('d',log_100000um_bins),nbinsY,array('d',y_log_100000um_bins))
hSignal.SetTitle(";"+xTitle+";"+yTitle+";Events")
hSignal.SetLineColor(1)

# get approximate lumi*xs weight from equivalent sample that was merged with mergeOut.py
def get_lumi_xs_weight(file_path):
    file_path = file_path.replace("putHadd","")
    f = TFile(file_path)
    hist_path = "PreselectionCutFlowPlotter/eventCounter"
    try:
        h = f.Get(hist_path).Clone()
    except ReferenceError:
        raise IOError("Could not load {} from {}".format(hist_path, file_path))
    return h.Integral() / h.GetEntries()

for dataset in datasets:

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

    if arguments.mc:
        lumi_xs_weight = get_lumi_xs_weight(fileName)

    for iEntry in tree:
        if arguments.mc:
            weight_product = lumi_xs_weight*getattr(tree, "weights_weightProduct")
        else:
            weight_product = 1.0

        if not (dataset.startswith("stopTo") and arguments.signal):
            totalCount += 1
        d01 = getattr(iEntry,var1)
        d02 = getattr(iEntry,var2)
        if d01<1.:
            d01 = 1.1
        if d02<1.:
            d02 = 1.1
        #print "d01 is: " + str(d01) + " d02 is: " + str(d02)
        if dataset.startswith("stopTo") and arguments.signal:
            hSignal.Fill(d01,d02,weight_product)
        else:
            h.Fill(d01,d02,weight_product)

        if (not (dataset.startswith("stopTo") and arguments.signal)) and d01>100. and d02>100.:
            srCount += 1

# divide bin contents by bin area
for hist in [h]:
    x_axis = hist.GetXaxis()
    y_axis = hist.GetYaxis()
    # loop over bins
    for i in range(1, x_axis.GetNbins()+1):
        for j in range(1, y_axis.GetNbins()+1):
            x_width = x_axis.GetBinWidth(i)
            y_width = y_axis.GetBinWidth(j)
            # account for skipped 0-1um range when filling hist
            if i == 1:
                x_width += 1
            if j == 1:
                y_width += 1
            area = x_width*y_width
            content = hist.GetBinContent(i, j)
            hist.SetBinContent(i, j, content/float(area))

    #Hists.append(h)
    inputFile.Close()

h.GetZaxis().SetRangeUser(1e-7, 1e5)
#h.GetZaxis().SetRangeUser(1e-11, 1e-3)
print "total number of events is: " + str(totalCount)
print "total number of events in inclusive SR is: " + str(srCount)
print "maximum bin content is: "+str(h.GetBinContent(h.GetMaximumBin()))


if arguments.signal:
    legend = TLegend(topLeft_x_left, 0.75, 0.8, 0.8)
    legend.SetTextSize(0.025)
    legend.SetBorderSize(1)
    legend.SetFillColor(0)
    legend.SetLineWidth(2)
    legend.SetFillStyle(1001)
    legend.AddEntry(hSignal, "\\~{\\text{t}} \\to \\text{b}\\ell, \\text{m}_{\\~{\\text{t}}}\\text{ = 1500 GeV, }c\\tau_{\\text{}_{0}}\\text{ = 1 cm}", 'f')

Canvas.cd()
if(arguments.diagramPlot):
    h.Draw("colz")
    LumiLabel.Draw()
    HeaderLabel.Draw()
    ABox.Draw()
    zeroLabelx.Draw()
    zeroLabely.Draw()
    xAxisBreak.Draw()
    xAxisBreakDiag1.Draw()
    xAxisBreakDiag2.Draw()
    yAxisBreak.Draw()
    yAxisBreakDiag1.Draw()
    yAxisBreakDiag2.Draw()
    BBox.Draw()
    CBox.Draw()
    IBox.Draw()
    IIBox.Draw()
    IIIBox.Draw()
    IVBox.Draw()
    Canvas.SaveAs("./abcdMethod.pdf")
    Canvas.SaveAs("./abcdMethod.png")
elif arguments.signal:
    hSignal.Draw("colz")
    LumiLabel.Draw()
    HeaderLabel.Draw()
    zeroLabelx.Draw()
    zeroLabely.Draw()
    xAxisBreak.Draw()
    xAxisBreakDiag1.Draw()
    xAxisBreakDiag2.Draw()
    yAxisBreak.Draw()
    yAxisBreakDiag1.Draw()
    yAxisBreakDiag2.Draw()
    legend.Draw()
    Canvas.SaveAs("./d0vsd0_" + analysisChannel + "_withSignal.ps")
    Canvas.SaveAs("./d0vsd0_" + analysisChannel + "_withSignal.png")
else:
    h.Draw("colz")
    LumiLabel.Draw()
    HeaderLabel.Draw()
    zeroLabelx.Draw()
    zeroLabely.Draw()
    xAxisBreak.Draw()
    xAxisBreakDiag1.Draw()
    xAxisBreakDiag2.Draw()
    yAxisBreak.Draw()
    yAxisBreakDiag1.Draw()
    yAxisBreakDiag2.Draw()
    Canvas.SaveAs("./d0vsd0_" + analysisChannel + ".pdf")
    Canvas.SaveAs("./d0vsd0_" + analysisChannel + ".png")

if(arguments.diagramPlot):
    CanvasPrelim.cd()
    h.Draw("colz")
    LumiPrelimLabel.Draw()
    HeaderLabel.Draw()
    ABox.Draw()
    zeroLabelx.Draw()
    zeroLabely.Draw()
    xAxisBreak.Draw()
    xAxisBreakDiag1.Draw()
    xAxisBreakDiag2.Draw()
    yAxisBreak.Draw()
    yAxisBreakDiag1.Draw()
    yAxisBreakDiag2.Draw()
    BBox.Draw()
    CBox.Draw()
    IBox.Draw()
    IIBox.Draw()
    IIIBox.Draw()
    IVBox.Draw()
    CanvasPrelim.SaveAs("./abcdMethod_CMSPreliminary.pdf")
    CanvasPrelim.SaveAs("./abcdMethod_CMSPreliminary.png")


#write histograms to root file for hepdata
if(arguments.diagramPlot):
    outFileSuffix = "bkg_"+analysisChannel
elif arguments.signal:
    outFileSuffix = "dataWithSignal_"+analysisChannel
else:
    outFileSuffix = "data_"+analysisChannel

outFilePrefix = "condor/%s/" % arguments.condorDir
outputFile = TFile(outFilePrefix+"d0plots_"+outFileSuffix+".root", "RECREATE")
outputFile.cd()
h.Write()
if arguments.signal:
    hSignal.Write()
outputFile.Close()
