#!/usr/bin/env python
import sys
import os
import re
import time
from math import *
from array import *
from decimal import *
from optparse import OptionParser
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *


####  Derive a scale factor such that the anti-isolated data can be a data-driven qcd dataset in the isolated region.
####  Simply normalize QCD such that the sum of MC and QCD matches the data

### parse the command-line options

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")

(arguments, args) = parser.parse_args()


if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")

from ROOT import TFile, gROOT, gStyle, gDirectory, TH1F, TIter, TKey, TF1, TF2


### setting ROOT options so our plots will look awesome and everyone will love us

gROOT.SetBatch()

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

def applySF (Histogram, sf):    
    xLimit = Histogram.GetNbinsX () + 2
    yLimit = Histogram.GetNbinsY () + 2
    zLimit = Histogram.GetNbinsZ () + 2
    if yLimit == 3:
      yLimit = 1
    if zLimit == 3:
      zLimit = 1
    for x in range (0, xLimit):
        for y in range (0, yLimit):
            for z in range (0, zLimit):
                bin = Histogram.GetBin (x, y, z)
                content = Histogram.GetBinContent (bin)
                error = Histogram.GetBinError (bin)
                newContent = content * sf
                newError = error * sf
                Histogram.SetBinContent (bin, newContent)
                Histogram.SetBinError (bin, newError)

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################


condor_dir = set_condor_output_dir(arguments)

fileName = condor_dir + "/" + data_dataset + ".root"
dataFile = TFile(fileName)

dataIsoHisto = dataFile.Get(region_names['signal'] + "CutFlowPlotter/cutFlow")
dataIsoYield = dataIsoHisto.GetBinContent(dataIsoHisto.GetNbinsX())
dataAntiIsoHisto = dataFile.Get(region_names['signal_antiIso'] + "CutFlowPlotter/cutFlow")
dataAntiIsoYield = dataAntiIsoHisto.GetBinContent(dataAntiIsoHisto.GetNbinsX())


mcIsoYield = 0
for sample in backgrounds:
    fileName = condor_dir + "/" + sample + ".root"
    MCFile = TFile(fileName)
    MCHisto = MCFile.Get(region_names['signal'] + "CutFlowPlotter/cutFlow")
    mcIsoYield += MCHisto.GetBinContent(MCHisto.GetNbinsX())


qcdIsoYield = dataIsoYield - mcIsoYield
qcdScaleFactor = float(qcdIsoYield)/float(dataAntiIsoYield)
print "qcdScaleFactor =", qcdScaleFactor

outputFileName = "QCDFromData.root"
outputFile = TFile(condor_dir + "/" + outputFileName, "RECREATE")
outputFile.cd()
gDirectory.mkdir(region_names['signal']+"Plotter")


#### open the input file and re-make its directory structure in the output file
inputFile = TFile(condor_dir + "/" + data_dataset + ".root")
inputFile.cd(region_names['signal_antiIso']+"Plotter")
for dir in gDirectory.GetListOfKeys(): # loop over histograms in the current directory
    print dir.GetClassName()
    if not re.match (r"TDirectory", dir.GetClassName()):
        continue
    outputFile.mkdir(region_names['signal']+"Plotter/"+dir.GetName())
    inputFile.cd(region_names['signal_antiIso']+"Plotter/"+dir.GetName())
    for plot in gDirectory.GetListOfKeys(): # loop over histograms in the current directory
        if not re.match (r"TH[123]", plot.GetClassName()):
            continue
        histogramName = plot.GetName()
        print "scaling and writing",histogramName
        Histogram = inputFile.Get(region_names['signal_antiIso']+"Plotter/"+dir.GetName()+"/"+histogramName).Clone()
        Histogram.SetDirectory(0)
        applySF (Histogram, qcdScaleFactor)
        
        outputFile.cd (region_names['signal']+"Plotter/"+dir.GetName())
        Histogram.Write ()

inputFile.Close()
outputFile.Close()
