#run with a command like this:
#python BartschAndQuast_ForEtaHists.py -l options.py -w EMuPreselection_2016Analysis_Signal_27Aug2018
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
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *
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

#only look at positive eta
xhiValues = array ('f')
for i in range(30):
    xhiValues.append(i*.1)
xlo = 0.

bkgdEleInts = []
bkgdMuInts = []

allSignalEleInts = []
allSignalMuInts = []

signalDataset = []
histEle = "Electron Plots/electronEta"
histMu = "Muon Plots/muonEta"


for dataset in datasets:
    if dataset=="Background":
        for xhi in xhiValues:
            (eleInt, eleIntError) = getHistIntegral(dataset,condor_dir,"PreselectionPlotter",histEle,xlo,xhi)
            (muInt, muIntError) = getHistIntegral(dataset,condor_dir,"PreselectionPlotter",histMu,xlo,xhi)
            bkgdEleInts.append(eleInt)
            bkgdMuInts.append(muInt)
    else:
        signalDataset.append(dataset)
        signalEleInts = []
        signalMuInts = []
        for xhi in xhiValues:
            (eleInt, eleIntError) = getHistIntegral(dataset,condor_dir,"PreselectionPlotter",histEle,xlo,xhi)
            (muInt, muIntError) = getHistIntegral(dataset,condor_dir,"PreselectionPlotter",histMu,xlo,xhi)
            signalEleInts.append(eleInt)
            signalMuInts.append(muInt)
        allSignalEleInts.append(signalEleInts)
        allSignalMuInts.append(signalMuInts)
        #print "for " + dataset + ", " + "in " + condor_dir
        #print "    electron integral from " + str(xlo) + " um to  is: " + str("%.1f" % eleInt) + " +/- " + str("%.1f" % eleIntError)
        #print "    muon integral from " + str(xlo) + " um to 2000 um is: " + str("%.1f" % muInt) + " +/- " + str("%.1f" % muIntError)

HistEles = []
HistMus = []

color = [1,2,4,6]

for signal in range(len(allSignalEleInts)):
    BartschAndQuastEles = array('f', [])
    BartschAndQuastMus = array('f', [])

    for bkgdEleInt,signalEleInt in zip(bkgdEleInts,allSignalEleInts[signal]):
        BartschAndQuastEle = 1.0*signalEleInt/(sqrt(bkgdEleInt))
        BartschAndQuastEles.append(BartschAndQuastEle)
    for bkgdMuInt,signalMuInt in zip(bkgdMuInts,allSignalMuInts[signal]):
        BartschAndQuastMu = 1.0*signalMuInt/(sqrt(bkgdMuInt))
        BartschAndQuastMus.append(BartschAndQuastMu)

    HistEle = ROOT.TGraphAsymmErrors(len(xhiValues),xhiValues,BartschAndQuastEles)
    HistEle.SetTitle("")
    HistEle.SetMarkerStyle(20)
    HistEle.SetMarkerColor(color[signal])
    HistEle.SetLineColor(color[signal])
    HistEles.append(HistEle)

    maxYEle = max(BartschAndQuastEles)
    maxIndexEle = BartschAndQuastEles.index(maxYEle)
    print "The optimal electron eta is: "+str("%.3f" % xhiValues[maxIndexEle]) + " for "+ str(signalDataset[signal])

    HistMu = ROOT.TGraphAsymmErrors(len(xhiValues),xhiValues,BartschAndQuastMus)
    HistMu.SetTitle("")
    HistMu.SetMarkerStyle(20)
    HistMu.SetMarkerColor(color[signal])
    HistMu.SetLineColor(color[signal])
    HistMus.append(HistMu)

    maxYMu = max(BartschAndQuastMus)
    maxIndexMu = BartschAndQuastMus.index(maxYMu)
    print "The optimal muon eta is: "+str("%.3f" % xhiValues[maxIndexMu]) + " for "+ str(signalDataset[signal])
    print "-----------"

legEle = TLegend( 0.4, 0.70, 0.75, 0.85 )
legEle.SetBorderSize(0)
legEle.SetTextSize(0.04)
legEle.SetFillColor(0)

CanvasEle = TCanvas( "CanvasEle", "CanvasEle", 100, 100, 700, 600 )
FrameEle = CanvasEle.DrawFrame(xhiValues[0],0,xhiValues[29], 0.2)
FrameEle.GetXaxis().SetTitle("Maximum electron eta")
FrameEle.GetYaxis().SetTitle("S/(#sqrt{S+B})")
FrameEle.GetXaxis().SetTitleOffset(1.2)
FrameEle.GetYaxis().SetTitleOffset(1.2) #linear
CanvasEle.cd()
for signal in range(len(signalDataset)):
    legEle.AddEntry(HistEles[signal],str(signalDataset[signal])+"/sqrt("+str(signalDataset[signal])+"+Bkg)","p")
    HistEles[signal].Draw("PEL")
legEle.Draw()
CanvasEle.SaveAs("EtaOpt_BartschAndQuast_Ele_linear.pdf")


legMu = TLegend( 0.4, 0.70, 0.75, 0.85 )
legMu.SetBorderSize(0)
legMu.SetTextSize(0.04)
legMu.SetFillColor(0)
CanvasMu = TCanvas( "CanvasMu", "CanvasMu", 100, 100, 700, 600 )
FrameMu = CanvasMu.DrawFrame(xhiValues[0],0,xhiValues[29],0.2) #linear
FrameMu.GetXaxis().SetTitle("Maximum muon eta")
FrameMu.GetYaxis().SetTitle("S/(#sqrt{S+B})")
FrameMu.GetXaxis().SetTitleOffset(1.2)
FrameMu.GetYaxis().SetTitleOffset(1.2) #linear
CanvasMu.cd()
for signal in range(len(signalDataset)):
    legMu.AddEntry(HistMus[signal],str(signalDataset[signal])+"/sqrt("+str(signalDataset[signal])+"+Bkg)","p")
    HistMus[signal].Draw("PEL")
legMu.Draw()
CanvasMu.SaveAs("EtaOpt_BartschAndQuast_Mu_linear.pdf")
