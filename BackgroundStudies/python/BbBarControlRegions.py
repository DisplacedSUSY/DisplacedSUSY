import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.BackgroundStudies.QCDPreselections import *

##############################################################
##### EVENT SELECTIONS FOR OUR QCD B-BBAR CONTROL REGIONS ####
##############################################################

BbBar_Muon_Selection = cms.PSet(
    name = cms.string("BbBar_Muon_Selection"),
    triggers = cms.vstring("HLT_Mu17_v"),
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
        cutString = cms.string("pt > 25"),
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
        cutString = cms.string("metMT < 60"),
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
        inputCollection = cms.string("jets"),
        cutString = cms.string("abs(eta) < 2.4 & pt > 20 & btagCombinedSecVertex > 0.679"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.string("secondary jets"),
        cutString = cms.string("abs(eta) < 2.4 & pt > 20"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.string("jet-secondary jet pairs"),
        cutString = cms.string("deltaPhi > 2.5"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.string("muon-secondary jet pairs"),
        cutString = cms.string("deltaR < 0.5"),
        numberRequired = cms.string(">= 1"),
      ),  
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
      ),
   )
)

##############################################################

BbBar_Electron_Selection = cms.PSet(
    name = cms.string("BbBar_Electron_Selection"),
    triggers = cms.vstring("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v"),
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
        cutString = cms.string("metMT < 60"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("jets"),
        cutString = cms.string("abs(eta) < 2.4 & pt > 20 & btagCombinedSecVertex > 0.244"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.string("secondary jets"),
        cutString = cms.string("abs(eta) < 2.4 & pt > 20"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.string("jet-secondary jet pairs"),
        cutString = cms.string("deltaPhi > 2.5"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.string("electron-secondary jet pairs"),
        cutString = cms.string("deltaR < 0.5"),
        numberRequired = cms.string(">= 1"),
      ),  
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
      ),
    )
)

###############################################################################

BbBar_Muon_Selection_AntiIso = cms.PSet(
    name = cms.string("BbBar_Muon_Selection_AntiIso"),
    triggers = cms.vstring(BbBar_Muon_Selection.triggers),
    cuts = cms.VPSet ()
)
BbBar_Muon_Selection_AntiIso.cuts = invert_isolation (BbBar_Muon_Selection.cuts)

BbBar_Electron_Selection_AntiIso = cms.PSet(
    name = cms.string("BbBar_Electron_Selection_AntiIso"),
    triggers = cms.vstring(BbBar_Electron_Selection.triggers),
    cuts = cms.VPSet ()
)
BbBar_Electron_Selection_AntiIso.cuts = invert_isolation (BbBar_Electron_Selection.cuts)

BbBar_Muon_Selection_NoIso = cms.PSet(
    name = cms.string("BbBar_Muon_Selection_NoIso"),
    triggers = cms.vstring(BbBar_Muon_Selection.triggers),
    cuts = cms.VPSet ()
)
BbBar_Muon_Selection_NoIso.cuts = invert_isolation (BbBar_Muon_Selection.cuts)
for cut in BbBar_Muon_Selection_NoIso.cuts:
	if 'dBeta' in str(cut.cutString):
		BbBar_Muon_Selection_NoIso.cuts.remove(cut)


BbBar_Electron_Selection_NoIso = cms.PSet(
    name = cms.string("BbBar_Electron_Selection_NoIso"),
    triggers = cms.vstring(BbBar_Electron_Selection.triggers),
    cuts = cms.VPSet ()
)
BbBar_Electron_Selection_NoIso.cuts = invert_isolation (BbBar_Electron_Selection.cuts)
for cut in BbBar_Electron_Selection_NoIso.cuts:
	if 'PF' in str(cut.cutString):
		BbBar_Electron_Selection_NoIso.cuts.remove(cut)
