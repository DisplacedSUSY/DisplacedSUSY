import FWCore.ParameterSet.Config as cms
import copy
import string
##########################################################################
##### Set up the EMu Skim Selections for the displaced SUSY analysis #####
##########################################################################

CosmicMuonSkimSelection = cms.PSet(
    name = cms.string("CosmicMuonSkimSelection"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > 15"),
            numberRequired = cms.string(">= 1")
        ),
    ),
)
