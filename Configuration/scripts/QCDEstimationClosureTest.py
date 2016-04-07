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


muFileToGet = TFile(bbbarMuFile)
eleFileToGet = TFile(bbbarEleFile)
muHistogramObj = muFileToGet.Get(bbbarMuIPShape)
muHistogram = muHistogramObj.Clone()
eleHistogramObj = eleFileToGet.Get(bbbarEleIPShape)
eleHistogram = eleHistogramObj.Clone()
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

scalingFactor = muRatio*eleRatio
scalingFactorError = getMulError(muRatio,eleRatio,muRatioError,eleRatioError) 



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
print "Scaling factor is: " + str(round(scalingFactor,3))
print "Scaling factor error is: " + str(round(scalingFactorError,3))
print "#################################################\n"
print "########          Estimate QCD          #########"

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

QCD = dataNorm * scalingFactor
QCDError = getMulError(dataNorm, scalingFactor, dataNormError , scalingFactorError)

print "Data-driven QCD is : " + str(round(QCD,5))
print "Data-driven QCD error is: " + str(round(QCDError,5))
print "#################################################\n"
print "########   Generate QCDFromData.root   #########"

os.system("mergeTFileServiceHistograms -i " + dataNormFile + " " + bgNormFile + " -w 1,-1 -o QCDNorm.root" )
qcdNormFile = TFile("QCDNorm.root")
outputFile = TFile(dataDrivenQCDFile,'RECREATE')
for key in qcdNormFile.GetListOfKeys():
    if (key.GetClassName() != "TDirectoryFile" or key.GetName() != normIPDistribution.split('/')[0]):
        continue
    rootDirectory = dataDrivenQCDIPDistribution.split('/')[0]
    outputFile.mkdir(rootDirectory)
    qcdNormFile.cd(normIPDistribution.split('/')[0])
    for key2 in gDirectory.GetListOfKeys():   
      if key2.GetClassName() == "TDirectoryFile" and 'beamspot' not in key2.GetName():
        level2Directory = rootDirectory+"/"+key2.GetName()
        outputFile.cd(rootDirectory)
        gDirectory.mkdir(key2.GetName())
        qcdNormFile.cd(normIPDistribution.split('/')[0] + "/" + key2.GetName())
        for key3 in gDirectory.GetListOfKeys():
          if re.match('TH1', key3.GetClassName()):   
            originHistObj = qcdNormFile.Get(normIPDistribution.split('/')[0] + "/" + key2.GetName() + "/" + key3.GetName())
            copiedHist = originHistObj.Clone()
            for n in range(0,copiedHist.GetXaxis().GetNbins() + 2): 
              copiedHist.SetBinContent(n, copiedHist.GetBinContent(n) * scalingFactor)
              copiedHist.SetBinError(n,getMulError(copiedHist.GetBinContent(n),scalingFactor,copiedHist.GetBinError(n), scalingFactorError))
            outputFile.cd(level2Directory)
            copiedHist.Write()
      if key2.GetClassName() == "TDirectoryFile" and 'Muon-beamspot' in key2.GetName():
        level2Directory = rootDirectory+"/"+key2.GetName()
        outputFile.cd(rootDirectory)
        gDirectory.mkdir(key2.GetName())
        qcdNormFile.cd(normIPDistribution.split('/')[0] + "/" + key2.GetName())
        for key3 in gDirectory.GetListOfKeys():
          if "muonAbsD0BeamspotS" == key3.GetName():
            originHistObj = qcdNormFile.Get(normIPDistribution.split('/')[0] + "/" + key2.GetName() + "/" + key3.GetName())      
            copiedHist = originHistObj.Clone()
            for n in range(1, copiedHist.GetXaxis().FindBin(normMuHigh)):
              copiedHist.SetBinContent(n,0.0)
              copiedHist.SetBinError(n,0.0)
            for n in range(copiedHist.GetXaxis().FindBin(normMuHigh), copiedHist.GetXaxis().FindBin(targetMuHigh)):
              factor = QCD/muNum
              copiedHist.SetBinContent(n,muHistogram.GetBinContent(int((n-1)/(muHistogram.GetBinWidth(1)/copiedHist.GetBinWidth(1)))+1)*factor/(muHistogram.GetBinWidth(1)/copiedHist.GetBinWidth(1)))
              copiedHist.SetBinError(n,muHistogram.GetBinError(int((n-1)/(muHistogram.GetBinWidth(1)/copiedHist.GetBinWidth(1))) +1)*factor/(muHistogram.GetBinWidth(1)/copiedHist.GetBinWidth(1)))
            outputFile.cd(level2Directory)
            copiedHist.Write() 
      if key2.GetClassName() == "TDirectoryFile" and 'Electron-beamspot' in key2.GetName():
        level2Directory = rootDirectory+"/"+key2.GetName()
        outputFile.cd(rootDirectory)
        gDirectory.mkdir(key2.GetName())
        qcdNormFile.cd(normIPDistribution.split('/')[0] + "/" + key2.GetName())
        for key3 in gDirectory.GetListOfKeys():
          if "electronAbsD0BeamspotS" == key3.GetName():
            originHistObj = qcdNormFile.Get(normIPDistribution.split('/')[0] + "/" + key2.GetName() + "/" + key3.GetName())      
            copiedHist = originHistObj.Clone()
            for n in range(0, copiedHist.GetXaxis().FindBin(normEleHigh)):
              copiedHist.SetBinContent(n,0.0)
              copiedHist.SetBinError(n,0.0)
            for n in range(copiedHist.GetXaxis().FindBin(normEleHigh), copiedHist.GetXaxis().FindBin(targetEleHigh)):
              copiedHist.SetBinContent(n,eleHistogram.GetBinContent(int((n-1)/(eleHistogram.GetBinWidth(1)/copiedHist.GetBinWidth(1)) + 1))*QCD/eleNum/(eleHistogram.GetBinWidth(1)/copiedHist.GetBinWidth(1)))
              copiedHist.SetBinError(n,eleHistogram.GetBinError(int((n-1)/(eleHistogram.GetBinWidth(1)/copiedHist.GetBinWidth(1))) + 1)*QCD/eleNum/(eleHistogram.GetBinWidth(1)/copiedHist.GetBinWidth(1)))
            outputFile.cd(level2Directory)
            copiedHist.Write() 
iPHistStrings = dataDrivenQCDIPDistribution.split('/')
newQCDHistogram = dataHistogram.Clone()
newQCDHistogram.SetBinContent(newQCDHistogram.GetXaxis().FindBin(targetMuLow), newQCDHistogram.GetYaxis().FindBin(targetEleLow), QCD)
newQCDHistogram.SetBinError(newQCDHistogram.GetXaxis().FindBin(targetMuLow), newQCDHistogram.GetYaxis().FindBin(targetEleLow), QCDError)
searchDir = outputFile.mkdir(iPHistStrings[0] + '/' + iPHistStrings[1])
outputFile.cd(iPHistStrings[0] + '/' + iPHistStrings[1])
newQCDHistogram.Write()

print "######## QCDFromData.root is Generated #########\n"
print "########           Sanity Check        #########"
qcdCountError = Double(0.0)
qcdCount = newQCDHistogram.IntegralAndError(newQCDHistogram.GetXaxis().FindBin(targetMuLow), newQCDHistogram.GetXaxis().FindBin(targetMuHigh) - 1, newQCDHistogram.GetYaxis().FindBin(targetEleLow), newQCDHistogram.GetYaxis().FindBin(targetEleHigh) - 1, qcdCountError)
print "######## QCD Count in QCDFromData.root #########"
print "QCD Events in QCDFromData.root: " + str(round(qcdCount,3))
print "QCD Events Error in QCDFromData.root: " + str(round(qcdCountError,3))
print "#################################################\n"

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

outputFile.Close()
dataFileToGet.Close()
bgFileToGet.Close()
muFileToGet.Close()
eleFileToGet.Close()
