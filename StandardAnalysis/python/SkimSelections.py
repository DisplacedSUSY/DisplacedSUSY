import FWCore.ParameterSet.Config as cms
import copy


#########################################################
############## ELECTRON MUON SKIM SELECTION #############
#########################################################

EMu_Skim = cms.PSet(
    name = cms.string("EMu_Skim"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
      # EVENT CLEANING
      cms.PSet (
        inputCollection = cms.string("events"),
        cutString = cms.string("FilterOutScraping > 0"),
        numberRequired = cms.string(">= 1")
      ),
      # EVENT HAS GOOD PV
      cms.PSet (
        inputCollection = cms.string("primaryvertexs"),
        cutString = cms.string("isGood > 0"),
        numberRequired = cms.string(">= 1")
      ),
      # ELECTRON CUT
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(eta) < 3 & pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      # MUON CUT
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(eta) < 3 & pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
   )
)

###########################################################
############## DOUBLE ELECTRON SKIM SELECTION #############
###########################################################

EE_Skim = cms.PSet(
    name = cms.string("EE_Skim"),
    triggers = cms.vstring("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v"), # TRIGGER
    cuts = cms.VPSet (
      # EVENT CLEANING
      cms.PSet (
        inputCollection = cms.string("events"),
        cutString = cms.string("FilterOutScraping > 0"),
        numberRequired = cms.string(">= 1")
      ),
      # EVENT HAS GOOD PV
      cms.PSet (
        inputCollection = cms.string("primaryvertexs"),
        cutString = cms.string("isGood > 0"),
        numberRequired = cms.string(">= 1")
      ),
      # ELECTRON CUT
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(eta) < 3 & pt > 20"),
        numberRequired = cms.string(">= 2")
      ),
   )
)

#######################################################
############## DOUBLE MUON SKIM SELECTION #############
#######################################################

MuMu_Skim = cms.PSet(
    name = cms.string("MuMu_Skim"),
    triggers = cms.vstring("HLT_Mu17_Mu8_v"), # TRIGGER
    cuts = cms.VPSet (
      # EVENT CLEANING
      cms.PSet (
        inputCollection = cms.string("events"),
        cutString = cms.string("FilterOutScraping > 0"),
        numberRequired = cms.string(">= 1")
      ),
      # EVENT HAS GOOD PV
      cms.PSet (
        inputCollection = cms.string("primaryvertexs"),
        cutString = cms.string("isGood > 0"),
        numberRequired = cms.string(">= 1")
      ),
      # MUON CUT
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(eta) < 3 & pt > 20"),
        numberRequired = cms.string(">= 2")
      ),
   )
)

