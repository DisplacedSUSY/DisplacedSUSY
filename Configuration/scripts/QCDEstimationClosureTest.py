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
from OSUT3Analysis.Configuration.miniAODV2Samples import *

parser = OptionParser()
parser = set_commandline_arguments(parser)

(arguments, args) = parser.parse_args()
if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")

def getDivError(a,b,deltaa,deltab):
    return sqrt(pow(deltaa,2)/pow(b,2) + pow(deltab,2)*pow(a,2)/pow(b,4))
def getMulError(a,b,deltaa,deltab):
    return sqrt(pow(deltaa,2)*pow(b,2) + pow(deltab,2)*pow(a,2))
def Round2DHistograms(histogram, precision):
    newHistogram = histogram.Clone()
    for j in range(1, histogram.GetYaxis().GetNbins() + 1):
        for i in range(1, histogram.GetXaxis().GetNbins() + 1): 
            newHistogram.SetBinContent(i, j, round(histogram.GetBinContent(i,j), precision))
            newHistogram.SetBinError(i, j, round(histogram.GetBinError(i,j), precision))
    return newHistogram


scaleFactors = {}
def getScaleFactor(bbbarMuFile, bbbarEleFile, bbbarMuIPShape, bbbarEleIPShape, regionMap, key):
    scaleFactorSet = {}
    muFileToGet = TFile(bbbarMuFile)
    eleFileToGet = TFile(bbbarEleFile)
    muHistogramObj = muFileToGet.Get(bbbarMuIPShape)
    muHistogram = muHistogramObj.Clone()
    eleHistogramObj = eleFileToGet.Get(bbbarEleIPShape)
    eleHistogram = eleHistogramObj.Clone()
    normMuLow     = regionMap["normMuLow"]
    normMuHigh    = regionMap["normMuHigh"]
    normEleLow    = regionMap["normEleLow"]
    normEleHigh   = regionMap["normEleHigh"]
    targetMuLow   = regionMap["targetMuLow"]
    targetMuHigh  = regionMap["targetMuHigh"]
    targetEleLow  = regionMap["targetEleLow"]
    targetEleHigh = regionMap["targetEleHigh"]
    muDenError = Double(0.0)
    muDen = muHistogram.IntegralAndError(muHistogram.GetXaxis().FindBin(normMuLow), muHistogram.GetXaxis().FindBin(normMuHigh) - 1, muDenError)
    muNumError = Double(0.0)
    if not muHistogram.GetXaxis().FindBin(targetMuHigh) > muHistogram.GetXaxis().GetNbins():
        muNum = muHistogram.IntegralAndError(muHistogram.GetXaxis().FindBin(targetMuLow), muHistogram.GetXaxis().FindBin(targetMuHigh) - 1, muNumError)
    else:
        muNum = muHistogram.IntegralAndError(muHistogram.GetXaxis().FindBin(targetMuLow), muHistogram.GetXaxis().GetNbins() + 1, muNumError)
    muRatio = muNum/muDen
    muRatioError = getDivError(muNum,muDen,muNumError,muDenError)
    eleDenError = Double(0.0)
    eleDen = eleHistogram.IntegralAndError(eleHistogram.GetXaxis().FindBin(normEleLow), eleHistogram.GetXaxis().FindBin(normEleHigh) - 1, eleDenError)
    eleNumError = Double(0.0)
    if not eleHistogram.GetXaxis().FindBin(targetEleHigh) > eleHistogram.GetXaxis().GetNbins():
        eleNum = eleHistogram.IntegralAndError(eleHistogram.GetXaxis().FindBin(targetEleLow), eleHistogram.GetXaxis().FindBin(targetEleHigh) - 1, eleNumError)
    else:
        eleNum = eleHistogram.IntegralAndError(eleHistogram.GetXaxis().FindBin(targetEleLow), eleHistogram.GetXaxis().GetNbins() + 1, eleNumError)
    eleRatio = eleNum/eleDen
    eleRatioError = getDivError(eleNum,eleDen,eleNumError,eleDenError)
   
    print "Muon SF: " + str(muRatio) + "+-"  + str(muRatioError)
    print "Electron SF: " + str(eleRatio) + "+-" + str(eleRatioError)
    
    scalingFactor = muRatio*eleRatio
    scalingFactorError = getMulError(muRatio,eleRatio,muRatioError,eleRatioError) 
    
    scaleFactorSet["muSF"] = muRatio
    scaleFactorSet["muSFErr"] = muRatioError
    scaleFactorSet["eleSF"] = eleRatio
    scaleFactorSet["eleSFErr"] = eleRatioError
    scaleFactorSet["totalSF"] = scalingFactor
    scaleFactorSet["totalSFErr"] = scalingFactorError
    scaleFactors[key] = scaleFactorSet   
    
    print "#################################################"
    print "To estimate QCD in " + targetSource + " with: "  
    print str(targetEleLow) + "cm < " + "dxy_e < " + str(targetEleHigh) + "cm"  
    print str(targetMuLow) + "cm < " + "dxy_mu < " + str(targetMuHigh) + "cm"  
    print "Using normalization got in " + normSource + " with: "
    print str(normEleLow) + "cm < " + "dxy_e < " + str(normEleHigh) + "cm"  
    print str(normMuLow) + "cm < " + "dxy_mu < " + str(normMuHigh) + "cm"  
    print "Using dxy shapes got in bbbar + lepton control region"
    print "#################################################\n"
    print "########     Get the scaling factors    #########"
    print "Scaling factor is: " + str(round(scalingFactor,5))
    print "Scaling factor error is: " + str(round(scalingFactorError,5))
    print "#################################################\n"

def compareYields(dataNormFile, bgNormFile, normIPDistribution, dataTargetFile, bgTargetFile, targetNormIPDistribution, regionMap, key):
    normMuLow     = regionMap["normMuLow"]
    normMuHigh    = regionMap["normMuHigh"]
    normEleLow    = regionMap["normEleLow"]
    normEleHigh   = regionMap["normEleHigh"]
    targetMuLow   = regionMap["targetMuLow"]
    targetMuHigh  = regionMap["targetMuHigh"]
    targetEleLow  = regionMap["targetEleLow"]
    targetEleHigh = regionMap["targetEleHigh"]
    dataFileToGet = TFile(dataNormFile)
    bgFileToGet = TFile(bgNormFile)
    dataHistogramObj = dataFileToGet.Get(normIPDistribution)
    bgHistogramObj = bgFileToGet.Get(normIPDistribution)
    dataHistogram = dataHistogramObj.Clone()
    bgHistogram = bgHistogramObj.Clone()
    dataHistogram.Sumw2() 
    dataHistogram.Add(bgHistogram,-1)
    dataNormError = Double(0.0)
    dataNorm = dataHistogram.IntegralAndError(dataHistogram.GetXaxis().FindBin(normMuLow), dataHistogram.GetXaxis().FindBin(normMuHigh) - 1, dataHistogram.GetYaxis().FindBin(normEleLow), dataHistogram.GetYaxis().FindBin(normEleHigh) - 1, dataNormError)
    scalingFactor = scaleFactors[key]["totalSF"]
    scalingFactorError = scaleFactors[key]["totalSFErr"] 
    QCD = dataNorm * scalingFactor
    QCDError = getMulError(dataNorm, scalingFactor, dataNormError , scalingFactorError)
    
    print key
    print "########  Estimation using data-driven QCD  #####"
    print "Data-driven QCD is : " + str(round(QCD,5))
    print "Data-driven QCD error is: " + str(round(QCDError,5))
    print "########  Event Count in target region  #########"
    
    dataFileToGet = TFile(dataTargetFile)
    bgFileToGet = TFile(bgTargetFile)
    dataHistogramObj = dataFileToGet.Get(targetNormIPDistribution)
    bgHistogramObj = bgFileToGet.Get(targetNormIPDistribution)
    dataHistogram = dataHistogramObj.Clone()
    bgHistogram = bgHistogramObj.Clone()
    dataHistogram.Sumw2() 
    dataHistogram.Add(bgHistogram,-1)
    dataCountError = Double(0.0)
    dataCount = dataHistogram.IntegralAndError(dataHistogram.GetXaxis().FindBin(targetMuLow), dataHistogram.GetXaxis().FindBin(targetMuHigh) - 1, dataHistogram.GetYaxis().FindBin(targetEleLow), dataHistogram.GetYaxis().FindBin(targetEleHigh) - 1, dataCountError)
    
    print "Data - no-QCD MC is: " + str(round(dataCount,3))
    print "Data - no-QCD MC error is: " + str(round(dataCountError,3))
    print "#################################################\n"


for regionMap in regionMaps:
    getScaleFactor(bbbarMuFile, bbbarEleFile, bbbarMuIPShape, bbbarEleIPShape, regionMaps[regionMap], regionMap)

if performClosure:
    for regionMap in regionMaps:
        compareYields(dataNormFile, bgNormFile, normIPDistribution, dataTargetFile, bgTargetFile, targetNormIPDistribution, regionMaps[regionMap], regionMap)    

finalScaleFactors = {}

for i in range(0,len(scaleFactors.keys())):
    if i != len(scaleFactors.keys()) - 1:
        finalScaleFactor = scaleFactors[scaleFactors.keys()[i]]["totalSF"] - scaleFactors[scaleFactors.keys()[i+1]]["totalSF"]
        finalScaleFactorErr = math.sqrt(pow(scaleFactors[scaleFactors.keys()[i]]["totalSFErr"],2) + pow(scaleFactors[scaleFactors.keys()[i+1]]["totalSFErr"],2))
        regionName = "signalRegion" + str(i + 1)
        finalScaleFactors[regionName] = {}
        finalScaleFactors[regionName]["finalSF"] = finalScaleFactor
        finalScaleFactors[regionName]["finalSFErr"] = finalScaleFactorErr
    else:
        regionName = "signalRegion" + str(i + 1)
        finalScaleFactors[regionName] = {}
        finalScaleFactors[regionName]["finalSF"] = scaleFactors[scaleFactors.keys()[i]]["totalSF"]
        finalScaleFactors[regionName]["finalSFErr"] = scaleFactors[scaleFactors.keys()[i]]["totalSFErr"]

for signalRegion in finalScaleFactors:
    print "Final scale factor in " + str(signalRegion) + " is: " + str(finalScaleFactors[signalRegion]["finalSF"]) + "+-" + str(finalScaleFactors[signalRegion]["finalSFErr"]) 



