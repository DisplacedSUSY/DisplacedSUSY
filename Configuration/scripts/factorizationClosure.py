#! /usr/bin/env python

# compareFactorizationCounting.py
# Make plots to compare factorization-method yields with counting-method yields

import sys
import random
import math
from array import array
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *

from ROOT import TString, TFile, TH2D, TGraphErrors, Double, TCanvas, TLegend

inputFile = TFile("/data/users/bcardwell/condor/EMuPreselection_MC_Dec9/DYJetsToLL_50.root")
inputHist = inputFile.Get("PreselectionPlotter/Electron-muon-beamspot Plots/electronAbsD0_vs_muonAbsD0_500um")
if not inputHist:
    print "Input histogram not found"
    sys.exit(0)

# Testing
#inputHist = TH2D("testHist", "testHist", 10, 0, 10, 10, 0, 10)
#for i in range(1000):
    #inputHist.Fill(random.randint(0, 9), random.randint(0, 9))

# Make everything arrays to please TGraph
countYields  = array('d')
factorYields = array('d')
dZeroVals    = array('d')
countErrors  = array('d')
factorErrors = array('d')
dZeroErrors  = array('d')

maxBinNum = inputHist.GetXaxis().GetNbins() # Assume xMax = yMax

# Get yields and errors
for bin in range(1, maxBinNum + 1): #arbitrary start point for testing

    # Used Freya's 0s, 1s, and +2s. Need to check
    totalError  = Double(0.0)
    targetError = Double(0.0)
    totalCount  = inputHist.IntegralAndError(1, maxBinNum + 2, 0, maxBinNum, totalError)
    targetCount = inputHist.IntegralAndError(bin, maxBinNum + 2, bin, maxBinNum, targetError)

    xError = Double(0.0)
    yError = Double(0.0)
    xCount = inputHist.IntegralAndError(bin, maxBinNum + 2, 0, maxBinNum, xError)
    yCount = inputHist.IntegralAndError(0, maxBinNum + 2, bin, maxBinNum, yError)

    countYields.append(targetCount)
    countErrors.append(targetError)

    factorYields.append(xCount * yCount / totalCount)
    factorError = Double(0.0)
    if xCount > 0 and yCount > 0 and totalCount > 0:
        factorError = math.pow(xError/xCount, 2) + math.pow(yError/yCount, 2) + math.pow(totalError/totalCount, 2)
        factorError = math.sqrt(factorError) * (xCount * yCount / totalCount)
    factorErrors.append(factorError)

    dZeroVals.append(inputHist.GetXaxis().GetBinLowEdge(bin))
    dZeroErrors.append(0)
    
# Hardcoded -2 is bad
countPlot  = TGraphErrors(maxBinNum - 2, dZeroVals, countYields,  dZeroErrors, countErrors)
factorPlot = TGraphErrors(maxBinNum - 2, dZeroVals, factorYields, dZeroErrors, factorErrors)

#Testing
print dZeroVals
print countYields
print factorYields

# Draw stuff, add legend, print
canvas = TCanvas("canvas", "ComparisonPlot", 200, 10, 700, 500)
countPlot.Draw("")
factorPlot.Draw("SAME")

countPlot.SetLineColor(3)
factorPlot.SetLineColor(1)

legend = TLegend(0.6, 0.7, 0.8, 0.8)
legend.AddEntry(countPlot, "Counting Method Yield", "l")
legend.AddEntry(factorPlot, "Factorization Method Yield", "l")
legend.Draw()

canvas.SetLogy()
canvas.Update()
canvas.SaveAs("compareTest.pdf")
