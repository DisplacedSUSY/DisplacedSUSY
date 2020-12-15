#!/usr/bin/env python

# makes plots directly from trees
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

from ROOT import TFile, TCanvas, TH1F, TLegend

#set up some names
if analysisChannel == "mumu":
    Lep0 = "Leading muon |d_{0}|"
    Lep1 = "Subleading muon |d_{0}|"
    path = "muon0GreaterOrLessThan100um"
elif analysisChannel == "ee":
    Lep0 = "Leading electron |d_{0}|"
    Lep1 = "Subleading electron |d_{0}|"
    path = "electron0GreaterOrLessThan100um"
elif analysisChannel == "emu":
    Lep0 = "Leading electron |d_{0}|"
    Lep1 = "Leading muon |d_{0}|"
    path = "electron0GreaterOrLessThan100um"


#set up canvases and histograms
canvas = TCanvas("canvas","canvas",100,100,700,550)

hLep1AbsD0_Lep0GreaterThan100um = TH1F("hLep1AbsD0_Lep0GreaterThan100um","",100,0,200)
hLep1AbsD0_Lep0GreaterThan100um.SetTitle(";"+Lep1+" [#mum];Entries (Unit Area Norm.)")
hLep1AbsD0_Lep0GreaterThan100um.SetLineColor(1)
hLep1AbsD0_Lep0GreaterThan100um.SetLineWidth(3)
hLep1AbsD0_Lep0GreaterThan100um.SetStats(0)
hLep1AbsD0_Lep0LessThan100um = TH1F("hLep1AbsD0_Lep0LessThan100um","",100,0,200)
hLep1AbsD0_Lep0LessThan100um.SetTitle(";"+Lep1+" [#mum];Entries (Unit Area Norm.)")
hLep1AbsD0_Lep0LessThan100um.SetLineColor(2)
hLep1AbsD0_Lep0LessThan100um.SetLineWidth(3)
hLep1AbsD0_Lep0LessThan100um.SetStats(0)

#loop over datasets and trees, fill histograms
for sample in datasets:
    fileName = "condor/%s/mergeOutputHadd/%s.root" % (arguments.condorDir,sample)
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
        print "no Tree, exiting"
        sys.exit(1)
    tree = inputFile.Get("PreselectionTreeMaker/Tree")

    nEntries = 0
    for iEntry in tree:
        nEntries += 1
        if analysisChannel == "mumu":
            if iEntry.muon_beamspot_absD0Muon0 > 100.:
                hLep1AbsD0_Lep0GreaterThan100um.Fill(iEntry.muon_beamspot_absD0Muon1)
            else:
                hLep1AbsD0_Lep0LessThan100um.Fill(iEntry.muon_beamspot_absD0Muon1)
        elif analysisChannel == "ee":
            if iEntry.electron_beamspot_absD0Electron0 > 100.:
                hLep1AbsD0_Lep0GreaterThan100um.Fill(iEntry.electron_beamspot_absD0Electron1)
            else:
                hLep1AbsD0_Lep0LessThan100um.Fill(iEntry.electron_beamspot_absD0Electron1)
        elif analysisChannel == "emu":
            if iEntry.electron_beamspot_absD0Electron0 > 100.:
                hLep1AbsD0_Lep0GreaterThan100um.Fill(iEntry.muon_beamspot_absD0Muon0)
            else:
                hLep1AbsD0_Lep0LessThan100um.Fill(iEntry.muon_beamspot_absD0Muon0)

    inputFile.Close()

#normalize to unit area
if(hLep1AbsD0_Lep0GreaterThan100um.Integral() > 0):
    hLep1AbsD0_Lep0GreaterThan100um.Scale(1./hLep1AbsD0_Lep0GreaterThan100um.Integral())
if(hLep1AbsD0_Lep0LessThan100um.Integral() > 0):
    hLep1AbsD0_Lep0LessThan100um.Scale(1./hLep1AbsD0_Lep0LessThan100um.Integral())

Leg = TLegend(0.15,0.7,0.50,0.85)
Leg.AddEntry(hLep1AbsD0_Lep0GreaterThan100um,Lep0+" > 100#mum ","l")
Leg.AddEntry(hLep1AbsD0_Lep0LessThan100um,Lep0+" < 100#mum ","l")
Leg.SetBorderSize(0)

canvas.cd()
hLep1AbsD0_Lep0GreaterThan100um.Draw("")
hLep1AbsD0_Lep0LessThan100um.Draw("same")
Leg.Draw()
outputPath = "condor/%s/" % (arguments.condorDir)
canvas.SaveAs(outputPath + path + ".pdf")
canvas.SaveAs(outputPath + path + ".png")
