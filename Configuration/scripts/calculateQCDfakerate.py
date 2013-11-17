#!/usr/bin/env python
from array import *
import sys
import os
import math
import re
from optparse import OptionParser
from OSUT3Analysis.Configuration.configurationOptions import *

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    sys.exit("please specify local configuration file")
        
            
from ROOT import TFile, gROOT, gStyle, gDirectory, TH1F, TH2F, Double

def get_integrals_and_errors(condor_dir,channel,dataset,histogram,threshold,minimum,maximum):
    out = []
    inputFile = TFile("condor/"+condor_dir+"/"+dataset+".root")
    Histogram = inputFile.Get("OSUAnalysis/"+channel+"/"+histogram).Clone()
    Histogram.SetDirectory(0)
    inputFile.Close()

    thresholdBin = Histogram.FindBin (threshold)
    if Histogram.GetXaxis().GetBinLowEdge(thresholdBin) - threshold > 0.00001:
        print "WARNING: your threshold value ("+str(threshold)+") is not on a bin edge"
        print "the edge of its bin is " + str(Histogram.GetXaxis().GetBinLowEdge(thresholdBin))
    minimumBin = Histogram.FindBin (minimum)
    if Histogram.GetXaxis().GetBinLowEdge(minimumBin) - minimum > 0.00001:
        print "WARNING: your minimum value ("+str(minimum)+") is not on a bin edge"
        print "the edge of its bin is " + str(Histogram.GetXaxis().GetBinLowEdge(minimumBin))
    maximumBin = Histogram.FindBin (maximum)
    if Histogram.GetXaxis().GetBinLowEdge(maximumBin) - maximum > 0.00001:
        print "WARNING: your maximum value ("+str(maximum)+") is not on a bin edge"
        print "the edge of its bin is " + str(Histogram.GetXaxis().GetBinLowEdge(maximumBin))

    isolatedIntegral = Double(0)
    isolatedIntegralError = Double(0)
    isolatedIntegral = Histogram.IntegralAndError(0,thresholdBin,isolatedIntegralError)
    out.append(isolatedIntegral)
    out.append(isolatedIntegralError)

    nonIsolatedIntegral = Double(0)
    nonIsolatedIntegralError = Double(0)
    nonIsolatedIntegral = Histogram.IntegralAndError(minimumBin,maximumBin,nonIsolatedIntegralError)
    out.append(nonIsolatedIntegral)
    out.append(nonIsolatedIntegralError)

    return out

def get_integrals_and_errors_2D(condor_dir,channel,dataset,histogram,thresholdX,minimumX,maximumX,thresholdY,minimumY,maximumY):
    out = []
    inputFile = TFile("condor/"+condor_dir+"/"+dataset+".root")
    Histogram = inputFile.Get("OSUAnalysis/"+channel+"/"+histogram).Clone()
    Histogram.SetDirectory(0)
    inputFile.Close()

    thresholdBinX = Histogram.GetXaxis().FindBin (thresholdX)
    if Histogram.GetXaxis().GetBinLowEdge(thresholdBinX) - thresholdX > 0.00001:
        print "WARNING: your threshold X value ("+str(thresholdX)+") is not on a bin edge"
        print "the edge of its bin is " + str(Histogram.GetXaxis().GetBinLowEdge(thresholdBinX))
    minimumBinX = Histogram.GetXaxis().FindBin (minimumX)
    if Histogram.GetXaxis().GetBinLowEdge(minimumBinX) - minimumX > 0.00001:
        print "WARNING: your minimum X value ("+str(minimumX)+") is not on a bin edge"
        print "the edge of its bin is " + str(Histogram.GetXaxis().GetBinLowEdge(minimumBinX))
    maximumBinX = Histogram.GetXaxis().FindBin (maximumX)
    if Histogram.GetXaxis().GetBinLowEdge(maximumBinX) - maximumX > 0.00001:
        print "WARNING: your maximum X value ("+str(maximumX)+") is not on a bin edge"
        print "the edge of its bin is " + str(Histogram.GetXaxis().GetBinLowEdge(maximumBinX))

    thresholdBinY = Histogram.GetYaxis().FindBin (thresholdY)
    if Histogram.GetYaxis().GetBinLowEdge(thresholdBinY) - thresholdY > 0.00001:
        print "WARNING: your threshold Y value ("+str(thresholdY)+") is not on a bin edge"
        print "the edge of its bin is " + str(Histogram.GetYaxis().GetBinLowEdge(thresholdBinY))
    minimumBinY = Histogram.GetYaxis().FindBin (minimumY)
    if Histogram.GetYaxis().GetBinLowEdge(minimumBinY) - minimumY > 0.00001:
        print "WARNING: your minimum Y value ("+str(minimumY)+") is not on a bin edge"
        print "the edge of its bin is " + str(Histogram.GetYaxis().GetBinLowEdge(minimumBinY))
    maximumBinY = Histogram.GetYaxis().FindBin (maximumY)
    if Histogram.GetYaxis().GetBinLowEdge(maximumBinY) - maximumY > 0.00001:
        print "WARNING: your maximum Y value ("+str(maximumY)+") is not on a bin edge"
        print "the edge of its bin is " + str(Histogram.GetYaxis().GetBinLowEdge(maximumBinY))



    isolatedIntegral = Double(0)
    isolatedIntegralError = Double(0)
    isolatedIntegral = Histogram.IntegralAndError(0,thresholdBinX,0,thresholdBinX,isolatedIntegralError)
    out.append(isolatedIntegral)
    out.append(isolatedIntegralError)

    nonIsolatedIntegral = Double(0)
    nonIsolatedIntegralError = Double(0)
    nonIsolatedIntegral = Histogram.IntegralAndError(minimumBinX,maximumBinX,minimumBinY,maximumBinY,nonIsolatedIntegralError)
    out.append(nonIsolatedIntegral)
    out.append(nonIsolatedIntegralError)

    return out


def calculate_lepton_fakerate(values):
	out = []
        IsolatedIntegral = values[0]
        IsolatedIntegralError = values[1]
        NonIsolatedIntegral = values[2]
        NonIsolatedIntegralError = values[3]
        if not (IsolatedIntegral == 0 or NonIsolatedIntegral == 0):
        	Ratio = round(IsolatedIntegral/NonIsolatedIntegral,4)
                Error = round(math.sqrt((IsolatedIntegralError**2)/(IsolatedIntegral**2)+(NonIsolatedIntegralError**2)/(NonIsolatedIntegral**2)),4)
        	out.append(Ratio)
        	out.append(Error)
                return out
        elif IsolatedIntegral == 0:
		print "0 events found in isolated"
                out.append(0)
                out.append(0)
                return out
        elif NonIsolatedIntegral == 0:
		print "0 events found in non-isolated region"
                out.append(0)
                out.append(0)
                return out
        return out


def calculate_event_fakerate(electron_values,muon_values):
	out = []
        ElectronFakeRate = electron_values[0]
        ElectronFakeRateError = electron_values[1]
        MuonFakeRate = muon_values[0]
        MuonFakeRateError = muon_values[1]

        if not (ElectronFakeRate == 0 or MuonFakeRate == 0):
        	EventFakeRate = round(MuonFakeRate*ElectronFakeRate,4)
                Error = round(math.sqrt((ElectronFakeRateError**2)+(MuonFakeRateError**2)),4)
        	out.append(EventFakeRate)
        	out.append(Error)
                return out
        elif ElectronFakeRate == 0:
		print "electron fake-rate = 0"
                out.append(0)
                out.append(0)
                return out
        elif MuonFakeRate == 0:
		print "muon fake-rate = 0"
                out.append(0)
                out.append(0)
                return out
        return out



print
print "                        ","electron fake-rate","muon fake-rate","event fake-rate"
print "                        ","------------------","--------------","---------------"

electron_integrals = []
electron_fakerate = []
muon_integrals = []
muon_fakerate = []
event_fakerate = []



#calculate everything for the MC in analysis region
electron_integrals = get_integrals_and_errors(analysis_condor_dir,analysis_channel,analysis_dataset,electron_iso_histogram,electron_iso_threshold,electron_iso_minimum,electron_iso_maximum)
electron_fakerate = calculate_lepton_fakerate(electron_integrals)
muon_integrals = get_integrals_and_errors(analysis_condor_dir,analysis_channel,analysis_dataset,muon_iso_histogram,muon_iso_threshold,muon_iso_minimum,muon_iso_maximum)
muon_fakerate = calculate_lepton_fakerate(muon_integrals)
event_fakerate = calculate_event_fakerate(electron_fakerate,muon_fakerate)

print "MC in analysis region:  ",
print str(electron_fakerate[0])+" +- "+str(electron_fakerate[1]*100)+"%    ",
print str(muon_fakerate[0])+" +- "+str(muon_fakerate[1]*100)+"%  ",
print str(event_fakerate[0])+" +- "+str(event_fakerate[1]*100)+"%"

del electron_integrals[:]
del electron_fakerate[:]
del muon_integrals[:]
del muon_fakerate[:]
del event_fakerate[:]

#calculate everything for the MC in control region
electron_integrals = get_integrals_and_errors(control_electron_condor_dir,control_electron_channel,control_MC_electron_dataset,electron_iso_histogram,electron_iso_threshold,electron_iso_minimum,electron_iso_maximum)
electron_fakerate = calculate_lepton_fakerate(electron_integrals)
muon_integrals = get_integrals_and_errors(control_muon_condor_dir,control_muon_channel,control_MC_muon_dataset,muon_iso_histogram,muon_iso_threshold,muon_iso_minimum,muon_iso_maximum)
muon_fakerate = calculate_lepton_fakerate(muon_integrals)
event_fakerate = calculate_event_fakerate(electron_fakerate,muon_fakerate)

print "MC in control region:   ",
print str(electron_fakerate[0])+" +- "+str(electron_fakerate[1]*100)+"%    ",
print str(muon_fakerate[0])+" +- "+str(muon_fakerate[1]*100)+"%  ",
print str(event_fakerate[0])+" +- "+str(event_fakerate[1]*100)+"%"

del electron_integrals[:]
del electron_fakerate[:]
del muon_integrals[:]
del muon_fakerate[:]
del event_fakerate[:]

#calculate everything for the data in control region
electron_integrals = get_integrals_and_errors(control_electron_condor_dir,control_electron_channel,control_data_electron_dataset,electron_iso_histogram,electron_iso_threshold,electron_iso_minimum,electron_iso_maximum)
electron_fakerate = calculate_lepton_fakerate(electron_integrals)
muon_integrals = get_integrals_and_errors(control_muon_condor_dir,control_muon_channel,control_data_muon_dataset,muon_iso_histogram,muon_iso_threshold,muon_iso_minimum,muon_iso_maximum)
muon_fakerate = calculate_lepton_fakerate(muon_integrals)
event_fakerate = calculate_event_fakerate(electron_fakerate,muon_fakerate)

print "data in control region: ",
print str(electron_fakerate[0])+" +- "+str(electron_fakerate[1]*100)+"%    ",
print str(muon_fakerate[0])+" +- "+str(muon_fakerate[1]*100)+"%  ",
print str(event_fakerate[0])+" +- "+str(event_fakerate[1]*100)+"%"


twoD_integrals = get_integrals_and_errors_2D(analysis_condor_dir,analysis_channel,analysis_dataset,electron_muon_iso_histogram,muon_iso_threshold,muon_iso_minimum,muon_iso_maximum,electron_iso_threshold,electron_iso_minimum,electron_iso_maximum)
print "twoD_integrals", twoD_integrals
event_fakerate = calculate_lepton_fakerate(twoD_integrals)
print "MC by cut and count:                                           ",
print str(event_fakerate[0])+" +- "+str(event_fakerate[1]*100)+"%"


