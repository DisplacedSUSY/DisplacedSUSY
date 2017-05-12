#! /usr/bin/env python

# factorizationClosure.py
# Make plots to compare factorization-method yields with counting-method yields
#
# Usage: factorizationClosure.py -l sampleConfig.py


import os
import sys
import random
import math
import re
from array import array
from optparse import OptionParser
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *


parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub(r".py$", r"", arguments.localConfig) + " import *")
else:
    print "Please specify a local config file"
    sys.exit(0)


from ROOT import TString, TFile, TH2D, TGraphErrors, Double, TCanvas, TLegend


def getYieldsAndErrors(hist, datasetName):

    # Make everything arrays to please TGraph
    countYields  = array('d')
    factorYields = array('d')
    dZeroVals    = array('d')
    countErrors  = array('d')
    factorErrors = array('d')
    dZeroErrors  = array('d')

    maxBinNum = hist.GetXaxis().GetNbins() # Assume xMax = yMax

    # Get yields and errors
    # Used Freya's 0s, 1s, and +2s. Need to check
    for bin in range(1, maxBinNum + 1):

        totalError  = Double(0.0)
        targetError = Double(0.0)
        totalCount  = hist.IntegralAndError(1, maxBinNum + 2, 0, maxBinNum, totalError)
        targetCount = hist.IntegralAndError(bin, maxBinNum + 2, bin, maxBinNum, targetError)

        xError = Double(0.0)
        yError = Double(0.0)
        xCount = hist.IntegralAndError(bin, maxBinNum + 2, 0, maxBinNum, xError)
        yCount = hist.IntegralAndError(0, maxBinNum + 2, bin, maxBinNum, yError)

        countYields.append(targetCount)
        countErrors.append(targetError)

        factorYields.append(xCount * yCount / totalCount)
        factorError = Double(0.0)
        if xCount > 0 and yCount > 0 and totalCount > 0:
            factorError = ( math.pow(xError/xCount, 2) + math.pow(yError/yCount, 2)
                          + math.pow(totalError/totalCount, 2) )
            factorError = math.sqrt(factorError) * (xCount * yCount / totalCount)
        factorErrors.append(factorError)

        dZeroVals.append(hist.GetXaxis().GetBinLowEdge(bin))
        dZeroErrors.append(0)
        

    countPlot  = TGraphErrors(len(dZeroVals), dZeroVals, countYields,  dZeroErrors, countErrors)
    factorPlot = TGraphErrors(len(dZeroVals), dZeroVals, factorYields, dZeroErrors, factorErrors)


    # Draw, add legend, print - still need to make pretty
    canvas = TCanvas("canvas", "ComparisonPlot", 200, 10, 700, 500)
    countPlot.Draw("")
    factorPlot.Draw("SAME")

    countPlot.SetLineColor(3)
    factorPlot.SetLineColor(1)
    countPlot.GetXaxis().SetTitle

    legend = TLegend(0.6, 0.7, 0.8, 0.8)
    legend.AddEntry(countPlot, "Counting Method Yield", "l")
    legend.AddEntry(factorPlot, "Factorization Method Yield", "l")
    legend.Draw()

    canvas.SetLogy()
    canvas.Update()
    canvas.SaveAs("factorizationClosure_" + re.sub(r".root$", r".pdf", datasetName))


for s in input_sources:
    inputFile = TFile("condor/" + s['condor_dir'] + "/" + s['dataset'])
    inputHist = inputFile.Get(s['channel'] + "Plotter/" + s['hist_dir'] + "/" + s['hist'])
    if not inputHist:
        print "Input histogram not found"
        sys.exit(0)
    getYieldsAndErrors(inputHist, s['dataset'])




