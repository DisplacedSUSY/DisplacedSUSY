import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.MuMuChannel.CutDefinitions import *

MuMuSkim = cms.PSet(
    name = cms.string("MuMuSkim"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (
        muon_eta_cut,
        muon_pt_25_cut,
        muon_global_cut
        ),
    )
)

EESkim = cms.PSet(
    name = cms.string("EESkim"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 2")
            ),
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > 40"), # thinking of HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15_v
            numberRequired = cms.string(">= 2")
            ),
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("isEBEEGap = 0"),
            numberRequired = cms.string(">= 2"),
            alias = cms.string("electron ECAL crack veto")
            ),
        )
)
