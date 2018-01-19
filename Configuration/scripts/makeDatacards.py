#!/usr/bin/env python

import os
import sys
import math
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
                  help="include a channel with specified lepton impact parameter in same units as input hist (the syntax for multiple channels is '-d STRING1 -d STRING2' etc.)")
parser.add_option("-m", "--d0Max", dest="d0Max", default = 999999999.0,
                  help="specific a max d0 cut")

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


def subtractSignalRegions(yields, errors):
    for cutIndex in range(len(arguments.d0Cuts)-1): # -1 => don't include the most exclusive region
        currentD0Cut = arguments.d0Cuts[cutIndex]
        nextD0Cut = arguments.d0Cuts[cutIndex+1]
        currentError = yields[currentD0Cut] * (errors[currentD0Cut]-1)
        nextError = yields[nextD0Cut] * (errors[nextD0Cut]-1)

        yields[currentD0Cut] = yields[currentD0Cut] - yields[nextD0Cut]
        if yields[currentD0Cut] > 0.0:
            errors[currentD0Cut] = math.sqrt(currentError*currentError - nextError*nextError) / yields[currentD0Cut] + 1
        else:
            errors[currentD0Cut] = 0
    return (yields, errors)


def GetYieldAndError(condor_dir, process, channel, d0_cut):
    yield_and_error = {}
    inputFile = TFile("condor/"+condor_dir+"/"+process.replace('.','p')+".root")
    d0HistogramTry = inputFile.Get(channel+"/"+d0histogramName)
    if not d0HistogramTry:
        print "WARNING: input histogram not found"
        yield_and_error['yield'] = 0.0
        yield_and_error['error'] = 0.0
        return yield_and_error

    d0Histogram = d0HistogramTry.Clone()
    d0Histogram.SetDirectory(0)
    inputFile.Close()

    x_min = d0Histogram.GetXaxis().FindBin (float(d0_cut))
    y_min = d0Histogram.GetYaxis().FindBin (float(d0_cut))
    x_max = d0Histogram.GetXaxis().FindBin (float(arguments.d0Max))
    y_max = d0Histogram.GetYaxis().FindBin (float(arguments.d0Max))

    intError = Double (0.0)
    fracError = 0.0

    yield_ = d0Histogram.IntegralAndError(x_min, x_max, y_min, y_max, intError)
    if yield_ > 0.0:
        fracError = 1.0 + (intError / yield_)

    yield_and_error['yield'] = yield_
    yield_and_error['error'] = fracError

    return yield_and_error


def writeDatacard(mass,lifetime):

    signal_dataset = "stop"+mass+"_"+lifetime+"mm"

    signal_yield = {}
    signal_error = {}

    for d0Cut in arguments.d0Cuts:
        signalYieldAndError = GetYieldAndError(signal_condor_dir, signal_dataset, signal_channel, d0Cut)
        signal_yield[d0Cut] = signalYieldAndError['yield']
        signal_error[d0Cut] = signalYieldAndError['error']

    # subtract the contributions from the more exclusive signal region
    (signal_yield, signal_error) = subtractSignalRegions(signal_yield, signal_error)

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
        for bg in bg_names:
            bin_row_2.append('d0min_'+str(d0Cut))
            process_name_row.append(bg)
            process_index_row.append(str(process_index))
            process_index = process_index + 1
            rate_row.append(str(round(bg_yields[bg][d0Cut],4)))
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

            for bg in backgrounds:
                row.append('-')

        datacard_data.append(row)

    #add a row for the statistical error of each background
    for bg in bg_names:
        row = [bg+"_stat",'lnN','']
        for d0Cut in arguments.d0Cuts:
            row.append('-') # for the signal
            for process_name in bg_names:
                if bg is process_name:
                    row.append(str(round(bg_errors[process_name][d0Cut],3)))
                else:
                    row.append('-')
        datacard_data.append(row)


#    datacard_data.append(empty_row)
#    comment_row = empty_row[:]
#    comment_row[0] = "# NORMALIZATION UNCERTAINTIES #"
#    datacard_data.append(comment_row)
#    datacard_data.append(empty_row)
#
#    #add a row for the cross-section error for the signal
#    row = ['signal_cross_sec','lnN','']
#    for d0Cut in arguments.d0Cuts:
#        if energy == '13':
#            row.append(str(round(float(signal_cross_sections_13TeV[mass]['error']),3)))
#        elif energy == '8':
#            row.append(str(round(float(signal_cross_sections_8TeV[mass]['error']),3)))
#        else:
#            row.append(str(round(float(signal_cross_sections_13TeV[mass]['error']),3)))
#
#        for bg in backgrounds:
#            row.append('-')
#    datacard_data.append(row)

    #add a row for the normalization error for each background
    for process_name in sorted(background_normalization_uncertainties):
        row = [process_name+"_norm",background_normalization_uncertainties[process_name]['type'],'']
        for d0Cut in arguments.d0Cuts:
            row.append('-') # for the signal
            for bg in bg_names:
                if process_name is bg:
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
            for bg in bg_names:
                if bg in global_systematic_uncertainties[uncertainty]['applyList']:
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
            for bg in bg_names:
                if bg is unique_systematic_uncertainties[uncertainty]['dataset']:
                    row.append(unique_systematic_uncertainties[uncertainty]['value'])
                else:
                    row.append('-')
        datacard_data.append(row)


    #add a new row for each uncertainty defined in external text files
    for uncertainty in systematics_dictionary:
        row = [uncertainty,'lnN','']
        for d0Cut in arguments.d0Cuts:
            if signal_dataset in systematics_dictionary[uncertainty][d0Cut]:
                row.append(systematics_dictionary[uncertainty][d0Cut][signal_dataset])
            else:
                row.append('-')
            for bg in bg_names:
                if bg in systematics_dictionary[uncertainty][d0Cut]:
                    row.append(systematics_dictionary[uncertainty][d0Cut][bg])
                else:
                    row.append('-')
        datacard_data.append(row)



    #write all rows to the datacard
    datacard.write(fancyTable(datacard_data))
    datacard.write('\n')


########################################################################################
########################################################################################



###setting up background yields and statistical errors
bg_yields = {}
bg_errors = {}

bg_names = [bg['name'] for bg in backgrounds]

arguments.d0Cuts.sort(key=float)

for bg in backgrounds:
    bg_yields[bg['name']] = {}
    bg_errors[bg['name']] = {}

    for d0Cut in arguments.d0Cuts:
        yieldAndError = {}
        yieldAndError = GetYieldAndError(bg['condor_dir'], bg['name'], bg['channel'], d0Cut)
        bg_yields[bg['name']][d0Cut] = yieldAndError['yield']
        bg_errors[bg['name']][d0Cut] = yieldAndError['error']

    # subtract the contributions from the more exclusive signal region
    (bg_yields[bg['name']], bg_errors[bg['name']]) = subtractSignalRegions(bg_yields[bg['name']], bg_errors[bg['name']])

# if a background prediction is null, just set it equal to the previous region's yield
for cutIndex in range(len(arguments.d0Cuts)):
    currentD0Cut = arguments.d0Cuts[cutIndex]
    lastD0Cut = arguments.d0Cuts[max(0,cutIndex-1)]
    for bg in bg_names:
        if not bg_yields[bg][currentD0Cut] > 0.0:
            bg_yields[bg][currentD0Cut] = bg_yields[bg][lastD0Cut]
            bg_errors[bg][currentD0Cut] = bg_errors[bg][lastD0Cut]

###getting all the external systematic errors and putting them in a dictionary
systematics_dictionary = {}
for systematic in external_systematic_uncertainties:
    systematics_dictionary[systematic] =  {}
    for d0Cut in arguments.d0Cuts:
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

###setting up observed number of events
observation = {}

for d0Cut in arguments.d0Cuts:

    if run_blind_limits:
        background_sum = 0
        for bg in bg_names:
            background_sum = background_sum + round(float(bg_yields[bg][d0Cut]),1)
        observation[d0Cut] = background_sum
    else:
        observation[d0Cut] = GetYieldAndError(data_condor_dir, data_dataset, data_channel, d0Cut)['yield']

###looping over signal models and writing a datacard for each
for mass in masses:
  for lifetime in lifetimes:
        print "making datacard_stop"+mass+"_"+lifetime+"mm.txt"
        writeDatacard(mass,lifetime)
