#!/usr/bin/env python

import time
import os
import sys
import math
import copy
import re
from array import *
from optparse import OptionParser
from operator import itemgetter

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *




parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-c", "--condorDir", dest="condorDir",
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


dataset_weights = {

    'WNjets' : 8.2,
    'Diboson' : 0.108,
    'SingleTop' : 0.88,
    'TTbar' : 0.042,
    'DY' : 0.773,

    }

from ROOT import TFile, gROOT, gStyle, gDirectory, TStyle, THStack, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TIter, TKey, TGraphErrors, Double


def GetYieldAndError(process,d0cut,factorize=True):

    integrateOutwardX = True
    integrateOutwardY = True
    #integrateOutwardX = False
    #integrateOutwardY = False

    inputFile = TFile(condor_dir+"/"+process+".root")
    HistogramObj = 0
    if process is "QCDFromData":
        HistogramObj = inputFile.Get("OSUAnalysis/"+qcdFromDataChannel+"/"+d0histogramName)
    elif types[process] is 'signalMC':
        HistogramObj = inputFile.Get("OSUAnalysis/"+signalChannel+"/"+d0histogramName)
    else:
        HistogramObj = inputFile.Get("OSUAnalysis/"+channel+"/"+d0histogramName)
    if not HistogramObj:
        print "WARNING:  Could not find histogram " + "OSUAnalysis/"+channel+"/"+d0histogramName + " in file " + process+".root" + ".  Will skip it and continue."
        return
    d0Histogram = HistogramObj.Clone()
    d0Histogram.SetDirectory(0)
    inputFile.Close()


    d0Histogram.SetDirectory(0)
    inputFile.Close()
    yieldAndErrorList = {}
    nBinsX = d0Histogram.GetNbinsX()
    nBinsY = d0Histogram.GetNbinsY()
    x0 = x1 = y0 = y1 = 0

    d0CutBinX = d0Histogram.GetXaxis ().FindBin (float(d0cut))
    d0CutBinY = d0Histogram.GetYaxis ().FindBin (float(d0cut))
    xValue = d0Histogram.GetXaxis().GetBinCenter(d0CutBinX)
    yValue = d0Histogram.GetYaxis().GetBinCenter(d0CutBinY)

    if ((xValue >= 0) == integrateOutwardX):
        x0 = d0CutBinX
        x1 = nBinsX + 1
    else:
        x0 = 0
        x1 = d0CutBinX
    if ((yValue >= 0) == integrateOutwardY):
        y0 = d0CutBinY
        y1 = nBinsY + 1
    else:
        y0 = 0
        y1 = d0CutBinY
    intError = Double (0.0)
    integral = 0.0

    if not factorize:
        integral = d0Histogram.IntegralAndError(x0,x1,y0,y1,intError)  
    else:
        totalError = Double (0.0)
        displacedXError = Double (0.0)
        displacedYError = Double (0.0)
        total = d0Histogram.IntegralAndError(0,nBinsX + 1,0,nBinsY + 1,totalError)
        displacedX = d0Histogram.IntegralAndError(x0,x1,0,nBinsY + 1,displacedXError)
        displacedY = d0Histogram.IntegralAndError(0,nBinsX + 1,y0,y1,displacedYError)

        yieldAndErrorList['total'] = total
        yieldAndErrorList['displacedX'] = displacedX
        yieldAndErrorList['displacedY'] = displacedY

        if process is "WNjets" or process is "Wjets":
            ttbarYields = {}
            ttbarYields = GetYieldAndError("TTbar",d0cut)
            if displacedX < 1.0e-12 and displacedY > 1.0e-12:
                displacedX = ttbarYields['displacedX']
                total = ttbarYields['total']
            if displacedY < 1.0e-12 and displacedX > 1.0e-12:
                displacedY = ttbarYields['displacedY']
                total = ttbarYields['total']

        integral = (displacedX * displacedY) / total
        intError = math.sqrt (displacedX * displacedX * displacedY * displacedY * totalError * totalError + total * total * displacedX * displacedX * displacedYError * displacedYError + total * total * displacedXError * displacedXError * displacedY * displacedY) / (total * total)

    #print channel + ", " + d0histogramName + ", " + process + ": " + str (integral)
            
    yieldAndErrorList['yield'] = integral
    yieldAndErrorList['error'] = intError
    return yieldAndErrorList

########################################################################################
########################################################################################

def getSystematicError(sample,channel):
    errorSquared = 0.0
    if types[sample] is "data":
        return 0.0
    if len(channel) is 0:
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

    # add sample-specific uncertainties
    for uncertainty in unique_systematic_uncertainties:
        if sample is unique_systematic_uncertainties[uncertainty]['dataset']:
            error = float(unique_systematic_uncertainties[uncertainty]['value']) -1
            errorSquared = errorSquared + error * error


    # add sample-specific uncertainties from text files
    for uncertainty in external_systematic_uncertainties:
        input_file_path = os.environ['CMSSW_BASE'] + "/src/" + external_systematics_directory + "/systematic_values__" + uncertainty + ".txt"
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

# sorting d0 list by size of cut
d0cuts_list = []
for d0cut in d0cuts_array:
    d0cuts_list.append(d0cut)
d0cuts_list.sort(key=float)



###setting up yields and errors
yields = {}
stat_errors = {}
sys_errors = {}
yields_strings = {}
stat_errors_strings = {}
sys_errors_strings = {}


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
    yields_strings[dataset] = {}
    stat_errors_strings[dataset] = {}
    sys_errors_strings[dataset] = {}

    for d0cut in d0cuts_array:
        
        yieldAndError = {}
        if dataset is 'QCDFromData' or types[dataset] is 'data' or types[dataset] is 'signalMC':
            yieldAndError = GetYieldAndError(dataset,d0cut,False)
        else:
            yieldAndError = GetYieldAndError(dataset,d0cut)

        if yieldAndError:

            yields[dataset][d0cut] = yieldAndError['yield']
            stat_errors[dataset][d0cut] = yieldAndError['error']

# subtract the contributions from the more exclusive signal region
for cutIndex in range(len(d0cuts_list)-1): # -1 => don't include the most exclusive region, since it doesn't need anything subtracted from it
    currentD0Cut = d0cuts_list[cutIndex]
    nextD0Cut = d0cuts_list[cutIndex+1]
    for dataset in datasets:
        currentError = stat_errors[dataset][currentD0Cut]
        nextError = stat_errors[dataset][nextD0Cut]
        yields[dataset][currentD0Cut] = yields[dataset][currentD0Cut] - yields[dataset][nextD0Cut]
        #print currentError,nextError
        #print currentError*currentError - nextError*nextError
        #if yields[dataset][currentD0Cut] > 0.0:
        #    stat_errors[dataset][currentD0Cut] = math.sqrt(currentError*currentError - nextError*nextError)
        #else:
        #    if dataset in dataset_weights:
        #        yields[dataset][currentD0Cut] = 0.69 * dataset_weights[dataset]
        #    else:
        #        stat_errors[dataset][currentD0Cut] = 0
        stat_errors[dataset][currentD0Cut] = math.sqrt(currentError*currentError - nextError*nextError)

#for dataset in datasets:
#    currentD0Cut = d0cuts_list[-1]
#    if not yields[dataset][currentD0Cut] > 0.0:
#        if dataset in dataset_weights:
#            yields[dataset][currentD0Cut] = 0.69 * dataset_weights[dataset]

for cutIndex in range(1,len(d0cuts_list)): # -1 => don't include the most exclusive region, since it doesn't need anything subtracted from it
    currentD0Cut = d0cuts_list[cutIndex]
    previousD0Cut = d0cuts_list[cutIndex-1]
    for dataset in datasets:
        if types[dataset] is "data":
            continue
        if yields[dataset][currentD0Cut] < 1.0e-12:
            yields[dataset][currentD0Cut] = copy.deepcopy (yields[dataset][previousD0Cut])
            stat_errors[dataset][currentD0Cut] = copy.deepcopy (stat_errors[dataset][previousD0Cut])

# format the numbers and turning them into strings

for dataset in datasets:

    for d0cut in d0cuts_array:
        
        # include systematic errors
        if arguments.includeSystematics:
            systematic_error = yields[dataset][d0cut]*getSystematicError(dataset,d0cut)
        if types[dataset] is "bgMC":
            bgMCSum[d0cut] = bgMCSum[d0cut] + yields[dataset][d0cut]
            bgMCStatErrSquared[d0cut] = bgMCStatErrSquared[d0cut] + stat_errors[dataset][d0cut] * stat_errors[dataset][d0cut]
            if arguments.includeSystematics:
                bgMCSysErrSquared[d0cut] = bgMCSysErrSquared[d0cut] + systematic_error * systematic_error

        if types[dataset] is not "data":
            yields_strings[dataset][d0cut] = formatNumber(str(round_sigfigs(yields[dataset][d0cut],2)).rstrip("0").rstrip("."))

        else: # this is the data
            yields_strings[dataset][d0cut] = formatNumber(str(int(yields[dataset][d0cut])))


        if arguments.includeSystematics:
            sys_errors_strings[dataset][d0cut] = formatNumber(str(round_sigfigs(systematic_error,1)).rstrip("0").rstrip("."))

        stat_errors_strings[dataset][d0cut] = formatNumber(str(round_sigfigs(stat_errors[dataset][d0cut],1)).rstrip("0").rstrip("."))


#print yields_strings
#print
#print stat_errors_strings
#print
#print sys_errors_strings


########################################################################################
########################################################################################

#printing the latex table of yields



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
        if yields_strings[dataset][d0cut].find('$0$') is not -1:
            line = line + yields_strings[dataset][d0cut] + " & "
        else:
            line = line + yields_strings[dataset][d0cut] + " $\pm$ " + stat_errors_strings[dataset][d0cut]
            if arguments.includeSystematics:
                line = line + " $\pm$ " + sys_errors_strings[dataset][d0cut]
            line = line + " & "

    line = line.rstrip("& ") + endLine + newLine
    fout.write(line)


#write a line with the sum of the backgrounds
if bgMCcounter is not 0:
        line = hLine+"background sum & "

        for d0cut in d0cuts_list:
    
            bgMCSum_ = formatNumber(str(round_sigfigs(bgMCSum[d0cut],2)).rstrip("0").rstrip("."))
            bgMCStatErr_ = formatNumber(str(round_sigfigs(math.sqrt(bgMCStatErrSquared[d0cut]),1)).rstrip("0").rstrip("."))
            line = line + bgMCSum_ + " $\pm$ " + bgMCStatErr_
            if arguments.includeSystematics:
                bgMCSysErr_ = formatNumber(str(round_sigfigs(math.sqrt(bgMCSysErrSquared[d0cut]),1)).rstrip("0").rstrip("."))
                line = line + " $\pm$ " + bgMCSysErr_
            line = line + " & "
                
        line = line.rstrip("& ") + endLine + newLine + hLine
        fout.write(line)

#write a line for each signalMC sample
signalCounter = 0
for dataset in datasets:

    if types[dataset] is not "signalMC" or not yields[dataset]:
        continue

    signalCounter = signalCounter + 1
        
    rawlabel = "$" + labels[dataset] + "$"
    label = rawlabel.replace("#","\\").replace("\\rightarrow","{\\rightarrow}").replace(" ","\\ ")

    line = label + " & "
    
    for d0cut in d0cuts_list:
        if yields_strings[dataset][d0cut].find('$0$') is not -1:
            line = line + yields_strings[dataset][d0cut] + " & "
        else:
            line = line + yields_strings[dataset][d0cut] + " $\pm$ " + stat_errors_strings[dataset][d0cut]
            if arguments.includeSystematics:
                line = line + " $\pm$ " + sys_errors_strings[dataset][d0cut]
            line = line + " & "

    line = line.rstrip("& ") + endLine + newLine
    fout.write(line)


if signalCounter > 0:
    line = endLine + newLine + hLine
    fout.write(line)

#write a line with the data
for dataset in datasets:

    if types[dataset] is not "data" or not yields[dataset]:
        continue

    rawlabel = "$" + labels[dataset] + "$"
    label = rawlabel.replace("#","\\").replace("\\rightarrow","{\\rightarrow}").replace(" ","\\ ")

    line = label + " & "
    
    for d0cut in d0cuts_list:
        line = line + yields_strings[dataset][d0cut] + " & "

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
