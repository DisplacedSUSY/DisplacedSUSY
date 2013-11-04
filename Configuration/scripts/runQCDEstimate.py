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
    exec("from " + arguments.localConfig.rstrip('.py') + " import *")



from ROOT import TFile, gROOT, gStyle, gDirectory, TH1F, TIter, TKey, TF1


### setting ROOT options so our plots will look awesome and everyone will love us

gROOT.SetBatch()


##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################


def GetFittedQCDYieldAndError(pathToDir,distribution):

    BackgroundHistograms = []

    fileName = condor_dir + "/" + data_dataset + ".root"
    if not os.path.exists(fileName):
        return 0 
    inputFile = TFile(fileName)
    if inputFile.IsZombie() or not inputFile.GetNkeys():
        return 0 

    TargetHistogram = inputFile.Get("OSUAnalysis/"+region_names['A']+"/"+distribution).Clone()
    TargetHistogram.SetDirectory(0)

    QCDHistogram = inputFile.Get("OSUAnalysis/"+region_names['C']+"/"+distribution).Clone()
    QCDHistogram.SetDirectory(0)
    BackgroundHistograms.append(QCDHistogram)

    CutFlowHistogram = inputFile.Get("OSUAnalysis/"+region_names['C']+"CutFlow")
    QCDInputYield = CutFlowHistogram.GetBinContent(CutFlowHistogram.GetNbinsX())

    inputFile.Close()

    for sample in fitting_backgrounds: # loop over different samples that get held constant in the fit

        dataset_file = "%s/%s.root" % (condor_dir,sample)
        inputFile = TFile(dataset_file)
        HistogramObj = inputFile.Get(pathToDir+"/"+region_names['A']+"/"+distribution)
        if not HistogramObj:
            print "WARNING:  Could not find histogram " + pathToDir + "/" + distribution + " in file " + dataset_file + ".  Will skip it and continue."
            continue
        Histogram = HistogramObj.Clone()
        Histogram.SetDirectory(0)
        inputFile.Close()

        BackgroundHistograms.append(Histogram)

    nBackgrounds = len(BackgroundHistograms)


    def fitf (x, par):
        xBin = BackgroundHistograms[0].FindBin (x[0])
        value = 0.0
        
        # create the fit function to be used, with one parameter for each yield and one parameter for the error (to be set to -1,0,1 for varying by +-1 sigma)
        for i in range (0, len (BackgroundHistograms)):
            value += par[i] * BackgroundHistograms[i].GetBinContent (xBin) + par[i + len (BackgroundHistograms)] * BackgroundHistograms[i].GetBinError (xBin)
            
        return value

    
    lowerLimit = TargetHistogram.GetBinLowEdge (1)
    upperLimit = TargetHistogram.GetBinLowEdge (TargetHistogram.GetNbinsX ()) + TargetHistogram.GetBinWidth (TargetHistogram.GetNbinsX ())
    func = TF1 ("fit", fitf, lowerLimit, upperLimit, 2*(nBackgrounds))

    # initialize QCD scale factor parameter
    func.SetParameter (0, 1.0)
    func.SetParName (0, 'QCD_ScaleFactor')

    # initialize the other backgrounds that are held constant
    for i in range (1, nBackgrounds):
        func.FixParameter (i, 1.0)
        nameString = "background_" + str(i)
        func.SetParName (i, nameString)

    # shift each constant background component up and down by 1 sigma, refit and save new yields
    parErrorRanges = []
    for i in range (1, len (BackgroundHistograms)):
        for j in [-1, 1]:
            for k in range (len (BackgroundHistograms), 2 * len (BackgroundHistograms)):
                func.FixParameter (k, 0)
            func.FixParameter (i + len (BackgroundHistograms), j)
            for k in range (0, 9):
                if j == -1:
                    print "Scale down " + func.GetParName (i) + " iteration " + str (k + 1) + "..."
                if j == 1:
                    print "Scale up " + func.GetParName (i) + " iteration " + str (k + 1) + "..."
                TargetHistogram.Fit ("fit", "QEMR0")
            TargetHistogram.Fit ("fit", "QEMR0")
            # add the new QCD yields to the list of errors
            parErrorRanges.append(func.GetParameter(0))

    # get the QCD yield for the central values of the background histograms
    for i in range (nBackgrounds, 2*(nBackgrounds)):
        func.FixParameter (i, 0)
    for i in range (0, 9):
        print "Iteration " + str (i + 1) + "..."
        TargetHistogram.Fit ("fit", "QEMR0")
    TargetHistogram.Fit ("fit", "QEMR0")

    # take average of the deviations from the central value
    scaleDown = parErrorRanges[0]
    scaleUp = parErrorRanges[1]
    parError = (abs (scaleUp - scaleDown)) / 2

    yieldAndError = []
    yieldAndError.append(func.GetParameter(0) * QCDInputYield)
    yieldAndError.append(parError)

    return yieldAndError


##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

def applySF (Histogram, sf, sfError):
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
                newError = sqrt (content * content * sfError * sfError + error * error * sf * sf)
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


# 1

yields = {}
for distribution in distributions_to_fit:
    yields[distribution] = GetFittedQCDYieldAndError("OSUAnalysis",distribution)

print
print
print '---------------------------------------------------------------------------------'
print
print

print "yields and errors for fitting different distributions"
print '-----------------------------------------------------'
for distribution in distributions_to_fit:
    print distribution, ": ", yields[distribution]


# 2

numerator = 0
denominator = 0

for distribution in distributions_to_fit:
    absoluteError = yields[distribution][0] * yields[distribution][1]
    errorSquared = absoluteError * absoluteError
    numerator += yields[distribution][0] / errorSquared
    denominator += 1 / errorSquared

average = numerator / denominator

# 3

RMS = 0

for distribution in distributions_to_fit:
    deviation = average - yields[distribution][0]
    RMS += deviation * deviation

RMS = RMS / len(distributions_to_fit)
RMS = sqrt(RMS)

print
print "QCD Yield in region A = ", average, "+-", RMS, "(+-", RMS/average*100, "%)"

# 4

#dictionaries to hold the yields and fractional errors for the ABCD method
yields = {}
errors = {}

yields['A'] = average
errors['A'] = RMS/average

CutFlowHistogram = inputFile.Get("OSUAnalysis/"+region_names['C']+"CutFlow")
yields['C'] = CutFlowHistogram.GetBinContent(CutFlowHistogram.GetNbinsX())
errors['C'] = CutFlowHistogram.GetBinError(CutFlowHistogram.GetNbinsX()) / yields['C']

CutFlowHistogram = inputFile.Get("OSUAnalysis/"+region_names['D']+"CutFlow")
yields['D'] = CutFlowHistogram.GetBinContent(CutFlowHistogram.GetNbinsX())
errors['D'] = CutFlowHistogram.GetBinError(CutFlowHistogram.GetNbinsX()) / yields['D']


# B = A/C * D
# deltaB = sqrt(deltaA^2+deltaC^2+deltaD^2)

yields['B'] = yields['A'] / yields['C'] * yields['D']
errors['B'] = sqrt(errors['A']*errors['A'] + errors['C']*errors['C'] + errors['D']*errors['D'])

scale_factor = yields['A'] / yields['C']
scale_factor_error = scale_factor * errors['B']


print
print "A/C (B/D) Scale Factor = ", scale_factor, "+-",scale_factor_error, "(+-", scale_factor_error/scale_factor*100, "%)"
print

# 5

outputFileName = "QCDFromData.root"
outputFile = TFile(condor_dir + "/" + outputFileName, "RECREATE")

channel_map = {}
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
        applySF (Histogram, scale_factor, scale_factor_error)
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
        applySF (Histogram, scale_factor, scale_factor_error)

        outputFile.cd (rootDirectory + "/" + channel_map[channel])
        Histogram.Write ()


inputFile.Close()
outputFile.Close()
