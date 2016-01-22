import FWCore.ParameterSet.Config as cms
import copy
import string


##########################################################################

#Electron isolation cut
electron_iso_cut = cms.PSet (
    inputCollection = cms.vstring("electrons"),
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
    alias = cms.string("electron isolation")
)

##########################################################################

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
    alias = cms.string("muon isolation")
)


#Basic electron selections
electron_basic_selection_cuts = cms.VPSet(
    # ELECTRON PT CUT
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > 42"),
        numberRequired = cms.string(">= 1")
    ),
    # ELECTRON CRACK VETO
    #cms.PSet (
    #    inputCollection = cms.vstring("electrons"),
    #    cutString = cms.string("isEBEEGap = 0"),
    #    numberRequired = cms.string(">= 1"),
    #    alias = cms.string("electron ECAL crack veto")
    #),
    # ELECTRON ETA CUT
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 1")
    ),
    # ELECTRON ID
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("                              \
          (abs(superCluster.eta) <= 1.479 & \
          missingInnerHits_ <= 2 & \
          abs(deltaEtaSuperClusterTrackAtVtx) < 0.00926 & \
          abs(deltaPhiSuperClusterTrackAtVtx) < 0.0336 & \
          full5x5_sigmaIetaIeta < 0.0101 & \
          hadronicOverEm < 0.0597 & \
          abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.012 & \
          passConversionVeto)|\
          (abs(superCluster.eta) > 1.479 & abs(superCluster.eta) < 2.5 &\
          missingInnerHits_ <= 1 & \
          abs(deltaEtaSuperClusterTrackAtVtx) < 0.00724 & \
          abs(deltaPhiSuperClusterTrackAtVtx) < 0.0918 & \
          full5x5_sigmaIetaIeta < 0.0279 & \
          hadronicOverEm < 0.0615 & \
          abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.00999 & \
          passConversionVeto)"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron tight displaced ID")
    ),
)

##########################################################################

# ELECTRON ID
electron_id_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("                              \
          (abs(superCluster.eta) <= 1.479 & \
          missingInnerHits_ <= 2 & \
          abs(deltaEtaSuperClusterTrackAtVtx) < 0.00926 & \
          abs(deltaPhiSuperClusterTrackAtVtx) < 0.0336 & \
          full5x5_sigmaIetaIeta < 0.0101 & \
          hadronicOverEm < 0.0597 & \
          abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.012 & \
          passConversionVeto)|\
          (abs(superCluster.eta) > 1.479 & abs(superCluster.eta) < 2.5 & \
          missingInnerHits_ <= 1 & \
          abs(deltaEtaSuperClusterTrackAtVtx) < 0.00724 & \
          abs(deltaPhiSuperClusterTrackAtVtx) < 0.0918 & \
          full5x5_sigmaIetaIeta < 0.0279 & \
          hadronicOverEm < 0.0615 & \
          abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.00999 & \
          passConversionVeto)"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron tight displaced ID")
)

##########################################################################

#General muon selections
muon_basic_selection_cuts = cms.VPSet(
    # MUON PT CUT
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > 40"),
        numberRequired = cms.string(">= 1")
    ),
    # MUON ETA CUT
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 1")
    ),
    # MUON ID
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("\
        isGlobalMuon & \
        isPFMuon & \
        globalTrack.hitPattern_.numberOfValidMuonHits > 0 & \
        globalTrack.normalizedChi2 < 10 & \
        numberOfMatchedStations > 1 & \
        innerTrack.hitPattern_.numberOfValidPixelHits > 0 & \
        innerTrack.hitPattern_.trackerLayersWithMeasurement > 5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("muon tight displaced ID")
    ),
)

##########################################################################

# MUON ID
muon_id_cut = cms.PSet (
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
)

##########################################################################

#Preselection cuts
preselection_emu_cuts = cms.VPSet(
    #Extra Lepton Veto
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
    #Extra Lepton Veto
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
    ),
    # ELECTRON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("electrons","beamspots"),
        cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) <= 0.02 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron dxy <= 0.02 cm")
    ),
    cms.PSet (
        inputCollection = cms.vstring("muons","beamspots"),
        cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) <= 0.02 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("muon dxy <= 0.02 cm")
    ),
    # ELECTRON AND MUON ARE OPPOSITELY CHARGED
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("electron.charge * muon.charge < 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("oppositely-charged e-mu pair")
   ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("deltaR(electron, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated (DeltaR > 0.5) e-mu pair")
    ),
)
