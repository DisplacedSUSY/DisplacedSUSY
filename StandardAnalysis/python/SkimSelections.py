import FWCore.ParameterSet.Config as cms
import copy


#########################################################
############## ELECTRON MUON SKIM SELECTION #############
#########################################################

EMuSkim = cms.PSet(
    name = cms.string("EMuSkim"),
#    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
      # ELECTRON CUT
      cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("abs(eta) < 3 & pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      # MUON CUT
      cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("abs(eta) < 3 & pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
   )
)

###########################################################
############## DOUBLE ELECTRON SKIM SELECTION #############
###########################################################

EESkim = cms.PSet(
    name = cms.string("EESkim"),
#    triggers = cms.vstring("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v"), # TRIGGER
    cuts = cms.VPSet (
      # ELECTRON CUT
      cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("abs(eta) < 3 & pt > 20"),
        numberRequired = cms.string(">= 2")
      ),
   )
)

#######################################################
############## DOUBLE MUON SKIM SELECTION #############
#######################################################

MuMuSkim = cms.PSet(
    name = cms.string("MuMuSkim"),
#    triggers = cms.vstring("HLT_Mu17_Mu8_v"), # TRIGGER
    cuts = cms.VPSet (
      # MUON CUT
      cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("abs(eta) < 3 & pt > 20"),
        numberRequired = cms.string(">= 2")
      ),
   )
)

#########################################################
################ MUON JET SKIM SELECTION ################
#########################################################

MuJetSkim = cms.PSet(
    name = cms.string("MuJetSkim"),
#    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
      # JET CUT
      cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("abs(eta) < 3 & pt > 30"),
        numberRequired = cms.string(">= 1")
      ),
      # MUON CUT
      cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("abs(eta) < 3 & pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
   )
)
