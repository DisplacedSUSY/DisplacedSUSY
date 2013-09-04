#!/usr/bin/env python

import time
import os
import sys
import math
import copy
from array import *
from optparse import OptionParser



integrateOutwardX = True
integrateOutwardY = True
#integrateOutwardX = False
#integrateOutwardY = False


parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-c", "--outputDir", dest="outputDir",
                  help="output directory")
parser.add_option("-d", "--d0Cut", dest="d0Cut",
                  help="lepton impact parameter requirement in cm")


(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + arguments.localConfig.rstrip('.py') + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

if arguments.outputDir:
    if not os.path.exists("limits/"+arguments.outputDir):
        os.system("mkdir limits/"+arguments.outputDir)
else:
    print "No output directory specified, shame on you"
    sys.exit(0)

if not arguments.d0Cut:
    print "No d0 cut specified, how could you?"
    sys.exit(0)

from ROOT import TFile, gROOT, gStyle, gDirectory, TStyle, THStack, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TIter, TKey, TGraphErrors, Double


def fancyTable(arrays):

    def areAllEqual(lst):
        return not lst or [lst[0]] * len(lst) == lst

    if not areAllEqual(map(len, arrays)):
        exit('Cannot print a table with unequal array lengths.')

    verticalMaxLengths = [max(value) for value in map(lambda * x:x, *[map(len, a) for a in arrays])]

    spacedLines = []

    for array in arrays:
        spacedLine = ''
        for i, field in enumerate(array):
            diff = verticalMaxLengths[i] - len(field)
            spacedLine += field + ' ' * diff + '\t'
        spacedLines.append(spacedLine)

    return '\n'.join(spacedLines)



def GetYieldAndError(condor_dir, process, channel):
    inputFile = TFile("condor/"+condor_dir+"/"+process+".root")
    d0Histogram = inputFile.Get("OSUAnalysis/"+channel+"/"+d0histogramName).Clone()
    d0Histogram.SetDirectory(0)
    inputFile.Close()
    yieldAndErrorList = {}
    nBinsX = d0Histogram.GetNbinsX()
    nBinsY = d0Histogram.GetNbinsY()
    x0 = x1 = y0 = y1 = 0

    d0CutBinX = d0Histogram.GetXaxis ().FindBin (float(arguments.d0Cut))
    d0CutBinY = d0Histogram.GetYaxis ().FindBin (float(arguments.d0Cut))
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
    integral = d0Histogram.IntegralAndError(x0,x1,y0,y1,intError)  
    fracError = 0.0
    if integral > 0.0:
        fracError = 1.0 + (intError / integral)

    #print channel + ", " + d0histogramName + ", " + process + ": " + str (integral) + " +- " + str (intError) + " (" + str (fracError) + ")"
            
    yieldAndErrorList['yield'] = integral
    yieldAndErrorList['error'] = fracError
    return yieldAndErrorList


def writeDatacard(mass,lifetime,branching_ratio):


    signal_dataset = "stop"+mass+"_"+lifetime+"mm_"+"br"+branching_ratio
    signalYieldAndError = GetYieldAndError(signal_condor_dir, signal_dataset, signal_channel)
    signal_yield = signalYieldAndError['yield']
    
    default_channel_name = "EMu"

    os.system("rm -f limits/"+arguments.outputDir+"/datacard_"+signal_dataset+".txt")
    datacard = open("limits/"+arguments.outputDir+"/datacard_"+signal_dataset+".txt", 'w')
    datacard.write('imax 1 number of channels\n')
    datacard.write('jmax '+ str(len(backgrounds)) + ' number of backgrounds\n')
    datacard.write('kmax * number of nuisance parameters\n')
    datacard.write('\n')

    #################
    bin_row = [ 'bin', ' ', ' ',default_channel_name]
    observation_row = [ 'observation', ' ', ' ', str(round(observation,0)) ]
    #################
    datacard.write('\n----------------------------------------\n')
    datacard.write(fancyTable([ bin_row, observation_row ]))
    datacard.write('\n----------------------------------------\n')

    bin_row_2 = [ 'bin', ' ', ' ' ]
    process_name_row  = [ 'process', ' ', ' ' ]
    process_index_row = [ 'process', ' ', ' ' ]
    rate_row = [ 'rate', ' ', ' ' ]
    datacard_data = [ bin_row_2, process_name_row, process_index_row, rate_row ]

    empty_row = ['','','']

    process_index = 0

    #add signal yield
    bin_row_2.append(default_channel_name)
    process_name_row.append(signal_dataset)
    process_index_row.append(str(process_index))
    process_index = process_index + 1
    rate_row.append(str(round(signal_yield,4)))
    empty_row.append('')

    #add background yields
    for background in backgrounds:
        bin_row_2.append(default_channel_name)
        process_name_row.append(background)
        process_index_row.append(str(process_index))
        process_index = process_index + 1
        rate_row.append(str(round(background_yields[background],4)))
        empty_row.append('')
        
    datacard_data.append(empty_row)

    #add a row for the cross-section error for the signal
    row = ['signal_cross_sec','lnN','',str(round(float(signal_cross_sections[mass]['error']),3))]
    for background in backgrounds:
        row.append('-')
    datacard_data.append(row)

    #add a row for the cross-section error for each background
    for process_name in background_cross_section_uncertainties:
        row = [process_name+"_xsec",background_cross_section_uncertainties[process_name]['type'],'','-']
        for background in backgrounds:
            if process_name is background:
                row.append(background_cross_section_uncertainties[process_name]['value'])
            else:
                row.append('-')
        datacard_data.append(row)

    datacard_data.append(empty_row)


    #add a row for the statistical normalization error for the signal
    signal_error = signalYieldAndError['error']
    signal_error_string = str(round(signal_error,3))
    row = ['signal_norm','lnN','',signal_error_string]
    for background in backgrounds:
        row.append('-')
    datacard_data.append(row)

    #add a row for the normalization error for each background
    for process_name in background_normalization_uncertainties:
        row = [process_name+"_norm",background_normalization_uncertainties[process_name]['type'],'','-']
        for background in backgrounds:
            if background is process_name:
                row.append(str(round(background_errors[process_name],3)))
            else:
                row.append('-')
        datacard_data.append(row)

    datacard_data.append(empty_row)

    
    #add a new row for each uncertainty specified in configuration file
    for uncertainty in systematic_uncertainties:
        row = [uncertainty,systematic_uncertainties[uncertainty]['type'],'']
        if 'signal' in systematic_uncertainties[uncertainty]['applyList']:
            row.append(systematic_uncertainties[uncertainty]['value'])
        else:
            row.append('-')
        for background in backgrounds:
            if background in systematic_uncertainties[uncertainty]['applyList']:
                row.append(systematic_uncertainties[uncertainty]['value'])
            else:
                row.append('-')
        datacard_data.append(row)

    #write all rows to the datacard
    datacard.write(fancyTable(datacard_data))
    datacard.write('\n')





########################################################################################
########################################################################################



###setting up background yields and errors
background_yields = {}
background_errors = {}

for background in backgrounds:

    yieldAndError = {}
    #only get the yield and error from the 2D d0 histogram if it's going to be used
    if background_normalization_values[background] is 'FromHistogram' or background_normalization_uncertainties[background]['value'] is 'FromHistogram':    
        yieldAndError = GetYieldAndError(background_sources[background]['condor_dir'], background, background_sources[background]['channel'])
        #print yieldAndError
        
    if background_normalization_values[background] is 'FromHistogram':
        background_yields[background] = yieldAndError['yield']
    else:
        background_yields[background] = float(background_normalization_values[background])

    if background_normalization_uncertainties[background]['value'] is 'FromHistogram':
        background_errors[background] = yieldAndError['error']
    else:
        background_errors[background] = float(background_normalization_uncertainties[background]['value'])
            

    #print background+" yield = "+str(background_yields[background])+" +- "+str(background_errors[background])+"%"

###setting up observed number of events
if run_blind_limits:
    background_sum = 0
    for background in backgrounds:
        background_sum = background_sum + round(float(background_yields[background]),1)
    observation = background_sum
else:
    observation = GetYield(data_condir_dir, dataset, data_channel)


###looping over signal models and writing a datacard for each
for mass in masses:
  for lifetime in lifetimes:
    for branching_ratio in branching_ratios:
        print "making datacard_stop"+mass+"_"+lifetime+"mm_"+"br"+branching_ratio+".txt"
        writeDatacard(mass,lifetime,branching_ratio)
