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

def GetEff(inputFile,numHist,denHist,histTitle):
    NumHistogramObj = inputFile.Get(numHist)
    DenHistogramObj = inputFile.Get(denHist)
    NumHistogram = NumHistogramObj.Clone()
    DenHistogram = DenHistogramObj.Clone()
    EffHistogram = NumHistogram
    EffHistogram.SetDirectory(0)
    EffHistogram.Sumw2()
    EffHistogram.Divide(NumHistogram,DenHistogram,1,1,"B")
    EffHistogram.SetTitle(histTitle)
    EffHistogram.GetYaxis().SetRangeUser(0,1.1)
    EffHistogram.SetLineColor(1)
    EffHistogram.SetMarkerColor(1)
    return EffHistogram
#Fitting = TF1("Fitting",FittingFunctionStraightLine,0,500,3)
#Fitting.SetParName(0, "efficiency")
#Fitting.SetParameter(0, 1)
#EffHistogramData.Fit(Fitting)


gStyle.SetOptStat(0)

inputFileData = TFile("./DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root")

startPath = "DQMData/Run 1/HLT/Run summary/EXO/"
muPtNumPath = "/muon_pt_numerator"
muPtDenPath = "/muon_pt_denominator"
muTitle = ";Muon p_{T} [GeV];Efficiency"

MuEffHistDoubleMu43NoFiltersNoVtx = GetEff(inputFileData,startPath+"DoubleMu43NoFiltersNoVtx"+muPtNumPath,startPath+"DoubleMu43NoFiltersNoVtx"+muPtDenPath,muTitle)
MuEffHistDoubleMu48NoFiltersNoVtx = GetEff(inputFileData,startPath+"DoubleMu48NoFiltersNoVtx"+muPtNumPath,startPath+"DoubleMu48NoFiltersNoVtx"+muPtDenPath,muTitle)
MuEffHistDoubleMu48NoFiltersNoVtx.SetLineColor(2)
MuEffHistDoubleMu48NoFiltersNoVtx.SetMarkerColor(2)

LegendDoubleMuXNoFiltersNoVtx = TLegend(0.4,0.3,0.85,0.5)
LegendDoubleMuXNoFiltersNoVtx.SetBorderSize(0)
LegendDoubleMuXNoFiltersNoVtx.AddEntry(MuEffHistDoubleMu43NoFiltersNoVtx,"DoubleMu43NoFiltersNoVtx","l")
LegendDoubleMuXNoFiltersNoVtx.AddEntry(MuEffHistDoubleMu48NoFiltersNoVtx,"DoubleMu48NoFiltersNoVtx","l")

CanvasEfficiencyVsMuonPt_DoubleMuXNoFiltersNoVtx = TCanvas("EfficiencyVsMuonPt_DoubleMuXNoFiltersNoVtx")
CanvasEfficiencyVsMuonPt_DoubleMuXNoFiltersNoVtx.cd()
MuEffHistDoubleMu43NoFiltersNoVtx.Draw("")
MuEffHistDoubleMu48NoFiltersNoVtx.Draw("same")
LegendDoubleMuXNoFiltersNoVtx.Draw()
CanvasEfficiencyVsMuonPt_DoubleMuXNoFiltersNoVtx.SaveAs("EfficiencyVsMuonPt_DoubleMuXNoFiltersNoVtx.pdf")


MuEffHistDoubleMu33NoFiltersNoVtxDisplaced = GetEff(inputFileData,startPath+"DoubleMu33NoFiltersNoVtxDisplaced"+muPtNumPath,startPath+"DoubleMu33NoFiltersNoVtxDisplaced"+muPtDenPath,muTitle)
MuEffHistDoubleMu40NoFiltersNoVtxDisplaced = GetEff(inputFileData,startPath+"DoubleMu40NoFiltersNoVtxDisplaced"+muPtNumPath,startPath+"DoubleMu40NoFiltersNoVtxDisplaced"+muPtDenPath,muTitle)
MuEffHistDoubleMu40NoFiltersNoVtxDisplaced.SetLineColor(2)
MuEffHistDoubleMu40NoFiltersNoVtxDisplaced.SetMarkerColor(2)

LegendDoubleMuXNoFiltersNoVtxDisplaced = TLegend(0.4,0.3,0.85,0.5)
LegendDoubleMuXNoFiltersNoVtxDisplaced.SetBorderSize(0)
LegendDoubleMuXNoFiltersNoVtxDisplaced.AddEntry(MuEffHistDoubleMu33NoFiltersNoVtxDisplaced,"DoubleMu33NoFiltersNoVtxDisplaced","l")
LegendDoubleMuXNoFiltersNoVtxDisplaced.AddEntry(MuEffHistDoubleMu40NoFiltersNoVtxDisplaced,"DoubleMu40NoFiltersNoVtxDisplaced","l")

CanvasEfficiencyVsMuonPt_DoubleMuXNoFiltersNoVtxDisplaced = TCanvas("EfficiencyVsMuonPt_DoubleMuXNoFiltersNoVtxDisplaced")
CanvasEfficiencyVsMuonPt_DoubleMuXNoFiltersNoVtxDisplaced.cd()
MuEffHistDoubleMu33NoFiltersNoVtxDisplaced.Draw("")
MuEffHistDoubleMu40NoFiltersNoVtxDisplaced.Draw("same")
LegendDoubleMuXNoFiltersNoVtxDisplaced.Draw()
CanvasEfficiencyVsMuonPt_DoubleMuXNoFiltersNoVtxDisplaced.SaveAs("EfficiencyVsMuonPt_DoubleMuXNoFiltersNoVtxDisplaced.pdf")



MuEffHistMu43NoFiltersNoVtx_Photon43_CaloIdL = GetEff(inputFileData,startPath+"Mu43NoFiltersNoVtx_Photon43_CaloIdL_MuLeg"+muPtNumPath,startPath+"Mu43NoFiltersNoVtx_Photon43_CaloIdL"+muPtDenPath,muTitle)
MuEffHistMu48NoFiltersNoVtx_Photon48_CaloIdL = GetEff(inputFileData,startPath+"Mu48NoFiltersNoVtx_Photon48_CaloIdL_MuLeg"+muPtNumPath,startPath+"Mu48NoFiltersNoVtx_Photon48_CaloIdL"+muPtDenPath,muTitle)
MuEffHistMu48NoFiltersNoVtx_Photon48_CaloIdL.SetLineColor(2)
MuEffHistMu48NoFiltersNoVtx_Photon48_CaloIdL.SetMarkerColor(2)

LegendMuXNoFiltersNoVtx_PhotonX_CaloIdL = TLegend(0.4,0.3,0.85,0.5)
LegendMuXNoFiltersNoVtx_PhotonX_CaloIdL.SetBorderSize(0)
LegendMuXNoFiltersNoVtx_PhotonX_CaloIdL.AddEntry(MuEffHistMu43NoFiltersNoVtx_Photon43_CaloIdL,"Mu43NoFiltersNoVtx_Photon43_CaloIdL","l")
LegendMuXNoFiltersNoVtx_PhotonX_CaloIdL.AddEntry(MuEffHistMu48NoFiltersNoVtx_Photon48_CaloIdL,"Mu48NoFiltersNoVtx_Photon48_CaloIdL","l")

CanvasEfficiencyVsMuonPt_MuXNoFiltersNoVtx_PhotonX_CaloIdL = TCanvas("EfficiencyVsMuonPt_MuXNoFiltersNoVtx_PhotonX_CaloIdL")
CanvasEfficiencyVsMuonPt_MuXNoFiltersNoVtx_PhotonX_CaloIdL.cd()
MuEffHistMu43NoFiltersNoVtx_Photon43_CaloIdL.Draw("")
MuEffHistMu48NoFiltersNoVtx_Photon48_CaloIdL.Draw("same")
LegendMuXNoFiltersNoVtx_PhotonX_CaloIdL.Draw()
CanvasEfficiencyVsMuonPt_MuXNoFiltersNoVtx_PhotonX_CaloIdL.SaveAs("EfficiencyVsMuonPt_MuXNoFiltersNoVtx_PhotonX_CaloIdL.pdf")



MuEffHistMu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL = GetEff(inputFileData,startPath+"Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_MuLeg"+muPtNumPath,startPath+"Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL"+muPtDenPath,muTitle)
MuEffHistMu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL = GetEff(inputFileData,startPath+"Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_MuLeg"+muPtNumPath,startPath+"Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL"+muPtDenPath,muTitle)
MuEffHistMu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL.SetLineColor(2)
MuEffHistMu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL.SetMarkerColor(2)

LegendMuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL = TLegend(0.4,0.3,0.85,0.5)
LegendMuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.SetBorderSize(0)
LegendMuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.AddEntry(MuEffHistMu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL,"Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL","l")
LegendMuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.AddEntry(MuEffHistMu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL,"Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL","l")

CanvasEfficiencyVsMuonPt_MuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL = TCanvas("EfficiencyVsMuonPt_MuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL")
CanvasEfficiencyVsMuonPt_MuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.cd()
MuEffHistMu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL.Draw("")
MuEffHistMu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL.Draw("same")
LegendMuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.Draw()
CanvasEfficiencyVsMuonPt_MuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.SaveAs("EfficiencyVsMuonPt_MuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.pdf")


elePtNumPath = "/electron_pt_variable_numerator"
elePtDenPath = "/electron_pt_variable_denominator"
eleTitle = ";Electron p_{T} [GeV];Efficiency"

EleEffHistMu43NoFiltersNoVtx_Photon43_CaloIdL = GetEff(inputFileData,startPath+"Mu43NoFiltersNoVtx_Photon43_CaloIdL_EleLeg"+elePtNumPath,startPath+"Mu43NoFiltersNoVtx_Photon43_CaloIdL"+elePtDenPath,eleTitle)
EleEffHistMu48NoFiltersNoVtx_Photon48_CaloIdL = GetEff(inputFileData,startPath+"Mu48NoFiltersNoVtx_Photon48_CaloIdL_EleLeg"+elePtNumPath,startPath+"Mu48NoFiltersNoVtx_Photon48_CaloIdL"+elePtDenPath,eleTitle)
EleEffHistMu48NoFiltersNoVtx_Photon48_CaloIdL.SetLineColor(2)
EleEffHistMu48NoFiltersNoVtx_Photon48_CaloIdL.SetMarkerColor(2)

LegendEleXNoFiltersNoVtx_PhotonX_CaloIdL = TLegend(0.4,0.3,0.85,0.5)
LegendEleXNoFiltersNoVtx_PhotonX_CaloIdL.SetBorderSize(0)
LegendEleXNoFiltersNoVtx_PhotonX_CaloIdL.AddEntry(EleEffHistMu43NoFiltersNoVtx_Photon43_CaloIdL,"Mu43NoFiltersNoVtx_Photon43_CaloIdL","l")
LegendEleXNoFiltersNoVtx_PhotonX_CaloIdL.AddEntry(EleEffHistMu48NoFiltersNoVtx_Photon48_CaloIdL,"Mu48NoFiltersNoVtx_Photon48_CaloIdL","l")

CanvasEfficiencyVsElectronPt_MuXNoFiltersNoVtx_PhotonX_CaloIdL = TCanvas("EfficiencyVsElectronPt_MuXNoFiltersNoVtx_PhotonX_CaloIdL")
CanvasEfficiencyVsElectronPt_MuXNoFiltersNoVtx_PhotonX_CaloIdL.cd()
EleEffHistMu43NoFiltersNoVtx_Photon43_CaloIdL.Draw("")
EleEffHistMu48NoFiltersNoVtx_Photon48_CaloIdL.Draw("same")
LegendEleXNoFiltersNoVtx_PhotonX_CaloIdL.Draw()
CanvasEfficiencyVsElectronPt_MuXNoFiltersNoVtx_PhotonX_CaloIdL.SaveAs("EfficiencyVsElectronPt_MuXNoFiltersNoVtx_PhotonX_CaloIdL.pdf")



EleEffHistMu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL = GetEff(inputFileData,startPath+"Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_EleLeg"+elePtNumPath,startPath+"Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL"+elePtDenPath,eleTitle)
EleEffHistMu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL = GetEff(inputFileData,startPath+"Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_EleLeg"+elePtNumPath,startPath+"Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL"+elePtDenPath,eleTitle)
EleEffHistMu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL.SetLineColor(2)
EleEffHistMu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL.SetMarkerColor(2)

LegendEleXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL = TLegend(0.4,0.3,0.85,0.5)
LegendEleXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.SetBorderSize(0)
LegendEleXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.AddEntry(EleEffHistMu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL,"Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL","l")
LegendEleXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.AddEntry(EleEffHistMu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL,"Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL","l")

CanvasEfficiencyVsElectronPt_MuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL = TCanvas("EfficiencyVsElectronPt_MuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL")
CanvasEfficiencyVsElectronPt_MuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.cd()
EleEffHistMu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL.Draw("")
EleEffHistMu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL.Draw("same")
LegendMuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.Draw()
CanvasEfficiencyVsElectronPt_MuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.SaveAs("EfficiencyVsElectronPt_MuXNoFiltersNoVtxDisplaced_PhotonX_CaloIdL.pdf")

inputFileData.Close()
