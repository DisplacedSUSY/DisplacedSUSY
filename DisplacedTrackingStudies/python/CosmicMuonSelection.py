import FWCore.ParameterSet.Config as cms
import copy
import string
##########################################################################
##### Set up the EMu Skim Selections for the displaced SUSY analysis #####
##########################################################################

CosmicMuonGLBSelection = cms.PSet(
    name = cms.string("CosmicMuonGLBSelection"),
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v"), # TRIGGER
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > 30"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("isGlobalMuon"),
            numberRequired = cms.string(">= 1"),
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("phi < 0"),
            numberRequired = cms.string(">= 1"),
        ),
    ),
)

CosmicMuonSTASelection = cms.PSet(
    name = cms.string("CosmicMuonSTASelection"),
    triggers = cms.vstring("HLT_L2Mu35_NoVertex_3Sta_NoBPTX3BX_NoHalo_v"), # TRIGGER
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > 30"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("isStandAloneMuon"),
            numberRequired = cms.string(">= 1"),
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("phi < 0"),
            numberRequired = cms.string(">= 1"),
        ),
    ),
)
