import FWCore.ParameterSet.Config as cms
import copy

MuMuSkim = cms.PSet(
    name = cms.string("MuMuSkim"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 2")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > 28"), # thinking of HLT_DoubleMu28NoFiltersNoVtxDisplaced_v
            numberRequired = cms.string(">= 2")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("isPFMuon & isGlobalMuon"),
            numberRequired = cms.string(">= 2"),
            alias = cms.string("Global Muon")
        ),
        # cms.PSet (
        #     inputCollection = cms.vstring("muons"),
        #     cutString = cms.string("\
        #     globalTrack.hitPattern_.numberOfValidMuonHits > 0 & \
        #     globalTrack.normalizedChi2 < 10 & \
        #     numberOfMatchedStations > 1 & \
        #     innerTrack.hitPattern_.numberOfValidPixelHits > 0 & \
        #     innerTrack.hitPattern_.trackerLayersWithMeasurement > 5"),
        #     numberRequired = cms.string(">= 2"),
        #     alias = cms.string("muon tight displaced ID")
        # ),
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
        # cms.PSet (
        #     inputCollection = cms.vstring("electrons"),
        #     cutString = cms.string("                              \
        #   (isEB & \
        #   missingInnerHits <= 2 & \
        #   abs(deltaEtaSuperClusterTrackAtVtx) < 0.00926 & \
        #   abs(deltaPhiSuperClusterTrackAtVtx) < 0.0336 & \
        #   full5x5_sigmaIetaIeta < 0.0101 & \
        #   hadronicOverEm < 0.0597 & \
        #   abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.012 & \
        #   passConversionVeto)|\
        #   (isEE & \
        #   missingInnerHits <= 1 & \
        #   abs(deltaEtaSuperClusterTrackAtVtx) < 0.00724 & \
        #   abs(deltaPhiSuperClusterTrackAtVtx) < 0.0918 & \
        #   full5x5_sigmaIetaIeta < 0.0279 & \
        #   hadronicOverEm < 0.0615 & \
        #   abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.00999 & \
        #   passConversionVeto)"),
        #     numberRequired = cms.string(">= 2"),
        #     alias = cms.string("electron tight displaced ID")
        #     ),
        )
)
