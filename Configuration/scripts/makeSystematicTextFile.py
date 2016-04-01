#!/usr/bin/env python
import sys
import os
import re
import math
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

parser.add_option("-i", "--inputHistogram", dest="inputHistogram",
                  help="choose an input histogram and calculate the yield from its integral (histogram should be filled once per event)")

(arguments, args) = parser.parse_args()


if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + arguments.localConfig.split(".")[0] + " import *")
else:
    print "please specify config file"



from ROOT import TFile, TH1F, Double


def getYield(sample,condor_dir,channel):
    dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    if not arguments.inputHistogram:
        cutFlowHistogram = inputFile.Get(channel+"CutFlowPlotter/cutFlow")
        if not cutFlowHistogram:
            print "WARNING: didn't find cutflow for ", sample, "dataset in", channel, "channel"
            return 0.0
        yield_ = cutFlowHistogram.GetBinContent(cutFlowHistogram.GetNbinsX())

    else:
        newChannel = channel + "Plotter"
        inputHistogram = inputFile.Get(newChannel + "/" + arguments.inputHistogram)
        if not inputHistogram:
            print "WARNING: didn't find input histogram for ", sample, "dataset in", newChannel, "channel"
            return 0.0
        statError_ = Double(0.0)
        yield_ = inputHistogram.IntegralAndError(0, inputHistogram.GetNbinsX()+1, statError_)
        
    inputFile.Close()
    return yield_


outputFile = os.environ['CMSSW_BASE']+"/src/DisplacedSUSY/Configuration/data/systematic_values__" + systematic_name + ".txt"
fout = open (outputFile, "w")

for sample in datasets:
    
    minus_yield = getYield(sample,condor_dir,minus_channel)
    central_yield = getYield(sample,condor_dir,central_channel)
    plus_yield = getYield(sample,condor_dir,plus_channel)

    minus_factor = 1.0 + (minus_yield-central_yield)/central_yield if central_yield != 0 else 0.0
    plus_factor  = 1.0 + (plus_yield-central_yield)/central_yield if central_yield != 0 else 0.0

    minus_factor = str(round_sigfigs(minus_factor,5))
    plus_factor  = str(round_sigfigs(plus_factor,5))

    fout.write (sample+" "+minus_factor+" "+plus_factor+"\n")

fout.close()




