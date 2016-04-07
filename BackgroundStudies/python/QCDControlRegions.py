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
        cutString = cms.string("matchedToLepton < 1 "),
        numberRequired = cms.string(">= 1")
    ),
    cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("neutralHadronEnergyFraction < 0.99 & chargedEmEnergyFraction < 0.99 & neutralEmEnergyFraction < 0.99 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string('loose bjet ID')
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
        alias = cms.string('loose bjet ID')
    ),
)

QCDMuonSkim = cms.PSet(
    name = cms.string("QCDMuonSkim"),
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > 30"),
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
            alias = cms.string('loose jet ID')
        ),
    )
)

##############################################################


QCDElectronSkim = cms.PSet(
    name = cms.string("QCDElectronSkim"),
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > 30"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("abs(eta) < 2.5"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("\
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
    )
)


##############################################################
# extra cuts for the control region

# CSV L working point
bjet_csvl_cut = cms.PSet (
    inputCollection = cms.vstring("bjets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.460"),
    numberRequired = cms.string(">= 1"),
)
# CSV M working point
bjet_csvm_cut = cms.PSet (
    inputCollection = cms.vstring("bjets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.800"),
    numberRequired = cms.string(">= 1"),
)
bjet_csvt_cut = cms.PSet (
    inputCollection = cms.vstring("bjets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.935"),
    numberRequired = cms.string(">= 1"),
)
jet_csvl_cut = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.460"),
    numberRequired = cms.string(">= 1"),
)
jet_csvl_inverted_cut = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags < 0.460"),
    numberRequired = cms.string(">= 1"),
)
dijet_cut = cms.PSet (
    inputCollection = cms.vstring("jets","bjets"),
    cutString = cms.string("abs(deltaPhi(jet,bjet)) > 2.5"),
    numberRequired = cms.string(">= 1"),
)
muonjet_cut = cms.PSet (
    inputCollection = cms.vstring("muons","jets"),
    cutString = cms.string("deltaR(muon,jet) < 0.5"),
    numberRequired = cms.string(">= 1"),
)
muonjet_veto_cut = cms.PSet (
    inputCollection = cms.vstring("muons","jets"),
    cutString = cms.string("deltaR(muon,jet) < 0.5"),
    numberRequired = cms.string("== 0"),
)
muonbjet_cut = cms.PSet (
    inputCollection = cms.vstring("muons","bjets"),
    cutString = cms.string("deltaR(muon,bjet) > 0.5"),
    numberRequired = cms.string(">= -1"),
)
electronjet_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","jets"),
    cutString = cms.string("deltaR(electron,jet) < 0.5"),
    numberRequired = cms.string(">= 1"),
)
electronjet_veto_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","jets"),
    cutString = cms.string("deltaR(electron,jet) < 0.5"),
    numberRequired = cms.string("== 0"),
)
electronjet_ptdiff_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","jets"),
    cutString = cms.string("abs(electron.pt - jet.pt) > 10"),
    numberRequired = cms.string(">= 1"),
)
electron_dxy_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) > 0.01 "),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron dxy > 0.01 cm")
)
muon_dxy_cut = cms.PSet (
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) > 0.01 "),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon dxy > 0.01 cm")
)
muonjet_ptdiff_cut = cms.PSet (
    inputCollection = cms.vstring("muons","jets"),
    cutString = cms.string("abs(muon.pt - jet.pt) > 10"),
    numberRequired = cms.string(">= 1"),
)
electronbjet_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","bjets"),
    cutString = cms.string("deltaR(electron,bjet) > 0.5"),
    numberRequired = cms.string(">= -1"),
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
        alias = cms.string("extra muon veto"),
)

electron_veto_cut = cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto"),
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
QCDMuonControlRegion.cuts.append(muon_inverted_iso_corr_cut)
QCDMuonControlRegion.cuts.append(muon_veto_cut)
QCDMuonControlRegion.cuts.append(muonbjet_cut)
for cut in QCDMuonControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

QCDMuonIsoControlRegion = cms.PSet(
    name = cms.string("QCDMuonIsoControlRegion"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)

QCDMuonIsoControlRegion.cuts.extend(muon_basic_selection_cuts)
QCDMuonIsoControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDMuonIsoControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDMuonIsoControlRegion.cuts.append(bjet_csvm_cut)
QCDMuonIsoControlRegion.cuts.append(dijet_cut)
QCDMuonIsoControlRegion.cuts.append(muonjet_cut)
QCDMuonIsoControlRegion.cuts.append(muon_dxy_cut)
QCDMuonIsoControlRegion.cuts.append(jet_csv_ranking_cut)
QCDMuonIsoControlRegion.cuts.append(muon_iso_corr_cut)
QCDMuonIsoControlRegion.cuts.append(muon_veto_cut)
QCDMuonIsoControlRegion.cuts.append(muonbjet_cut)
for cut in QCDMuonIsoControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

QCDMuonNoIsoDisplacedControlRegion = cms.PSet(
    name = cms.string("QCDMuonNoIsoDisplacedControlRegion"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)

QCDMuonNoIsoDisplacedControlRegion.cuts.extend(muon_basic_selection_cuts)
QCDMuonNoIsoDisplacedControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDMuonNoIsoDisplacedControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDMuonNoIsoDisplacedControlRegion.cuts.append(bjet_csvm_cut)
QCDMuonNoIsoDisplacedControlRegion.cuts.append(dijet_cut)
QCDMuonNoIsoDisplacedControlRegion.cuts.append(muonjet_cut)
QCDMuonNoIsoDisplacedControlRegion.cuts.append(muon_dxy_cut)
QCDMuonNoIsoDisplacedControlRegion.cuts.append(jet_csv_ranking_cut)
QCDMuonNoIsoDisplacedControlRegion.cuts.append(muon_loose_iso_corr_cut)
QCDMuonNoIsoDisplacedControlRegion.cuts.append(muon_veto_cut)
QCDMuonNoIsoDisplacedControlRegion.cuts.append(muonbjet_cut)
for cut in QCDMuonNoIsoDisplacedControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")


QCDMuonDisplacedControlRegion = cms.PSet(
    name = cms.string("QCDMuonDisplacedControlRegion"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)

QCDMuonDisplacedControlRegion.cuts.extend(muon_basic_selection_cuts)
QCDMuonDisplacedControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDMuonDisplacedControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDMuonDisplacedControlRegion.cuts.append(bjet_csvm_cut)
QCDMuonDisplacedControlRegion.cuts.append(dijet_cut)
QCDMuonDisplacedControlRegion.cuts.append(muonjet_cut)
QCDMuonDisplacedControlRegion.cuts.append(muon_dxy_cut)
QCDMuonDisplacedControlRegion.cuts.append(jet_csv_ranking_cut)
QCDMuonDisplacedControlRegion.cuts.append(muon_inverted_iso_corr_cut)
QCDMuonDisplacedControlRegion.cuts.append(muon_veto_cut)
QCDMuonDisplacedControlRegion.cuts.append(muonbjet_cut)
for cut in QCDMuonDisplacedControlRegion.cuts:
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
QCDElectronControlRegion.cuts.append(bjet_csvt_cut)
QCDElectronControlRegion.cuts.append(dijet_cut)
QCDElectronControlRegion.cuts.append(electronjet_cut)
QCDElectronControlRegion.cuts.append(jet_csv_ranking_cut)
QCDElectronControlRegion.cuts.append(electron_inverted_iso_corr_cut)
QCDElectronControlRegion.cuts.append(electron_veto_cut)
QCDElectronControlRegion.cuts.append(electronbjet_cut)
# pT threshold should be determined by the trigger
for cut in QCDElectronControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")

QCDElectronNoTriggerControlRegion = cms.PSet(
    name = cms.string("QCDElectronNoTriggerControlRegion"),
# still need to choose an optimal trigger
    #triggers = cms.vstring("HLT_Photon90_v","HLT_Photon120_v","HLT_Photon175_v","HLT_Photon165_HE10_v","HLT_Photon22_R9Id90_HE10_IsoM_v","HLT_Photon30_R9Id90_HE10_IsoM_v","HLT_Photon36_R9Id90_HE10_IsoM_v","HLT_Photon50_R9Id90_HE10_IsoM_v","HLT_Photon75_R9Id90_HE10_IsoM_v","HLT_Photon90_R9Id90_HE10_IsoM_v","HLT_Photon120_R9Id90_HE10_IsoM_v","HLT_Photon165_R9Id90_HE10_IsoM_v","HLT_Photon90_CaloIdL_PFHT500_v","HLT_Photon90_CaloIdL_PFHT600_v","HLT_Photon500_v","HLT_Photon600_v","HLT_Photon135_PFMET100_v","HLT_Photon250_NoHE_v","HLT_Photon300_NoHE_v","HLT_Photon22_v","HLT_Photon30_v","HLT_Photon36_v","HLT_Photon50_v","HLT_Photon75_v"),
    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)

QCDElectronNoTriggerControlRegion.cuts.extend(electron_basic_selection_cuts)
QCDElectronNoTriggerControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDElectronNoTriggerControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDElectronNoTriggerControlRegion.cuts.append(bjet_csvt_cut)
QCDElectronNoTriggerControlRegion.cuts.append(dijet_cut)
QCDElectronNoTriggerControlRegion.cuts.append(electronjet_cut)
QCDElectronNoTriggerControlRegion.cuts.append(jet_csv_ranking_cut)
QCDElectronNoTriggerControlRegion.cuts.append(electron_inverted_iso_corr_cut)
QCDElectronNoTriggerControlRegion.cuts.append(electron_veto_cut)
QCDElectronNoTriggerControlRegion.cuts.append(electronbjet_cut)
# pT threshold should be determined by the trigger
for cut in QCDElectronNoTriggerControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")

QCDElectronEBControlRegion = cms.PSet(
    name = cms.string("QCDElectronEBControlRegion"),
# still need to choose an optimal trigger
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
#    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)

QCDElectronEBControlRegion.cuts.extend(electron_basic_selection_eb_cuts)
QCDElectronEBControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDElectronEBControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDElectronEBControlRegion.cuts.append(bjet_csvt_cut)
QCDElectronEBControlRegion.cuts.append(dijet_cut)
QCDElectronEBControlRegion.cuts.append(electronjet_cut)
QCDElectronEBControlRegion.cuts.append(jet_csv_ranking_cut)
QCDElectronEBControlRegion.cuts.append(electron_inverted_iso_corr_cut)
QCDElectronEBControlRegion.cuts.append(electron_veto_cut)
QCDElectronEBControlRegion.cuts.append(electronbjet_cut)
# pT threshold should be determined by the trigger
for cut in QCDElectronEBControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")

QCDElectronEEControlRegion = cms.PSet(
    name = cms.string("QCDElectronEEControlRegion"),
# still need to choose an optimal trigger
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
#    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)

QCDElectronEEControlRegion.cuts.extend(electron_basic_selection_ee_cuts)
QCDElectronEEControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDElectronEEControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDElectronEEControlRegion.cuts.append(bjet_csvt_cut)
QCDElectronEEControlRegion.cuts.append(dijet_cut)
QCDElectronEEControlRegion.cuts.append(electronjet_cut)
QCDElectronEEControlRegion.cuts.append(jet_csv_ranking_cut)
QCDElectronEEControlRegion.cuts.append(electron_inverted_iso_corr_cut)
QCDElectronEEControlRegion.cuts.append(electron_veto_cut)
QCDElectronEEControlRegion.cuts.append(electronbjet_cut)
# pT threshold should be determined by the trigger
for cut in QCDElectronEEControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")

QCDElectronLFControlRegion = cms.PSet(
    name = cms.string("QCDElectronLFControlRegion"),
# still need to choose an optimal trigger
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
#    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)

QCDElectronLFControlRegion.cuts.extend(electron_basic_selection_cuts)
QCDElectronLFControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDElectronLFControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDElectronLFControlRegion.cuts.append(bjet_csvt_cut)
QCDElectronLFControlRegion.cuts.append(dijet_cut)
QCDElectronLFControlRegion.cuts.append(electronjet_cut)
QCDElectronLFControlRegion.cuts.append(jet_csvl_inverted_cut)
QCDElectronLFControlRegion.cuts.append(electron_inverted_iso_corr_cut)
QCDElectronLFControlRegion.cuts.append(electron_veto_cut)
QCDElectronLFControlRegion.cuts.append(electronbjet_cut)
# pT threshold should be determined by the trigger
for cut in QCDElectronLFControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")

QCDElectronHFControlRegion = cms.PSet(
    name = cms.string("QCDElectronHFControlRegion"),
# still need to choose an optimal trigger
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
#    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)

QCDElectronHFControlRegion.cuts.extend(electron_basic_selection_cuts)
QCDElectronHFControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDElectronHFControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDElectronHFControlRegion.cuts.append(bjet_csvt_cut)
QCDElectronHFControlRegion.cuts.append(dijet_cut)
QCDElectronHFControlRegion.cuts.append(electronjet_cut)
QCDElectronHFControlRegion.cuts.append(jet_csvl_cut)
QCDElectronHFControlRegion.cuts.append(electron_inverted_iso_corr_cut)
QCDElectronHFControlRegion.cuts.append(electron_veto_cut)
QCDElectronHFControlRegion.cuts.append(electronbjet_cut)
# pT threshold should be determined by the trigger
for cut in QCDElectronHFControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")

QCDElectronIsoControlRegion = cms.PSet(
    name = cms.string("QCDElectronIsoControlRegion"),
# still need to choose an optimal trigger
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
#    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)

QCDElectronIsoControlRegion.cuts.extend(electron_basic_selection_cuts)
QCDElectronIsoControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDElectronIsoControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDElectronIsoControlRegion.cuts.append(bjet_csvt_cut)
QCDElectronIsoControlRegion.cuts.append(dijet_cut)
QCDElectronIsoControlRegion.cuts.append(electronjet_cut)
QCDElectronIsoControlRegion.cuts.append(jet_csv_ranking_cut)
QCDElectronIsoControlRegion.cuts.append(electron_iso_corr_cut)
QCDElectronIsoControlRegion.cuts.append(electron_dxy_cut)
QCDElectronIsoControlRegion.cuts.append(electron_veto_cut)
QCDElectronIsoControlRegion.cuts.append(electronbjet_cut)
# pT threshold should be determined by the trigger
for cut in QCDElectronIsoControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")

QCDElectronIsoJetVetoControlRegion = cms.PSet(
    name = cms.string("QCDElectronIsoJetVetoControlRegion"),
# still need to choose an optimal trigger
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
#    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)

QCDElectronIsoJetVetoControlRegion.cuts.extend(electron_basic_selection_cuts)
QCDElectronIsoJetVetoControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDElectronIsoJetVetoControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDElectronIsoJetVetoControlRegion.cuts.append(bjet_csvt_cut)
QCDElectronIsoJetVetoControlRegion.cuts.append(dijet_cut)
QCDElectronIsoJetVetoControlRegion.cuts.append(electronjet_veto_cut)
QCDElectronIsoJetVetoControlRegion.cuts.append(jet_csv_ranking_cut)
QCDElectronIsoJetVetoControlRegion.cuts.append(electron_iso_corr_cut)
QCDElectronIsoJetVetoControlRegion.cuts.append(electron_dxy_cut)
QCDElectronIsoJetVetoControlRegion.cuts.append(electron_veto_cut)
QCDElectronIsoJetVetoControlRegion.cuts.append(electronbjet_cut)
# pT threshold should be determined by the trigger
for cut in QCDElectronIsoJetVetoControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")

QCDElectronDisplacedControlRegion = cms.PSet(
    name = cms.string("QCDElectronDisplacedControlRegion"),
# still need to choose an optimal trigger
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
#    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)

QCDElectronDisplacedControlRegion.cuts.extend(electron_basic_selection_cuts)
QCDElectronDisplacedControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDElectronDisplacedControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDElectronDisplacedControlRegion.cuts.append(bjet_csvt_cut)
QCDElectronDisplacedControlRegion.cuts.append(dijet_cut)
QCDElectronDisplacedControlRegion.cuts.append(electronjet_cut)
QCDElectronDisplacedControlRegion.cuts.append(electron_dxy_cut)
QCDElectronDisplacedControlRegion.cuts.append(jet_csv_ranking_cut)
QCDElectronDisplacedControlRegion.cuts.append(electron_inverted_iso_corr_cut)
QCDElectronDisplacedControlRegion.cuts.append(electron_veto_cut)
QCDElectronDisplacedControlRegion.cuts.append(electronbjet_cut)
# pT threshold should be determined by the trigger
for cut in QCDElectronDisplacedControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")

QCDElectronDisplacedNoTriggerControlRegion = cms.PSet(
    name = cms.string("QCDElectronDisplacedNoTriggerControlRegion"),
# still need to choose an optimal trigger
    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)

QCDElectronDisplacedNoTriggerControlRegion.cuts.extend(electron_basic_selection_cuts)
QCDElectronDisplacedNoTriggerControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDElectronDisplacedNoTriggerControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDElectronDisplacedNoTriggerControlRegion.cuts.append(bjet_csvm_cut)
QCDElectronDisplacedNoTriggerControlRegion.cuts.append(dijet_cut)
QCDElectronDisplacedNoTriggerControlRegion.cuts.append(electronjet_cut)
QCDElectronDisplacedNoTriggerControlRegion.cuts.append(electron_dxy_cut)
QCDElectronDisplacedNoTriggerControlRegion.cuts.append(jet_csv_ranking_cut)
QCDElectronDisplacedNoTriggerControlRegion.cuts.append(electron_inverted_iso_corr_cut)
QCDElectronDisplacedNoTriggerControlRegion.cuts.append(electron_veto_cut)
QCDElectronDisplacedNoTriggerControlRegion.cuts.append(electronbjet_cut)
# pT threshold should be determined by the trigger
for cut in QCDElectronDisplacedNoTriggerControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")

QCDElectronNoIsoDisplacedControlRegion = cms.PSet(
    name = cms.string("QCDElectronNoIsoDisplacedControlRegion"),
# still need to choose an optimal trigger
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
    cuts = cms.VPSet ()
)

QCDElectronNoIsoDisplacedControlRegion.cuts.extend(electron_basic_selection_cuts)
QCDElectronNoIsoDisplacedControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDElectronNoIsoDisplacedControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDElectronNoIsoDisplacedControlRegion.cuts.append(bjet_csvt_cut)
QCDElectronNoIsoDisplacedControlRegion.cuts.append(dijet_cut)
QCDElectronNoIsoDisplacedControlRegion.cuts.append(electronjet_cut)
QCDElectronNoIsoDisplacedControlRegion.cuts.append(electron_dxy_cut)
QCDElectronNoIsoDisplacedControlRegion.cuts.append(jet_csv_ranking_cut)
QCDElectronNoIsoDisplacedControlRegion.cuts.append(electron_loose_iso_corr_cut)
QCDElectronNoIsoDisplacedControlRegion.cuts.append(electron_veto_cut)
QCDElectronNoIsoDisplacedControlRegion.cuts.append(electronbjet_cut)
# pT threshold should be determined by the trigger
for cut in QCDElectronNoIsoDisplacedControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
