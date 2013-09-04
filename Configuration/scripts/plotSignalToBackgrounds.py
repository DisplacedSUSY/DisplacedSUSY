#!/usr/bin/env python
from array import *
import sys
import os
import math
from OSUT3Analysis.Configuration.configurationOptions import *

sys.path.append(os.getcwd())
sys.argv.pop(0)

for arg in sys.argv:
    exec("from " + arg.rstrip('.py') + " import *")

from ROOT import TFile, gROOT, gStyle, gDirectory, TStyle, THStack, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TIter, TKey, TGraphErrors, Double

integrateOutwardX = True
integrateOutwardY = True

histogramNames = [
  "electronAbsD0BeamspotVsMuonAbsD0Beamspot",
]

maxX = 0.05
maxY = 0.05
rebinFactor = 1

gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)

outputFile = TFile("signalToBackgrounds.root", "RECREATE")

channels = []
histograms = []
processed_datasets = []

#### check which input datasets have valid output files
for sample in datasets:
    testFile = TFile(sample+".root")
    if not (testFile.IsZombie()):
        processed_datasets.append(sample)

#### open first input file and re-make its directory structure in the output file
testFile = TFile(processed_datasets[0]+".root")
testFile.cd()
for key in testFile.GetListOfKeys():
    if (key.GetClassName() != "TDirectoryFile"):
        continue
    outputFile.cd()
    outputFile.mkdir(key.GetName())
    rootDirectory = key.GetName()

    testFile.cd(key.GetName())
    for key2 in gDirectory.GetListOfKeys():
        if (key2.GetClassName() != "TDirectoryFile"):
            continue
        outputFile.cd(key.GetName())
        gDirectory.mkdir(key2.GetName())
        channels.append(key2.GetName())




for channel in channels: # loop over final states, which each have their own directory

    if channel != "Isolated":
        continue

    testFile.cd(rootDirectory+"/"+channel)
    histograms = []
    for key in gDirectory.GetListOfKeys():
        if (key.GetClassName() == "TH2D" or key.GetClassName() == "TH1D"):
            histograms.append(key.GetName())

    if histogramNames:
        histograms = histogramNames

    outputFile.cd(rootDirectory+"/"+channel)

    for histogramName in histograms:

        IntegratedSignalHistogram = 0
        IntegratedBackgroundHistogram = 0

        for sample in processed_datasets: # loop over different samples as listed in configurationOptions.py

            print "Channel: " + channel + ", Histogram: " + histogramName + ", Sample: " + sample

            inputFile = TFile(sample+".root")
            if(inputFile.IsZombie()):
                continue
            Histogram = inputFile.Get(rootDirectory+"/"+channel+"/"+histogramName).Clone()
            Histogram.SetDirectory(0)
            Histogram.SetName("original")
            Histogram.Rebin2D(rebinFactor,rebinFactor)
            IntegratedHistogram = inputFile.Get(rootDirectory+"/"+channel+"/"+histogramName).Clone()
            IntegratedHistogram.SetDirectory(0)
            IntegratedHistogram.Rebin2D(rebinFactor,rebinFactor)
            inputFile.Close()

            if Histogram.ClassName () == "TH2D":
                nBinsX = Histogram.GetNbinsX()
                nBinsY = Histogram.GetNbinsY()
                for x in range(1,nBinsX + 1):
                    for y in range(1,nBinsY + 1):
                        x0 = x1 = y0 = y1 = 0
                        xValue = Histogram.GetXaxis().GetBinCenter(x)
                        yValue = Histogram.GetYaxis().GetBinCenter(y)
                        if math.fabs(xValue) > maxX or math.fabs(yValue) > maxY:
                          continue
                        if ((xValue >= 0) == integrateOutwardX):
                            x0 = x
                            x1 = nBinsX + 1
                        else:
                            x0 = 0
                            x1 = x
                        if ((yValue >= 0) == integrateOutwardY):
                            y0 = y
                            y1 = nBinsY + 1
                        else:
                            y0 = 0
                            y1 = y
                        intError = Double (0.0)
                        IntegratedHistogram.SetBinContent (x,y,Histogram.IntegralAndError(x0,x1,y0,y1,intError))
                        IntegratedHistogram.SetBinError (x,y,intError)
            if Histogram.ClassName () == "TH1D":
                nBinsX = Histogram.GetNbinsX()
                for x in range(1,nBinsX + 1):
                    x0 = x1 = 0
                    xValue = Histogram.GetXaxis().GetBinCenter(x)
                    if math.fabs(xValue) > maxX:
                      continue
                    if ((Histogram.GetXaxis().GetBinCenter(x) >= 0) == integrateOutwardX):
                        x0 = x
                        x1 = nBinsX + 1
                    else:
                        x0 = 0
                        x1 = x
                    intError = Double (0.0)
                    IntegratedHistogram.SetBinContent (x,Histogram.IntegralAndError(x0,x1,intError))
                    IntegratedHistogram.SetBinError (x,intError)

            if (types[sample] == "signalMC"):
                if (IntegratedSignalHistogram == 0):
                    IntegratedSignalHistogram = IntegratedHistogram
                else:
                    IntegratedSignalHistogram.Add(IntegratedHistogram)
            if (types[sample] == "bgMC"):
                if (IntegratedBackgroundHistogram == 0):
                    IntegratedBackgroundHistogram = IntegratedHistogram
                else:
                    IntegratedBackgroundHistogram.Add(IntegratedHistogram)

        IntegratedBackgroundHistogram.Add(IntegratedSignalHistogram)
        if IntegratedBackgroundHistogram.ClassName () == "TH2D":
            nBinsX = IntegratedBackgroundHistogram.GetNbinsX()
            nBinsY = IntegratedBackgroundHistogram.GetNbinsY()
            for x in range(1,nBinsX + 1):
                for y in range(1,nBinsY + 1):
                    xValue = Histogram.GetXaxis().GetBinCenter(x)
                    yValue = Histogram.GetYaxis().GetBinCenter(y)
                    if math.fabs(xValue) > maxX or math.fabs(yValue) > maxY:
                      continue
                    rootS = math.sqrt(IntegratedBackgroundHistogram.GetBinContent(x,y))
                    if rootS > 0.0:
                        rootSError = IntegratedBackgroundHistogram.GetBinError(x,y) / (2.0 * rootS)
                    else:
                        rootSError = 0.0
                    IntegratedBackgroundHistogram.SetBinContent(x,y,rootS)
                    IntegratedBackgroundHistogram.SetBinError(x,y,rootSError)
        if IntegratedBackgroundHistogram.ClassName () == "TH1D":
            nBinsX = IntegratedBackgroundHistogram.GetNbinsX()
            for x in range(1,nBinsX + 1):
                xValue = Histogram.GetXaxis().GetBinCenter(x)
                if math.fabs(xValue) > maxX:
                  continue
                rootS = math.sqrt(IntegratedBackgroundHistogram.GetBinContent(x))
                if rootS > 0.0:
                    rootSError = IntegratedBackgroundHistogram.GetBinError(x) / (2.0 * rootS)
                else:
                    rootSError = 0.0
                IntegratedBackgroundHistogram.SetBinContent(x,rootS)
                IntegratedBackgroundHistogram.SetBinError(x,rootSError)
        backgroundName = IntegratedBackgroundHistogram.GetName()
        signalName = IntegratedSignalHistogram.GetName()
        IntegratedBackgroundHistogram.SetName(backgroundName+"Denominator")
        IntegratedSignalHistogram.SetName(signalName+"Numerator")
        outputFile.cd(rootDirectory+"/"+channel)
        IntegratedBackgroundHistogram.Write()
        IntegratedSignalHistogram.Write()
        IntegratedSignalHistogram.Divide(IntegratedBackgroundHistogram)
        IntegratedSignalHistogram.SetName(signalName)
        outputFile.cd(rootDirectory+"/"+channel)
        IntegratedSignalHistogram.Write()

outputFile.Close()
