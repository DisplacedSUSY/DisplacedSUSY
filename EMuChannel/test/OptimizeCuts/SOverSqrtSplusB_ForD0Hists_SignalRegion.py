#run with a command like this:
#python SOverSqrtSplusB_ForD0Hists_SignalRegion.py -l options.py -w DisplacedLeptons2016/Preselection_D0CutOptimization
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

from DisplacedSUSY.Configuration.configurationOptions import *
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

xloValues = array ('f') #mm
for i in range(100):
    xloValues.append(20.*i) #2000 um
xhi = 2000 #um

bkgdEleInts = []
bkgdMuInts = []

allSignalEleInts = []
allSignalMuInts = []

signalDataset = []
histEle = "Electron Plots/electronAbsD0_2mm"
histMu = "Muon Plots/muonAbsD0_2mm"


for dataset in datasets:
    if dataset=="Background": 
        for xlo in xloValues:
            (eleInt, eleIntError) = getHistIntegral(dataset,condor_dir,"PreselectionPlotter",histEle,xlo,xhi)
            (muInt, muIntError) = getHistIntegral(dataset,condor_dir,"PreselectionPlotter",histMu,xlo,xhi)
            bkgdEleInts.append(eleInt)
            bkgdMuInts.append(muInt)
    else:
        signalDataset.append(dataset)
        signalEleInts = []
        signalMuInts = []
        for xlo in xloValues:
            (eleInt, eleIntError) = getHistIntegral(dataset,condor_dir,"PreselectionPlotter",histEle,xlo,xhi)
            (muInt, muIntError) = getHistIntegral(dataset,condor_dir,"PreselectionPlotter",histMu,xlo,xhi)
            signalEleInts.append(eleInt)
            signalMuInts.append(muInt)
        allSignalEleInts.append(signalEleInts)
        allSignalMuInts.append(signalMuInts)
        #print "for " + dataset + ", " + "in " + condor_dir 
        #print "    electron integral from " + str(xlo) + " um to 2000 um is: " + str("%.1f" % eleInt) + " +/- " + str("%.1f" % eleIntError)
        #print "    muon integral from " + str(xlo) + " um to 2000 um is: " + str("%.1f" % muInt) + " +/- " + str("%.1f" % muIntError)

HistEles = []
HistMus = []

color = [1,2,4,6]

for signal in range(len(allSignalEleInts)):
    SoverSqrtSplusBEles = array('f', [])
    SoverSqrtSplusBMus = array('f', [])

    for bkgdEleInt,signalEleInt in zip(bkgdEleInts,allSignalEleInts[signal]):    
        SoverSqrtSplusBEle = signalEleInt/sqrt(signalEleInt+bkgdEleInt)
        SoverSqrtSplusBEles.append(SoverSqrtSplusBEle)
    for bkgdMuInt,signalMuInt in zip(bkgdMuInts,allSignalMuInts[signal]):
        SoverSqrtSplusBMu = signalMuInt/sqrt(signalMuInt+bkgdMuInt)
        SoverSqrtSplusBMus.append(SoverSqrtSplusBMu)

    HistEle = ROOT.TGraphAsymmErrors(len(xloValues),xloValues,SoverSqrtSplusBEles)
    HistEle.SetTitle("")
    HistEle.SetMarkerStyle(20)
    HistEle.SetMarkerColor(color[signal])
    HistEle.SetLineColor(color[signal])
    HistEles.append(HistEle)

    maxYEle = max(SoverSqrtSplusBEles)
    maxIndexEle = SoverSqrtSplusBEles.index(maxYEle)
    print "The optimal electron |d0| is: "+str("%.3f" % xloValues[maxIndexEle]) + " um for "+ str(signalDataset[signal])

    HistMu = ROOT.TGraphAsymmErrors(len(xloValues),xloValues,SoverSqrtSplusBMus)
    HistMu.SetTitle("")
    HistMu.SetMarkerStyle(20)
    HistMu.SetMarkerColor(color[signal])
    HistMu.SetLineColor(color[signal])
    HistMus.append(HistMu)

    maxYMu = max(SoverSqrtSplusBMus)
    maxIndexMu = SoverSqrtSplusBMus.index(maxYMu)
    print "The optimal muon |d0| is: "+str("%.3f" % xloValues[maxIndexMu]) + " um for "+ str(signalDataset[signal])
    print "-----------"

legEle = TLegend( 0.4, 0.70, 0.75, 0.85 )
legEle.SetBorderSize(0)
legEle.SetTextSize(0.04)
legEle.SetFillColor(0)

CanvasEle = TCanvas( "CanvasEle", "CanvasEle", 100, 100, 700, 600 )
FrameEle = CanvasEle.DrawFrame(0,0,xloValues[99], 350)
FrameEle.GetXaxis().SetTitle("Minimum Electron |d_{0}| [#mum]")
FrameEle.GetYaxis().SetTitle("S/#sqrt{S+B}")
FrameEle.GetXaxis().SetTitleOffset(1.2)
FrameEle.GetYaxis().SetTitleOffset(1.2) #linear
CanvasEle.cd()
for signal in range(len(signalDataset)):
    legEle.AddEntry(HistEles[signal],str(signalDataset[signal])+"/sqrt(Bkg)","p")
    HistEles[signal].Draw("PEL")
legEle.Draw()
CanvasEle.SaveAs("SOverSqrtSplusB_Ele_linear.pdf")


legMu = TLegend( 0.4, 0.70, 0.75, 0.85 )
legMu.SetBorderSize(0)
legMu.SetTextSize(0.04)
legMu.SetFillColor(0)
CanvasMu = TCanvas( "CanvasMu", "CanvasMu", 100, 100, 700, 600 )
FrameMu = CanvasMu.DrawFrame(0,0,xloValues[99],350) #linear
FrameMu.GetXaxis().SetTitle("Minimum Muon |d_{0}| [#mum]")
FrameMu.GetYaxis().SetTitle("S/#sqrt{S+B}")
FrameMu.GetXaxis().SetTitleOffset(1.2)
FrameMu.GetYaxis().SetTitleOffset(1.2) #linear
CanvasMu.cd()
for signal in range(len(signalDataset)):
    legMu.AddEntry(HistMus[signal],str(signalDataset[signal])+"/sqrt(Bkg)","p")
    HistMus[signal].Draw("PEL")
legMu.Draw()
CanvasMu.SaveAs("SOverSqrtSplusB_Mu_linear.pdf")

