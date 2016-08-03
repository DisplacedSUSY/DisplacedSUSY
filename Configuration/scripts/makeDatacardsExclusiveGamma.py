#!/usr/bin/env python

import time
import os
import sys
import math
from math import *
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
parser.add_option("-m", "--d0Max", dest="d0Max", default = 999.0,
                  help="specific a max d0 cut")

def getDivError(a,b,deltaa,deltab):
    return sqrt(pow(deltaa,2)/pow(b,2) + pow(deltab,2)*pow(a,2)/pow(b,4))
def getMulError(a,b,deltaa,deltab):
    return sqrt(pow(deltaa,2)*pow(b,2) + pow(deltab,2)*pow(a,2))

(arguments, args) = parser.parse_args()

d0Max = arguments.d0Max

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
    yieldAndErrorList = {}
    print process, d0Cut
    if process != "QCDFromData":
        inputFile = TFile("condor/"+condor_dir+"/"+process+".root")
        d0HistogramTry = inputFile.Get(channel+"/"+d0histogramName)
        if not d0HistogramTry:
            print "WARNING: input histogram not found"
            yieldAndErrorList['yield'] = 0.0
            yieldAndErrorList['error'] = 0.0
            return yieldAndErrorList
        d0Histogram = d0HistogramTry.Clone()
        d0Histogram.SetDirectory(0)
        inputFile.Close()

        nBinsX = d0Histogram.GetNbinsX()
        nBinsY = d0Histogram.GetNbinsY()

        d0CutBinX = d0Histogram.GetXaxis().FindBin (float(d0Cut))
        d0CutBinY = d0Histogram.GetYaxis().FindBin (float(d0Cut))
    
        d0CutMaxX = d0Histogram.GetXaxis().FindBin (float(arguments.d0Max))
        d0CutMaxY = d0Histogram.GetYaxis().FindBin (float(arguments.d0Max))
    
        intError = Double (0.0)
        fracError = 0.0
    
        if process.find("stop") is not -1 or types[process] is "data":
            yield_ = d0Histogram.IntegralAndError(d0CutBinX,d0CutMaxX - 1,d0CutBinY,d0CutMaxY - 1,intError)
            if yield_ > 0.0:
                fracError = 1.0 + (intError / yield_)
            yieldAndErrorList['yield'] = yield_
            yieldAndErrorList['error'] = fracError
        else:
            inputFile = TFile("condor/"+condor_dir+"/"+process+".root")
            effInputFile = TFile("condor/"+condor_dir+"/"+process+"_DxyEff.root")
            HistogramObj = inputFile.Get(channel+"/"+d0histogramName)
            MuHistogramObj = effInputFile.Get(mud0histogramName)
            EleHistogramObj = effInputFile.Get(eled0histogramName)
            if not HistogramObj:
                print "WARNING:  Could not find histogram " + channel+d0histogramName + " in file " + process+".root" + ".  Will skip it and continue."
                return
            if not MuHistogramObj:
                print "WARNING:  Could not find histogram " + mud0histogramName + " in file " + process+"_DxyEff.root" + ".  Will skip it and continue."
                return
            if not EleHistogramObj:
                print "WARNING:  Could not find histogram " + eled0histogramName + " in file " + process+"_DxyEff.root" + ".  Will skip it and continue."
                return
            d0Histogram = HistogramObj.Clone()
            d0Histogram.SetDirectory(0)
            mud0Histogram = MuHistogramObj.Clone()
            mud0Histogram.SetDirectory(0)
            eled0Histogram = EleHistogramObj.Clone()
            eled0Histogram.SetDirectory(0)
            inputFile.Close()
        
            yieldAndErrorList = {}
            
            muSF = 0
            eleSF = 0
            muSFErr = 0 
            eleSFErr = 0
            muNBins = mud0Histogram.GetNbinsX()
            mud0CutBin  = mud0Histogram.GetXaxis ().FindBin (float(d0Cut))
            mud0CutUpper = mud0Histogram.GetXaxis ().FindBin (float(d0Max))
            if mud0Histogram.GetXaxis ().FindBin (float(d0Cut)) >= mud0Histogram.GetNbinsX ():
                 mud0CutBin = mud0Histogram.GetNbinsX ()
            if mud0Histogram.GetXaxis ().FindBin (float(d0Max)) > mud0Histogram.GetNbinsX ():
                muSF = mud0Histogram.GetBinContent(mud0CutBin)
                muSFErr = sqrt(pow(mud0Histogram.GetBinError(mud0CutBin),2))
            elif mud0Histogram.GetBinContent(mud0CutBin) == mud0Histogram.GetBinContent(mud0CutUpper):
       	       	muSF = mud0Histogram.GetBinContent(mud0CutBin)
       		muSFErr = sqrt(pow(mud0Histogram.GetBinError(mud0CutUpper),2) + pow(mud0Histogram.GetBinError(mud0CutBin),2))
    	    else: 
       		muSF = mud0Histogram.GetBinContent(mud0CutUpper) - mud0Histogram.GetBinContent(mud0CutBin)
       		muSFErr = sqrt(pow(mud0Histogram.GetBinError(mud0CutUpper),2) + pow(mud0Histogram.GetBinError(mud0CutBin),2))
            
            eleNBins = eled0Histogram.GetNbinsX()
            eled0CutBin  = eled0Histogram.GetXaxis ().FindBin (float(d0Cut))
            eled0CutUpper  = eled0Histogram.GetXaxis ().FindBin (float(d0Max))
            if eled0Histogram.GetXaxis ().FindBin (float(d0Cut)) > eled0Histogram.GetNbinsX ():
                eled0CutBin = eled0Histogram.GetNbinsX ()
            if eled0Histogram.GetXaxis ().FindBin (float(d0Max)) > eled0Histogram.GetNbinsX ():
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
            normIntegral = d0Histogram.IntegralAndError(0, nBinsX + 1, 0, nBinsY + 1, normIntErr)  
            targetYield = normIntegral*overalSF
            targetYieldErr = getMulError(normIntegral, overalSF, normIntErr, overalSFErr)
            if targetYield:
                fracError = 1.0 + (targetYieldErr / targetYield)        
            yieldAndErrorList['yield'] = targetYield
            yieldAndErrorList['error'] = fracError
    else:
        if d0Cut == '0.02':
            yieldAndErrorList['yield'] = 0.3992
            yieldAndErrorList['error'] = 3.4832
        if d0Cut == '0.05':
            yieldAndErrorList['yield'] = 0.0588
            yieldAndErrorList['error'] = 0.5129
        if d0Cut == '0.1':
            yieldAndErrorList['yield'] = 0.0021
            yieldAndErrorList['error'] = 0.0186 
            #yieldAndErrorList['yield'] = round(targetYield,4)
            #yieldAndErrorList['error'] = round(fracError,4)
    
    return yieldAndErrorList


def writeDatacard(mass,lifetime):
    if '.' in lifetime:
        lifetime = lifetime.replace('.','p')
    signal_dataset = "stop"+mass+"_"+lifetime+"mm"
#    signal_dataset = "stopHadron"+mass+"_"+lifetime+"mm_"+"br"+branching_ratio

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

   
    signal_dataset = "stop"+mass+"_"+lifetime.replace('p','.')+"mm" 
    os.system("rm -f limits/"+arguments.outputDir+"/datacard_"+signal_dataset+".txt")
    datacard = open("limits/"+arguments.outputDir+"/datacard_"+signal_dataset+".txt", 'w')

    datacard.write('imax ' + str(len(arguments.d0Cuts)*2) + ' number of channels\n')
    datacard.write('jmax '+ str(len(backgrounds) + 1) + ' number of backgrounds\n')
    datacard.write('kmax * number of nuisance parameters\n')
    datacard.write('\n')

    #################
    bin_row = [ 'bin', ' ']
    observation_row = [ 'observation', ' ']
    for d0Cut in arguments.d0Cuts:
        bin_row.append('d0min_'+str(d0Cut))
        observation_row.append(str(round(observation[d0Cut],0)))
    ################# Hard coded to add control bins  #################
        bin_row.append('control_' + 'd0min_'+str(d0Cut))
        observation_row.append(str(1))
    ###################################################################
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
            rate_row.append(str(round(background_yields[background][d0Cut],8)))
            empty_row.append('')
            if background is 'QCDFromData':
                bin_row_2.append('control_' + 'd0min_'+str(d0Cut))
                process_name_row.append('QCDFromData')
                process_index_row.append(str(process_index))
                rate_row.append('0.2')
                empty_row.append('')
                bin_row_2.append('control_' + 'd0min_'+str(d0Cut))
                process_name_row.append('NonQCD')
                process_index_row.append(str(process_index + 1))
                rate_row.append('1.109')
                empty_row.append('')
                process_index = process_index + 2
            else:
                process_index = process_index + 1 
                
                 
 
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
                signal_error_string = str(round(signal_yield[d0Cut]/original_events,8))
                row.append(signal_error_string)
            else:
                row.append('-') # for signal in other region

            for background in backgrounds:
                if background == 'QCDFromData': 
                    row.append('-')
                    row.append('-')
                    row.append('-')
                else:
                    row.append('-')
      
        datacard_data.append(row)

    #add a row for the statistical error of each background in each region

    # first do the QCD, since it's a special case
    for background in backgrounds:
        if background is not 'QCDFromData':
            continue
        for d0Cut in arguments.d0Cuts:
            name = background+'_stat_' + 'd0min_' + str(d0Cut)
            type = 'lnU'
            row =  [name,type,'']
                
            for d0CutInner in arguments.d0Cuts:
                row.append('-') # for signal
                for process_name in backgrounds:
                    if background is process_name:
                        if d0Cut is d0CutInner:
                            if background_yields[process_name][d0Cut] > 0.0:
                                row.append(str(25))
                                row.append(str(25))
                                row.append('-')
                            else:
                                row.append("0")
                                row.append("0")
                                row.append("0")
                        else:   
                            row.append('-')
                            row.append('-')
                            row.append('-')
                    else:
                        row.append('-')
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
                    row.append(str(round(background_errors[process_name][d0Cut],8)))
                elif process_name is 'QCDFromData':
                    row.append('-')
                    row.append('-')
                    row.append('-')
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
        if energy == '13':
            row.append(str(round(float(signal_cross_sections_13TeV[mass]['error']),3)))
        elif energy == '8':
            row.append(str(round(float(signal_cross_sections_8TeV[mass]['error']),3)))
        else:
            row.append(str(round(float(signal_cross_sections_13TeV[mass]['error']),3)))

        for background in backgrounds:
            if background is 'QCDFromData':
                row.append('-')
            	row.append('-')
            	row.append('-')
            else:	
		row.append('-')
    datacard_data.append(row)

    #add a row for the normalization error for each background
    for process_name in sorted(background_normalization_uncertainties):
        row = [process_name+"_norm",background_normalization_uncertainties[process_name]['type'],'']
        for d0Cut in arguments.d0Cuts:
            row.append('-') # for the signal
            for background in backgrounds:
                if process_name is background:
                    if process_name != 'QCDFromData':
                        row.append(background_normalization_uncertainties[process_name]['value'])
                    else:
                        row.append(background_normalization_uncertainties[process_name][str(d0Cut)]['value'])
                        row.append('-')
                        row.append('-')
                elif background == 'QCDFromData':
                    row.append('-')
                    row.append('-')
                    row.append('-')
                else:    
                   row.append('-')
        datacard_data.append(row)

    row = ["NonQCD_norm",'lnN','']
    for d0Cut in arguments.d0Cuts:
        row.append('-') # for the signal
        for background in backgrounds:
            if background != 'QCDFromData':
                row.append('-')
            else:
                row.append('-')
                row.append('-')
                row.append('1.1049')
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
                elif background == 'QCDFromData':
                    row.append('-')
                    row.append('-')
                    row.append('-')
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
                    if background != 'QCDFromData':
                        row.append(unique_systematic_uncertainties[uncertainty]['value'])
                    else: 
                        row.append('-')
                        row.append('-')
                        row.append('-')
                else:
                    row.append('-')
        datacard_data.append(row)

    #add a new row for each uncertainty defined in external text files
    for uncertainty in systematics_dictionary:
        row = [uncertainty,'lnN','']
        for d0Cut in arguments.d0Cuts:
            if signal_dataset in systematics_dictionary[uncertainty][float(d0Cut)]:
                row.append(systematics_dictionary[uncertainty][float(d0Cut)][signal_dataset])
            else:
                row.append('-')
            for background in backgrounds:
                if background in systematics_dictionary[uncertainty][float(d0Cut)]:
                        row.append(systematics_dictionary[uncertainty][(float(d0Cut))][background])
                elif background == 'QCDFromData':
                    row.append('-')
                    row.append('-')
                    row.append('-')
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
        #if background is not "QCDFromData":
        #    continue
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
    for d0Cut in arguments.d0Cuts:
        systematics_dictionary[systematic][float(d0Cut)] = {}
        input_file = open(os.environ['CMSSW_BASE']+"/src/DisplacedSUSY/Configuration/data/systematic_values__" + systematic + ".txt")
        for line in input_file:
            line = line.rstrip("\n").split(" ")
            dataset = line[0]
            if len(line) is 2:
                systematics_dictionary[systematic][float(d0Cut)][dataset] = line[1]
            elif len(line) is 3:
                systematics_dictionary[systematic][float(d0Cut)][dataset]= line[1]+"/"+line[2]

            # turn off systematic when the central yield is zero
            if systematics_dictionary[systematic][float(d0Cut)][dataset] == '0' or systematics_dictionary[systematic][float(d0Cut)][dataset] == '0/0':
                systematics_dictionary[systematic][float(d0Cut)][dataset] = '-'
            
            
#print systematics_dictionary['pdf']['0.02']['stop300_7.0mm_br0']





###setting up observed number of events
observation = {}

for d0Cut in arguments.d0Cuts:

    if run_blind_limits:
        background_sum = 0
        for background in backgrounds:
            background_sum = background_sum + round(float(background_yields[background][d0Cut]),1)
        observation[d0Cut] = background_sum
    else:
        observation[d0Cut] = GetYieldAndError(data_condor_dir, data_dataset, data_channel, d0Cut)['yield']



###looping over signal models and writing a datacard for each
for mass in masses:
  for lifetime in lifetimes:
        print "making datacard_stop"+mass+"_"+lifetime+"mm.txt"
        writeDatacard(mass,lifetime)
