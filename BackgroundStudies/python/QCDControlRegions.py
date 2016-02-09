import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.CutDefinitions import *

##############################################################
##### EVENT SELECTIONS FOR OUR QCD B-BBAR CONTROL REGIONS ####
##############################################################
jet_basic_selection_cuts = cms.VPSet(
    cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 1")
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
)

bjet_basic_selection_cuts = cms.VPSet(
    cms.PSet (
        inputCollection = cms.vstring("bjets"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 1")
    ),
    cms.PSet (
        inputCollection = cms.vstring("bjets"),
        cutString = cms.string("pt > 30"),
        numberRequired = cms.string(">= 1")
    ),
    cms.PSet (
        inputCollection = cms.vstring("bjets"),
        cutString = cms.string("neutralHadronEnergyFraction < 0.99 & chargedEmEnergyFraction < 0.99 & neutralEmEnergyFraction < 0.99 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string('bjet ID')
    ),
)

QCDMuonSkim = cms.PSet(
    name = cms.string("QCDMuonSkim"),
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > 20"),
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
            numberRequired = cms.string(">= 2"),
        ),
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("pt > 30"),
            numberRequired = cms.string(">= 2")
        ),
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("neutralHadronEnergyFraction < 0.99 & chargedEmEnergyFraction < 0.99 & neutralEmEnergyFraction < 0.99 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0"),
            numberRequired = cms.string(">= 2"),
            alias = cms.string('jet ID')
        ),
    )
)

##############################################################


QCDElectronSkim = cms.PSet(
    name = cms.string("QCDElectronSkim"),
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > 20"),
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
            numberRequired = cms.string(">= 2"),
        ),
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("pt > 30"),
            numberRequired = cms.string(">= 2")
        ),
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("neutralHadronEnergyFraction < 0.99 & chargedEmEnergyFraction < 0.99 & neutralEmEnergyFraction < 0.99 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0"),
            numberRequired = cms.string(">= 2"),
            alias = cms.string('jet ID')
        ),
        # loose CSV working point for run 2
        #cms.PSet (
        #    inputCollection = cms.vstring("jets"),
        #    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.605"),
        #    numberRequired = cms.string(">= 1"),
        #),
    )
)


##############################################################
# extra cuts for the control region

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
jet_csv_ranking_cut = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 1"),
    arbitration = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags"), 
    alias = cms.string("leading CSV jet"),
)

muon_veto_cut = cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("leading muon"),
)

electron_veto_cut = cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("leading electron"),
)

##############################################################

QCDMuonControlRegion = cms.PSet(
    name = cms.string("QCDMuonControlRegion"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)

QCDMuonControlRegion.cuts.extend(muon_basic_selection_cuts)
QCDMuonControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDMuonControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDMuonControlRegion.cuts.append(bjet_csvm_cut)
QCDMuonControlRegion.cuts.append(dijet_cut)
QCDMuonControlRegion.cuts.append(muonjet_cut)
QCDMuonControlRegion.cuts.append(jet_csv_ranking_cut)
QCDMuonControlRegion.cuts.append(muon_inverted_iso_cut)
QCDMuonControlRegion.cuts.append(muon_veto_cut)
for cut in QCDMuonControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

##############################################################

QCDElectronControlRegion = cms.PSet(
    name = cms.string("QCDElectronControlRegion"),
# still need to choose an optimal trigger
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
#    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)

QCDElectronControlRegion.cuts.extend(electron_basic_selection_cuts)
QCDElectronControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDElectronControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDElectronControlRegion.cuts.append(bjet_csvm_cut)
QCDElectronControlRegion.cuts.append(dijet_cut)
QCDElectronControlRegion.cuts.append(electronjet_cut)
QCDElectronControlRegion.cuts.append(jet_csv_ranking_cut)
QCDElectronControlRegion.cuts.append(electron_inverted_iso_cut)
QCDElectronControlRegion.cuts.append(electron_veto_cut)
# pT threshold should be determined by the trigger
for cut in QCDElectronControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")

