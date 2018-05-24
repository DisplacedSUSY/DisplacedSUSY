#!/usr/bin/env python
import sys
import os
import re
import time
from array import array
import math
from ROOT import TFile, TH2D, TH1D,TFile, gROOT, TGraphErrors, Double, TF1, TF2, TCanvas, gStyle, TLegend

def FittingFunctionTurnOn(x,par):
    return par[2] / (1 + math.exp(-par[1]*(x[0] - par[0])))
def FittingFunctionStraightLine(x,par):
    return par[0]
def Round2DHistograms(histogram, precision):
    newHistogram = histogram.Clone()
    for j in range(1, histogram.GetYaxis().GetNbins() + 1):
        for i in range(1, histogram.GetXaxis().GetNbins() + 1):
            newHistogram.SetBinContent(i, j, round(histogram.GetBinContent(i,j), precision))
            newHistogram.SetBinError(i, j, round(histogram.GetBinError(i,j), precision))
    return newHistogram

gStyle.SetOptStat(0)
inputFileData = TFile("./DQM_HltExoDqm_NoBPTX_Run2018A_PromptReco_22May2018.root")

EffJetE60HistObj = inputFileData.Get("DQMData/Run 1/HLT/Run summary/EXO/NoBPTX/JetE60/effic_jetE")
EffJetE70HistObj = inputFileData.Get("DQMData/Run 1/HLT/Run summary/EXO/NoBPTX/JetE70/effic_jetE")
EffL2Mu40HistObj = inputFileData.Get("DQMData/Run 1/HLT/Run summary/EXO/NoBPTX/L2Mu40/effic_muonPt")
EffL2Mu45HistObj = inputFileData.Get("DQMData/Run 1/HLT/Run summary/EXO/NoBPTX/L2Mu45/effic_muonPt")
EffJetE60Hist = EffJetE60HistObj.Clone()
EffJetE70Hist = EffJetE70HistObj.Clone()
EffL2Mu40Hist = EffL2Mu40HistObj.Clone()
EffL2Mu45Hist = EffL2Mu45HistObj.Clone()
EffJetE60Hist.SetDirectory(0)
EffJetE70Hist.SetDirectory(0)
EffL2Mu40Hist.SetDirectory(0)
EffL2Mu45Hist.SetDirectory(0)
EffJetE60Hist.SetTitle("")
EffJetE70Hist.SetTitle("")
EffL2Mu40Hist.SetTitle("")
EffL2Mu45Hist.SetTitle("")
EffJetE60Hist.GetYaxis().SetRangeUser(0,1.1)
EffJetE70Hist.GetYaxis().SetRangeUser(0,1.1)
EffL2Mu40Hist.GetYaxis().SetRangeUser(0,1.1)
EffL2Mu45Hist.GetYaxis().SetRangeUser(0,1.1)
EffJetE60Hist.SetLineColor(1)
EffJetE70Hist.SetLineColor(2)
EffL2Mu40Hist.SetLineColor(1)
EffL2Mu45Hist.SetLineColor(2)
EffJetE60Hist.SetMarkerColor(1)
EffJetE70Hist.SetMarkerColor(2)
EffL2Mu40Hist.SetMarkerColor(1)
EffL2Mu45Hist.SetMarkerColor(2)

#Fitting = TF1("Fitting",FittingFunctionStraightLine,0,500,3)
#Fitting.SetParName(0, "efficiency")
#Fitting.SetParameter(0, 1)
#EffJetE60Hist.Fit(Fitting)

LegendJetE = TLegend(0.5,0.3,0.85,0.5)
LegendJetE.SetBorderSize(0)
LegendJetE.AddEntry(EffJetE60Hist,"JetE60","l")
LegendJetE.AddEntry(EffJetE70Hist,"JetE70","l")

CanvasJetE = TCanvas("Efficiency_NoBPTX_JetE")
CanvasJetE.cd()
EffJetE60Hist.Draw("")
EffJetE70Hist.Draw("same")
LegendJetE.Draw()
CanvasJetE.SaveAs("Efficiency_NoBPTX_JetE.pdf")

LegendL2Mu = TLegend(0.5,0.3,0.85,0.5)
LegendL2Mu.SetBorderSize(0)
LegendL2Mu.AddEntry(EffL2Mu40Hist,"L2Mu40","l")
LegendL2Mu.AddEntry(EffL2Mu45Hist,"L2Mu45","l")

CanvasL2Mu = TCanvas("Efficiency_NoBPTX_L2Mu")
CanvasL2Mu.cd()
EffL2Mu40Hist.Draw("")
EffL2Mu45Hist.Draw("same")
LegendL2Mu.Draw()
CanvasL2Mu.SaveAs("Efficiency_NoBPTX_L2Mu.pdf")

inputFileData.Close()

