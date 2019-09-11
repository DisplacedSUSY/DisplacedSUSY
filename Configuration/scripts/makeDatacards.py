#!/usr/bin/env python

import os
import sys
import math
import re
import json
from array import *
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from DisplacedSUSY.Configuration.systematicsDefinitions import *
from OSUT3Analysis.Configuration.configurationOptions import *

from ROOT import TFile, gROOT, gStyle, gDirectory, TStyle, THStack, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TIter, TKey, TGraphErrors, Double

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDir", dest="condorDir",
                  help="condor working directory")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified"
    sys.exit(0)

if arguments.condorDir:
    if not os.path.exists("limits/"+arguments.condorDir):
        os.system("mkdir limits/"+arguments.condorDir)
else:
    print "No output directory specified"
    sys.exit(0)

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

def get_hist(hist_info):
    file_path = 'condor/{}/{}'.format(hist_info['dir'], hist_info['file'])
    try:
        f = TFile(file_path)
        h = f.Get(hist_info['hist']).Clone()
    except:
        print "Could not load", hist_info['hist'], "from", file_path
        sys.exit()

    h.SetDirectory(0)
    return h

# class to represent non-overlapping signal regions in d0-d0-pT space
class SignalRegion:
    def __init__(self, name, d0_max, d0_0_lo, d0_0_hi, d0_1_lo, d0_1_hi, pt_lo, pt_hi):
        self.name = name
        self.d0_0_lo = d0_0_lo
        self.d0_0_hi = d0_0_hi
        self.d0_1_lo = d0_1_lo
        self.d0_1_hi = d0_1_hi
        self.pt_lo   = pt_lo
        self.pt_hi   = pt_hi
        self.d0_max  = d0_max

    def get_yield_and_error(self, hist):
        d0_bin_max = hist.GetXaxis().FindBin(self.d0_max)-1
        x_bin_lo = hist.GetXaxis().FindBin(self.d0_0_lo)
        x_bin_hi = hist.GetXaxis().FindBin(self.d0_0_hi)-1
        y_bin_lo = hist.GetYaxis().FindBin(self.d0_0_lo)
        y_bin_hi = hist.GetYaxis().FindBin(self.d0_0_hi)-1
        z_bin_lo = hist.GetZaxis().FindBin(self.pt_lo)
        z_bin_hi = hist.GetZaxis().FindBin(self.pt_hi)-1

        # include pT overflow in integral if SR extends to edge of pT axis
        if z_bin_hi == hist.GetNbinsZ():
            z_bin_hi += 1

        # just integrate the rectangular prism if it's the outermost signal region
        if self.d0_0_hi == self.d0_1_hi == self.d0_max:
            x_bin_hi += 1 # include d0_0 overflow
            y_bin_hi += 1 # include d0_1 overflow
            error = Double()
            return (hist.IntegralAndError(x_bin_lo, x_bin_hi, y_bin_lo, y_bin_hi,
                                          z_bin_lo, z_bin_hi, error), error)

        # otherwise integrate L-shape region one leg at a time
        else:
            if d0_bin_max == hist.GetNbinsX():
                d0_bin_max += 1 # include overflow
            leg_0_err = Double()
            leg_1_err = Double()
            leg_0_yield = hist.IntegralAndError(x_bin_lo, d0_bin_max, y_bin_lo, y_bin_hi,
                                                z_bin_lo, z_bin_hi, leg_0_err)
            leg_1_yield = hist.IntegralAndError(x_bin_lo, x_bin_hi, y_bin_hi, d0_bin_max,
                                                z_bin_lo, z_bin_hi, leg_1_err)

            return propagateError("sum", leg_0_yield, leg_0_err, leg_1_yield, leg_1_err)


###################################################################################################

# get dict containing bg estimates and signal region definitions
with open('condor/{}/{}'.format(background['dir'], background['file'])) as bg_json:
    bg_estimates = json.load(bg_json)

backgrounds = bg_estimates.keys()
signal_regions = []
bg_yields = {}
bg_errors = {}

# put background estimate and signal region info into more useful form
for sample, regions in bg_estimates.iteritems():
    bg_yields[sample] = {}
    bg_errors[sample] = {}

    for sr in regions:
        sr_name = 'SR_{}um_{}um_{}GeV'.format(int(sr['d0_0'][0]),
                                              int(sr['d0_1'][0]), int(sr['pt'][0]))
        signal_regions.append(SignalRegion(sr_name, sr['d0_max'], sr['d0_0'][0], sr['d0_0'][1],
                                                                  sr['d0_1'][0], sr['d0_1'][1],
                                                                  sr['pt'][0], sr['pt'][1]))
        bg_yields[sample][sr_name] = sr['estimate']
        bg_errors[sample][sr_name] = sr['stat_err']

# set up observed number of events
observed_yields = {}
for sr in signal_regions:
    if blinded:
        observed_yields[sr.name] = sum([bg_yields[bg][sr.name] for bg in backgrounds])
    else:
        (observed_yields[sr.name], _) = sr.get_yield_and_error(get_hist(data))

# get all the external systematic errors and put them in a dictionary
# fixme: why not just write systematics in a python dictionary to start with?
systematics_dictionary = {}
for systematic in external_systematic_uncertainties:
    systematics_dictionary[systematic] = {}
    for sr in signal_regions:
        systematics_dictionary[systematic][sr.name] = {}
        input_file = open(os.environ['CMSSW_BASE'] +
                          "/src/DisplacedSUSY/Configuration/data/systematic_values__" +
                          systematic + ".txt")
        for line in input_file:
            line = line.rstrip("\n").split(" ")
            dataset = line[0]
            if len(line) is 2:
                systematics_dictionary[systematic][sr.name][dataset] = line[1]
            elif len(line) is 3:
                systematics_dictionary[systematic][sr.name][dataset]= line[1]+"/"+line[2]

            # turn off systematic when the central yield is zero
            if (systematics_dictionary[systematic][sr.name][dataset] == '0' or
                systematics_dictionary[systematic][sr.name][dataset] == '0/0'):
                systematics_dictionary[systematic][sr.name][dataset] = '-'

# write a datacard for each signal point
for signal['name'] in signal_points:
    # rename sub-mm samples to match sample names
    signal['name'] = signal['name'].replace('.', 'p')

    signal['file'] = signal['name'] + ".root"
    datacard_name = 'datacard_{}.txt'.format(signal['name'])
    print "making", datacard_name

    signal_yields = {}
    signal_errors = {}
    for sr in signal_regions:
        (signal_yield, signal_error) = sr.get_yield_and_error(get_hist(signal))
        signal_yields[sr.name] = signal_yield * lumi_factor # fixme: remove after adding signal from all years
        signal_errors[sr.name] = signal_error * math.sqrt(lumi_factor) # fixme: remove after adding signal from all years

    datacard_path = 'limits/{}/{}'.format(arguments.condorDir, datacard_name)
    datacard = open(datacard_path, 'w')

    datacard.write('imax ' + str(len(signal_regions)) + ' number of channels\n')
    datacard.write('jmax '+ str(len(backgrounds)) + ' number of backgrounds\n')
    datacard.write('kmax * number of nuisance parameters\n')
    datacard.write('\n')

    bin_row = [ 'bin', ' ']
    observation_row = [ 'observation', ' ']
    for sr in signal_regions:
        bin_row.append(sr.name)
        observation_row.append(str(round(observed_yields[sr.name], 0)))

    datacard.write('\n----------------------------------------\n')
    datacard.write(fancyTable([bin_row, observation_row]))
    datacard.write('\n----------------------------------------\n')

    bin_row_2 = [ 'bin', ' ', ' ' ]
    process_name_row  = [ 'process', ' ', ' ' ]
    process_index_row = [ 'process', ' ', ' ' ]
    rate_row = [ 'rate', ' ', ' ' ]
    datacard_data = [ bin_row_2, process_name_row, process_index_row, rate_row ]

    empty_row = ['','','']

    for sr in signal_regions:
        process_index = 0

        # add signal yield
        bin_row_2.append(sr.name)
        process_name_row.append(signal['name'])
        process_index_row.append(str(process_index))
        process_index += 1
        rate_row.append(str(round(signal_yields[sr.name], 4)))
        empty_row.append('')

        # add background yields
        for bg in backgrounds:
            bin_row_2.append(sr.name)
            process_name_row.append(bg)
            process_index_row.append(str(process_index))
            process_index += 1
            rate_row.append(str(round(bg_yields[bg][sr.name], 4)))
            empty_row.append('')

    datacard_data.append(empty_row)
    comment_row = empty_row[:]
    comment_row[0] = "# STATISTICAL UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)

    # add a row for the statistical uncertainty on the signal yield in each region
    for sr in signal_regions:
        name = 'signal_stat_' + sr.name
        row = [name, 'gmN']
        try:
            original_events = (signal_yields[sr.name] / signal_errors[sr.name])**2
            scale_factor = signal_yields[sr.name] / original_events
        except ZeroDivisionError:
            original_events = 0
            scale_factor = 0
        row.append(str(int(original_events)))

        # write uncertainty in column for appropriate region and '-' in all other columns
        for sr_test in signal_regions:
            if sr.name == sr_test.name:
                row.append(str(round(scale_factor, 7)))
            else:
                row.append('-')

            for bg in backgrounds:
                row.append('-')

        datacard_data.append(row)

    # add a row for the statistical uncertainty for each background
    for bg in backgrounds:
        row = [bg+"_stat",'lnN','']
        for sr in signal_regions:
            row.append('-') # for the signal
            for bg_test in backgrounds:
                if bg == bg_test:
                    row.append(str(round(bg_errors[bg][sr.name], 3)))
                else:
                    row.append('-')

        datacard_data.append(row)

    # add a row for the normalization error for each background
    for process_name in sorted(background_normalization_uncertainties):
        row = [process_name+"_norm",background_normalization_uncertainties[process_name]['type'],'']
        for sr in signal_regions:
            row.append('-') # for the signal
            for bg in backgrounds:
                if process_name == bg:
                    row.append(background_normalization_uncertainties[process_name]['value'])
                else:
                    row.append('-')
        datacard_data.append(row)

    datacard_data.append(empty_row)
    comment_row = empty_row[:]
    comment_row[0] = "# SYSTEMATIC UNCERTAINTIES #"
    datacard_data.append(comment_row)
    datacard_data.append(empty_row)

    # add a new row for each global uncertainty specified in configuration file
    for uncertainty in global_systematic_uncertainties:
        row = [uncertainty,'lnN','']
        for sr in signal_regions:
            if 'signal' in global_systematic_uncertainties[uncertainty]['applyList']:
                row.append(global_systematic_uncertainties[uncertainty]['value'])
            else:
                row.append('-')
            for bg in backgrounds:
                if bg in global_systematic_uncertainties[uncertainty]['applyList']:
                    row.append(global_systematic_uncertainties[uncertainty]['value'])
                else:
                    row.append('-')
        datacard_data.append(row)

    # add a new row for each uncertainty defined in external text files
    for uncertainty in systematics_dictionary:
        row = [uncertainty,'lnN','']
        for sr in signal_regions:
            if signal['name'] in systematics_dictionary[uncertainty][sr.name]:
                row.append(systematics_dictionary[uncertainty][sr.name][signal['name']])
            else:
                row.append('-')
            for bg in backgrounds:
                if bg in systematics_dictionary[uncertainty][sr.name]:
                    row.append(systematics_dictionary[uncertainty][sr.name][bg])
                else:
                    row.append('-')
        datacard_data.append(row)

    # write all rows to the datacard
    datacard.write(fancyTable(datacard_data))
    datacard.write('\n')
