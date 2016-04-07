#!/usr/bin/env python

import time
import os
import sys
import math
import copy
import re
from math import *
from array import *
from optparse import OptionParser
from operator import itemgetter

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *


parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--condorDir", dest="condorDir",
                  help="condor output directory")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

if arguments.condorDir:
    condor_dir = set_condor_output_dir(arguments)
else:
    print "No condor output directory specified, shame on you"
    sys.exit(0)


from ROOT import TFile, gROOT, gStyle, gDirectory, TStyle, THStack, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TIter, TKey, TGraphErrors, Double

def getDivError(a,b,deltaa,deltab):
    return sqrt(pow(deltaa,2)/pow(b,2) + pow(deltab,2)*pow(a,2)/pow(b,4))
def getMulError(a,b,deltaa,deltab):
    return sqrt(pow(deltaa,2)*pow(b,2) + pow(deltab,2)*pow(a,2))

def MakeEffHist(process):
    inputFile  = TFile(condor_dir+"/"+process+".root")
    outputFile = TFile(condor_dir+"/"+process+"_DxyEff.root","RECREATE")
    MuHistogramObj = inputFile.Get(channel+"Plotter/"+mud0histogramName)
    EleHistogramObj = inputFile.Get(channel+"Plotter/"+eled0histogramName)
    if not MuHistogramObj:
        print "WARNING:  Could not find histogram " + channel+"Plotter/"+mud0histogramName + " in file " + process+".root" + ".  Will skip it and continue."
        return
    if not EleHistogramObj:
        print "WARNING:  Could not find histogram " + channel+"Plotter/"+eled0histogramName + " in file " + process+".root" + ".  Will skip it and continue."
        return
    
    mud0Histogram = MuHistogramObj.Clone()
    mud0Histogram.SetDirectory(0)
    newMud0Histogram = MuHistogramObj.Clone()
    newMud0Histogram.SetDirectory(0)
    eled0Histogram = EleHistogramObj.Clone()
    eled0Histogram.SetDirectory(0)
    newEled0Histogram = EleHistogramObj.Clone()
    newEled0Histogram.SetDirectory(0)
    inputFile.Close()
    muNBins = mud0Histogram.GetNbinsX()
    eleNBins = eled0Histogram.GetNbinsX()
    eleLimit = 0.0
    eleLimitErr = 0.0   
    muLimit = 0.0
    muLimitErr = 0.0
   
    for d0bin in range(1, muNBins + 1):     
        muDenErr = Double(0.0) 
        muDenIntegral = mud0Histogram.IntegralAndError(0, muNBins + 1, muDenErr)
        muNumErr = Double(0.0) 
        muNumIntegral = mud0Histogram.IntegralAndError(d0bin, muNBins + 1 ,muNumErr)
        muSF = muNumIntegral/muDenIntegral
        muSFErr = getDivError(muNumIntegral, muDenIntegral, muNumErr, muDenErr)
        if muSF <= 0:
            if muLimit == 0.0:
                muLimit = newMud0Histogram.GetBinContent(d0bin - 1)   
                muLimitErr = newMud0Histogram.GetBinError(d0bin - 1)   
                newMud0Histogram.SetBinContent(d0bin, muLimit)
                newMud0Histogram.SetBinError(d0bin, muLimitErr)
            else:
                newMud0Histogram.SetBinContent(d0bin, muLimit)
                newMud0Histogram.SetBinError(d0bin, muLimitErr)
        else:
            newMud0Histogram.SetBinContent(d0bin, muSF)
            newMud0Histogram.SetBinError(d0bin, muSFErr)
    newMud0Histogram.SetBinContent(muNBins, newMud0Histogram.GetBinContent(muNBins - 1))
    newMud0Histogram.SetBinError(muNBins, newMud0Histogram.GetBinError(muNBins - 1))
    outputFile.cd()
    newMud0Histogram.Write()    
    
    for d0bin in range(1, eleNBins + 1):     
        eleDenErr = Double(0.0) 
        eleDenIntegral = eled0Histogram.IntegralAndError(0, eleNBins + 1, eleDenErr)
        eleNumErr = Double(0.0) 
        eleNumIntegral = eled0Histogram.IntegralAndError(d0bin, eleNBins + 1 ,eleNumErr)
        eleSF = eleNumIntegral/eleDenIntegral
        eleSFErr = getDivError(eleNumIntegral, eleDenIntegral, eleNumErr, eleDenErr)
        if eleSF <= 0:
            if eleLimit == 0.0:
                eleLimit = newEled0Histogram.GetBinContent(d0bin - 1)   
                eleLimitErr = newEled0Histogram.GetBinError(d0bin - 1)   
                newEled0Histogram.SetBinContent(d0bin, eleLimit)
                newEled0Histogram.SetBinError(d0bin, eleLimitErr)
            else:
                newEled0Histogram.SetBinContent(d0bin, eleLimit)
                newEled0Histogram.SetBinError(d0bin, eleLimitErr)
        else:
            newEled0Histogram.SetBinContent(d0bin, eleSF)
            newEled0Histogram.SetBinError(d0bin, eleSFErr)
    newEled0Histogram.SetBinContent(eleNBins, newEled0Histogram.GetBinContent(eleNBins - 1))
    newEled0Histogram.SetBinError(eleNBins, newEled0Histogram.GetBinError(eleNBins - 1))
    outputFile.cd()
    newEled0Histogram.Write()    
    outputFile.Close()

for dataset in datasets:
    yieldAndError = MakeEffHist(dataset)
