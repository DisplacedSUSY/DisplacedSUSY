import FWCore.ParameterSet.Config as cms
import copy
import string

##########################################################################

#Basic jet selections
jet_basic_selection_cuts = cms.VPSet(
    cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 0")
    ),
    cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pt > 30"),
        numberRequired = cms.string(">= 0")
    ),
    cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("neutralHadronEnergyFraction < 0.99 & chargedEmEnergyFraction < 0.99 & neutralEmEnergyFraction < 0.99 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0"),
        numberRequired = cms.string(">= 0"),
        alias = cms.string('jet ID')
    ),
)

##########################################################################

# Electron inverted isolation cut
electron_inverted_iso_cut = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string('          \
        ((pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho*AEff))/pt >= 0.0646 & \
        (pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho*AEff))/pt <= 1.5 & isEE ) |\
        ((pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho_*AEff_))/pt >= 0.0354 & (pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho_*AEff_))/pt <= 1.5 & isEB) \
        '),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("inverted electron isolation")
)

##########################################################################

# Muon inverted isolation cut
muon_inverted_iso_cut = cms.PSet (
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
    alias = cms.string("inverted muon isolation")
)

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

##########################################################################

# ELECTRON-JET OVERLAP VETO
electron_jet_deltaR_cut = cms.PSet (
        inputCollection = cms.vstring("electrons", "jets"),
        cutString = cms.string("deltaR(electron, jet) > 0.05 & deltaR(electron, jet) < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("electron near jet veto")
)

##########################################################################

# MUON-JET OVERLAP VETO
muon_jet_deltaR_cut = cms.PSet (
        inputCollection = cms.vstring("muons", "jets"),
        cutString = cms.string("deltaR(muon, jet) > 0.05 & deltaR(muon, jet) < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("muon near jet veto")
)

##########################################################################


#Basic electron selections
electron_basic_selection_cuts = cms.VPSet(
    # ELECTRON ETA CUT
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 1")
    ),
    # ELECTRON CRACK VETO
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("isEBEEGap = 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron ECAL crack veto")
    ),
    # ELECTRON PT CUT
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
    ),
    # ELECTRON ID
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
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

##########################################################################

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

##########################################################################

#Preselection cuts
preselection_emu_cuts = cms.VPSet(
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("deltaR(electron, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated (DeltaR > 0.5) e-mu pair")
    ),
    #Extra Lepton Veto
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
    ),
    #Extra Lepton Veto
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)

##########################################################################

# OPPOSITE SIGN E-MU PAIR
os_emu_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("electron.charge * muon.charge < 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("oppositely-charged e-mu pair")
)

##########################################################################

# SAME SIGN E-MU PAIR
ss_emu_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("electron.charge * muon.charge > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("like-charged e-mu pair")
)

##########################################################################