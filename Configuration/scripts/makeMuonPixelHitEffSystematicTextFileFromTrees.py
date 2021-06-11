#!/usr/bin/env python
# computes the signal systematic on the muon pixel hit efficiency from the cosmic MC/NoBPTX efficiency plots and signal from the trees
# signal trees made from events that pass the Preselection

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
parser.add_option("-a", "--append", action="store_true", dest="append", default=False,
                  help="append to systematic text file instead of overwriting")

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


from ROOT import TFile, TCanvas, TH1F, TLegend, gROOT

gROOT.SetBatch()

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    year = "2016"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    year = "2017"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    year = "2018"
else:
    year = "2018"
    print "What CMSSW release are you in? We expect you to be in 80X or 94X or 102X"



def getMeanEfficiency(signalSample,condorDir,cosmicSample): #cosmicSample is cosmic MC or NoBPTX data
    fileName = "condor/%s/mergeOutputHadd/%s.root" % (condorDir,signalSample)
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
        print "no Tree, setting getMeanEfficiency to -1"
        return -1.
    tree = inputFile.Get("PreselectionTreeMaker/Tree")
    sumOfEffProduct = 0.
    sumOfWeights = 0.

    if cosmicSample == "MC":
        if year == "2016":
            eff = [
                0.682070669847,
                0.722389788117,
                0.745095636197,
                0.929132396871,
                0.977161149819,
                0.988029289664,
                0.977631687437,
                0.949902931374,
                0.847715599925,
                0.597362734829,
                0.0180688386968,
            ]
        elif year == "2017":
            eff = [
                0.817868253194,
                0.816094883865,
                0.839584351557,
                0.942103428524,
                0.984868459637,
                0.993818203692,
                0.990206174522,
                0.991043217126,
                0.980381330136,
                0.953046619656,
                0.407785191142,
            ]

        elif year == "2018":
            eff = [
                0.772595706798,
                0.73327521658,
                0.784521601897,
                0.9131607252,
                0.984594816139,
                0.995364501365,
                0.985351052296,
                0.987226295578,
                0.978794042909,
                0.95153597154,
                0.408356830726,
            ]
    elif cosmicSample == "data":
        if year == "2016":
            eff = [
                0.9,
                0.860759493671,
                0.864406779661,
                0.954545454545,
                1.0,
                1.0,
                0.923076923077,
                0.892857142857,
                0.880952380952,
                0.62962962963,
                0.0138888888889,
            ]
        elif year == "2017":
            eff = [
                0.714285714286,
                0.741258741259,
                0.80303030303,
                0.907692307692,
                0.934782608696,
                0.960784313725,
                0.961538461538,
                0.990384615385,
                0.944134078212,
                0.962864721485,
                0.371821305842,
            ]
        elif year == "2018":
            eff = [
                0.643776824034,
                0.714285714286,
                0.762376237624,
                0.907216494845,
                1.0,
                0.972972972973,
                0.974358974359,
                0.966101694915,
                0.952755905512,
                0.952054794521,
                0.42828685259,
            ]

    if analysisChannel == "mumu":
        var1 = "muon_beamspot_absD0Muon0"
        var2 = "muon_beamspot_absD0Muon1"
    elif analysisChannel == "emu":
        var1 = "muon_beamspot_absD0Muon0"
        var2 = "electron_beamspot_absD0Electron0"

    for iEntry in tree:
        d01 = getattr(iEntry,var1)
        d02 = getattr(iEntry,var2)
        #print "d01 is: " + str(d01) + " d02 is: " + str(d02)

        #get in inclusive signal region (leading leptons |d0| > 100 um) and get sum of product of efficiencies
        if d01> 100. and d02 > 100. and d01<100000.0 and d02<100000.0:
            if d01>100.0 and d01<5000.0:
                eff1 = eff[0]
            elif d01>5000.0 and d01<10000.0:
                eff1 = eff[1]
            elif d01>10000.0 and d01<15000.0:
                eff1 = eff[2]
            elif d01>15000.0 and d01<20000.0:
                eff1 = eff[3]
            elif d01>20000.0 and d01<25000.0:
                eff1 = eff[4]
            elif d01>25000.0 and d01<35000.0:
                eff1 = eff[5]
            elif d01>35000.0 and d01<45000.0:
                eff1 = eff[6]
            elif d01>45000.0 and d01<55000.0:
                eff1 = eff[7]
            elif d01>55000.0 and d01<75000.0:
                eff1 = eff[8]
            elif d01>75000.0 and d01<95000.0:
                eff1 = eff[9]
            elif d01>95000.0 and d01<100000.0:
                eff1 = eff[10]

            if d02>100.0 and d02<5000.0:
                eff2 = eff[0]
            elif d02>5000.0 and d02<10000.0:
                eff2 = eff[1]
            elif d02>10000.0 and d02<15000.0:
                eff2 = eff[2]
            elif d02>15000.0 and d02<20000.0:
                eff2 = eff[3]
            elif d02>20000.0 and d02<25000.0:
                eff2 = eff[4]
            elif d02>25000.0 and d02<35000.0:
                eff2 = eff[5]
            elif d02>35000.0 and d02<45000.0:
                eff2 = eff[6]
            elif d02>45000.0 and d02<55000.0:
                eff2 = eff[7]
            elif d02>55000.0 and d02<75000.0:
                eff2 = eff[8]
            elif d02>75000.0 and d02<95000.0:
                eff2 = eff[9]
            elif d02>95000.0 and d02<100000.0:
                eff2 = eff[10]

            if analysisChannel == "emu":
                eff2 = 1.0

            #print "eff1 is: " + str(eff1) + " eff2 is: " + str(eff2)
            sumOfEffProduct += 1.0*eff1*eff2
            sumOfWeights += 1.0

    inputFile.Close()
    #print "sumOfEffProduct is: " + str(sumOfEffProduct)
    #print "sumOfWeights is: " + str(sumOfWeights)
    #print "sumOfEffProduct/sumOfWeights is: " + str(1.0*sumOfEffProduct/sumOfWeights)
    if sumOfEffProduct == sumOfWeights == 0.:
        return 1.0
    else:
        return 1.0*sumOfEffProduct/sumOfWeights


base_name = "muonPixelHitEff"
if year == "2016":
    base_name += "16"
sys_name = "{}_{}_{}".format(base_name, analysisChannel, year)

outputFile = "{}/src/DisplacedSUSY/Configuration/data/systematic_values__{}.txt".format(os.environ['CMSSW_BASE'], sys_name)
open_mode = "a" if arguments.append else "w"
fout = open (outputFile, open_mode)
print "now starting muon pixel hit efficiency systematic for " + analysisChannel + " and " + year

lowest_fraction = 1.
highest_fraction = 0.
sum_fractions = 0.
num_signalSamples = 0

canvasVsLifetime = TCanvas("canvasVsLifetime","canvasVsLifetime",100,100,700,550)
canvasVsLifetime.SetGrid()

canvasVsMass = TCanvas("canvasVsMass","canvasVsMass",100,100,700,550)
canvasVsMass.SetGrid()

# histograms of the systematic vs lifetime, for 1000 GeV mass
hSystVsLifetime = TH1F("hSystVsLifetime","",5,0,5)
hSystVsLifetime.SetTitle(";Lifetime [mm];Syst uncert [%]")
hSystVsLifetime.SetMarkerColor(1)
hSystVsLifetime.SetMarkerStyle(20)
lifetimes = ["0.1","1","10","100","1000"]
SystsVsLifetime = []

# histograms of the systematic vs mass, for 1mm lifetime
hSystVsMass = TH1F("hSystVsMass","",3,0,3)
hSystVsMass.SetTitle(";Mass [GeV];Syst uncert [%]")
hSystVsMass.SetMarkerColor(2)
hSystVsMass.SetMarkerStyle(21)
masses = ["200", "1000", "1800"]
SystsVsMass = []

for signalSample in datasets:
    print "starting "+signalSample
    num_signalSamples += 1

    #find relative difference in mean efficiency, and write to a text file
    MC_efficiency = getMeanEfficiency(signalSample,arguments.condorDir,"MC") #cosmic MC
    data_efficiency = getMeanEfficiency(signalSample,arguments.condorDir,"data") #NoBPTX data

    if MC_efficiency == data_efficiency == -1.:
        factor = 0.01
        fraction = 0.99
    else:
        factor = 1.0*data_efficiency/MC_efficiency if MC_efficiency != 0 else 1.0
        fraction = factor - 1.0 if factor>1.0 else 1.0-factor
    #print "factor is: "+ str(factor)

    if MC_efficiency == 0:
        print "MC efficiency is 0 for " + str(signalSample)
    if MC_efficiency == 0:
        print "data efficiency is 0 for " + str(signalSample)

    factor = str(round_sigfigs(factor,5))

    fout.write (signalSample+" "+factor+" "+factor+"\n")

    sum_fractions += fraction

    if fraction < lowest_fraction:
        lowest_fraction = fraction
    if fraction > highest_fraction:
        highest_fraction = fraction

    if signalSample=="stopToLB1000_0p1mm" or signalSample=="stopToLB1000_1mm" or signalSample=="stopToLB1000_10mm" or signalSample=="stopToLB1000_100mm" or signalSample=="stopToLB1000_1000mm":
        SystsVsLifetime.append(100.*fraction)

    if signalSample=="stopToLB200_1mm" or signalSample=="stopToLB1000_1mm" or signalSample=="stopToLB1800_1mm":
        SystsVsMass.append(100.*fraction)

fout.close()

print "systematic uncertainty ranges from " + str(100.*lowest_fraction) + " to " + str(100.*highest_fraction) + "%"
print "average syst uncert is " + str(100.*sum_fractions/(num_signalSamples)) + "%"
print "######"

for b in range(0,hSystVsLifetime.GetNbinsX()):
    hSystVsLifetime.SetBinContent(b+1,SystsVsLifetime[b])
    hSystVsLifetime.GetXaxis().SetBinLabel(b+1,lifetimes[b])

for b in range(0,hSystVsMass.GetNbinsX()):
    hSystVsMass.SetBinContent(b+1,SystsVsMass[b])
    hSystVsMass.GetXaxis().SetBinLabel(b+1,masses[b])


hSystVsLifetime.GetYaxis().SetRangeUser(-0.001,2.*max(SystsVsLifetime))
hSystVsMass.GetYaxis().SetRangeUser(-0.001,2.*max(SystsVsMass))

LegLifetime = TLegend(0.15,0.7,0.50,0.85)
LegLifetime.AddEntry(hSystVsLifetime,"stop -> lb, 1000 GeV","p")

LegMass = TLegend(0.15,0.7,0.50,0.85)
LegMass.AddEntry(hSystVsMass,"stop -> lb, 1 mm","p")

output_path = "systs"+analysisChannel+year
if not os.path.exists(output_path):
    os.makedirs(output_path)

canvasVsLifetime.cd()
hSystVsLifetime.Draw("p")
LegLifetime.Draw()
canvasVsLifetime.SaveAs(output_path + "/" + sys_name + "VsLifetime.pdf")

canvasVsMass.cd()
hSystVsMass.Draw("p")
LegMass.Draw()
canvasVsMass.SaveAs(output_path + "/" + sys_name + "VsMass.pdf")
