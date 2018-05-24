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

inputFileData = TFile("./DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root")
outputFile = TFile("Efficiency_DoubleMuon_DoubleMu43NoFiltersNoVtx.root", "RECREATE")

NumHistogramObj = inputFileData.Get("DQMData/Run 1/HLT/Run summary/EXO/DoubleMu43NoFiltersNoVtx/muon_pt_numerator")
DenHistogramObj = inputFileData.Get("DQMData/Run 1/HLT/Run summary/EXO/DoubleMu43NoFiltersNoVtx/muon_pt_denominator")
NumHistogram = NumHistogramObj.Clone()
DenHistogram = DenHistogramObj.Clone()
#NumHistogram.Rebin(10)
#DenHistogram.Rebin(10)
EffHistogramData = NumHistogram
EffHistogramData.SetDirectory(0)
EffHistogramData.Sumw2()
EffHistogramData.Divide(NumHistogram,DenHistogram,1,1,"B")

Fitting = TF1("Fitting",FittingFunctionStraightLine,0,500,3)
Fitting.SetParName(0, "efficiency")
Fitting.SetParameter(0, 1)
EffHistogramData.Fit(Fitting)

EffHistogramData.Write()



Canvas = TCanvas("Efficiency_DoubleMu43NoFiltersNoVtx")
Canvas.cd()
EffHistogramData.Draw("")
Canvas.Write()
Canvas.SaveAs("Efficiency_DoubleMu43NoFiltersNoVtx.pdf")
outputFile.Close()
inputFileData.Close()
