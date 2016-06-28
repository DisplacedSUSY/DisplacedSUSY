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
    #cms.PSet (
    #    inputCollection = cms.vstring("jets"),
    #    cutString = cms.string("matchedToLepton < 1 "),
    #    numberRequired = cms.string(">= 0")
    #),
    cms.PSet (
        inputCollection = cms.vstring("jets"),
        #loose jet Id
        #cutString = cms.string("neutralHadronEnergyFraction < 0.99 & chargedEmEnergyFraction < 0.99 & neutralEmEnergyFraction < 0.99 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0"),
        #tight lepton veto Id
        cutString = cms.string("neutralHadronEnergyFraction < 0.90 & chargedEmEnergyFraction < 0.90 & neutralEmEnergyFraction < 0.90 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0 & muonEnergyFraction < 0.8"),
        numberRequired = cms.string(">= 0"),
        alias = cms.string('tight lepton veto jet ID')
    ),
)

##########################################################################

#Basic bjet selections
bjet_basic_selection_cuts = cms.VPSet(
    cms.PSet (
        inputCollection = cms.vstring("bjets"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 0")
    ),
    cms.PSet (
        inputCollection = cms.vstring("bjets"),
        cutString = cms.string("pt > 30"),
        numberRequired = cms.string(">= 0")
    ),
    cms.PSet (
        inputCollection = cms.vstring("bjets"),
        #loose jet Id
        #cutString = cms.string("neutralHadronEnergyFraction < 0.99 & chargedEmEnergyFraction < 0.99 & neutralEmEnergyFraction < 0.99 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0"),
        #tight lepton veto Id
        cutString = cms.string("neutralHadronEnergyFraction < 0.90 & chargedEmEnergyFraction < 0.90 & neutralEmEnergyFraction < 0.90 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0 & muonEnergyFraction < 0.8"),
        numberRequired = cms.string(">= 0"),
        alias = cms.string('tight lepton veto bjet ID')
    ),
)

##########################################################################

# Electron inverted isolation cut
electron_inverted_iso_cut = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string('          \
        ((pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho*AEff))/pt >= 0.15 & \
        (pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho*AEff))/pt <= 1.5)'
     ),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("inverted electron isolation")
)

electron_inverted_dbeta_iso_cut = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string('          \
        ((pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - 0.5*pfIso_.sumPUPt))/pt >= 0.15 & \
        (pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - 0.5*pfIso_.sumPUPt))/pt <= 1.5)'
     ),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("inverted electron dbeta isolation")
)

electron_inverted_iso_corr_cut = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string('          \
        pfdRhoIsoCorr >= 0.15 & pfdRhoIsoCorr <= 1.5 \
         '),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("inverted electron isolation corrected")
)

##########################################################################

# Electron loose isolation cut
electron_loose_iso_cut = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string('          \
        (pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho*AEff))/pt <= 1.5'),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("loose electron isolation")
)

electron_loose_iso_corr_cut = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string('          \
        pfdRhoIsoCorr <= 1.5 \
    '),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("loose electron isolation corrected")
)
##########################################################################

# Muon inverted isolation cut
muon_inverted_iso_cut = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string('               \
        (pfIsolationR04_.sumChargedHadronPt + max(0.0, pfIsolationR04_.sumNeutralHadronEt + pfIsolationR04_.sumPhotonEt - 0.5*pfIsolationR04_.sumPUPt))/pt >= 0.15 & \
        (pfIsolationR04_.sumChargedHadronPt + max(0.0, pfIsolationR04_.sumNeutralHadronEt + pfIsolationR04_.sumPhotonEt - 0.5*pfIsolationR04_.sumPUPt))/pt <= 1.5\
       '),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("inverted muon isolation")
)

muon_inverted_iso_corr_cut = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string('               \
        pfdBetaIsoCorr >= 0.15 & pfdBetaIsoCorr <= 1.5 \
       '),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("inverted muon isolation corrected")
)
##########################################################################

# Muon loose isolation cut
muon_loose_iso_cut = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("                \
        (pfIsolationR04_.sumChargedHadronPt \
        + max(0.0,                          \
        pfIsolationR04_.sumNeutralHadronEt  \
        + pfIsolationR04_.sumPhotonEt       \
        - 0.5*pfIsolationR04_.sumPUPt))     \
        /pt <= 1.5                          \
       "),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("loose muon isolation")
)

muon_loose_iso_corr_cut = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("                \
        pfdBetaIsoCorr <= 1.5\
       "),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("loose muon isolation corrected")
)

##########################################################################

#Electron isolation cut
electron_iso_corr_cut = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("        \
        (pfdRhoIsoCorr <= 0.0646 && isEE) | \
        (pfdRhoIsoCorr <= 0.0354  && isEB) \
        "),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron isolation corrected")
)

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
        - rho*AEff))                \
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

muon_iso_corr_cut = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("                \
        pfdBetaIsoCorr <= 0.15\
        "),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon isolation corrected")
)

##########################################################################

# ELECTRON-JET OVERLAP VETO
electron_jet_deltaR_cut = cms.PSet (
        inputCollection = cms.vstring("electrons", "jets"),
        cutString = cms.string("deltaR(electron, jet) < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("electron near jet veto")
)

##########################################################################

# MUON-JET OVERLAP VETO
muon_jet_deltaR_cut = cms.PSet (
        inputCollection = cms.vstring("muons", "jets"),
        cutString = cms.string("deltaR(muon, jet) < 0.5"),
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
          missingInnerHits <= 2 & \
          abs(deltaEtaSuperClusterTrackAtVtx) < 0.00926 & \
          abs(deltaPhiSuperClusterTrackAtVtx) < 0.0336 & \
          full5x5_sigmaIetaIeta < 0.0101 & \
          hadronicOverEm < 0.0597 & \
          abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.012 & \
          passConversionVeto)|\
          (isEE & \
          missingInnerHits <= 1 & \
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
          (isEB & \
          missingInnerHits <= 2 & \
          abs(deltaEtaSuperClusterTrackAtVtx) < 0.00926 & \
          abs(deltaPhiSuperClusterTrackAtVtx) < 0.0336 & \
          full5x5_sigmaIetaIeta < 0.0101 & \
          hadronicOverEm < 0.0597 & \
          abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.012 & \
          passConversionVeto)|\
          (isEE & \
          missingInnerHits <= 1 & \
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
    # GLOBAL MUON
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("isGlobalMuon & isPFMuon"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("Global Muon")
    ),
    # MUON ID
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("\
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
muon_global_cut = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("isGlobalMuon & isPFMuon"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Global Muon")
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
        globalTrack.normalizedChi2 < 10 & \
        innerTrack.hitPattern_.numberOfValidPixelHits > 0 & \
        innerTrack.hitPattern_.trackerLayersWithMeasurement > 5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon tight displaced ID")
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

#Displaced control region specific cuts
displaced_control_region_cuts = cms.VPSet(
    # MUON DXY DISPLACED
    cms.PSet (
        inputCollection = cms.vstring("muons","beamspots"),
        cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) > 0.01 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("muon dxy > 0.01 cm")
    ),
    # ELECTRON DISPLACED
    cms.PSet (
        inputCollection = cms.vstring("electrons","beamspots"),
        cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) > 0.01 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron dxy > 0.01 cm")
    ),
    # MUON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("muons","beamspots"),
        cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) <= 0.02 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("muon dxy <= 0.02 cm")
    ),
    # ELECTRON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("electrons","beamspots"),
        cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) <= 0.02 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron dxy <= 0.02 cm")
    ),
    # OPPOSITE SIGN E-MU PAIR
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("electron.charge * muon.charge < 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("oppositely charged e-mu pair")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("deltaR(electron, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
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
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)

##########################################################################
#Blinded control region specific cuts
electron_blinded_control_region_cuts = cms.VPSet(
    #ELECTRON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("electrons","beamspots"),
        cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) <= 0.02"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron blinding cuts")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("deltaR(electron, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
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
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)

muon_blinded_control_region_cuts = cms.VPSet(
    #MUON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("muons","beamspots"),
        cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) <= 0.02"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("muon blinding cuts")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("deltaR(electron, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
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
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)

blinded_control_region_cuts = cms.VPSet(
    # DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("electrons","muons","beamspots"),
        cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) <= 0.02 | abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) <= 0.02"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("blinded cuts")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("deltaR(electron, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
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
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)

displaced_blinded_control_region_cuts = cms.VPSet(
    # DXY BLINDING
    #Only blind the region where both muons and electrons have dxy > 0.02 cm. Also we place a dxy cut on the leptons(dxy > 0.01 cm)
    cms.PSet (
        inputCollection = cms.vstring("electrons","muons","beamspots"),
        cutString = cms.string("(abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) <= 0.02 | abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) <= 0.02) & (abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) >= 0.01 & abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) >= 0.01) "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("displaced cuts")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("deltaR(electron, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
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
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)

loose_displaced_blinded_control_region_cuts = cms.VPSet(
    # DXY BLINDING
    #Only blind the region where both muons and electrons have dxy > 0.02 cm. Also we place a looser dxy cut on the leptons(dxy > 0.005 cm)
    cms.PSet (
        inputCollection = cms.vstring("electrons","muons","beamspots"),
        cutString = cms.string("(abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) <= 0.02 | abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) <= 0.02) & (abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) >= 0.005 & abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) >= 0.005) "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("loose displaced cuts")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("deltaR(electron, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
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
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)
