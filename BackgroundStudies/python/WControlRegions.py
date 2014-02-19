import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.BackgroundStudies.QCDPreselections import *

##############################################################
##### EVENT SELECTIONS FOR OUR QCD B-BBAR CONTROL REGIONS ####
##############################################################

Wjets_Muon_Selection = cms.PSet(
    name = cms.string("Wjets_Muon_Selection"),
    triggers = cms.vstring("HLT_IsoMu24_v"),
    cuts = cms.VPSet (
      cms.PSet (
        inputCollection = cms.string("events"),
        cutString = cms.string("FilterOutScraping > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("primaryvertexs"),
        cutString = cms.string("isGood > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 35"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("tightIDdisplaced > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("metMT > 40"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("relPFdBetaIso < 0.12"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
      ),
      cms.PSet (
        inputCollection = cms.string("mets"),
        cutString = cms.string("pt > 40"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.string("jets"),
        cutString = cms.string("pt > 30"),
        numberRequired = cms.string(">= 0"),
      ),
   )
)

Wjets_Muon_Selection_WithBtagVeto = cms.PSet(
    name = cms.string("Wjets_Muon_Selection_WithBtagVeto"),
    triggers = cms.vstring("HLT_IsoMu24_v"),
    cuts = cms.VPSet (),
)

Wjets_Muon_Selection_WithBtagVeto.cuts.extend(copy.deepcopy(Wjets_Muon_Selection.cuts))

btag_veto_cut = cms.PSet(
	inputCollection = cms.string("jets"),
        cutString = cms.string("btagCombinedSecVertex > 0.244"),
	numberRequired = cms.string("== 0 "),
	isVeto = cms.bool(True)
        )
Wjets_Muon_Selection_WithBtagVeto.cuts.append(btag_veto_cut)

Wjets_Muon_Selection_NearJetVeto = cms.PSet(
    name = cms.string("Wjets_Muon_Selection_NearJetVeto"),
    triggers = cms.vstring("HLT_IsoMu24_v"),
    cuts = cms.VPSet (),
)

Wjets_Muon_Selection_NearJetVeto.cuts.extend(copy.deepcopy(Wjets_Muon_Selection_WithBtagVeto.cuts))

nearjet_veto_cut = cms.PSet(
	inputCollection = cms.string("muon-jet pairs"),
        cutString = cms.string("deltaR < 0.5"),
	numberRequired = cms.string("== 0 "),
	isVeto = cms.bool(True)
        )
Wjets_Muon_Selection_NearJetVeto.cuts.append(nearjet_veto_cut)

Wjets_Muon_Selection_BadCSVVeto = cms.PSet(
    name = cms.string("Wjets_Muon_Selection_BadCSVVeto"),
    triggers = cms.vstring("HLT_IsoMu24_v"),
    cuts = cms.VPSet (),
)

Wjets_Muon_Selection_BadCSVVeto.cuts.extend(copy.deepcopy(Wjets_Muon_Selection_WithBtagVeto.cuts))

badcsv_veto_cut = cms.PSet(
	inputCollection = cms.string("jets"),
        cutString = cms.string("btagCombinedSecVertex < 0"),
	numberRequired = cms.string("== 0 "),
	isVeto = cms.bool(True)
        )
Wjets_Muon_Selection_BadCSVVeto.cuts.append(badcsv_veto_cut)
##############################################################

Wjets_Electron_Selection = cms.PSet(
    name = cms.string("Wjets_Electron_Selection"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet (
      cms.PSet (
        inputCollection = cms.string("events"),
        cutString = cms.string("FilterOutScraping > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("primaryvertexs"),
        cutString = cms.string("isGood > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("isEBEEGap == 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron ECAL crack veto")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("mvaNonTrig_HtoZZto4l > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("passConvVeto > 0 & numberOfLostHits = 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron conversion rejection")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("relPFrhoIso < 0.1"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("metMT > 40"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1")
      ),
    )
)


