#!/usr/bin/env python

# computes the signal systematics (pileup, lepton id and isolation, lepton d0 smearing) from the trees
# trees made from events that pass the Preselection

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
from OSUT3Analysis.Configuration.cutUtilities import *

### parse the command-line options

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")
parser.add_option("-s", "--systematicName", dest="systematicName",
                  help="the systematic uncertainty you want to calculate (pileup, electronIDandIso, muonIDandIso, electronD0Smearing, or muonD0Smearing)")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "you forgot to specify a config file with -l"
    sys.exit(1)

if not arguments.condorDir:
    print "you forgot to specify a condor directory with -w"
    sys.exit(1)
else:
    condirDir = arguments.condorDir

if not arguments.systematicName:
    print "you forgot to specify a systematic (pileup, electronIDandIso, muonIDandIso, electronD0Smearing, or muonD0Smearing) with -s"
    sys.exit(1)

from ROOT import TFile, TCanvas, TH1F, TLegend

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    year = "2016"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    year = "2017"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    year = "2018"
else:
    year = "2018"
    print "What CMSSW release are you in? We expect you to be in 80X or 94X or 102X"

#map systematic name to tree branch names (central, plus, minus variables)
if arguments.systematicName == "electronD0Smearing" or arguments.systematicName == "muonD0Smearing":
    central_variable = "central"
    minus_variable = "down"
    plus_variable = "up"

elif arguments.systematicName == "electronIDandIso":
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
        central_variable = "eventvariable_electronID2016Tight"
        minus_variable = "eventvariable_electronID2016TightDown"
        plus_variable = "eventvariable_electronID2016TightUp"
    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
        central_variable = "eventvariable_electronID2017Tight"
        minus_variable = "eventvariable_electronID2017TightDown"
        plus_variable = "eventvariable_electronID2017TightUp"
    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
        central_variable = "eventvariable_electronID2018Tight"
        minus_variable = "eventvariable_electronID2018TightDown"
        plus_variable = "eventvariable_electronID2018TightUp"
    else:
        print "What CMSSW release are you in? We expect you to be in 80X or 94X or 102X"

elif arguments.systematicName == "muonIDandIso":
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
        central_variable = "eventvariable_muonIso2016TightTightIDGH"
        minus_variable = "eventvariable_muonIso2016TightTightIDGHDown"
        plus_variable = "eventvariable_muonIso2016TightTightIDGHUp"
    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
        central_variable = "eventvariable_muonIso2017TightTightID"
        minus_variable = "eventvariable_muonIso2017TightTightIDDown"
        plus_variable = "eventvariable_muonIso2017TightTightIDUp"
    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
        central_variable = "eventvariable_muonIso2018TightTightID"
        minus_variable = "eventvariable_muonIso2018TightTightIDDown"
        plus_variable = "eventvariable_muonIso2018TightTightIDUp"
    else:
        print "What CMSSW release are you in? We expect you to be in 80X or 94X or 102X"

elif arguments.systematicName == "pileup":
    central_variable = "eventvariable_puScalingFactor"
    minus_variable = "eventvariable_puScalingFactorDown"
    plus_variable = "eventvariable_puScalingFactorUp"


#get sum of weights in inclusive signal region
if arguments.systematicName == "electronD0Smearing" or arguments.systematicName == "muonD0Smearing":
    def getSumOfWeights(sample,condorDir,smearingVar): #smearingVar is minus, central, or plus
        fileName = "condor/%s/mergeOutputHadd/%s.root" % (condorDir,sample)
        inputFile = TFile(fileName)
        if(inputFile.IsZombie()):
            print "input file is zombie"
            sys.exit(1)
        inputFile.cd()
        keys = []
        for key in inputFile.GetListOfKeys():
            keys.append(key.GetName())
            if (key.GetClassName() != "TDirectoryFile"):
                print "no TDirectoryFile"
                sys.exit(1)
        if not "PreselectionTreeMaker" in keys:
            print "no Tree, setting getSumOfWeights to -1"
            return -1.
        tree = inputFile.Get("PreselectionTreeMaker/Tree")
        sumOfWeights = 0.

        if smearingVar == "central":
            if analysisChannel == "mumu":
                var1 = "muon_beamspot_absD0Muon0"
                var2 = "muon_beamspot_absD0Muon1"
            elif analysisChannel == "ee":
                var1 = "electron_beamspot_absD0Electron0"
                var2 = "electron_beamspot_absD0Electron1"
            elif analysisChannel == "emu":
                var1 = "electron_beamspot_absD0Electron0"
                var2 = "muon_beamspot_absD0Muon0"

        #vary both muons and both electrons at the same time in the mumu and ee channels
        #vary electron and muon one at at time in the emu channel
        elif smearingVar == "up":
            if analysisChannel == "mumu":
                var1 = "muon_beamspot_absSmearedUpD0Muon0"
                var2 = "muon_beamspot_absSmearedUpD0Muon1"
            elif analysisChannel == "ee":
                var1 = "electron_beamspot_absSmearedUpD0Electron0"
                var2 = "electron_beamspot_absSmearedUpD0Electron1"
            elif analysisChannel == "emu":
                if arguments.systematicName == "electronD0Smearing":
                    var1 = "electron_beamspot_absSmearedUpD0Electron0"
                    var2 = "muon_beamspot_absD0Muon0"
                elif arguments.systematicName == "muonD0Smearing":
                    var1 = "electron_beamspot_absD0Electron0"
                    var2 = "muon_beamspot_absSmearedUpD0Muon0"

        elif smearingVar == "down":
            if analysisChannel == "mumu":
                var1 = "muon_beamspot_absSmearedDownD0Muon0"
                var2 = "muon_beamspot_absSmearedDownD0Muon1"
            elif analysisChannel == "ee":
                var1 = "electron_beamspot_absSmearedDownD0Electron0"
                var2 = "electron_beamspot_absSmearedDownD0Electron1"
            elif analysisChannel == "emu":
                if arguments.systematicName == "electronD0Smearing":
                    var1 = "electron_beamspot_absSmearedDownD0Electron0"
                    var2 = "muon_beamspot_absD0Muon0"
                elif arguments.systematicName == "muonD0Smearing":
                    var1 = "electron_beamspot_absD0Electron0"
                    var2 = "muon_beamspot_absSmearedDownD0Muon0"

        for iEntry in tree:
            #get in inclusive signal region (leading leptons |d0| > 100 um) and get sum of weights
            #print str(getattr(iEntry,var1)) + " " + str(getattr(iEntry,var2))
            if getattr(iEntry,var1)> 100. and getattr(iEntry,var2) > 100.:
                sumOfWeights += 1.

        inputFile.Close()
        return sumOfWeights

else:
    def getSumOfWeights(sample,condorDir,weights): #weights are minus, central, or plus
        fileName = "condor/%s/mergeOutputHadd/%s.root" % (condorDir,sample)
        inputFile = TFile(fileName)
        if(inputFile.IsZombie()):
            print "input file is zombie"
            sys.exit(1)
        inputFile.cd()
        keys = []
        for key in inputFile.GetListOfKeys():
            keys.append(key.GetName())
            if (key.GetClassName() != "TDirectoryFile"):
                print "no TDirectoryFile"
                sys.exit(1)
        if not "PreselectionTreeMaker" in keys:
            print "no Tree, setting getSumOfWeights to -1"
            return -1.
        tree = inputFile.Get("PreselectionTreeMaker/Tree")
        sumOfWeights = 0.

        for iEntry in tree:
            #get in inclusive signal region (leading leptons |d0| > 100 um) and get sum of weights
            if ((analysisChannel == "mumu" and iEntry.muon_beamspot_absD0Muon0 > 100. and iEntry.muon_beamspot_absD0Muon1 > 100.) or
                (analysisChannel == "ee" and iEntry.electron_beamspot_absD0Electron0 > 100. and iEntry.electron_beamspot_absD0Electron1 > 100.) or
                (analysisChannel == "emu" and iEntry.electron_beamspot_absD0Electron0 > 100. and iEntry.muon_beamspot_absD0Muon0 > 100.)):
                sumOfWeights += getattr(iEntry,weights)

        inputFile.Close()
        return sumOfWeights


outputFile = os.environ['CMSSW_BASE']+"/src/DisplacedSUSY/Configuration/data/systematic_values__" + arguments.systematicName + "_" + analysisChannel + "_" + year + ".txt"
fout = open (outputFile, "w")
print "now starting " + arguments.systematicName + " systematic for " + analysisChannel + " and " + year

lowest_fraction = 1.
highest_fraction = 0.
sum_fractions = 0.
num_samples = 0

canvasVsLifetime = TCanvas("canvasVsLifetime","canvasVsLifetime",100,100,700,550)
canvasVsLifetime.SetGrid()

canvasVsMass = TCanvas("canvasVsMass","canvasVsMass",100,100,700,550)
canvasVsMass.SetGrid()

# histograms of the systematic vs lifetime, for 1000 GeV mass
hPlusSystVsLifetime = TH1F("hPlusSystVsLifetime","",5,0,5)
hPlusSystVsLifetime.SetTitle(";Lifetime [mm];Syst uncert [%]")
hPlusSystVsLifetime.SetMarkerColor(1)
hPlusSystVsLifetime.SetMarkerStyle(20)
hMinusSystVsLifetime = TH1F("hMinusSystVsLifetime","",5,0,5)
hMinusSystVsLifetime.SetTitle(";Lifetime [mm];Syst uncert [%]")
hMinusSystVsLifetime.SetMarkerColor(2)
hMinusSystVsLifetime.SetMarkerStyle(21)
lifetimes = ["0.1","1","10","100","1000"]
plusSystsVsLifetime = []
minusSystsVsLifetime = []

# histograms of the systematic vs mass, for 1mm lifetime
hPlusSystVsMass = TH1F("hPlusSystVsMass","",3,0,3)
hPlusSystVsMass.SetTitle(";Mass [GeV];Syst uncert [%]")
hPlusSystVsMass.SetMarkerColor(4)
hPlusSystVsMass.SetMarkerStyle(22)
hMinusSystVsMass = TH1F("hMinusSystVsMass","",3,0,3)
hMinusSystVsMass.SetTitle(";Mass [GeV];Syst uncert [%]")
hMinusSystVsMass.SetMarkerColor(6)
hMinusSystVsMass.SetMarkerStyle(23)
masses = ["200", "1000", "1800"]
plusSystsVsMass = []
minusSystsVsMass = []

for sample in datasets:
    num_samples += 1

    #find relative difference in sum of weights, and write to a text file
    minus_yield = getSumOfWeights(sample,arguments.condorDir,minus_variable)
    central_yield = getSumOfWeights(sample,arguments.condorDir,central_variable)
    plus_yield = getSumOfWeights(sample,arguments.condorDir,plus_variable)

    if minus_yield == central_yield == plus_yield == -1.:
        minus_factor = 0.01
        plus_factor = 1.99
        minus_fraction = plus_fraction = 0.99
    else:
        minus_factor = 1.0 + (minus_yield-central_yield)/central_yield if central_yield != 0 else 1.0
        plus_factor  = 1.0 + (plus_yield-central_yield)/central_yield if central_yield != 0 else 1.0
        minus_fraction = abs(minus_yield-central_yield)/central_yield if central_yield != 0 else 0.
        plus_fraction = abs(plus_yield-central_yield)/central_yield if central_yield != 0 else 0.

    if central_yield == 0:
        print "central yield is 0 for " + str(sample)

    minus_factor = str(round_sigfigs(minus_factor,5))
    plus_factor  = str(round_sigfigs(plus_factor,5))

    fout.write (sample+" "+minus_factor+" "+plus_factor+"\n")

    sum_fractions += minus_fraction
    sum_fractions += plus_fraction

    if minus_fraction < lowest_fraction:
        lowest_fraction = minus_fraction
    if minus_fraction > highest_fraction:
        highest_fraction = minus_fraction
    if plus_fraction < lowest_fraction:
        lowest_fraction = plus_fraction
    if plus_fraction > highest_fraction:
        highest_fraction = plus_fraction

    if sample=="stopToLB1000_0p1mm" or sample=="stopToLB1000_1mm" or sample=="stopToLB1000_10mm" or sample=="stopToLB1000_100mm" or sample=="stopToLB1000_1000mm":
        plusSystsVsLifetime.append(100.*plus_fraction)
        minusSystsVsLifetime.append(100.*minus_fraction)

    if sample=="stopToLB200_1mm" or sample=="stopToLB1000_1mm" or sample=="stopToLB1800_1mm":
        plusSystsVsMass.append(100.*plus_fraction)
        minusSystsVsMass.append(100.*minus_fraction)

fout.close()

print "systematic uncertainty ranges from " + str(100.*lowest_fraction) + " to " + str(100.*highest_fraction) + "%"
print "average syst uncert is " + str(100.*sum_fractions/(2*num_samples)) + "%"
print "######"

for b in range(0,hPlusSystVsLifetime.GetNbinsX()):
    hPlusSystVsLifetime.SetBinContent(b+1,plusSystsVsLifetime[b])
    hPlusSystVsLifetime.GetXaxis().SetBinLabel(b+1,lifetimes[b])
    hMinusSystVsLifetime.SetBinContent(b+1,minusSystsVsLifetime[b])
    hMinusSystVsLifetime.GetXaxis().SetBinLabel(b+1,lifetimes[b])

for b in range(0,hPlusSystVsMass.GetNbinsX()):
    hPlusSystVsMass.SetBinContent(b+1,plusSystsVsMass[b])
    hPlusSystVsMass.GetXaxis().SetBinLabel(b+1,masses[b])
    hMinusSystVsMass.SetBinContent(b+1,minusSystsVsMass[b])
    hMinusSystVsMass.GetXaxis().SetBinLabel(b+1,masses[b])


hPlusSystVsLifetime.GetYaxis().SetRangeUser(-0.001,2.*max(plusSystsVsLifetime+minusSystsVsLifetime))
hMinusSystVsLifetime.GetYaxis().SetRangeUser(-0.001,2.*max(plusSystsVsLifetime+minusSystsVsLifetime))
hPlusSystVsMass.GetYaxis().SetRangeUser(-0.001,2.*max(plusSystsVsMass+minusSystsVsMass))
hMinusSystVsMass.GetYaxis().SetRangeUser(-0.001,2.*max(plusSystsVsMass+minusSystsVsMass))

LegLifetime = TLegend(0.15,0.7,0.50,0.85)
LegLifetime.AddEntry(hPlusSystVsLifetime,"plus syst, stop -> lb, 1000 GeV","p")
LegLifetime.AddEntry(hMinusSystVsLifetime,"minus syst, stop -> lb, 1000 GeV","p")

LegMass = TLegend(0.15,0.7,0.50,0.85)
LegMass.AddEntry(hPlusSystVsMass,"plus syst, stop -> lb, 1 mm","p")
LegMass.AddEntry(hMinusSystVsMass,"minus syst, stop -> lb, 1 mm","p")

output_path = "systs"+analysisChannel+year
if not os.path.exists(output_path):
    os.makedirs(output_path)

canvasVsLifetime.cd()
hPlusSystVsLifetime.Draw("p")
hMinusSystVsLifetime.Draw("psame")
LegLifetime.Draw()
canvasVsLifetime.SaveAs(output_path + "/" + arguments.systematicName + "_" + analysisChannel + "_" + year + "VsLifetime.pdf")

canvasVsMass.cd()
hPlusSystVsMass.Draw("p")
hMinusSystVsMass.Draw("psame")
LegMass.Draw()
canvasVsMass.SaveAs(output_path + "/" + arguments.systematicName + "_" + analysisChannel + "_" + year + "VsMass.pdf")
