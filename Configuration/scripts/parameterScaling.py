#!/usr/bin/env python

from decimal import *
import sys
import os
import re
from math import *
from array import *
from ROOT import *  
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

def getDivError(a,b,deltaa,deltab):
    return sqrt(pow(deltaa,2)/pow(b,2) + pow(deltab,2)*pow(a,2)/pow(b,4))
def getMulError(a,b,deltaa,deltab):
    return sqrt(pow(deltaa,2)*pow(b,2) + pow(deltab,2)*pow(a,2))

parser = OptionParser()
parser = set_commandline_arguments(parser)
(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")

condor_dir = "condor/%s" % condorDir

for cut in cuts:
    print "Signal Selection: " + str(cut) + " cm"

    fileToGet = TFile(condor_dir + '/' + dataset + '.root')
    muonDxyHistogramObj = fileToGet.Get(dxParametrizationChannelPlotter + "/Muon-beamspot Plots/absMuonDxyInclusive")
    muonDxyHistogram = muonDxyHistogramObj.Clone()
    totalYieldsHistogramObj = fileToGet.Get(dxParametrizationChannelPlotter + "/Electron-muon-beamspot Plots/electronIpMuonIpInclusive")
    totalYieldsHistogram = totalYieldsHistogramObj.Clone()
    TotalNumberError = Double(0.0)
    TotalNumber = totalYieldsHistogram.IntegralAndError(0, totalYieldsHistogram.GetNbinsX() + 1, 0, totalYieldsHistogram.GetNbinsY() + 1, TotalNumberError)
    mDenError = Double(0.0)
    mDenYields = muonDxyHistogram.IntegralAndError(0, muonDxyHistogram.GetXaxis().GetNbins() + 1, mDenError)
    mNumError = Double(0.0)
    mNumYields = muonDxyHistogram.IntegralAndError(muonDxyHistogram.GetXaxis().FindBin(cut), muonDxyHistogram.GetXaxis().GetNbins() + 1, mNumError)
    muonDxyRatio = mNumYields/mDenYields
    muonDxyRatioError = getDivError(mNumYields,mDenYields,mNumError,mDenError)
    
    eleDxyHistogramObj = fileToGet.Get(dxParametrizationChannelPlotter + "/Electron-beamspot Plots/absElectronDxyInclusive")
    eleDxyHistogram = eleDxyHistogramObj.Clone()
    eDenError = Double(0.0)
    eDenYields = eleDxyHistogram.IntegralAndError(0, eleDxyHistogram.GetXaxis().GetNbins() + 1, eDenError)
    eNumError = Double(0.0)
    eNumYields = eleDxyHistogram.IntegralAndError(eleDxyHistogram.GetXaxis().FindBin(cut), eleDxyHistogram.GetXaxis().GetNbins() + 1, eNumError)
    eleDxyRatio = eNumYields/eDenYields
    eleDxyRatioError = getDivError(eNumYields,eDenYields,eNumError,eDenError)
    
    totalDxyEfficiency = muonDxyRatio * eleDxyRatio
    totalDxyEfficiencyError = getMulError(muonDxyRatio,eleDxyRatio,muonDxyRatioError,eleDxyRatioError)
    
    YieldsByDxyParametrization = totalDxyEfficiency * TotalNumber
    ErrorByxyParametrization = getMulError(TotalNumber,totalDxyEfficiency,TotalNumberError,totalDxyEfficiencyError)
    
    print "Estimated by dxy parametrization: " + str(YieldsByDxyParametrization ) + " +- " + str(ErrorByxyParametrization)
    
    
    fileToGet = TFile(condor_dir + '/' + dataset + '.root')
    pTHistogramObj = fileToGet.Get(ptScalingChannelPlotter + "/Electron-muon-beamspot Plots/electronPtMuonPt")
    pTHistogram = pTHistogramObj.Clone()
    pTDenError = Double(0.0)
    pTDenYields = pTHistogram.IntegralAndError(0, pTHistogram.GetNbinsX() + 1, 0, pTHistogram.GetNbinsY() + 1, pTDenError)
    pTNumError = Double(0.0)
    pTNumYields = pTHistogram.IntegralAndError(pTHistogram.GetXaxis().FindBin(42),pTHistogram.GetNbinsX() + 1, pTHistogram.GetYaxis().FindBin(40), pTHistogram.GetNbinsY() + 1, pTNumError)
    pTRatio = pTNumYields/pTDenYields
    pTRatioError = getDivError(pTNumYields,pTDenYields,pTNumError,pTDenError)
    
    totalYieldsHistogramObj = fileToGet.Get(ptScalingChannelPlotter + "/Electron-muon-beamspot Plots/electronIpMuonIpInclusive")
    totalYieldsHistogram = totalYieldsHistogramObj.Clone()
    totalYieldsError = Double(0.0)
    totalYields = totalYieldsHistogram.IntegralAndError(totalYieldsHistogram.GetXaxis().FindBin(cut), totalYieldsHistogram.GetNbinsX() + 1, totalYieldsHistogram.GetYaxis().FindBin(cut), totalYieldsHistogram.GetNbinsY() + 1, totalYieldsError)
    
    YieldsByPtScaling = pTRatio * totalYields
    ErrorByPtScaling = getMulError(totalYields,pTRatio,totalYieldsError,pTRatioError)
    
    print "Estimated by pT scaling: " + str(YieldsByPtScaling) + " +- " + str(ErrorByPtScaling)
    
    fileToGet = TFile(condor_dir + '/'  + dataset + '.root')
    totalYieldsHistogramObj = fileToGet.Get(directCutChannelPlotter + "/Electron-muon-beamspot Plots/electronIpMuonIpInclusive")
    totalYieldsHistogram = totalYieldsHistogramObj.Clone()
    totalYieldsError = Double(0.0)
    totalYields = totalYieldsHistogram.IntegralAndError(totalYieldsHistogram.GetXaxis().FindBin(cut), totalYieldsHistogram.GetNbinsX() + 1, totalYieldsHistogram.GetYaxis().FindBin(cut), totalYieldsHistogram.GetNbinsY() + 1, totalYieldsError)
    
    print "Estimated by direct cuts: " + str(totalYields) + " +- " + str(totalYieldsError)
