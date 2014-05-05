#!/usr/bin/env python

import time
import os
import sys
import math
import copy
import re
from array import *
from optparse import OptionParser
from DisplacedSUSY.Configuration.systematicsDefinitions import *
from OSUT3Analysis.Configuration.configurationOptions import *




parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-c", "--outputDir", dest="outputDir",
                  help="output directory")
parser.add_option("-d", "--d0Cut", action="append", dest="d0Cuts",
                  help="include a channel with specified lepton impact parameter requirement in cm, (the syntax for multiple channels is '-d STRING1 -d STRING2' etc.)")


(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

if arguments.outputDir:
    if not os.path.exists("limits/"+arguments.outputDir):
        os.system("mkdir limits/"+arguments.outputDir)
else:
    print "No output directory specified, shame on you"
    sys.exit(0)

if not arguments.d0Cuts:
    print "No d0 cuts specified, how could you?"
    sys.exit(0)



    
integrateOutwardX = True
integrateOutwardY = True


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



def GetYieldAndError(condor_dir, process, channel, d0Cut):
    inputFile = TFile("condor/"+condor_dir+"/"+process+".root")
    print process, d0Cut

    d0Histogram = inputFile.Get("OSUAnalysis/"+channel+"/"+d0histogramName).Clone()
    d0Histogram.SetDirectory(0)
    inputFile.Close()
    yieldAndErrorList = {}
    nBinsX = d0Histogram.GetNbinsX()
    nBinsY = d0Histogram.GetNbinsY()
    x0 = x1 = y0 = y1 = 0

    d0CutBinX = d0Histogram.GetXaxis().FindBin (float(d0Cut))
    d0CutBinY = d0Histogram.GetYaxis().FindBin (float(d0Cut))
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
    fracError = 0.0

    # just do normal 2D d0 cuts
    if process.find("stop") is not -1 or types[process] is "data" or process is "QCDFromData":
        yield_ = d0Histogram.IntegralAndError(x0,x1,y0,y1,intError)
        if yield_ > 0.0:
            fracError = 1.0 + (intError / yield_)

    # do 2D factorized d0 cuts
    else:
        totalError =  Double (0.0)
        totalIntegral = d0Histogram.IntegralAndError(0,x1,0,y1,totalError)

        if process is "WNjets":
            ttbarFile = TFile("condor/"+condor_dir+"/"+"TTbar"+".root")
            ttbarHistogram = ttbarFile.Get("OSUAnalysis/"+channel+"/"+d0histogramName).Clone()
            ttbarHistogram.SetDirectory(0)
            inputFile.Close()
            xError = Double (0.0)
            xIntegral = ttbarHistogram.IntegralAndError(x0,x1,0,y1,xError)
            xEfficiency = xIntegral/ttbarHistogram.Integral(0,x1,0,y1)

        else:
            xError = Double (0.0)
            xIntegral = d0Histogram.IntegralAndError(x0,x1,0,y1,xError)
            xEfficiency = xIntegral/totalIntegral
        
        yError = Double (0.0)
        yIntegral = d0Histogram.IntegralAndError(0,x1,y0,y1,yError)
        yEfficiency = yIntegral/totalIntegral
        
        factorizedEfficiency = xEfficiency * yEfficiency
        yield_ = factorizedEfficiency * totalIntegral
        factorizedYieldError = Double (0.0)
        if xIntegral > 0.0 and yIntegral > 0.0 and  totalIntegral > 0.0:
            factorizedYieldError = (xError/xIntegral)*(xError/xIntegral)+(yError/yIntegral)*(yError/yIntegral)+(totalError/totalIntegral)*(totalError/totalIntegral)
            factorizedYieldError = math.sqrt(factorizedYieldError)
        fracError = 1.0 + factorizedYieldError

    yieldAndErrorList['yield'] = yield_
    yieldAndErrorList['error'] = fracError
    return yieldAndErrorList


def writeDatacard(mass,lifetime,branching_ratio):


#    signal_dataset = "stop"+mass+"_"+lifetime+"mm_"+"br"+branching_ratio
    signal_dataset = "stopHadron"+mass+"_"+lifetime+"mm_"+"br"+branching_ratio

    signal_yield = {}
    signal_error = {}    

    for d0Cut in arguments.d0Cuts:
        signalYieldAndError = GetYieldAndError(signal_condor_dir, signal_dataset, signal_channel, d0Cut)
        signal_yield[d0Cut] = signalYieldAndError['yield']
        signal_error[d0Cut] = signalYieldAndError['error']        

    # subtract the contributions from the more exclusive signal region - signal
    for cutIndex in range(len(arguments.d0Cuts)-1): # -1 => don't include the most exclusive region, since it doesn't need anything subtracted from it
        currentD0Cut = arguments.d0Cuts[cutIndex]
        nextD0Cut = arguments.d0Cuts[cutIndex+1]
        currentError = signal_yield[currentD0Cut] * (signal_error[currentD0Cut]-1)
        nextError = signal_yield[nextD0Cut] * (signal_error[nextD0Cut]-1)

        signal_yield[currentD0Cut] = signal_yield[currentD0Cut] - signal_yield[nextD0Cut]
        if signal_yield[currentD0Cut] > 0.0:
            signal_error[currentD0Cut] = math.sqrt(currentError*currentError - nextError*nextError) / signal_yield[currentD0Cut] + 1
        else:
            signal_error[currentD0Cut] = 0


    
    os.system("rm -f limits/"+arguments.outputDir+"/datacard_"+signal_dataset+".txt")
    datacard = open("limits/"+arguments.outputDir+"/datacard_"+signal_dataset+".txt", 'w')

    datacard.write('imax ' + str(len(arguments.d0Cuts)) + ' number of channels\n')
    datacard.write('jmax '+ str(len(backgrounds)) + ' number of backgrounds\n')
    datacard.write('kmax * number of nuisance parameters\n')
    datacard.write('\n')

    #################
    bin_row = [ 'bin', ' ']
    observation_row = [ 'observation', ' ']
    for d0Cut in arguments.d0Cuts:
        bin_row.append('d0min_'+str(d0Cut))
        observation_row.append(str(round(observation[d0Cut],0)))

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

    for d0Cut in arguments.d0Cuts:

        process_index = 0

        #add signal yield
        bin_row_2.append('d0min_'+str(d0Cut))
        process_name_row.append(signal_dataset)
        process_index_row.append(str(process_index))
        process_index = process_index + 1
        rate_row.append(str(round(signal_yield[d0Cut],4)))
        empty_row.append('')

        #add background yields
        for background in backgrounds:
            #print background
            bin_row_2.append('d0min_'+str(d0Cut))
            process_name_row.append(background)
            process_index_row.append(str(process_index))
            process_index = process_index + 1
            rate_row.append(str(round(background_yields[background][d0Cut],4)))
            empty_row.append('')
        
    datacard_data.append(empty_row)
    comment_row = empty_row[:]
    comment_row[0] = "# STATISTICAL UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)


    #add a row for the statistical errors of the signal in each region
    for d0Cut in arguments.d0Cuts:
        name = 'signal_stat_' + 'd0min_' + str(d0Cut)
        row = [name,'gmN']
        error = abs(signal_error[d0Cut]-1)
        original_events = 1.0/(error*error)
        row.append(str(int(original_events)))

        for d0CutInner in arguments.d0Cuts:
            if d0Cut is d0CutInner:
                signal_error_string = str(round(signal_yield[d0Cut]/original_events,7))
                row.append(signal_error_string)
            else:
                row.append('-') # for signal in other region

            for background in backgrounds:
                row.append('-')

        datacard_data.append(row)

    #add a row for the statistical error of each background in each region

    # first do the QCD, since it's a special case
    for background in backgrounds:
        if background is not 'QCDFromData':
            continue
        for d0Cut in arguments.d0Cuts:
            name = background+'_stat_' + 'd0min_' + str(d0Cut)
            type = 'gmN'
            row =  [name,type]
            if background_yields[background][d0Cut] > 0.0:
                error = abs(background_errors[background][d0Cut]-1)
                original_events = 1.0/(error*error)
                row.append(str(int(original_events)))
            else:
                row.append('0')
                
            for d0CutInner in arguments.d0Cuts:
                row.append('-') # for signal
                for process_name in backgrounds:
                    if background is process_name and d0Cut is d0CutInner:
                        if background_yields[process_name][d0Cut] > 0.0:
                            row.append(str(round(background_yields[process_name][d0Cut]/original_events,7)))
                        else:
                            row.append("0")
                            #row.append(str(dataset_weights[process_name]))
                    else:
                        row.append('-') # for signal in other region 

            datacard_data.append(row)



    #add a row for the statistical error of each background
    for background in backgrounds:
        if background is 'QCDFromData':
            continue
        row = [background+"_stat",'lnN','']
        for d0Cut in arguments.d0Cuts:
            row.append('-') # for the signal
            for process_name in backgrounds:
                if background is process_name:
                    row.append(str(round(background_errors[process_name][d0Cut],3)))
                else:
                    row.append('-')
        datacard_data.append(row)


    datacard_data.append(empty_row)
    comment_row = empty_row[:]
    comment_row[0] = "# NORMALIZATION UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)

    #add a row for the cross-section error for the signal
    row = ['signal_cross_sec','lnN','']
    for d0Cut in arguments.d0Cuts:
        row.append(str(round(float(signal_cross_sections[mass]['error']),3)))
        for background in backgrounds:
            row.append('-')
    datacard_data.append(row)

    #add a row for the normalization error for each background
    for process_name in sorted(background_normalization_uncertainties):
        row = [process_name+"_norm",background_normalization_uncertainties[process_name]['type'],'']
        for d0Cut in arguments.d0Cuts:
            row.append('-') # for the signal
            for background in backgrounds:
                if process_name is background:
                    row.append(background_normalization_uncertainties[process_name]['value'])
                else:
                    row.append('-')
        datacard_data.append(row)

    datacard_data.append(empty_row)
    comment_row = empty_row[:]
    comment_row[0] = "# SYSTEMATIC UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)


    
    #add a new row for each global uncertainty specified in configuration file
    for uncertainty in global_systematic_uncertainties:
        row = [uncertainty,'lnN','']
        for d0Cut in arguments.d0Cuts:        
            if 'signal' in global_systematic_uncertainties[uncertainty]['applyList']:
                row.append(global_systematic_uncertainties[uncertainty]['value'])
            else:
                row.append('-')
            for background in backgrounds:
                if background in global_systematic_uncertainties[uncertainty]['applyList']:
                    row.append(global_systematic_uncertainties[uncertainty]['value'])
                else:
                    row.append('-')
        datacard_data.append(row)


    #add a new row for each dataset-specific uncertainty specified in configuration file
    for uncertainty in unique_systematic_uncertainties:
        row = [uncertainty,'lnN','']
        for d0Cut in arguments.d0Cuts:        
            if 'signal' is unique_systematic_uncertainties[uncertainty]['dataset']:
                row.append(unique_systematic_uncertainties[uncertainty]['value'])
            else:
                row.append('-')
            for background in backgrounds:
                if background is unique_systematic_uncertainties[uncertainty]['dataset']:
                    row.append(unique_systematic_uncertainties[uncertainty]['value'])
                else:
                    row.append('-')
        datacard_data.append(row)


    #add a new row for each uncertainty defined in external text files
    for uncertainty in systematics_dictionary:
        row = [uncertainty,'lnN','']
        for d0Cut in arguments.d0Cuts:
            if signal_dataset in systematics_dictionary[uncertainty][float(float(d0Cut))]:
                row.append(systematics_dictionary[uncertainty][float(d0Cut)][signal_dataset])
            else:
                row.append('-')
            for background in backgrounds:
                if background in systematics_dictionary[uncertainty][float(d0Cut)]:
                    row.append(systematics_dictionary[uncertainty][(float(d0Cut))][background])
                else:
                    row.append('-')
        datacard_data.append(row)



    #write all rows to the datacard
    datacard.write(fancyTable(datacard_data))
    datacard.write('\n')





########################################################################################
########################################################################################



###setting up background yields and statistical errors
background_yields = {}
background_errors = {}

backgrounds.sort()
arguments.d0Cuts.sort()

for background in backgrounds:

    background_yields[background] = {}
    background_errors[background] = {}    

    for d0Cut in arguments.d0Cuts:

        yieldAndError = {}
        yieldAndError = GetYieldAndError(background_sources[background]['condor_dir'], background, background_sources[background]['channel'], d0Cut)
        #print background, d0Cut
        #print yieldAndError

        background_yields[background][d0Cut] = yieldAndError['yield']
        background_errors[background][d0Cut] = yieldAndError['error']



        #print "for d0 > "+d0Cut+":"
        #print background+" yield = "+str(background_yields[background][d0Cut])+" +- "+str(100*(background_errors[background][d0Cut]-1))+"%"


# subtract the contributions from the more exclusive signal region - backgrounds
for cutIndex in range(len(arguments.d0Cuts)-1): # -1 => don't include the most exclusive region, since it doesn't need anything subtracted from it
    currentD0Cut = arguments.d0Cuts[cutIndex]
    nextD0Cut = arguments.d0Cuts[cutIndex+1]
    for background in backgrounds:
        if background is not "QCDFromData":
            continue
        currentError = background_yields[background][currentD0Cut] * (background_errors[background][currentD0Cut]-1)
        nextError = background_yields[background][nextD0Cut] * (background_errors[background][nextD0Cut]-1)
        background_yields[background][currentD0Cut] = background_yields[background][currentD0Cut] - background_yields[background][nextD0Cut]
        if background_yields[background][currentD0Cut] > 0.0:
            background_errors[background][currentD0Cut] = math.sqrt(currentError*currentError - nextError*nextError) / background_yields[background][currentD0Cut] + 1
        else: 
            background_errors[background][currentD0Cut] = 0


# if a background prediction is null, just set it equal to the previous region's yield
for cutIndex in range(len(arguments.d0Cuts)):
    currentD0Cut = arguments.d0Cuts[cutIndex]
    lastD0Cut = arguments.d0Cuts[max(0,cutIndex-1)]
    for background in backgrounds:
        if not background_yields[background][currentD0Cut] > 0.0:
            background_yields[background][currentD0Cut] = background_yields[background][lastD0Cut]
            background_errors[background][currentD0Cut] = background_errors[background][lastD0Cut]

    


###getting all the external systematic errors and putting them in a dictionary
systematics_dictionary = {}
for systematic in external_systematic_uncertainties:
    systematics_dictionary[systematic] =  {}
    for d0Cut in d0cuts_array:
        systematics_dictionary[systematic][d0Cut] = {}
        input_file = open(os.environ['CMSSW_BASE']+"/src/DisplacedSUSY/Configuration/data/systematic_values__" + systematic + ".txt")
        for line in input_file:
            line = line.rstrip("\n").split(" ")
            dataset = line[0]
            if len(line) is 2:
                systematics_dictionary[systematic][d0Cut][dataset] = line[1]
            elif len(line) is 3:
                systematics_dictionary[systematic][d0Cut][dataset]= line[1]+"/"+line[2]

            # turn off systematic when the central yield is zero
            if systematics_dictionary[systematic][d0Cut][dataset] == '0' or systematics_dictionary[systematic][d0Cut][dataset] == '0/0':
                systematics_dictionary[systematic][d0Cut][dataset] = '-'
            
            
#print systematics_dictionary['pdf']['0.02']['stop300_7.0mm_br0']





###setting up observed number of events
observation = {}

for d0Cut in arguments.d0Cuts:

    if run_blind_limits:
        background_sum = 0
        for background in backgrounds:
            background_sum = background_sum + round(float(background_yields[background]),1)
        observation[d0Cut] = background_sum
    else:
        observation[d0Cut] = GetYieldAndError(data_condor_dir, data_dataset, data_channel, d0Cut)['yield']




###looping over signal models and writing a datacard for each
for mass in masses:
  for lifetime in lifetimes:
    for branching_ratio in branching_ratios:
        print "making datacard_stop"+mass+"_"+lifetime+"mm_"+"br"+branching_ratio+".txt"
        writeDatacard(mass,lifetime,branching_ratio)
