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
parser.add_option("-s", "--standAlone", action="store_true", dest="standAlone", default=False,
                                    help="adds the necessary header to be able to compile it")
parser.add_option("-S", "--systematics", action="store_true", dest="includeSystematics", default=False,
                                    help="also lists the systematic uncertainties")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

if arguments.includeSystematics:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", systematics_file) + " import *")

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

def GetYieldAndError(process,d0cut):
    if process == "WJetsToLNu":
        processTmp = "Diboson"
    else:
        processTmp = process
    inputFile = TFile(condor_dir+"/"+process+".root")
    effInputFile = TFile(condor_dir+"/"+processTmp+"_DxyEff.root")
    HistogramObj = inputFile.Get(channel+"Plotter/"+d0histogramName)
    MuHistogramObj = effInputFile.Get(mud0histogramName)
    EleHistogramObj = effInputFile.Get(eled0histogramName)
    if not HistogramObj:
        print "WARNING:  Could not find histogram " + channel+"Plotter/"+d0histogramName + " in file " + process+".root" + ".  Will skip it and continue."
        return
    if not MuHistogramObj:
        print "WARNING:  Could not find histogram " + mud0histogramName + " in file " + processTmp+"_DxyEff.root" + ".  Will skip it and continue."
        return
    if not EleHistogramObj:
        print "WARNING:  Could not find histogram " + eled0histogramName + " in file " + processTmp+"_DxyEff.root" + ".  Will skip it and continue."
        return
    d0Histogram = HistogramObj.Clone()
    d0Histogram.SetDirectory(0)
    mud0Histogram = MuHistogramObj.Clone()
    mud0Histogram.SetDirectory(0)
    eled0Histogram = EleHistogramObj.Clone()
    eled0Histogram.SetDirectory(0)
    inputFile.Close()

    yieldAndErrorList = {}

    muNBins = mud0Histogram.GetNbinsX()
    mud0CutBin  = mud0Histogram.GetXaxis ().FindBin (float(d0cut))
    mud0CutUpper = mud0Histogram.GetXaxis ().FindBin (float(d0UpperCut))
    if mud0Histogram.GetXaxis ().FindBin (float(d0cut)) >= mud0Histogram.GetNbinsX ():
       mud0CutBin = mud0Histogram.GetNbinsX ()
    if mud0Histogram.GetXaxis ().FindBin (float(d0UpperCut)) > mud0Histogram.GetNbinsX ():
       muSF = mud0Histogram.GetBinContent(mud0CutBin)
       muSFErr = sqrt(pow(mud0Histogram.GetBinError(mud0CutBin),2))
    elif mud0Histogram.GetBinContent(mud0CutBin) == mud0Histogram.GetBinContent(mud0CutUpper):
       muSF = mud0Histogram.GetBinContent(mud0CutBin)
       muSFErr = sqrt(pow(mud0Histogram.GetBinError(mud0CutUpper),2) + pow(mud0Histogram.GetBinError(mud0CutBin),2))
    else: 
       muSF = mud0Histogram.GetBinContent(mud0CutUpper) - mud0Histogram.GetBinContent(mud0CutBin)
       muSFErr = sqrt(pow(mud0Histogram.GetBinError(mud0CutUpper),2) + pow(mud0Histogram.GetBinError(mud0CutBin),2))
    
    eleNBins = eled0Histogram.GetNbinsX()
    eled0CutBin  = eled0Histogram.GetXaxis ().FindBin (float(d0cut))
    eled0CutUpper  = eled0Histogram.GetXaxis ().FindBin (float(d0UpperCut))
    if eled0Histogram.GetXaxis ().FindBin (float(d0cut)) > eled0Histogram.GetNbinsX ():
        eled0CutBin = eled0Histogram.GetNbinsX ()
    if eled0Histogram.GetXaxis ().FindBin (float(d0UpperCut)) > eled0Histogram.GetNbinsX ():
       eleSF = eled0Histogram.GetBinContent(eled0CutBin)
       eleSFErr = sqrt(pow(eled0Histogram.GetBinError(eled0CutBin),2))
    elif eled0Histogram.GetBinContent(eled0CutBin) == eled0Histogram.GetBinContent(eled0CutUpper):
       eleSF = eled0Histogram.GetBinContent(eled0CutBin)
       eleSFErr = sqrt(pow(eled0Histogram.GetBinError(eled0CutUpper),2) + pow(eled0Histogram.GetBinError(eled0CutBin),2))
    else: 
       eleSF = eled0Histogram.GetBinContent(eled0CutUpper) - eled0Histogram.GetBinContent(eled0CutBin)
       eleSFErr = sqrt(pow(eled0Histogram.GetBinError(eled0CutUpper),2) + pow(eled0Histogram.GetBinError(eled0CutBin),2))

    overalSF = muSF*eleSF
    overalSFErr = getMulError(muSF, eleSF, muSFErr, eleSFErr)

    nBinsX = d0Histogram.GetNbinsX()
    nBinsY = d0Histogram.GetNbinsY()

    normIntErr = Double (0.0)
    normIntegral = d0Histogram.IntegralAndError(0, nBinsX, 0, nBinsY, normIntErr)
    targetYield = normIntegral*overalSF
    targetYieldErr = getMulError(normIntegral, overalSF, normIntErr, overalSFErr)
            
    #yieldAndErrorList['yield'] = round(targetYield,4)
    yieldAndErrorList['yield'] = targetYield
    #yieldAndErrorList['error'] = round(targetYieldErr,4)
    yieldAndErrorList['error'] = targetYieldErr
    return yieldAndErrorList

########################################################################################
########################################################################################
def getSystematicError(sample):
    errorSquared = 0.0
    if types[sample] is "data":
        return 0.0

    # add uncertainty on normalization method
    if sample in background_normalization_uncertainties:
        input_error = background_normalization_uncertainties[sample]['value']
        if '/' in input_error:
            line = input_error.split('/')
            minus_error = float(line[0]) - 1
            plus_error = float(line[1]) - 1
            if abs(minus_error) > abs(plus_error):
                error = minus_error
            else:
                error = plus_error
        else:
            error = float(input_error) - 1
        errorSquared = errorSquared + error * error


    # add global uncertainties
    for uncertainty in global_systematic_uncertainties:
        if sample in global_systematic_uncertainties[uncertainty]['applyList']:
            error = float(global_systematic_uncertainties[uncertainty]['value']) -1
            errorSquared = errorSquared + error * error

    # add sample-specific uncertainties from text files
    for uncertainty in external_systematic_uncertainties:
        input_file_path = os.environ['CMSSW_BASE'] + "/src/" + external_systematics_directory + "systematic_values__" + uncertainty + ".txt"
        if not os.path.exists(input_file_path):
            print "WARNING: didn't find ",input_file_path
            print "   will skip this systematic for this channel"
            return 0
        input_file = open(input_file_path)
        for line in input_file:
            line = line.rstrip("n").split(" ")
            dataset = line[0]
            if dataset != sample:
                continue

            if line[1] != '0':
                if len(line) is 2: #just one error
                    error = float(line[1]) - 1
                elif len(line) is 3: #asymmetric +- errors (we'll take the bigger one)
                    minus_error = float(line[1]) - 1
                    plus_error = float(line[2]) - 1
                    if abs(minus_error) > abs(plus_error):
                        error = minus_error
                    else:
                        error = plus_error
                errorSquared = errorSquared + error * error


    return math.sqrt(errorSquared)

########################################################################################
########################################################################################

########################################################################################
########################################################################################



###setting up yields and errors
yields = {}
stat_errors = {}
sys_errors = {}


bgMCSum = {}
bgMCStatErrSquared = {}
bgMCSysErrSquared = {}


for d0cut in d0cuts_array:
    bgMCSum[d0cut] = 0
    bgMCStatErrSquared[d0cut] = 0
    bgMCSysErrSquared[d0cut] = 0


for dataset in datasets:
    yields[dataset] = {}
    stat_errors[dataset] = {}
    sys_errors[dataset] = {}

    for d0cut in d0cuts_array:

        yieldAndError = {}
        yieldAndError = GetYieldAndError(dataset,d0cut)

        # print yieldAndError
        if yieldAndError:

            # include systematic errors
            if arguments.includeSystematics:
                systematic_error = yieldAndError['yield']*getSystematicError(dataset)
            if types[dataset] is "bgMC":            
                bgMCSum[d0cut] = bgMCSum[d0cut] + yieldAndError['yield']
                bgMCStatErrSquared[d0cut] = bgMCStatErrSquared[d0cut] + yieldAndError['error'] * yieldAndError['error']
                if arguments.includeSystematics:
                    bgMCSysErrSquared[d0cut] = bgMCSysErrSquared[d0cut] + systematic_error * systematic_error

            if types[dataset] is "bgMC":
                yields[dataset][d0cut] = formatNumber(str(round_sigfigs(yieldAndError['yield'],4)).rstrip("0").rstrip("."))
            else: # this is the data
                yields[dataset][d0cut] = formatNumber(str(int(yieldAndError['yield'])))
            stat_errors[dataset][d0cut] = formatNumber(str(round_sigfigs(yieldAndError['error'],1)).rstrip("0").rstrip("."))
            if arguments.includeSystematics:
                sys_errors[dataset][d0cut] = formatNumber(str(round_sigfigs(systematic_error,1)).rstrip("0").rstrip("."))


#                print dataset,d0cut,bgMCSum[d0cut],"+-",bgMCErrSquared[d0cut],"^2"

#print yields







########################################################################################
########################################################################################

#printing the latex table of yields


# sorting d0 list by size of cut
d0cuts_list = []
for d0cut in d0cuts_array:
    d0cuts_list.append(d0cut)
d0cuts_list.sort(key=float)


hLine = "\\hline\n"
endLine = " \\\\ "
newLine = " \n"



outputFile = condor_dir + "/signalRegionYields_" + plainTextString(channel) + ".tex"
fout = open (outputFile, "w")
if(arguments.standAlone):
    fout.write ("\\documentclass[a2paper,24pt]{article}"+newLine)
    fout.write ("\\usepackage[landscape,margin=0.15cm]{geometry}"+newLine)
    fout.write ("\\begin{document}"+newLine)
    fout.write ("\\pagestyle{empty}"+newLine)

line = "\\begin{table}\\renewcommand{\\arraystretch}{1.2}\\begin{center}\\begin{tabular}{l"
for i in range(0,len(d0cuts_list)):
    line = line + "r"
line = line + "}"+newLine+hLine
fout.write (line)

line = "Event Source & "
for d0cut in d0cuts_list:
    line = line + "$\lvert d_{0} \\rvert > " + str(d0cut) + "$ cm & "
line = line.rstrip("& ")+endLine+newLine+hLine
fout.write(line)

#write a line for each background sample
bgMCcounter = 0
for dataset in datasets:

    if types[dataset] is not "bgMC":
        continue
    bgMCcounter = bgMCcounter + 1
    rawlabel = "$" + labels[dataset] + "$"
    label = rawlabel.replace("#","\\").replace("\\rightarrow","{\\rightarrow}").replace(" ","\\ ")

    line = label + " & "

    for d0cut in d0cuts_list:
        if yields[dataset][d0cut].find('$0$') is not -1:
            line = line + yields[dataset][d0cut] + " & "
        else:
            line = line + yields[dataset][d0cut] + " $\pm$ " + stat_errors[dataset][d0cut]
            if arguments.includeSystematics:
                line = line + " $\pm$ " + sys_errors[dataset][d0cut]
            line = line + " & "

    line = line.rstrip("& ") + endLine + newLine
    fout.write(line)


#write a line with the sum of the backgrounds
if bgMCcounter is not 0:
        line = hLine+"background sum & "

        for d0cut in d0cuts_list:

            bgMCSum_ = formatNumber(str(round_sigfigs(bgMCSum[d0cut],4)).rstrip("0").rstrip("."))
            bgMCStatErr_ = formatNumber(str(round_sigfigs(math.sqrt(bgMCStatErrSquared[d0cut]),1)).rstrip("0").rstrip("."))
            line = line + bgMCSum_ + " $\pm$ " + bgMCStatErr_
            if arguments.includeSystematics:
                bgMCSysErr_ = formatNumber(str(round_sigfigs(math.sqrt(bgMCSysErrSquared[d0cut]),1)).rstrip("0").rstrip("."))
                line = line + " $\pm$ " + bgMCSysErr_
            line = line + " & "

        line = line.rstrip("& ") + endLine + newLine + hLine
        fout.write(line)

for dataset in datasets:


    if types[dataset] is not "data" or not yields[dataset]:
        continue

    rawlabel = "$" + labels[dataset] + "$"
    label = rawlabel.replace("#","\\").replace("\\rightarrow","{\\rightarrow}").replace(" ","\\ ")

    line = label + " & "

    for d0cut in d0cuts_list:
        line = line + yields[dataset][d0cut] + " & "

    line = line.rstrip("& ") + endLine + newLine + hLine
    fout.write(line)


fout.write("\\end{tabular} \\end{center} \\end{table}"+newLine)
if(arguments.standAlone):
    fout.write("\\end{document}"+newLine)

fout.close()

if arguments.standAlone:
    #process tex files to make pdf files
    command = "pdflatex -interaction=batchmode -output-directory=./%s %s > /dev/null" % (condor_dir,outputFile)
    os.system(command)
    os.system(command)
    #os.system("rm %s" % outputFile)
    os.system("rm %saux" % (outputFile.rstrip("tex")))
    os.system("rm %slog" % (outputFile.rstrip("tex")))
    print "Finished writing cutFlow to " + outputFile + " and compiling pdf"
