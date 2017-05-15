#! /usr/bin/env python

# factorizationClosure.py
# Make plots to compare factorization-method yields with counting-method yields
#
# Usage: factorizationClosure.py -l configFile.py -w workingDirectory


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
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub(r".py$", r"", arguments.localConfig) + " import *")
else:
    print "Please specify a local config file"
    sys.exit(0)

if arguments.condorDir:
    condorDir = arguments.condorDir
else:
    print "Please specify a working directory"
    sys.exit(0)


from ROOT import (TString, TFile, TH2D, TGraphErrors, Double, TCanvas, TLegend,
                  gROOT, gStyle, TDirectory, TMultiGraph)

# Make plots look nice (copied from makePlots)
gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetCanvasDefH(600)
gStyle.SetCanvasDefW(600)
gStyle.SetCanvasDefX(0)
gStyle.SetCanvasDefY(0)
gStyle.SetPadTopMargin(0.056)
gStyle.SetPadBottomMargin(0.13)
gStyle.SetPadLeftMargin(0.1476)
gStyle.SetPadRightMargin(0.05)
gStyle.SetHistTopMargin(0)
gStyle.SetTitleColor(1, "XYZ")
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.05, "XYZ")
gStyle.SetTitleXSize(0.04)
gStyle.SetTitleXOffset(1.25)
gStyle.SetTitleYSize(0.04)
gStyle.SetTitleYOffset(1.5)
#gStyle.SetTextFont(42)
gStyle.SetTextAlign(12)
gStyle.SetLabelColor(1, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelOffset(0.005, "XYZ")
gStyle.SetLabelSize(0.04, "XYZ")
gStyle.SetAxisColor(1, "XYZ")
gStyle.SetStripDecimals(True)
gStyle.SetTickLength(0.03, "XYZ")
gStyle.SetNdivisions(505, "XYZ")
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gROOT.ForceStyle()


def getFactorError(xCount, yCount,totalCount, xError, yError, totalError):
    factorError = 0.0;
    if xCount > 0 and yCount > 0 and totalCount > 0:
        factorError = ( math.pow(xError/xCount, 2) + math.pow(yError/yCount, 2)
                      + math.pow(totalError/totalCount, 2) )
        factorError = math.sqrt(factorError) * (xCount * yCount / totalCount)
    return factorError


def makePlots(yieldsAndErrors, datasetName, outputFile):

    countPlot  = TGraphErrors(len(yieldsAndErrors['dZeroVals']),
                              yieldsAndErrors['dZeroVals'],
                              yieldsAndErrors['countYields'],
                              yieldsAndErrors['dZeroErrors'],
                              yieldsAndErrors['countErrors'])

    factorPlot = TGraphErrors(len(yieldsAndErrors['dZeroVals']),
                              yieldsAndErrors['dZeroVals'],
                              yieldsAndErrors['factorYields'],
                              yieldsAndErrors['dZeroErrors'],
                              yieldsAndErrors['factorErrors'])

    canvas = TCanvas(datasetName, datasetName)
    canvas.SetLogy()

    legend = TLegend(0.6, 0.7, 0.8, 0.8)
    legend.AddEntry(countPlot, "Counting Method Yield", "l")
    legend.AddEntry(factorPlot, "Factorization Method Yield", "l")

    countPlot.Draw()
    factorPlot.Draw("SAME")
    legend.Draw()

    countPlot.SetLineColor(30)
    factorPlot.SetLineColor(38)
    countPlot.SetTitle(datasetName)
    countPlot.GetXaxis().SetTitle("d0 [mum]")
    countPlot.GetYaxis().SetTitle("Target Region Yield")

    canvas.Update()

    outputFile.cd()
    dir = outputFile.mkdir(datasetName)
    dir.cd()
    canvas.Write()


def getYieldsAndErrors(hist):

    # Make arrays to please TGraph
    countYields  = array('d')
    factorYields = array('d')
    dZeroVals    = array('d')
    countErrors  = array('d')
    factorErrors = array('d')
    dZeroErrors  = array('d')

    maxBinNum = hist.GetXaxis().GetNbins() # Assume xMax = yMax

    for bin in range(1, maxBinNum + 1):

        totalError  = Double(0.0)
        targetError = Double(0.0)
        totalCount  = hist.IntegralAndError(1, maxBinNum + 1, 1, maxBinNum, totalError)
        targetCount = hist.IntegralAndError(bin, maxBinNum + 2, bin, maxBinNum,
                                            targetError)

        xError = Double(0.0)
        yError = Double(0.0)
        xCount = hist.IntegralAndError(bin, maxBinNum + 1, 1, maxBinNum, xError)
        yCount = hist.IntegralAndError(1, maxBinNum + 1, bin, maxBinNum, yError)

        countYields.append(targetCount)
        countErrors.append(targetError)

        factorYields.append(xCount * yCount / totalCount)
        factorErrors.append(getFactorError(xCount, yCount, totalCount,
                                           xError, yError, totalError))

        dZeroVals.append(hist.GetXaxis().GetBinLowEdge(bin))
        dZeroErrors.append(0)

    yieldsAndErrors = {}
    yieldsAndErrors['dZeroVals'] = dZeroVals
    yieldsAndErrors['dZeroErrors'] = dZeroErrors
    yieldsAndErrors['countYields'] = countYields
    yieldsAndErrors['countErrors'] = countErrors
    yieldsAndErrors['factorYields'] = factorYields
    yieldsAndErrors['factorErrors'] = factorErrors

    return yieldsAndErrors


##########################################################################################
##########################################################################################


outputFile = TFile("factorizationClosure_" + condorDir + ".root", "recreate")

for s in input_sources:
    inputFile = TFile("condor/%s/%s.root" % (condorDir, s['dataset']))
    if not inputFile:
        print "Input file not found"
        sys.exit(0)
    inputHist = inputFile.Get(s['histPath'])
    if not inputHist:
        print "Input histogram not found"
        sys.exit(0)

    yieldsAndErrors = getYieldsAndErrors(inputHist)
    makePlots(yieldsAndErrors, s['dataset'], outputFile)


