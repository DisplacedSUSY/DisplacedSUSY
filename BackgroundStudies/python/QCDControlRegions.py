import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.CutDefinitions import *

##############################################################
##### EVENT SELECTIONS FOR OUR QCD B-BBAR CONTROL REGIONS ####
##############################################################

QCDMuonSkim = cms.PSet(
    name = cms.string("QCDMuonSkim"),
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > 10"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("abs(eta) < 2.5"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("\
                                    isGlobalMuon & \
                                    isPFMuon & \
                                    globalTrack.normalizedChi2 < 10 & \
                                    globalTrack.hitPattern_.numberOfValidMuonHits > 0 & \
                                    numberOfMatchedStations > 1 & \
                                    innerTrack.hitPattern_.numberOfValidPixelHits > 0 & \
                                    innerTrack.hitPattern_.trackerLayersWithMeasurement > 5"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("muon tight displaced ID")
        ),
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 1"),
        ),
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("pt > 30"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("neutralHadronEnergyFraction < 0.99 & chargedEmEnergyFraction < 0.99 & neutralEmEnergyFraction < 0.99 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string('jet ID')
        ),
        # loose CSV working point for run 2
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.605"),
            numberRequired = cms.string(">= 1"),
        ),
    )
)

##############################################################


QCDElectronSkim = cms.PSet(
    name = cms.string("QCDElectronSkim"),
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > 10"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("abs(eta) < 2.5"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("      \
                                    (isEB & \
                                    missingInnerHits_ <= 2 & \
                                    abs(deltaEtaSuperClusterTrackAtVtx) < 0.00926 & \
                                    abs(deltaPhiSuperClusterTrackAtVtx) < 0.0336 & \
                                    full5x5_sigmaIetaIeta < 0.0101 & \
                                    hadronicOverEm < 0.0597 & \
                                    abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.012 & \
                                    passConversionVeto)|\
                                    (isEE & \
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
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 1"),
        ),
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("pt > 30"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("neutralHadronEnergyFraction < 0.99 & chargedEmEnergyFraction < 0.99 & neutralEmEnergyFraction < 0.99 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string('jet ID')
        ),
        # loose CSV working point for run 2
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.605"),
            numberRequired = cms.string(">= 1"),
        ),
    )
)


##############################################################
# extra cuts for the control region

# dummy muon cut
muon_dummy_cut = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 1"),
)

# CSV L working point
bjet_csvl_cut = cms.PSet (
    inputCollection = cms.vstring("bjets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.605"),
    numberRequired = cms.string(">= 1"),
)
# CSV M working point
bjet_csvm_cut = cms.PSet (
    inputCollection = cms.vstring("bjets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.89"),
    numberRequired = cms.string(">= 1"),
)
dijet_cut = cms.PSet (
    inputCollection = cms.vstring("jets","bjets"),
    cutString = cms.string("abs(deltaPhi(jet,bjet)) > 2.5"),
    numberRequired = cms.string(">= 1"),
)
muonjet_cut = cms.PSet (
    inputCollection = cms.vstring("muons","jets"),
    cutString = cms.string("deltaR(muon,jet) < 0.2"),
    numberRequired = cms.string(">= 1"),
)
electronjet_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","jets"),
    cutString = cms.string("deltaR(electron,jet) < 0.2"),
    numberRequired = cms.string(">= 1"),
)
muon_inverted_iso_cut = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("                \
        (pfIsolationR04_.sumChargedHadronPt \
        + max(0.0,                          \
        pfIsolationR04_.sumNeutralHadronEt  \
        + pfIsolationR04_.sumPhotonEt       \
        - 0.5*pfIsolationR04_.sumPUPt))     \
        /pt >= 0.15                         \
       "),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("inverted muon isolation")
)


##############################################################

QCDMuonControlRegion = cms.PSet(
    name = cms.string("QCDMuonControlRegion"),
    triggers = cms.vstring("HLT_Mu20_v"),
    cuts = cms.VPSet ()
)

QCDMuonControlRegion.cuts.append(muon_global_cut)
QCDMuonControlRegion.cuts.extend(muon_basic_selection_cuts)
QCDMuonControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDMuonControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDMuonControlRegion.cuts.append(bjet_csvl_cut)
QCDMuonControlRegion.cuts.append(dijet_cut)
QCDMuonControlRegion.cuts.append(muonjet_cut)
QCDMuonControlRegion.cuts.append(muon_inverted_iso_cut)

##############################################################

QCDElectronControlRegion = cms.PSet(
    name = cms.string("QCDElectronControlRegion"),
# still need to choose an optimal trigger
#    triggers = cms.vstring("HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v"),
    cuts = cms.VPSet ()
)

QCDElectronControlRegion.cuts.extend(electron_basic_selection_cuts)
QCDElectronControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDElectronControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDElectronControlRegion.cuts.append(bjet_csvl_cut)
QCDElectronControlRegion.cuts.append(dijet_cut)
QCDElectronControlRegion.cuts.append(electronjet_cut)

