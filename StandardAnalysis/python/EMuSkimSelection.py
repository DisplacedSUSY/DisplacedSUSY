import FWCore.ParameterSet.Config as cms
import copy
import string
##########################################################################
######## Set up the EMu Skim Selections for the displaced SUSY analysis #########
##########################################################################
##########################################################################
EMuSkimSelection = cms.PSet(
    name = cms.string("EMuSkimSelection"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > 25"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > 25"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("isPFMuon & isGlobalMuon"),
            numberRequired = cms.string(">= 1")
        ),
    ),
)

EMuSkimSelectionInclusiveTrigger = cms.PSet(
    name = cms.string("EMuSkimSelectionInclusiveTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)

EMuSkimSelectionInclusiveTrigger.cuts = cms.VPSet (copy.deepcopy(EMuSkimSelection.cuts))

