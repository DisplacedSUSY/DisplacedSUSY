#!/usr/bin/env python

# makes plot of yields in SR
# all numbers in these plots are obtained from the output of the abcd script
# usage: python makeSRYieldsPlots.py -r
# -r option makes ratio plots, needed now for paper/supplemental material

import sys
import os
import re
import math
import functools
from math import *
from array import *
from decimal import *
from optparse import OptionParser
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *
from OSUT3Analysis.Configuration.cutUtilities import *

parser = OptionParser()
parser = set_commandline_arguments(parser)

(arguments, args) = parser.parse_args()

from ROOT import gROOT, gStyle, gPad, TFile, TCanvas, TH1, TH1F, TGraphAsymmErrors, TPaveLabel, TLegend, TLine

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
gStyle.SetTitleYSize(0.05)
gStyle.SetTitleYOffset(1.1)
gStyle.SetTextAlign(12)
gStyle.SetLabelColor(1, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelOffset(0.008, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetAxisColor(1, "XYZ")
gStyle.SetStripDecimals(True)
gStyle.SetTickLength(0.03, "XYZ")
gStyle.SetNdivisions(505, "XYZ")
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gStyle.SetErrorX(0)
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
HeaderTextRun2 = "113-118 fb^{-1} (13 TeV)"

HeaderLabel2016 = TPaveLabel(header_x_left,y_bottom,header_x_right,y_top,HeaderText2016,"NDC")
HeaderLabel2016.SetTextAlign(32)
HeaderLabel2016.SetTextFont(42)
HeaderLabel2016.SetTextSize(0.9)

HeaderLabel201718 = TPaveLabel(header_x_left,y_bottom,header_x_right,y_top,HeaderText201718,"NDC")
HeaderLabel201718.SetTextAlign(32)
HeaderLabel201718.SetTextFont(42)
HeaderLabel201718.SetTextSize(0.9)

HeaderLabelRun2 = TPaveLabel(header_x_left,y_bottom,header_x_right,y_top,HeaderTextRun2,"NDC")
HeaderLabelRun2.SetTextAlign(32)
HeaderLabelRun2.SetTextFont(42)
HeaderLabelRun2.SetTextSize(0.9)

LumiLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS","NDC")
LumiLabel.SetTextFont(62)
LumiLabel.SetTextSize(1)
LumiLabel.SetTextAlign(12)

LumiPrelimLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS Preliminary","NDC")
LumiPrelimLabel.SetTextFont(62)
LumiPrelimLabel.SetTextSize(1)
LumiPrelimLabel.SetTextAlign(12)

# the default is somehow bold for these, so you have to explicitly make the e's unbold (with a "second" #bf{})
# to make them match the #mu's (which you can't get bold because they are greek letter... but really cuz root)
EMuLabel = TPaveLabel(emu_x_left,emu_y_bottom,emu_x_right,emu_y_top,"#bf{e}#mu","nb")
EMuLabel.SetTextFont(62)
EMuLabel.SetTextSize(0.7)
EMuLabel.SetTextAlign(22)

EELabel = TPaveLabel(ee_x_left,emu_y_bottom,ee_x_right,emu_y_top,"#bf{ee}","nb")
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
    HeaderLabelRun2,
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
emueeLine.SetLineWidth(2)
eemumuLine.SetLineWidth(2)

emueeRatioLine = TLine(5,-2.4,5,100)
eemumuRatioLine = TLine(10,-2.4,10,100)
emueeRatioLine.SetLineWidth(2)
eemumuRatioLine.SetLineWidth(2)

Canvas2016 = TCanvas("canvas2016","")
Canvas2016Prelim = TCanvas("canvas2016Preliminary","")
Canvas201718 = TCanvas("canvas201718","")
Canvas201718Prelim = TCanvas("canvas201718Preliminary","")
CanvasRun2 = TCanvas("canvasRun2","")
CanvasRun2Prelim = TCanvas("canvasRun2Preliminary","")

canvases = [
    Canvas2016,
    Canvas2016Prelim,
    Canvas201718,
    Canvas201718Prelim,
    CanvasRun2,
    CanvasRun2Prelim,
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
    if arguments.makeRatioPlots:
        canvas.SetFillStyle(0)
        canvas.Divide(1,2)
        canvas.cd(1)
        gPad.SetPad(0,0.25,1,1)
        gPad.SetMargin(0.15,0.05,0.0,0.15)
        gPad.SetFillStyle(0)
        gPad.SetLogy()
        gPad.Update()
        gPad.Draw()
        canvas.cd(2)
        gPad.SetPad(0,0,1,0.25)
        #format: gPad.SetMargin(l,r,b,t)
        gPad.SetMargin(0.15,0.05,0.4,0.01)
        gPad.SetFillStyle(0)
        gPad.SetGridy(1)
        gPad.Update()
        gPad.Draw()
        canvas.cd(1)

#central values
#          emu SR I low pt, emu SR I high pt, emu SR II, emu SR III, emu SR IV, ee SR I low pt, ee SR I high pt, ee SR II, ee SR III, ee SR IV, mumu SR I low pt, mumu SR I high pt, mumu SR II, mumu SR III, mumu SR IV
Obs2016 = [8,               1,                0,         0,          0,         40,             0,               0,        1,         0,        15,               0,                 0,          1,           0]
Obs201718 = [28, 3, 0, 1, 0, 48, 0, 1, 4, 0, 1, 1, 1, 1, 0]
ObsRun2 = [i+j for i,j in zip(Obs2016,Obs201718)]

Exp2016 = [3.8, 0.41, 0.09, 0.15, 0.003, 18.1, 0.22, 0.51, 0.43, 0.01, 7.4, 0.25, 0.17, 0.19, 0.01]
Exp201718 = [37.9, 0.75, 0.23, 0.71, 0.01, 62, 0.85, 2.8, 3.6, 0.24, 3.5, 0.69, 0.08, 0.14, 0.01]
ExpRun2 = [i+j for i,j in zip(Exp2016,Exp201718)]

Sig2016 = [0., 0.02, 0.07, 0.05, 0.19, 0., 0.01, 0.03, 0.02, 0.07, 0., 0.01, 0.04, 0.03, 0.14]
Sig201718 = [0.01, 0.13, 0.42, 0.31, 1.15, 0., 0.06, 0.19, 0.15, 0.44, 0., 0.07, 0.23, 0.18, 0.78]
SigRun2 = [i+j for i,j in zip(Sig2016,Sig201718)]

#uncertainties
Sig2016err = [0., 0.008, 0.027, 0.020, 0.074, 0., 0.002, 0.005, 0.004, 0.012, 0., 0.007, 0.028, 0.021, 0.099]
Sig201718err = [0.004, 0.046, 0.147, 0.109, 0.4, 0., 0.016, 0.051, 0.039, 0.115, 0., 0.032, 0.104, 0.081, 0.351]
SigRun2err = [sqrt(i*i+j*j) for i,j in zip(Sig2016err,Sig201718err)]

hObs2016 = TH1F("hObs2016","",15,0,15)
hObs2016.SetMarkerStyle(20)
hObs2016.SetMarkerColor(1)
hObs2016.SetLineColor(1)
hObs2016.SetLineWidth(1)
hObs2016.SetBinErrorOption(TH1.kPoisson)
hObs2016.SetDirectory(0)

hObs201718 = TH1F("hObs201718","",15,0,15)
hObs201718.SetMarkerStyle(20)
hObs201718.SetMarkerColor(1)
hObs201718.SetLineColor(1)
hObs201718.SetLineWidth(1)
hObs201718.SetBinErrorOption(TH1.kPoisson)
hObs201718.SetDirectory(0)

hObsRun2 = TH1F("hObsRun2","",15,0,15)
hObsRun2.SetMarkerStyle(20)
hObsRun2.SetMarkerColor(1)
hObsRun2.SetLineColor(1)
hObsRun2.SetLineWidth(1)
hObsRun2.SetBinErrorOption(TH1.kPoisson)
hObsRun2.SetDirectory(0)

hExp2016 = TH1F("hExp2016","",15,0,15)
hExp2016.SetFillStyle(1001)
hExp2016.SetFillColor(866)#kAzure+6
hExp2016.SetLineWidth(0)
hExp2016.SetDirectory(0)

hExp201718 = TH1F("hExp201718","",15,0,15)
hExp201718.SetFillStyle(1001)
hExp201718.SetFillColor(866)#kAzure+6
hExp201718.SetLineWidth(0)
hExp201718.SetDirectory(0)

hExpRun2 = TH1F("hExpRun2","",15,0,15)
hExpRun2.SetFillStyle(1001)
hExpRun2.SetFillColor(866)#kAzure+6
hExpRun2.SetLineWidth(0)
hExpRun2.SetDirectory(0)

hSig2016 = TH1F("hSig2016","",15,0,15)
hSig2016.SetLineColor(2)
hSig2016.SetLineWidth(3)
hSig2016.SetDirectory(0)

hSig201718 = TH1F("hSig201718","",15,0,15)
hSig201718.SetLineColor(2)
hSig201718.SetLineWidth(3)
hSig201718.SetDirectory(0)

hSigRun2 = TH1F("hSigRun2","",15,0,15)
hSigRun2.SetLineColor(2)
hSigRun2.SetLineWidth(3)
hSigRun2.SetDirectory(0)

for i in range(1,16):
    hObs2016.SetBinContent(i,Obs2016[i-1])
    hObs201718.SetBinContent(i,Obs201718[i-1])
    hObsRun2.SetBinContent(i,ObsRun2[i-1])
    hExp2016.SetBinContent(i,Exp2016[i-1])
    hExp201718.SetBinContent(i,Exp201718[i-1])
    hExpRun2.SetBinContent(i,ExpRun2[i-1])
    hSig2016.SetBinContent(i,Sig2016[i-1])
    hSig201718.SetBinContent(i,Sig201718[i-1])
    hSigRun2.SetBinContent(i,SigRun2[i-1])
    hSig2016.SetBinError(i,Sig2016err[i-1])
    hSig201718.SetBinError(i,Sig201718err[i-1])
    hSigRun2.SetBinError(i,SigRun2err[i-1])

def makeTGraphAsymmErrors(x, y, x_errDown, x_errUp, y_errDown, y_errUp):
    graph_arrays = [array('d', arg) for arg in [x, y, x_errDown, x_errUp, y_errDown, y_errUp]]
    return TGraphAsymmErrors(int(len(x)), *graph_arrays)

ExpUncert_x = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5]
ExpUncert_xErr = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]

Exp2016ErrUp = [4.8,0.53,0.12,0.15,0.004, 11, 0.17, 1.02, 0.85, 0.02, 3,0.11,0.11,0.12,0.01]
Exp2016ErrDown = [3.8,0.41,0.09,0.15,0.003,  11,0.16,0.51,0.43,0.01,   3,0.11,0.11,0.12,0.01]
hExpUncert2016 = makeTGraphAsymmErrors(ExpUncert_x, Exp2016, ExpUncert_xErr, ExpUncert_xErr, Exp2016ErrDown, Exp2016ErrUp)
hExpUncert2016.SetName("hExpUncert2016")
hExpUncert2016.SetFillStyle(3002)
hExpUncert2016.SetFillColor(13)
hExpUncert2016.SetLineWidth(0)

Exp201718ErrUp = [13, 0.41, 0.27, 0.76, 0.02,   18, 0.33, 1.1, 1.4, 0.10,   1.5, 0.31, 0.12, 0.19, 0.02]
Exp201718ErrDown = [13,0.34,0.23,0.71,0.01,  17, 0.35, 1.1, 1.4, 0.09,  1.5, 0.31, 0.08, 0.14, 0.01]
hExpUncert201718 = makeTGraphAsymmErrors(ExpUncert_x, Exp201718, ExpUncert_xErr, ExpUncert_xErr, Exp201718ErrDown, Exp201718ErrUp)
hExpUncert201718.SetName("hExpUncert201718")
hExpUncert201718.SetFillStyle(3002)
hExpUncert201718.SetFillColor(13)
hExpUncert201718.SetLineWidth(0)

#simply sum upper and lower uncertainties in quadrature: not quite right, but good enough here
ExpRun2ErrDown = [sqrt(i*i+j*j) for i,j in zip(Exp2016ErrDown,Exp201718ErrDown)]
ExpRun2ErrUp = [sqrt(i*i+j*j) for i,j in zip(Exp2016ErrUp,Exp201718ErrUp)]
hExpUncertRun2 = makeTGraphAsymmErrors(ExpUncert_x, ExpRun2, ExpUncert_xErr, ExpUncert_xErr, ExpRun2ErrDown, ExpRun2ErrUp)
hExpUncertRun2.SetName("hExpUncertRun2")
hExpUncertRun2.SetFillStyle(3002)
hExpUncertRun2.SetFillColor(13)
hExpUncertRun2.SetLineWidth(0)

hists = [
    hObs2016,
    hObs201718,
    hObsRun2,
    hExp2016,
    hExp201718,
    hExpRun2,
    hSig2016,
    hSig201718,
    hSigRun2,
]

for hist in hists:
    hist.SetTitle(";SR;Events")
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
    hist.GetYaxis().SetRangeUser(0.0005,100000) #log y axis
    for i in range(hist.GetNbinsX()):
        hist.GetXaxis().ChangeLabel(i,-1,-1,1,2)

Leg = TLegend(0.2,0.62,0.9,0.82)
Leg.AddEntry(hObs2016,"Data","ep")
Leg.AddEntry(hExp2016,"Background","f")
Leg.AddEntry(hExpUncert2016,"Background uncertainty","f")
Leg.AddEntry(hSig2016,"\\~{\\text{t}} \\to \\text{b}\\ell, \\text{m}_{\\~{\\text{t}}}\\text{ = 1500 GeV, }c\\tau_{0}\\text{ = 1 cm}","l")
Leg.SetBorderSize(0)


if arguments.makeRatioPlots:
    Canvas2016.cd(1)
else:
    Canvas2016.cd()
hExp2016.Draw()
hExpUncert2016.Draw("e2same")
hSig2016.Draw("histesame")
hObs2016.Draw("pe0same")
LumiLabel.Draw()
HeaderLabel2016.Draw()
Leg.Draw()
EMuLabel.Draw()
EELabel.Draw()
MuMuLabel.Draw()
emueeLine.Draw()
eemumuLine.Draw()

if arguments.makeRatioPlots:
    Canvas2016Prelim.cd(1)
else:
    Canvas2016Prelim.cd()
hExp2016.Draw()
hExpUncert2016.Draw("e2same")
hSig2016.Draw("histesame")
hObs2016.Draw("pe0same")
LumiPrelimLabel.Draw()
HeaderLabel2016.Draw()
Leg.Draw()
EMuLabel.Draw()
EELabel.Draw()
MuMuLabel.Draw()
emueeLine.Draw()
eemumuLine.Draw()

if arguments.makeRatioPlots:
    Canvas201718.cd(1)
else:
    Canvas201718.cd()
hExp201718.Draw()
hExpUncert201718.Draw("e2same")
hSig201718.Draw("histesame")
hObs201718.Draw("pe0same")
LumiLabel.Draw()
HeaderLabel201718.Draw()
Leg.Draw()
EMuLabel.Draw()
EELabel.Draw()
MuMuLabel.Draw()
emueeLine.Draw()
eemumuLine.Draw()

if arguments.makeRatioPlots:
    Canvas201718Prelim.cd(1)
else:
    Canvas201718Prelim.cd()
hExp201718.Draw()
hExpUncert201718.Draw("e2same")
hSig201718.Draw("histesame")
hObs201718.Draw("pe0same")
LumiPrelimLabel.Draw()
HeaderLabel201718.Draw()
Leg.Draw()
EMuLabel.Draw()
EELabel.Draw()
MuMuLabel.Draw()
emueeLine.Draw()
eemumuLine.Draw()

if arguments.makeRatioPlots:
    CanvasRun2.cd(1)
else:
    CanvasRun2.cd()
hExpRun2.Draw()
hExpUncertRun2.Draw("e2same")
hSigRun2.Draw("histesame")
hObsRun2.Draw("pe0same")
LumiLabel.Draw()
HeaderLabelRun2.Draw()
Leg.Draw()
EMuLabel.Draw()
EELabel.Draw()
MuMuLabel.Draw()
emueeLine.Draw()
eemumuLine.Draw()

if arguments.makeRatioPlots:
    CanvasRun2Prelim.cd(1)
else:
    CanvasRun2Prelim.cd()
hExpRun2.Draw()
hExpUncertRun2.Draw("e2same")
hSigRun2.Draw("histesame")
hObsRun2.Draw("pe0same")
LumiPrelimLabel.Draw()
HeaderLabelRun2.Draw()
Leg.Draw()
EMuLabel.Draw()
EELabel.Draw()
MuMuLabel.Draw()
emueeLine.Draw()
eemumuLine.Draw()

#write histograms to root file for hepdata
outputFile = TFile("SRyields.root", "RECREATE")
pdfSuffix = ""
dummyRatios = []
ratios = []
ratioUncerts = []
ratioLegs = []

def getRatioPlot(ratioName, hObs, hExp, ratioUncertName, expErrDown, expErrUp):
    # make dummy ratio histogram to get proper axes
    dummyRatio = hObs.Clone(ratioName)
    dummyRatio.Add(hExp, -1)
    dummyRatio.Divide(hExp)
    dummyRatio.SetDirectory(0)

    ratioValues = []
    obsValues = []
    obsErrDown = []
    obsErrUp = []
    expValues = []
    for i in range(1, hObs.GetNbinsX()+1):
        obsValues.append(hObs.GetBinContent(i))
        obsErrUp.append(hObs.GetBinErrorUp(i))
        obsErrDown.append(hObs.GetBinErrorLow(i))
        expValues.append(hExp.GetBinContent(i))

    # calculate ratios; only account for poisson uncertainty on observed
    ratioValues = [(o-e)/e for o, e in zip(obsValues, expValues)]
    ratioErrUp = [u/e for u, e in zip(obsErrUp, expValues)]
    ratioErrDown = [u/e for u, e in zip(obsErrDown, expValues)]

    zero_errors = len(ratioValues)*[0]
    ratio = makeTGraphAsymmErrors(ExpUncert_x, ratioValues, zero_errors, zero_errors, ratioErrDown, ratioErrUp)
    ratio.SetName(ratioUncertName)
    ratio.SetMarkerStyle(8)

    # calculate relative expected uncertainty values to show uncertainty on estimate
    expRelValues = [0.0 for v in expValues]
    expRelErrUp = [u/e for u, e in zip(expErrUp, expValues)]
    expRelErrDown = [u/e for u, e in zip(expErrDown, expValues)]

    ratioUncert = makeTGraphAsymmErrors(ExpUncert_x, expRelValues, ExpUncert_xErr, ExpUncert_xErr, expRelErrDown, expRelErrUp)
    ratioUncert.SetName(ratioUncertName)
    ratioUncert.SetFillStyle(3002)
    ratioUncert.SetFillColor(13)
    ratioUncert.SetLineWidth(0)

    ratioLeg = TLegend(0.43,0.75,0.65,0.9)
    ratioLeg.SetBorderSize(0)
    ratioLeg.AddEntry(ratioUncert,"Bkg. uncertainty","f")

    dummyRatio.GetYaxis().SetNdivisions(505)
    dummyRatio.GetYaxis().SetTitle("#frac{Data-Bkg.}{Bkg.}")
    dummyRatio.GetYaxis().SetLabelSize(0.14)
    dummyRatio.GetYaxis().SetLabelOffset(0.008)
    dummyRatio.GetYaxis().SetTitleSize(0.14)
    dummyRatio.GetYaxis().SetTitleOffset(.3)
    dummyRatio.GetYaxis().SetRangeUser(-2, 7)

    dummyRatio.GetXaxis().SetLabelSize(0.16)
    dummyRatio.GetXaxis().SetLabelOffset(0.04)
    dummyRatio.GetXaxis().SetTitleSize(0.14)
    dummyRatio.GetXaxis().SetTitleOffset(1.25)

    return dummyRatio, ratio, ratioUncert, ratioLeg

if arguments.makeRatioPlots:
    pdfSuffix = "_withRatioPlots"
    for canvas in canvases:
        print "canvasName is: "+canvas.GetName()
        if canvas.GetName() == "canvas2016":
            dummyRatio, ratio, ratioUncert, ratioLeg = getRatioPlot("ratio2016",hObs2016,hExp2016,"ratioUncert2016",Exp2016ErrDown,Exp2016ErrUp)
        elif canvas.GetName() == "canvas2016Preliminary":
            dummyRatio, ratio, ratioUncert, ratioLeg = getRatioPlot("ratio2016Prelim",hObs2016,hExp2016,"ratioUncert2016Prelim",Exp2016ErrDown,Exp2016ErrUp)
        elif canvas.GetName() == "canvas201718":
            dummyRatio, ratio, ratioUncert, ratioLeg = getRatioPlot("ratio201718",hObs201718,hExp201718,"ratioUncert201718",Exp201718ErrDown,Exp201718ErrUp)
        elif canvas.GetName() == "canvas201718Preliminary":
            dummyRatio, ratio, ratioUncert, ratioLeg = getRatioPlot("ratio201718Prelim",hObs201718,hExp201718,"ratioUncert201718Prelim",Exp201718ErrDown,Exp201718ErrUp)
        elif canvas.GetName() == "canvasRun2":
            dummyRatio, ratio, ratioUncert, ratioLeg = getRatioPlot("ratioRun2",hObsRun2,hExpRun2,"ratioUncertRun2",ExpRun2ErrDown,ExpRun2ErrUp)
        elif canvas.GetName() == "canvasRun2Preliminary":
            dummyRatio, ratio, ratioUncert, ratioLeg = getRatioPlot("ratioRun2Prelim",hObsRun2,hExpRun2,"ratioUncertRun2Prelim",ExpRun2ErrDown,ExpRun2ErrUp)

        dummyRatios.append(dummyRatio)
        ratios.append(ratio)
        ratioUncerts.append(ratioUncert)
        ratioLegs.append(ratioLeg)

    for i, canvas in enumerate(canvases):
        canvas.cd(2)
        dummyRatios[i].Draw("axis")
        ratios[i].Draw("pz0same")
        ratioUncerts[i].Draw("e2same")
        emueeRatioLine.Draw()
        eemumuRatioLine.Draw()
        ratioLegs[i].Draw()
        gPad.Modified()
        gPad.Update()
        gPad.RedrawAxis()
        outputFile.cd()
        ratios[i].Write()
        ratioUncerts[i].Write()


#need to save as .ps so that TMathText appears properly (can't with pdf)
Canvas2016.SaveAs("./SR2016yields"+pdfSuffix+".ps")
Canvas2016Prelim.SaveAs("./SR2016yields_CMSPreliminary"+pdfSuffix+".ps")
Canvas201718.SaveAs("./SR201718yields"+pdfSuffix+".ps")
Canvas201718Prelim.SaveAs("./SR201718yields_CMSPreliminary"+pdfSuffix+".ps")
CanvasRun2.SaveAs("./SRRun2yields"+pdfSuffix+".ps")
CanvasRun2Prelim.SaveAs("./SRRun2yields_CMSPreliminary"+pdfSuffix+".ps")

Canvas2016.SaveAs("./SR2016yields"+pdfSuffix+".png")
Canvas2016Prelim.SaveAs("./SR2016yields_CMSPreliminary"+pdfSuffix+".png")
Canvas201718.SaveAs("./SR201718yields"+pdfSuffix+".png")
Canvas201718Prelim.SaveAs("./SR201718yields_CMSPreliminary"+pdfSuffix+".png")
CanvasRun2.SaveAs("./SRRun2yields"+pdfSuffix+".png")
CanvasRun2Prelim.SaveAs("./SRRun2yields_CMSPreliminary"+pdfSuffix+".png")


outputFile.cd()

hExp2016.Write()
hExpUncert2016.Write()
hSig2016.Write()
hObs2016.Write()

hExp201718.Write()
hExpUncert201718.Write()
hSig201718.Write()
hObs201718.Write()

hExpRun2.Write()
hExpUncertRun2.Write()
hSigRun2.Write()
hObsRun2.Write()

outputFile.Close()
