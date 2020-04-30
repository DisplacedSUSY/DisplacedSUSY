#run with a command like this:
#python SOverSqrtSPlusB_ForMuonIsoHists.py -l PreselectionOptions.py -w EMuPreselection_HeavyMesons_2018Analysis_27Apr2020
import time
import os
import sys
import math
import copy
import re
import ROOT
from math import *
from array import *
from optparse import OptionParser
from operator import itemgetter
#from ROOT import *

from OSUT3Analysis.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.miniAODV2_102X_Samples import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *
from OSUT3Analysis.Configuration.histogramUtilities import *

from ROOT import TFile, gROOT, gStyle, gDirectory, TStyle, THStack, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TIter, TKey, TPaveLabel
#sys.argv = []
gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetTextFont(42)
gROOT.ForceStyle()


parser = OptionParser()
parser = set_commandline_arguments(parser)
(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

if arguments.condorDir:
    condor_dir = arguments.condorDir
else:
    print "No condor output directory specified, shame on you"
    sys.exit(0)

xhiValues = array ('f')
for i in range(100):
    xhiValues.append(i*.05)
xlo = 0.

bkgdMuInts = []
allSignalMuInts = []

signalDataset = []
histMu = "Muon Plots/muonRhoBasedIsolation"


for dataset in datasets:
    #if dataset=="Background":
    if dataset=="TTJets_Lept":
        for xhi in xhiValues:
            (muInt, muIntError) = getHistIntegral(dataset,condor_dir,"PreselectionHeavyMesonsPlotter",histMu,xlo,xhi)
            bkgdMuInts.append(muInt)
            print str("%.1f" % muInt) + " +/- " + str("%.1f" % muIntError) + ", for xlo: "+str(xlo) + " and xhi: " + str(xhi)
        print "for " + dataset + ", " + "in " + condor_dir
        print "    muon integral from " + str(xlo) + " to 5 (in iso) is: " + str("%.1f" % muInt) + " +/- " + str("%.1f" % muIntError)

    else:
        signalDataset.append(dataset)
        signalMuInts = []
        for xhi in xhiValues:
            (muInt, muIntError) = getHistIntegral(dataset,condor_dir,"PreselectionHeavyMesonsPlotter",histMu,xlo,xhi)
            signalMuInts.append(muInt)
            print str("%.1f" % muInt) + " +/- " + str("%.1f" % muIntError) + ", for xlo: "+str(xlo) + " and xhi: " + str(xhi)
        allSignalMuInts.append(signalMuInts)
        print "for " + dataset + ", " + "in " + condor_dir
        print "    muon integral from " + str(xlo) + " to 5 (in iso) is: " + str("%.1f" % muInt) + " +/- " + str("%.1f" % muIntError)

HistMus = []

color = [1,2,4,6]

for signal in range(len(allSignalMuInts)):
    BartschAndQuastMus = array('f', [])

    for bkgdMuInt,signalMuInt in zip(bkgdMuInts,allSignalMuInts[signal]):
        BartschAndQuastMu = 1.*signalMuInt/(sqrt(signalMuInt+bkgdMuInt))
        BartschAndQuastMus.append(BartschAndQuastMu)

    HistMu = ROOT.TGraphAsymmErrors(len(xhiValues),xhiValues,BartschAndQuastMus)
    HistMu.SetTitle("")
    HistMu.SetMarkerStyle(20)
    HistMu.SetMarkerColor(color[signal])
    HistMu.SetLineColor(color[signal])
    HistMus.append(HistMu)

    maxYMu = max(BartschAndQuastMus)
    maxIndexMu = BartschAndQuastMus.index(maxYMu)
    print "The optimal muon isolation is: "+str("%.3f" % xhiValues[maxIndexMu]) + " for "+ str(signalDataset[signal])
    print "-----------"

legMu = TLegend( 0.4, 0.70, 0.75, 0.85 )
legMu.SetBorderSize(0)
legMu.SetTextSize(0.04)
legMu.SetFillColor(0)
CanvasMu = TCanvas( "CanvasMu", "CanvasMu", 100, 100, 700, 600 )
FrameMu = CanvasMu.DrawFrame(0,0,xhiValues[99],200) #linear
FrameMu.GetXaxis().SetTitle("Maximum muon isolation")
FrameMu.GetYaxis().SetTitle("S/#sqrt{B}")
FrameMu.GetXaxis().SetTitleOffset(1.2)
FrameMu.GetYaxis().SetTitleOffset(1.2) #linear
CanvasMu.cd()
for signal in range(len(signalDataset)):
    legMu.AddEntry(HistMus[signal],"S/sqrt(S+B)","p")
    HistMus[signal].Draw("PEL")
legMu.Draw()
CanvasMu.SaveAs("SOverSqrtB_MuIso_linear.pdf")
