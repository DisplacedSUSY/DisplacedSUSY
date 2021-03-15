#!/usr/bin/env python

# data trees made from events that pass the Preselection

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
#parser = set_commandline_arguments(parser)
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
else:
    condirDir = arguments.condorDir


from ROOT import gROOT, gStyle, TFile, TCanvas, TH2F, TH1F, TPaveLabel

gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetCanvasDefH(600)
gStyle.SetCanvasDefW(600)
gStyle.SetCanvasDefX(0)
gStyle.SetCanvasDefY(0)
gStyle.SetPadTopMargin(0.15)
gStyle.SetPadBottomMargin(0.15)
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadRightMargin(0.15)
gStyle.SetTitleColor(1, "XYZ")
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.05, "XYZ")
gStyle.SetTitleXSize(0.04)
gStyle.SetTitleXOffset(1.25)
gStyle.SetTitleYSize(0.04)
gStyle.SetTitleYOffset(1.5)
gStyle.SetTextAlign(12)
gStyle.SetLabelColor(1, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelOffset(0.005, "XYZ")
gStyle.SetLabelSize(0.04, "XYZ")
gStyle.SetAxisColor(1, "XYZ")
gStyle.SetStripDecimals(True)
gStyle.SetTickLength(0.03, "XYZ")
gStyle.SetNdivisions(505, "XYZ")
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gROOT.ForceStyle()

#bestest place for lumi. label, in top left corner
topLeft_x_left    = 0.15
y_bottom  = 0.85
topLeft_x_right   = 0.50
y_top     = 0.9

#position for header
header_x_left    = 0.55
header_x_right   = 0.91


LumiInFb = intLumi/1000.
#LumiText = str.format('{0:.1f}', LumiInFb) + " fb^{-1}"
LumiText = "{:d} fb^{{-1}}".format(int(round(LumiInFb)))
HeaderText = LumiText + " (13 TeV)"

HeaderLabel = TPaveLabel(header_x_left,y_bottom,header_x_right,y_top,HeaderText,"NDC")
HeaderLabel.SetTextAlign(32)
HeaderLabel.SetTextFont(42)
HeaderLabel.SetTextSize(0.697674)
HeaderLabel.SetBorderSize(0)
HeaderLabel.SetFillColor(0)
HeaderLabel.SetFillStyle(0)

LumiPrelimLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS Preliminary","NDC")
LumiPrelimLabel.SetTextFont(62)
LumiPrelimLabel.SetTextSize(0.8)
LumiPrelimLabel.SetTextAlign(12)
LumiPrelimLabel.SetBorderSize(0)
LumiPrelimLabel.SetFillColor(0)
LumiPrelimLabel.SetFillStyle(0)

if analysisChannel == "mumu":
    #var1 = "eventvariable_run"
    #var1 = "muon_phiMuon0"
    #var2 = "muon_phiMuon1"
    #xTitle = "Leading muon #phi"
    #yTitle = "Subleading muon #phi"

    #var1 = "muon_etaMuon0"
    #var2 = "muon_etaMuon1"
    #xTitle = "Leading muon #eta"
    #yTitle = "Subleading muon #eta"

    #var1 = "muon_layerOfFirstValidPixelHitMuon0"
    #var2 = "muon_layerOfFirstValidPixelHitMuon1"
    #xTitle = "Layer number of first valid pixel hit for leading muon"
    #yTitle = "Layer number of first valid pixel hit for subleading muon"

    #var1 = "muon_numberOfValidPixelHitsMuon0"
    #var2 = "muon_numberOfValidPixelHitsMuon1"
    #xTitle = "Leading muon number of valid pixel hits"
    #yTitle = "Subleading muon number of valid pixel hits"

    #var1 = "muon_layerOfFirstValidPixelHitMuon0"
    #var1 = "muon_etaMuon0"
    #var2 = "muon_numberOfValidPixelHitsMuon0"
    var1 = "muon_phiMuon0"
    #varA = "muon_layerOfFirstValidPixelHitMuon1"
    #varA = "muon_etaMuon1"
    #varB = "muon_numberOfValidPixelHitsMuon1"
    #varB = "muon_phiMuon1"
    #xTitle = "Layer number of first valid pixel hit for muons"
    #xTitle = "Muon #eta"
    #xTitle = "Run number"
    #yTitle = "Muon number of valid pixel hits"
    #xTitle = "M_{#mu#mu} [GeV]"
    xTitle = "Leading muon #phi"

    var2 = "muon_beamspot_d0Muon0"
    #varA = "muon_beamspot_d0Muon1"
    yTitle = "Muon d_{0} [#mum]"

    varA = "muon_beamspot_absD0Muon0"
    varB = "muon_beamspot_absD0Muon1"

    #xTitle = "Muon #phi"
    #xTitle = "Muon #eta"
    #yTitle = "Events"
else:
    print "wrong analysis channel, exiting"
    sys.exit(1)

CanvasPrelim = TCanvas("CanvasPreliminary","")
CanvasPrelim.SetHighLightColor(2)
CanvasPrelim.Range(-72.16495,-10.50091,516.9367,82.84142)
CanvasPrelim.SetFillColor(0)
CanvasPrelim.SetBorderMode(0)
CanvasPrelim.SetBorderSize(2)
CanvasPrelim.SetFrameBorderMode(0)
CanvasPrelim.SetFrameBorderMode(0)

CanvasMean = TCanvas("CanvasMean","")
CanvasMean.SetHighLightColor(2)
CanvasMean.Range(-72.16495,-10.50091,516.9367,82.84142)
CanvasMean.SetFillColor(0)
CanvasMean.SetBorderMode(0)
CanvasMean.SetBorderSize(2)
CanvasMean.SetFrameBorderMode(0)
CanvasMean.SetFrameBorderMode(0)

CanvasStdDev = TCanvas("CanvasStdDev","")
CanvasStdDev.SetHighLightColor(2)
CanvasStdDev.Range(-72.16495,-10.50091,516.9367,82.84142)
CanvasStdDev.SetFillColor(0)
CanvasStdDev.SetBorderMode(0)
CanvasStdDev.SetBorderSize(2)
CanvasStdDev.SetFrameBorderMode(0)
CanvasStdDev.SetFrameBorderMode(0)

#h = TH2F("h","",5, -0.5, 4.5, 6, 0, 6) #layer of first valid pixel hit vs number of valid pixel hits
#h = TH2F("h","",5, -0.5, 4.5, 64, -3.2, 3.2) #layer of first valid pixel hit vs phi
#h = TH2F("h","", 64, -3.2, 3.2, 64, -3.2, 3.2) #phi vs phi
#h = TH2F("h","", 60, -3, 3, 60, -3, 3) #eta vs eta
#h = TH2F("h","", 60, -3, 3, 64, -3.2, 3.2) #eta vs phi
#h = TH2F("h","", 5, -0.5, 4.5, 5, -0.5, 4.5) #layer of first valid pixel hit vs layer of first valid pixel hit
#h = TH2F("h","", 6, 0, 6, 6, 0, 6) #num of valid pixel hits vs num of valid pixel hits
#h = TH1F("h","", 92, 278000, 324000) #run number
#h = TH1F("h","", 140, 278000, 285000) #run number
#h = TH1F("h","", 64, -3.2, 3.2) #phi
#h = TH1F("h","", 60, -3, 3) #eta
#h = TH1F("h","", 5, -0.5, 4.5) #layer of first valid pixel hit
#h = TH1F("h","", 6, 0, 6) #num of valid pixel hits
#h = TH1F("h","", 40, 70, 110) #invariant mass
#h.SetMarkerStyle(20)
#h.SetLineColor(1)
#h.SetTitle(";"+xTitle+";"+yTitle)
totalCount = 0
nDatasets = 0

Hists = []
MeanHists = []
SDHists = []

for dataset in datasets:
    h = TH2F("h","", 64, -3.2, 3.2, 100, -500, 500 ) #phi vs d0
    h.SetTitle(";"+xTitle+";"+yTitle)

    fileName = "condor/%s/mergeOutputHadd/%s.root" % (arguments.condorDir,dataset)
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
    #if not "InclusiveSignalRegionTreeMaker" in keys:
    if not "PreselectionTreeMaker" in keys:
        print "no Tree, setting getMeanEfficiency to -1"
        sys.exit(1)
    #tree = inputFile.Get("InclusiveSignalRegionTreeMaker/Tree")
    tree = inputFile.Get("PreselectionTreeMaker/Tree")

    for iEntry in tree:
        totalCount += 1
        var1_ = getattr(iEntry,var1)
        var2_ = getattr(iEntry,var2)
        varA_ = getattr(iEntry,varA)
        varB_ = getattr(iEntry,varB)

        if(varA_ < 50. and varB_ < 50.): #PCR
            h.Fill(var1_,var2_)

        #print "run is: "+ str(getattr(iEntry,"eventvariable_run"))
        #print "muon_ptMuon0 is: " + str(getattr(iEntry,"muon_ptMuon0")) + " muon_etaMuon0 is: " + str(getattr(iEntry,"muon_etaMuon0")) + " muon_phiMuon0 is: " + str(getattr(iEntry,"muon_phiMuon0"))
        #print "muon_layerOfFirstValidPixelHitMuon0 is: " + str(var1_) + " muon_numberOfValidPixelHitsMuon0 is: " + str(var2_)
        #print "muon_ptMuon1 is: " + str(getattr(iEntry,"muon_ptMuon1")) + " muon_etaMuon1 is: " + str(getattr(iEntry,"muon_etaMuon1")) + " muon_phiMuon1 is: " + str(getattr(iEntry,"muon_phiMuon1"))
        #print "muon_layerOfFirstValidPixelHitMuon1 is: " + str(varA_) + " muon_numberOfValidPixelHitsMuon1 is: " + str(varB_)

        #phi0_ = getattr(iEntry, "muon_phiMuon0")
        #phi1_ = getattr(iEntry, "muon_phiMuon1")
        #energy0_ = getattr(iEntry, "muon_energyMuon0")
        #energy1_ = getattr(iEntry, "muon_energyMuon1")
        #px0_ = getattr(iEntry, "muon_pxMuon0")
        #px1_ = getattr(iEntry, "muon_pxMuon1")
        #py0_ = getattr(iEntry, "muon_pyMuon0")
        #py1_ = getattr(iEntry, "muon_pyMuon1")
        #pz0_ = getattr(iEntry, "muon_pzMuon0")
        #pz1_ = getattr(iEntry, "muon_pzMuon1")
        #eSum_ = energy0_ + energy1_
        #pxSum_ = px0_ + px1_
        #pySum_ = py0_ + py1_
        #pzSum_ = pz0_ + pz1_
        #invMass_ = math.sqrt(eSum_*eSum_ - pxSum_*pxSum_ - pySum_*pySum_ - pzSum_*pzSum_)
        #print "invariant mass is: " + str(invMass_)
        #print "########"
        #print ""
        #if(invMass_>70. and invMass_<110.):
        #if(abs(phi0_)>1.34 and abs(phi0_)<1.67 and abs(phi1_)>1.34 and abs(phi1_)<1.67):
            #print "invariant mass is: " + str(invMass_)
            #h.Fill(var1_,var2_)
            #h.Fill(varA_,varB_)
            #h.Fill(var1_)
            #h.Fill(var2_)
            #h.Fill(invMass_)

    inputFile.Close()

    #h.GetYaxis().SetRangeUser(0,6)
    print "total number of events is: " + str(totalCount)

    # get y projections
    y_projections = []
    for bin_ix in range(1, h.GetXaxis().GetNbins()+1):
        y_projections.append(h.ProjectionY(str(bin_ix), bin_ix, bin_ix))

    # plot y-projection stats vs x
    mean_plot = h.ProjectionX("mean")
    std_dev_plot = h.ProjectionX("standard deviation")

    for bin_ix, y_projection in enumerate(y_projections):
        mean_plot.SetBinContent(bin_ix+1, y_projection.GetMean())
        mean_plot.SetBinError(bin_ix+1, y_projection.GetMeanError())
        std_dev_plot.SetBinContent(bin_ix+1, y_projection.GetStdDev())
        std_dev_plot.SetBinError(bin_ix+1, y_projection.GetStdDevError())
    for plot in [mean_plot, std_dev_plot]:
        plot.SetStats(False)
        plot.SetMarkerStyle(20+nDatasets)
        plot.SetLineColor(1+nDatasets)
        plot.SetMarkerColor(1+nDatasets)

    mean_plot.GetYaxis().SetTitle("d_0 mean [#mum]")
    std_dev_plot.GetYaxis().SetRangeUser(0,20)
    std_dev_plot.GetYaxis().SetTitle("d_0 standard deviation [#mum]")

    Hists.append(h)
    MeanHists.append(mean_plot)
    SDHists.append(std_dev_plot)
    nDatasets += 1

CanvasMean.cd()
MeanHists[0].Draw()
for i in range(len(MeanHists)-1):
    MeanHists[i+1].Draw("same")
LumiPrelimLabel.Draw()
HeaderLabel.Draw()
CanvasMean.SaveAs("./meanLeadingMuonD0_vs_leadingMuonPhi.pdf")

CanvasStdDev.cd()
SDHists[0].Draw()
for i in range(len(SDHists)-1):
    SDHists[i+1].Draw("same")
LumiPrelimLabel.Draw()
HeaderLabel.Draw()
CanvasStdDev.SaveAs("./stdDevLeadingMuonD0_vs_leadingMuonPhi.pdf")

CanvasPrelim.cd()
h.Draw("colz")
#h.Draw("pe")
LumiPrelimLabel.Draw()
HeaderLabel.Draw()
#CanvasPrelim.SaveAs("./muonLayerOfFirstValidPixelHit_vs_muonNumberOfValidPixelHits.pdf")
#CanvasPrelim.SaveAs("./muonLayerOfFirstValidPixelHit_vs_muonPhi.pdf")
#CanvasPrelim.SaveAs("./runNumber.pdf")
#CanvasPrelim.SaveAs("./muonPhi_8events.pdf")
#CanvasPrelim.SaveAs("./muonEta_8events.pdf")
#CanvasPrelim.SaveAs("./muonLayerOfFirstValidPixelHit_8events.pdf")
#CanvasPrelim.SaveAs("./muonNumberOfValidPixelHits_8events.pdf")
#CanvasPrelim.SaveAs("./invMass_8events.pdf")
#CanvasPrelim.SaveAs("./muonLayerOfFirstValidPixelHit_vs_muonNumberOfValidPixelHits_8events.pdf")
#CanvasPrelim.SaveAs("./muonLayerOfFirstValidPixelHit_vs_muonPhi_8events.pdf")
#CanvasPrelim.SaveAs("./muonEta_vs_muonPhi_8events.pdf")
#CanvasPrelim.SaveAs("./zMassWindow_Muon0PhiVsMuon1Phi.pdf")
#CanvasPrelim.SaveAs("./zMassWindow_Muon0EtaVsMuon1Eta.pdf")
#CanvasPrelim.SaveAs("./zMassWindow_Muon0LayerOfFirstValidPixelHitVsMuon1LayerOfFirstValidPixelHit.pdf")
#CanvasPrelim.SaveAs("./zMassWindow_Muon0NumberOfValidPixelHitsVsMuon1NumberOfValidPixelHits.pdf")
CanvasPrelim.SaveAs("./leadingMuonD0_vs_leadingMuonPhi.pdf")
