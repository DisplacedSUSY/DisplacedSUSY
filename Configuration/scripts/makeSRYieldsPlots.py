#!/usr/bin/env python

# makes plot of yields in SR
# usage: python makeSRYieldsPlots.py

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

from ROOT import gROOT, gStyle, TFile, TCanvas, TH1F, TGraphAsymmErrors, TPaveLabel, TLegend, TLine

gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetCanvasDefH(600)
gStyle.SetCanvasDefW(800)
gStyle.SetCanvasDefX(0)
gStyle.SetCanvasDefY(0)
gStyle.SetPadTopMargin(0.15)
gStyle.SetPadBottomMargin(0.15)
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadRightMargin(0.05)
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
gStyle.SetLabelOffset(0.008, "XYZ")
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
header_x_left    = 0.60
header_x_right   = 0.95

#position for emu label (user coord)
#emu_y_bottom = 50 #linear y-axis
#emu_y_top = 60
emu_y_bottom = 10 #log y-axis
emu_y_top = 60
emu_x_left = 1
emu_x_right = 4

#position for ee label (user coord)
ee_x_left = 6
ee_x_right = 9

#position for mumu label (user coord)
mumu_x_left = 11
mumu_x_right = 14


HeaderText2016 = "16 fb^{-1} (13 TeV)"
HeaderText201718 = "97-102 fb^{-1} (13 TeV)"

HeaderLabel2016 = TPaveLabel(header_x_left,y_bottom,header_x_right,y_top,HeaderText2016,"NDC")
HeaderLabel2016.SetTextAlign(32)
HeaderLabel2016.SetTextFont(42)
HeaderLabel2016.SetTextSize(0.697674)

HeaderLabel201718 = TPaveLabel(header_x_left,y_bottom,header_x_right,y_top,HeaderText201718,"NDC")
HeaderLabel201718.SetTextAlign(32)
HeaderLabel201718.SetTextFont(42)
HeaderLabel201718.SetTextSize(0.697674)

LumiLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS","NDC")
LumiLabel.SetTextFont(62)
LumiLabel.SetTextSize(0.8)
LumiLabel.SetTextAlign(12)

LumiPrelimLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS Preliminary","NDC")
LumiPrelimLabel.SetTextFont(62)
LumiPrelimLabel.SetTextSize(0.8)
LumiPrelimLabel.SetTextAlign(12)

EMuLabel = TPaveLabel(emu_x_left,emu_y_bottom,emu_x_right,emu_y_top,"e#mu","nb")
EMuLabel.SetTextFont(62)
EMuLabel.SetTextSize(0.7)
EMuLabel.SetTextAlign(22)

EELabel = TPaveLabel(ee_x_left,emu_y_bottom,ee_x_right,emu_y_top,"ee","nb")
EELabel.SetTextFont(62)
EELabel.SetTextSize(0.7)
EELabel.SetTextAlign(22)

MuMuLabel = TPaveLabel(mumu_x_left,emu_y_bottom,mumu_x_right,emu_y_top,"#mu#mu","nb")
MuMuLabel.SetTextFont(62)
MuMuLabel.SetTextSize(0.7)
MuMuLabel.SetTextAlign(22)

labels = [
    HeaderLabel2016,
    HeaderLabel201718,
    LumiLabel,
    LumiPrelimLabel,
    EMuLabel,
    EELabel,
    MuMuLabel,
]

for label in labels:
    label.SetBorderSize(0)
    label.SetFillColor(0)
    label.SetFillStyle(0)


emueeLine = TLine(5,0,5,100)
eemumuLine = TLine(10,0,10,100)


Canvas2016 = TCanvas("canvas2016","")
Canvas2016Prelim = TCanvas("canvas2016Preliminary","")
Canvas201718 = TCanvas("canvas201718","")
Canvas201718Prelim = TCanvas("canvas201718Preliminary","")

canvases = [
    Canvas2016,
    Canvas2016Prelim,
    Canvas201718,
    Canvas201718Prelim,
    ]

for canvas in canvases:
    canvas.SetHighLightColor(2)
    canvas.Range(-72.16495,-10.50091,516.9367,82.84142)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetBorderSize(2)
    canvas.SetTickx(1)
    canvas.SetTicky(1)
    canvas.SetFrameBorderMode(0)
    canvas.SetFrameBorderMode(0)
    canvas.SetLogy()


hObs2016 = TH1F("hObs2016","",15,0,15)
hObs2016.SetMarkerStyle(20)
hObs2016.SetMarkerColor(1)
hObs2016.SetBinContent(1,8)   #emu SR I low pt
hObs2016.SetBinContent(2,1)   #emu SR I high pt
hObs2016.SetBinContent(3,0)   #emu SR II
hObs2016.SetBinContent(4,0)   #emu SR III
hObs2016.SetBinContent(5,0)   #emu SR IV
hObs2016.SetBinContent(6,40)  #ee SR I low pt
hObs2016.SetBinContent(7,0)   #ee SR I high pt
hObs2016.SetBinContent(8,0)   #ee SR II
hObs2016.SetBinContent(9,1)   #ee SR III
hObs2016.SetBinContent(10,0)  #ee SR IV
hObs2016.SetBinContent(11,15) #mumu SR I low pt
hObs2016.SetBinContent(12,0)  #mumu SR I high pt
hObs2016.SetBinContent(13,0)  #mumu SR II
hObs2016.SetBinContent(14,1)  #mumu SR III
hObs2016.SetBinContent(15,0)  #mumu SR IV

hObs201718 = TH1F("hObs201718","",15,0,15)
hObs201718.SetMarkerStyle(20)
hObs201718.SetMarkerColor(1)
hObs201718.SetBinContent(1,28) #emu SR I low pt
hObs201718.SetBinContent(2,3) #emu SR I high pt
hObs201718.SetBinContent(3,0) #emu SR II
hObs201718.SetBinContent(4,1) #emu SR III
hObs201718.SetBinContent(5,0) #emu SR IV
hObs201718.SetBinContent(6,48) #ee SR I low pt
hObs201718.SetBinContent(7,0) #ee SR I high pt
hObs201718.SetBinContent(8,1) #ee SR II
hObs201718.SetBinContent(9,4) #ee SR III
hObs201718.SetBinContent(10,0)#ee SR IV
hObs201718.SetBinContent(11,1)#mumu SR I low pt
hObs201718.SetBinContent(12,1)#mumu SR I high pt
hObs201718.SetBinContent(13,1)#mumu SR II
hObs201718.SetBinContent(14,1)#mumu SR III
hObs201718.SetBinContent(15,0)#mumu SR IV

hExp2016 = TH1F("hExp2016","",15,0,15)
hExp2016.SetFillStyle(1001)
hExp2016.SetFillColor(866)#kAzure+6
hExp2016.SetLineWidth(0)
hExp2016.SetBinContent(1,3.8) #emu SR I low pt
hExp2016.SetBinContent(2,0.41) #emu SR I high pt
hExp2016.SetBinContent(3,0.09) #emu SR II
hExp2016.SetBinContent(4,0.15) #emu SR III
hExp2016.SetBinContent(5,0.003) #emu SR IV
hExp2016.SetBinContent(6,18.1) #ee SR I low pt
hExp2016.SetBinContent(7,0.22) #ee SR I high pt
hExp2016.SetBinContent(8,0.51) #ee SR II
hExp2016.SetBinContent(9,0.43) #ee SR III
hExp2016.SetBinContent(10,0.01)#ee SR IV
hExp2016.SetBinContent(11,7.4)#mumu SR I low pt
hExp2016.SetBinContent(12,0.25)#mumu SR I high pt
hExp2016.SetBinContent(13,0.17)#mumu SR II
hExp2016.SetBinContent(14,0.19)#mumu SR III
hExp2016.SetBinContent(15,0.01)#mumu SR IV

hExp201718 = TH1F("hExp201718","",15,0,15)
hExp201718.SetFillStyle(1001)
hExp201718.SetFillColor(866)#kAzure+6
hExp201718.SetLineWidth(0)
hExp201718.SetBinContent(1,37.9) #emu SR I low pt
hExp201718.SetBinContent(2,0.75) #emu SR I high pt
hExp201718.SetBinContent(3,0.23) #emu SR II
hExp201718.SetBinContent(4,0.71) #emu SR III
hExp201718.SetBinContent(5,0.01) #emu SR IV
hExp201718.SetBinContent(6,62) #ee SR I low pt
hExp201718.SetBinContent(7,0.85) #ee SR I high pt
hExp201718.SetBinContent(8,2.8) #ee SR II
hExp201718.SetBinContent(9,3.6) #ee SR III
hExp201718.SetBinContent(10,0.24)#ee SR IV
hExp201718.SetBinContent(11,3.5)#mumu SR I low pt
hExp201718.SetBinContent(12,0.69)#mumu SR I high pt
hExp201718.SetBinContent(13,0.08)#mumu SR II
hExp201718.SetBinContent(14,0.14)#mumu SR III
hExp201718.SetBinContent(15,0.01)#mumu SR IV

hSig2016 = TH1F("hSig2016","",15,0,15)
hSig2016.SetLineColor(2)
hSig2016.SetLineWidth(3)
hSig2016.SetBinContent(1,0.) #emu SR I low pt
hSig2016.SetBinContent(2,0.02) #emu SR I high pt
hSig2016.SetBinContent(3,0.07) #emu SR II
hSig2016.SetBinContent(4,0.05) #emu SR III
hSig2016.SetBinContent(5,0.19) #emu SR IV
hSig2016.SetBinContent(6,0.) #ee SR I low pt
hSig2016.SetBinContent(7,0.01) #ee SR I high pt
hSig2016.SetBinContent(8,0.03) #ee SR II
hSig2016.SetBinContent(9,0.02) #ee SR III
hSig2016.SetBinContent(10,0.07)#ee SR IV
hSig2016.SetBinContent(11,0.)#mumu SR I low pt
hSig2016.SetBinContent(12,0.01)#mumu SR I high pt
hSig2016.SetBinContent(13,0.04)#mumu SR II
hSig2016.SetBinContent(14,0.03)#mumu SR III
hSig2016.SetBinContent(15,0.14)#mumu SR IV

hSig2016.SetBinError(1,0.) #emu SR I low pt
hSig2016.SetBinError(2,0.008) #emu SR I high pt
hSig2016.SetBinError(3,0.027) #emu SR II
hSig2016.SetBinError(4,0.020) #emu SR III
hSig2016.SetBinError(5,0.074) #emu SR IV
hSig2016.SetBinError(6,0.) #ee SR I low pt
hSig2016.SetBinError(7,0.002) #ee SR I high pt
hSig2016.SetBinError(8,0.005) #ee SR II
hSig2016.SetBinError(9,0.004) #ee SR III
hSig2016.SetBinError(10,0.012)#ee SR IV
hSig2016.SetBinError(11,0.)#mumu SR I low pt
hSig2016.SetBinError(12,0.007)#mumu SR I high pt
hSig2016.SetBinError(13,0.028)#mumu SR II
hSig2016.SetBinError(14,0.021)#mumu SR III
hSig2016.SetBinError(15,0.099)#mumu SR IV

hSig201718 = TH1F("hSig201718","",15,0,15)
hSig201718.SetLineColor(2)
hSig201718.SetLineWidth(3)
hSig201718.SetBinContent(1,0.01) #emu SR I low pt
hSig201718.SetBinContent(2,0.13) #emu SR I high pt
hSig201718.SetBinContent(3,0.42) #emu SR II
hSig201718.SetBinContent(4,0.31) #emu SR III
hSig201718.SetBinContent(5,1.15) #emu SR IV
hSig201718.SetBinContent(6,0.) #ee SR I low pt
hSig201718.SetBinContent(7,0.06) #ee SR I high pt
hSig201718.SetBinContent(8,0.19) #ee SR II
hSig201718.SetBinContent(9,0.15) #ee SR III
hSig201718.SetBinContent(10,0.44)#ee SR IV
hSig201718.SetBinContent(11,0.)#mumu SR I low pt
hSig201718.SetBinContent(12,0.07)#mumu SR I high pt
hSig201718.SetBinContent(13,0.23)#mumu SR II
hSig201718.SetBinContent(14,0.18)#mumu SR III
hSig201718.SetBinContent(15,0.78)#mumu SR IV

hSig201718.SetBinError(1,0.004) #emu SR I low pt
hSig201718.SetBinError(2,0.046) #emu SR I high pt
hSig201718.SetBinError(3,0.147) #emu SR II
hSig201718.SetBinError(4,0.109) #emu SR III
hSig201718.SetBinError(5,0.4) #emu SR IV
hSig201718.SetBinError(6,0.) #ee SR I low pt
hSig201718.SetBinError(7,0.016) #ee SR I high pt
hSig201718.SetBinError(8,0.051) #ee SR II
hSig201718.SetBinError(9,0.039) #ee SR III
hSig201718.SetBinError(10,0.115)#ee SR IV
hSig201718.SetBinError(11,0.)#mumu SR I low pt
hSig201718.SetBinError(12,0.032)#mumu SR I high pt
hSig201718.SetBinError(13,0.104)#mumu SR II
hSig201718.SetBinError(14,0.081)#mumu SR III
hSig201718.SetBinError(15,0.351)#mumu SR IV

def makeTGraphAsymmErrors(x, y, x_errDown, x_errUp, y_errDown, y_errUp):
    graph_arrays = [array('d', arg) for arg in [x, y, x_errDown, x_errUp, y_errDown, y_errUp]]
    return TGraphAsymmErrors(int(len(x)), *graph_arrays)

ExpUncert_x = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5]
ExpUncert_xErr = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]

ExpUncert2016_y = [3.8, 0.41, 0.09, 0.15, 0.003, 18.1, 0.22, 0.51, 0.43, 0.01,7.4,0.25,0.17,0.19,0.01]
ExpUncert2016_yErrDown = [3.8,0.41,0.09,0.15,0.003,  17.6,0.22,0.51,0.43,0.01,   3,0.11,0.11,0.12,0.01]
ExpUncert2016_yErrUp = [4.6,0.50,0.12,0.15,0.004, 4.3, 0.11, 1.02, 0.85, 0.02, 3,0.11,0.11,0.12,0.01]
hExpUncert2016 = makeTGraphAsymmErrors(ExpUncert_x, ExpUncert2016_y, ExpUncert_xErr, ExpUncert_xErr, ExpUncert2016_yErrDown, ExpUncert2016_yErrUp)
hExpUncert2016.SetFillStyle(3002)
hExpUncert2016.SetFillColor(13)
hExpUncert2016.SetLineWidth(0)

ExpUncert201718_y = [37.9,0.75,0.23,0.71,0.01,62,0.85,2.8,3.6,0.24,3.5,0.69,0.08,0.14,0.01]
ExpUncert201718_yErrDown = [12.8,0.34,0.23,0.71,0.01,  17, 0.35, 1.1, 1.4, 0.09,  1.5, 0.31, 0.08, 0.14, 0.01]
ExpUncert201718_yErrUp = [12.8, 0.41, 0.27, 0.76, 0.02,   18, 0.33, 1.1, 1.4, 0.10,   1.5, 0.31, 0.12, 0.19, 0.02]
hExpUncert201718 = makeTGraphAsymmErrors(ExpUncert_x, ExpUncert201718_y, ExpUncert_xErr, ExpUncert_xErr, ExpUncert201718_yErrDown, ExpUncert201718_yErrUp)
hExpUncert201718.SetFillStyle(3002)
hExpUncert201718.SetFillColor(13)
hExpUncert201718.SetLineWidth(0)

hists = [
    hObs2016,
    hObs201718,
    hExp2016,
    hExp201718,
    hSig2016,
    hSig201718,
]

for hist in hists:
    hist.SetTitle(";SR;Events / bin")
    hist.GetXaxis().SetBinLabel(1,"I, low p_{T}")
    hist.GetXaxis().SetBinLabel(2,"I, high p_{T}")
    hist.GetXaxis().SetBinLabel(3,"II")
    hist.GetXaxis().SetBinLabel(4,"III")
    hist.GetXaxis().SetBinLabel(5,"IV")
    hist.GetXaxis().SetBinLabel(6,"I, low p_{T}")
    hist.GetXaxis().SetBinLabel(7,"I, high p_{T}")
    hist.GetXaxis().SetBinLabel(8,"II")
    hist.GetXaxis().SetBinLabel(9,"III")
    hist.GetXaxis().SetBinLabel(10,"IV")
    hist.GetXaxis().SetBinLabel(11,"I, low p_{T}")
    hist.GetXaxis().SetBinLabel(12,"I, high p_{T}")
    hist.GetXaxis().SetBinLabel(13,"II")
    hist.GetXaxis().SetBinLabel(14,"III")
    hist.GetXaxis().SetBinLabel(15,"IV")
    #hist.GetYaxis().SetRangeUser(-0.1,100) # linear y axis
    hist.GetYaxis().SetRangeUser(0.001,100000) #log y axis
    for i in range(hist.GetNbinsX()):
        hist.GetXaxis().ChangeLabel(i,-1,-1,1,2)
    #hist.GetXaxis().Paint("L")

Leg = TLegend(0.2,0.6,0.8,0.8)
Leg.AddEntry(hObs2016,"Data","p")
Leg.AddEntry(hExp2016,"Background","f")
Leg.AddEntry(hExpUncert2016,"Background uncertainty","f")
Leg.AddEntry(hSig2016,"#tilde{t}#tilde{t} #rightarrow lb lb, M = 1500 GeV, c#tau = 1 cm","l")
Leg.SetBorderSize(0)

Canvas2016.cd()
hExp2016.Draw()
hExpUncert2016.Draw("e2same")
hSig2016.Draw("histesame")
hObs2016.Draw("psame")
LumiLabel.Draw()
HeaderLabel2016.Draw()
Leg.Draw()
EMuLabel.Draw()
EELabel.Draw()
MuMuLabel.Draw()
emueeLine.Draw()
eemumuLine.Draw()
Canvas2016.SaveAs("./SR2016yields.pdf")

Canvas2016Prelim.cd()
hExp2016.Draw()
hExpUncert2016.Draw("e2same")
hSig2016.Draw("histesame")
hObs2016.Draw("psame")
LumiPrelimLabel.Draw()
HeaderLabel2016.Draw()
Leg.Draw()
EMuLabel.Draw()
EELabel.Draw()
MuMuLabel.Draw()
emueeLine.Draw()
eemumuLine.Draw()
Canvas2016Prelim.SaveAs("./SR2016yields_CMSPreliminary.pdf")

Canvas201718.cd()
hExp201718.Draw()
hExpUncert201718.Draw("e2same")
hSig201718.Draw("histesame")
hObs201718.Draw("psame")
LumiLabel.Draw()
HeaderLabel201718.Draw()
Leg.Draw()
EMuLabel.Draw()
EELabel.Draw()
MuMuLabel.Draw()
emueeLine.Draw()
eemumuLine.Draw()
Canvas201718.SaveAs("./SR201718yields.pdf")

Canvas201718Prelim.cd()
hExp201718.Draw()
hExpUncert201718.Draw("e2same")
hSig201718.Draw("histesame")
hObs201718.Draw("psame")
LumiPrelimLabel.Draw()
HeaderLabel201718.Draw()
Leg.Draw()
EMuLabel.Draw()
EELabel.Draw()
MuMuLabel.Draw()
emueeLine.Draw()
eemumuLine.Draw()
Canvas201718Prelim.SaveAs("./SR201718yields_CMSPreliminary.pdf")
