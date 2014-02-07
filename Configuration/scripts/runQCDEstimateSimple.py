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



### parse the command-line options

parser = OptionParser()
parser = set_commandline_arguments(parser)

parser.remove_option("-o")
parser.remove_option("-n")
parser.remove_option("-u")
parser.remove_option("-e")
parser.remove_option("-r")
parser.remove_option("-R")
parser.remove_option("-d")
parser.remove_option("-b")
parser.remove_option("--2D")
parser.remove_option("-y")
parser.remove_option("-p")

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


def GetFittedQCDYieldAndError(pathToDir):

    BackgroundHistograms = {}
   
    fileName = condor_dir + "/" + data_dataset + ".root"
    if not os.path.exists(fileName):
        return 0 
    inputFile = TFile(fileName)
    if inputFile.IsZombie() or not inputFile.GetNkeys():
        return 0 
    DataHistogram = inputFile.Get("OSUAnalysis/"+region_names['A']+"CutFlow").Clone()
    DataHistogram.SetDirectory(0)
    
    nBins = DataHistogram.GetNbinsX ()
    content = DataHistogram.GetBinContent (nBins)
    error = DataHistogram.GetBinError (nBins)
    relError = error / content if content > 0 else 0
    print 'Data : ' + str(content) + ' +- ' + str(error) + ' ( +-' + str(relError * 100.0) + '% )' 

    inputFile.Close()

    for sample in fitting_backgrounds: # loop over different samples that get held constant in the fit

        dataset_file = "%s/%s.root" % (condor_dir,sample)
        inputFile = TFile(dataset_file)
        HistogramObj = inputFile.Get(pathToDir+"/"+region_names['A']+"CutFlow")
        if not HistogramObj:
            print "WARNING:  Could not find histogram " + pathToDir + "CutFlow" + " in file " + dataset_file + ".  Will skip it and continue."
            continue
        MCHistogram = HistogramObj.Clone()
        MCHistogram.SetDirectory(0)
        inputFile.Close()
        BackgroundHistograms[sample] = MCHistogram

    ###getting all the systematic errors and putting them in a dictionary
    systematics_dictionary = {}
    for systematic in external_systematic_uncertainties:
        input_file = open(os.environ['CMSSW_BASE']+"/src/DisplacedSUSY/Configuration/data/systematic_values__" + systematic + ".txt")
        for line in input_file:
            line = line.rstrip("\n").split(" ")
            dataset = line[0]
            if dataset not in systematics_dictionary:
                systematics_dictionary[dataset] = {}
                systematics_dictionary[dataset]['+'] = 0.0
                systematics_dictionary[dataset]['-'] = 0.0
            if len(line) is 2:
                line[1] = float (line[1])
                systematics_dictionary[dataset]['+'] += (line[1] - 1.0) * (line[1] - 1.0)
                systematics_dictionary[dataset]['-'] += (line[1] - 1.0) * (line[1] - 1.0)
            elif len(line) is 3:
                line[1] = float (line[1])
                line[2] = float (line[2])
                if line[1] > line[2]:
                    line[1],line[2] = line[2],line[1]
                systematics_dictionary[dataset]['+'] += (line[2] - 1.0) * (line[2] - 1.0)
                systematics_dictionary[dataset]['-'] += (1.0 - line[1]) * (1.0 - line[1])
    
    totalSystematicPlus = 0.0
    totalSystematicMinus = 0.0
    for HistName in BackgroundHistograms:
        Hist = BackgroundHistograms[HistName]
        nBins = Hist.GetNbinsX ()
        content = Hist.GetBinContent (nBins)
        error = Hist.GetBinError (nBins)
        if HistName in systematics_dictionary:
            totalSystematicPlus += systematics_dictionary[HistName]['+'] * content
            totalSystematicMinus += systematics_dictionary[HistName]['-'] * content
        else:
            print "WARNING: no systematics found for " + HistName
        DataHistogram.Add(Hist,-1)
        relError = error / content if content > 0 else 0
        print str(HistName) + ' : ' + str(content) + ' +- ' + str(error) + ' ( +-' + str(relError * 100.0) + '% )' 
    
    nBins = DataHistogram.GetNbinsX ()
    content = DataHistogram.GetBinContent (nBins)
    error = DataHistogram.GetBinError (nBins) / 2.0
    error *= error

    yieldAndError = []
    yieldAndError.append(content)
    yieldAndError.append(sqrt (error + totalSystematicPlus))
    yieldAndError.append(sqrt (error + totalSystematicMinus))

    return yieldAndError


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

def subtractImpurities (Histogram,channel=""):
    for sample in impurities:
        dataset_file = "%s/%s.root" % (condor_dir,sample)
        inputFile = TFile(dataset_file)
        ImpurityHistogram = inputFile.Get(rootDirectory+"/"+channel+"/"+histogramName).Clone()
        ImpurityHistogram.SetDirectory(0)
        inputFile.Close()
        Histogram.Add(ImpurityHistogram,-1)

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################


condor_dir = set_condor_output_dir(arguments)

fileName = condor_dir + "/" + data_dataset + ".root"
inputFile = TFile(fileName)

# outline
# -------
#
# 1. perform fit for each input distribution - vary background (including systematics)
# 2. find weighted average
# 3. find RMS of fitted yields about weighted average
# 4. get ABCD scaling factor and error
# 5. produce QCDFromData.root for preselection and signal region
print '########################################################################'
print "#This is runQCDEstimateSimple.py, which does not do the fitting at all.#"
print '########################################################################'
print
YieldsAndErrorInA = GetFittedQCDYieldAndError("OSUAnalysis")
print
print '-----------------------------------------------------------------------------------------------------------------'

plus = YieldsAndErrorInA[1]
minus = YieldsAndErrorInA[2]
plusRelative = YieldsAndErrorInA[1] / YieldsAndErrorInA[0] if YieldsAndErrorInA[0] > 0 else 0
minusRelative = YieldsAndErrorInA[2] / YieldsAndErrorInA[0] if YieldsAndErrorInA[0] > 0 else 0
print "QCD Yield in Region A by Subtracting MC from Data = ", YieldsAndErrorInA[0], "+", plus, "-", minus, "(+", plusRelative, "-", minusRelative, "%)"
print '-----------------------------------------------------------------------------------------------------------------'

# 4

#dictionaries to hold the yields and fractional errors for the ABCD method
yields = {}
errors = {}

yields['A'] = YieldsAndErrorInA[0]
errors['A'] = {}
errors['A']['+'] = YieldsAndErrorInA[1] / yields['A']
errors['A']['-'] = YieldsAndErrorInA[2] / yields['A']

CutFlowHistogram = inputFile.Get("OSUAnalysis/"+region_names['C']+"CutFlow")
yields['C'] = CutFlowHistogram.GetBinContent(CutFlowHistogram.GetNbinsX())
errors['C'] = {}
errors['C']['+'] = (CutFlowHistogram.GetBinError(CutFlowHistogram.GetNbinsX()) / 2.0) / yields['C']
errors['C']['-'] = (CutFlowHistogram.GetBinError(CutFlowHistogram.GetNbinsX()) / 2.0) / yields['C']

CutFlowHistogram = inputFile.Get("OSUAnalysis/"+region_names['D']+"CutFlow")
yields['D'] = CutFlowHistogram.GetBinContent(CutFlowHistogram.GetNbinsX())
errors['D'] = {}
errors['D']['+'] = (CutFlowHistogram.GetBinError(CutFlowHistogram.GetNbinsX()) / 2.0) / yields['D']
errors['D']['-'] = (CutFlowHistogram.GetBinError(CutFlowHistogram.GetNbinsX()) / 2.0) / yields['D']


# B = A/C * D
# deltaB = sqrt(deltaA^2+deltaC^2+deltaD^2)

yields['B'] = yields['A'] / yields['C'] * yields['D']
errors['B'] = {}
errors['B']['+'] = sqrt(errors['A']['+']*errors['A']['+'] + errors['C']['+']*errors['C']['+'] + errors['D']['+']*errors['D']['+'])
errors['B']['-'] = sqrt(errors['A']['-']*errors['A']['-'] + errors['C']['-']*errors['C']['-'] + errors['D']['-']*errors['D']['-'])

errors['A/C'] = {}
errors['A/C']['+'] = sqrt(errors['A']['+']*errors['A']['+'] + errors['C']['+']*errors['C']['+'])
errors['A/C']['-'] = sqrt(errors['A']['-']*errors['A']['-'] + errors['C']['-']*errors['C']['-'])

scale_factor = yields['A'] / yields['C']
scale_factor_rel_error_plus = errors['A/C']['+'] * 100.0
scale_factor_rel_error_minus = errors['A/C']['-'] * 100.0
scale_factor_error_plus = scale_factor *errors['A/C']['+']
scale_factor_error_minus = scale_factor *errors['A/C']['-']


print '-----------------------------------------------------------------------------------------------------------------'
print "A/C (B/D) Scale Factor = ", scale_factor, "+",scale_factor_error_plus, "-", scale_factor_error_minus, "(+", scale_factor_rel_error_plus, "-", scale_factor_rel_error_minus, "%)"
print '-----------------------------------------------------------------------------------------------------------------'

# 5

outputFileName = "QCDFromData.root"
outputFile = TFile(condor_dir + "/" + outputFileName, "RECREATE")

channel_map = {}
channel_map[region_names['C']] = region_names['A']
channel_map[region_names['D']] = region_names['B']
channel_map[region_names['signal_antiIso']] = region_names['signal']

input_channels = []

#### open the input file and re-make its directory structure in the output file
inputFile = TFile(condor_dir + "/" + data_dataset + ".root")
inputFile.cd()
for key in inputFile.GetListOfKeys():
    if (key.GetClassName() != "TDirectoryFile"):
        continue
    outputFile.cd()
    rootDirectory = key.GetName()
    outputFile.mkdir(rootDirectory)

    inputFile.cd(rootDirectory)
    for key2 in gDirectory.GetListOfKeys():
        if (key2.GetClassName() != "TDirectoryFile"):
            continue
        current_channel_name = key2.GetName()
        if current_channel_name in channel_map:
            input_channels.append(current_channel_name)
            outputFile.cd(rootDirectory)
            gDirectory.mkdir(channel_map[current_channel_name])


#do the thing for cutflow histograms
inputFile.cd(rootDirectory)
for key in gDirectory.GetListOfKeys(): # loop over histograms in the current directory
    if not re.match (r"TH[123]", key.GetClassName()):
        continue
    histogramName = key.GetName()

    for channel in input_channels:
        if histogramName.find(channel) is -1:
            continue

        Histogram = inputFile.Get(rootDirectory+"/"+histogramName).Clone()
        Histogram.SetDirectory(0)

        subtractImpurities (Histogram)
        applySF (Histogram, scale_factor)
        outputFile.cd (rootDirectory)

        #change the names of the cutflow histograms, so it will still work with makeYieldsTables.py
        Histogram.Write(Histogram.GetName().replace(channel,channel_map[channel]))

#do the thing for histograms in the channels directories
for channel in input_channels: # loop over final states, which each have their own directory

    print "Applying scale factor for " + channel + " -> " + channel_map[channel]

    inputFile.cd(rootDirectory+"/"+channel)
    
    for key in gDirectory.GetListOfKeys(): # loop over histograms in the current directory
        if not re.match (r"TH[123]", key.GetClassName()):
            continue
        histogramName = key.GetName()

        Histogram = inputFile.Get(rootDirectory+"/"+channel+"/"+histogramName).Clone()
        Histogram.SetDirectory(0)

        subtractImpurities (Histogram,channel)
        applySF (Histogram, scale_factor)

        outputFile.cd (rootDirectory + "/" + channel_map[channel])
        Histogram.Write ()


inputFile.Close()
outputFile.Close()
