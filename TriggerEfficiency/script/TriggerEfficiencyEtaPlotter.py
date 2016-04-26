#!/usr/bin/env python
import sys
import os
import re
import time
from array import array
import math
from ROOT import TFile, TH2D, TH1D,TFile, gROOT, TGraphErrors, Double, TF1, TF2, TCanvas  

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

inputFileMC = TFile("/data/users/bing/condor/TriggerEfficiency76X_IsoCorr_April11thPreApr/TTJets_DiLept.root")
DenHistogramObj = inputFileMC.Get("TTbartoEMuMETTriggerPlotter/Electron-muon Plots/electronEtaMuonEta")
NumHistogramObj = inputFileMC.Get("TTbartoEMuMETTriggerPassEMuTriggerPlotter/Electron-muon Plots/electronEtaMuonEta")
NumHistogram = NumHistogramObj.Clone().ProjectionX("Num",0,-1,"e")
DenHistogram = DenHistogramObj.Clone().ProjectionX("Den",0,-1,"e")
xBins = array('d',[0,0.2,0.4,0.6,1.0,1.4,1.8,2.4])
NumHistogramNew = NumHistogram.Rebin(1,"Parameter Summary",xBins)
DenHistogramNew = DenHistogram.Rebin(1,"dennew",xBins)
EffHistogramMC = NumHistogramNew
EffHistogramMC.Sumw2()
EffHistogramMC.Divide(NumHistogramNew,DenHistogramNew,1,1,"B")
#EffHistogramMC = TGraphAsymmErrors()
#EffHistogramMC.BayesDivide(NumHistogramNew,DenHistogramNew,"w");

inputFileData = TFile("/data/users/bing/condor/TriggerEfficiency76X_IsoCorr_April11thPreApr/MET_2015D.root")
outputFile = TFile("DataMCRatio_Muon_Eta.root", "RECREATE")
DenHistogramObj = inputFileData.Get("TTbartoEMuMETTriggerPlotter/Electron-muon Plots/electronEtaMuonEta")
NumHistogramObj = inputFileData.Get("TTbartoEMuMETTriggerPassEMuTriggerPlotter/Electron-muon Plots/electronEtaMuonEta")
NumHistogram = NumHistogramObj.Clone().ProjectionX("Num",0,-1,"e")
DenHistogram = DenHistogramObj.Clone().ProjectionX("Den",0,-1,"e")
xBins = array('d',[0,0.2,0.4,0.6,1.0,1.4,1.8,2.4])
NumHistogramNew = NumHistogram.Rebin(1,"Parameter Summary",xBins)
DenHistogramNew = DenHistogram.Rebin(1,"dennew",xBins)
EffHistogramData = NumHistogramNew
EffHistogramData.Sumw2()
EffHistogramData.Divide(NumHistogramNew,DenHistogramNew,1,1,"B")
#EffHistogramData = TGraphAsymmErrors()
#EffHistogramData.BayesDivide(NumHistogramNew,DenHistogramNew,"w");

RatioHistogram = EffHistogramData.Clone()
RatioHistogram.Sumw2()
RatioHistogram.Divide(EffHistogramData,EffHistogramMC,1,1)

Fitting = TF1("Fitting",FittingFunctionStraightLine,0,500,3)
Fitting.SetParName(0, "efficiency")
Fitting.SetParameter(0, 1)
RatioHistogram.Fit(Fitting)

RatioHistogram.Write()
outputFile.Close()



DenHistogramObj = inputFileMC.Get("TTbartoEMuMETTriggerPlotter/Electron-muon Plots/electronEtaMuonEta")
NumHistogramObj = inputFileMC.Get("TTbartoEMuMETTriggerPassEMuTriggerPlotter/Electron-muon Plots/electronEtaMuonEta")
NumHistogram = NumHistogramObj.Clone().ProjectionY("Num",0,-1,"e")
DenHistogram = DenHistogramObj.Clone().ProjectionY("Den",0,-1,"e")
xBins = array('d',[0,0.2,0.4,0.6,1.0,1.4,1.8,2.4])
NumHistogramNew = NumHistogram.Rebin(7,"Parameter Summary",xBins)
DenHistogramNew = DenHistogram.Rebin(7,"dennew",xBins)
EffHistogramMC = NumHistogramNew
EffHistogramMC.Sumw2()
EffHistogramMC.Divide(NumHistogramNew,DenHistogramNew,1,1,"B")
#EffHistogramMC = TGraphAsymmErrors()
#EffHistogramMC.BayesDivide(NumHistogramNew,DenHistogramNew,"w");

outputFile = TFile("DataMCRatio_Electron_Eta.root", "RECREATE")
DenHistogramObj = inputFileData.Get("TTbartoEMuMETTriggerPlotter/Electron-muon Plots/electronEtaMuonEta")
NumHistogramObj = inputFileData.Get("TTbartoEMuMETTriggerPassEMuTriggerPlotter/Electron-muon Plots/electronEtaMuonEta")
NumHistogram = NumHistogramObj.Clone().ProjectionY("Num",0,-1,"e")
DenHistogram = DenHistogramObj.Clone().ProjectionY("Den",0,-1,"e")
xBins = array('d',[0,0.2,0.4,0.6,1.0,1.4,1.8,2.4])
NumHistogramNew = NumHistogram.Rebin(7,"Parameter Summary",xBins)
DenHistogramNew = DenHistogram.Rebin(7,"dennew",xBins)
EffHistogramData = NumHistogramNew
EffHistogramData.Sumw2()
EffHistogramData.Divide(NumHistogramNew,DenHistogramNew,1,1,"B")
#EffHistogramData = TGraphAsymmErrors()
#EffHistogramData.BayesDivide(NumHistogramNew,DenHistogramNew,"w");

RatioHistogram = EffHistogramData.Clone()
RatioHistogram.Sumw2()
RatioHistogram.Divide(EffHistogramData,EffHistogramMC,1,1)

Fitting = TF1("Fitting",FittingFunctionStraightLine,0,500,3)
Fitting.SetParName(0, "efficiency")
Fitting.SetParameter(0, 1)
RatioHistogram.Fit(Fitting)

RatioHistogram.Write()
outputFile.Close()


Canvas = TCanvas("Ratio")

DenHistogramObj = inputFileMC.Get("TTbartoEMuMETTriggerPlotter/Electron-muon Plots/electronEtaMuonEta")
NumHistogramObj = inputFileMC.Get("TTbartoEMuMETTriggerPassEMuTriggerPlotter/Electron-muon Plots/electronEtaMuonEta")
NumHistogram = NumHistogramObj.Clone()
DenHistogram = DenHistogramObj.Clone()
xBins = array('d',[0,0.2,0.4,0.6,1.0,1.4,1.8,2.4])
yBins = array('d',[0,0.2,0.4,0.6,1.0,1.4,1.8,2.4])
NumHistogramNew = TH2D("Efficiency","Efficiency",7,xBins,7,yBins)
for j in range(1, NumHistogram.GetYaxis().GetNbins() + 1):
  for i in range(1, NumHistogram.GetXaxis().GetNbins() + 1): 
    NumHistogramNew.Fill(NumHistogram.GetXaxis().GetBinCenter(i),NumHistogram.GetYaxis().GetBinCenter(j),NumHistogram.GetBinContent(i,j));
DenHistogramNew = TH2D("Efficiency","Efficiency",7,xBins,7,yBins)
for j in range(1, DenHistogram.GetYaxis().GetNbins() + 1):
  for i in range(1, DenHistogram.GetXaxis().GetNbins() + 1): 
    DenHistogramNew.Fill(DenHistogram.GetXaxis().GetBinCenter(i),DenHistogram.GetYaxis().GetBinCenter(j),DenHistogram.GetBinContent(i,j));
EffHistogramMC = NumHistogramNew
EffHistogramMC.Sumw2()
EffHistogramMC.Divide(NumHistogramNew,DenHistogramNew,1,1,"B");
EffHistogramMC = Round2DHistograms(EffHistogramMC,3)

outputFile = TFile("DataMCRatio2D_Eta.root", "RECREATE")
DenHistogramObj = inputFileData.Get("TTbartoEMuMETTriggerPlotter/Electron-muon Plots/electronEtaMuonEta")
NumHistogramObj = inputFileData.Get("TTbartoEMuMETTriggerPassEMuTriggerPlotter/Electron-muon Plots/electronEtaMuonEta")
NumHistogram = NumHistogramObj.Clone()
DenHistogram = DenHistogramObj.Clone()
xBins = array('d',[0,0.2,0.4,0.6,1.0,1.4,1.8,2.4])
yBins = array('d',[0,0.2,0.4,0.6,1.0,1.4,1.8,2.4])
NumHistogramNew = TH2D("Efficiency","Efficiency",7,xBins,7,yBins)
for j in range(1, NumHistogram.GetYaxis().GetNbins() + 1):
  for i in range(1, NumHistogram.GetXaxis().GetNbins() + 1): 
    NumHistogramNew.Fill(NumHistogram.GetXaxis().GetBinCenter(i),NumHistogram.GetYaxis().GetBinCenter(j),NumHistogram.GetBinContent(i,j));
DenHistogramNew = TH2D("Efficiency","Efficiency",7,xBins,7,yBins)
for j in range(1, DenHistogram.GetYaxis().GetNbins() + 1):
  for i in range(1, DenHistogram.GetXaxis().GetNbins() + 1): 
    DenHistogramNew.Fill(DenHistogram.GetXaxis().GetBinCenter(i),DenHistogram.GetYaxis().GetBinCenter(j),DenHistogram.GetBinContent(i,j));
EffHistogramData = NumHistogramNew
EffHistogramData.Sumw2()
EffHistogramData.Divide(NumHistogramNew,DenHistogramNew,1,1,"B");
EffHistogramData = Round2DHistograms(EffHistogramData,3)

RatioHistogram = EffHistogramData
RatioHistogram.Sumw2()
RatioHistogram.Divide(EffHistogramData,EffHistogramMC,1,1)
RatioHistogram = Round2DHistograms(RatioHistogram,3)
RatioHistogram.SetDirectory(0)

Canvas.cd()
RatioHistogram.Draw("COLZ TEXT E")
Canvas.Write()
outputFile.Close()
inputFileData.Close()
inputFileMC.Close()
