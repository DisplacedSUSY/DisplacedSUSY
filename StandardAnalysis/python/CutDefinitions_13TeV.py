import FWCore.ParameterSet.Config as cms
import copy
import string
# Electron inversed isolation cut 
electron_inversed_iso_cut = cms.PSet (
    inputCollection = cms.vstring("candeles"),
    cutString = cms.string('          \
        ((pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho*AEff))/pt >= 0.0646 & \
        (pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho*AEff))/pt <= 1.5 & isEE ) |\
        ((pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho_*AEff_))/pt >= 0.0354 & (pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho_*AEff_))/pt <= 1.5 & isEB) \
        '),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron non-isolated")
)
# Muon inversed isolation cut 
muon_inversed_iso_cut = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("                \
        (pfIsolationR04_.sumChargedHadronPt \
        + max(0.0,                          \
        pfIsolationR04_.sumNeutralHadronEt  \
        + pfIsolationR04_.sumPhotonEt       \
        - 0.5*pfIsolationR04_.sumPUPt))     \
        /pt >= 0.15 &&                      \
        (pfIsolationR04_.sumChargedHadronPt \
        + max(0.0,                          \
        pfIsolationR04_.sumNeutralHadronEt  \
        + pfIsolationR04_.sumPhotonEt       \
        - 0.5*pfIsolationR04_.sumPUPt))     \
        /pt <= 1.5                          \
       "),
    numberRequired = cms.string(">= 1"), 
    alias = cms.string("muon non-isolated")
)
#Electron isolation cut
electron_iso_cut = cms.PSet (
    inputCollection = cms.vstring("candeles"),
    cutString = cms.string("        \
        ((pfIso_.sumChargedHadronPt   \
        + max(0.0,                    \
        pfIso_.sumNeutralHadronEt     \
        + pfIso_.sumPhotonEt          \
        - rho*AEff))                  \
        /pt <= 0.0646 && isEE)  |        \
        ((pfIso_.sumChargedHadronPt   \
        + max(0.0,                    \
        pfIso_.sumNeutralHadronEt     \
        + pfIso_.sumPhotonEt          \
        - rho_*AEff_))                \
        /pt <= 0.0354 && isEB)"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron isolated")
)
# Muon isolation cut 
muon_iso_cut = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("                \
        (pfIsolationR04_.sumChargedHadronPt \
        + max(0.0,                          \
        pfIsolationR04_.sumNeutralHadronEt  \
        + pfIsolationR04_.sumPhotonEt       \
        - 0.5*pfIsolationR04_.sumPUPt))     \
        /pt <= 0.15                         \
       "),
    numberRequired = cms.string(">= 1"), 
    alias = cms.string("muon isolated")
)
#Basic electron selections 
electron_basic_selection_cuts = cms.VPSet(
    # ELECTRON ETA CUT
    cms.PSet (
        inputCollection = cms.vstring("candeles"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 1")
    ),
    # ELECTRON CRACK VETO
    cms.PSet (
        inputCollection = cms.vstring("candeles"),
        cutString = cms.string("isEBEEGap = 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron ECAL crack veto")
    ),
    # ELECTRON PT CUT
    cms.PSet (
        inputCollection = cms.vstring("candeles"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
    ),
    # ELECTRON ID
    cms.PSet (
        inputCollection = cms.vstring("candeles"),
        cutString = cms.string("                              \
          (isEB & \
          missingInnerHits_ <= 2 & \
          abs(deltaEtaSuperClusterTrackAtVtx) < 0.00926 & \
          abs(deltaPhiSuperClusterTrackAtVtx) < 0.0336 & \
          full5x5_sigmaIetaIeta < 0.0101 & \
          hadronicOverEm < 0.0597 & \
          abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.012 & \
          !vtxFitConversion)|\
          (isEE & \
          missingInnerHits_ <= 1 & \
          abs(deltaEtaSuperClusterTrackAtVtx) < 0.00724 & \
          abs(deltaPhiSuperClusterTrackAtVtx) < 0.0918 & \
          full5x5_sigmaIetaIeta < 0.0279 & \
          hadronicOverEm < 0.0615 & \
          abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.00999 & \
          !vtxFitConversion)"),          
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron tight displaced ID")
    ),
)
#General muon selections
muon_basic_selection_cuts = cms.VPSet(
    # MUON ETA CUT
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 1")
    ),
    # MUON PT CUT
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
    ),
    # MUON ID
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("\
        isGlobalMuon & \
        isPFMuon & \
        globalTrack.hitPattern_.numberOfValidMuonHits > 0 & \
        numberOfMatchedStations > 1 & \
        innerTrack.hitPattern_.numberOfValidPixelHits > 0 & \
        innerTrack.hitPattern_.trackerLayersWithMeasurement > 5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("muon tight displaced ID")
    ),
)
