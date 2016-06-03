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
    #Using tight lepton veto jet ID. https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID#Recommendations_for_13_TeV_data 
    cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("neutralHadronEnergyFraction < 0.90 & chargedEmEnergyFraction < 0.90 & neutralEmEnergyFraction < 0.90 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0 & muonEnergyFraction < 0.8"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string('tight lepton veto jet ID')
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
    #Using tight lepton veto jet ID. https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID#Recommendations_for_13_TeV_data 
    cms.PSet (
        inputCollection = cms.vstring("bjets"),
        cutString = cms.string("neutralHadronEnergyFraction < 0.90 & chargedEmEnergyFraction < 0.90 & neutralEmEnergyFraction < 0.90 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0 & muonEnergyFraction < 0.8"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string('tight lepton veto bjet ID')
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
        #Tight muon ID with dxy dz removed.
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
        #Using tight lepton veto jet ID. https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID#Recommendations_for_13_TeV_data 
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("neutralHadronEnergyFraction < 0.90 & chargedEmEnergyFraction < 0.90 & neutralEmEnergyFraction < 0.90 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0 & muonEnergyFraction < 0.8"),
            numberRequired = cms.string(">= 2"),
            alias = cms.string('tight lepton veto jet ID')
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
        #Tight Electron ID with dxy dz removed.
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
            cutString = cms.string("neutralHadronEnergyFraction < 0.90 & chargedEmEnergyFraction < 0.90 & neutralEmEnergyFraction < 0.90 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0 & muonEnergyFraction < 0.8"),
            numberRequired = cms.string(">= 2"),
            alias = cms.string('tight lepton veto jet ID')
        ),
    )
)


##############################################################
############# extra cuts for the control region ##############
##############################################################
#Cuts on bjets
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
    arbitration = cms.string("random"),
)
# CSV T working point
bjet_csvt_cut = cms.PSet (
    inputCollection = cms.vstring("bjets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.935"),
    numberRequired = cms.string(">= 1"),
    arbitration = cms.string("random"),
)
#Cuts on bjets
# CSV L working point
jet_csvl_cut = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.460"),
    numberRequired = cms.string(">= 1"),
)
# CSV M working point
jet_csvm_cut = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.800"),
    numberRequired = cms.string(">= 1"),
)
# CSV T working point
jet_csvt_cut = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.935"),
    numberRequired = cms.string(">= 1"),
)
#Extra CSV cuts on jets to select special type of events
jet_csvl_inverted_cut = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags < 0.460"),
    numberRequired = cms.string(">= 1"),
)
jet_light_flavor_veto_cut = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.200"),
    numberRequired = cms.string(">= 1"),
)

jet_csvl_inverted_cut = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags < 0.460"),
    numberRequired = cms.string(">= 1"),
)
#Pileup jets peak ar low end
jet_PuId_cut = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pileupJetId >= 0.9"),
    numberRequired = cms.string(">= 1"),
)
#Topology cuts
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
#Only select bjets not close to the muons
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
#Only select bjets not close to the electron
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
#Extra lepton veto
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

######################################################################
################  basic bb + non-iso muon selection   ################
######################################################################
QCDMuonControlRegion = cms.PSet(
    name = cms.string("QCDMuonControlRegion"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)
QCDMuonControlRegion.cuts.extend(muon_basic_selection_cuts)
QCDMuonControlRegion.cuts.append(muon_inverted_iso_corr_cut)
QCDMuonControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDMuonControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDMuonControlRegion.cuts.append(bjet_csvm_cut)
QCDMuonControlRegion.cuts.append(dijet_cut)
QCDMuonControlRegion.cuts.append(muonjet_cut)
QCDMuonControlRegion.cuts.append(muon_veto_cut)
for cut in QCDMuonControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

##########################################################################
################   bb + non-iso displaced muon selection   ###############
##########################################################################

QCDMuonDisplacedControlRegion = cms.PSet(
    name = cms.string("QCDMuonDisplacedControlRegion"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)
QCDMuonDisplacedControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDMuonControlRegion.cuts))
QCDMuonDisplacedControlRegion.cuts.insert(5,muon_dxy_cut)

##########################################################################
################     bb  +  iso displaced muon selection   ###############
##########################################################################

QCDMuonIsoControlRegion = cms.PSet(
    name = cms.string("QCDMuonIsoControlRegion"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)
QCDMuonIsoControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDMuonDisplacedControlRegion.cuts))
for cut in QCDMuonIsoControlRegion.cuts:
    if "pfdBetaIsoCorr" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pfdBetaIsoCorr <= 0.15")
        cut.alias = cms.string("muon isolation corrected")

###################################################################################
################bb + iso displaced muon selection with various B WP ###############
###################################################################################

QCDMuonIsoTightBControlRegion = cms.PSet(
    name = cms.string("QCDMuonIsoTightBControlRegion"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)
QCDMuonIsoTightBControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDMuonIsoControlRegion.cuts))
QCDMuonIsoTightBControlRegion.cuts.insert(9,jet_csvt_cut)

QCDMuonIsoMediumBControlRegion = cms.PSet(
    name = cms.string("QCDMuonIsoMediumBControlRegion"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)
QCDMuonIsoMediumBControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDMuonIsoControlRegion.cuts))
QCDMuonIsoMediumBControlRegion.cuts.insert(9,jet_csvm_cut)

QCDMuonIsoLooseBControlRegion = cms.PSet(
    name = cms.string("QCDMuonIsoLooseBControlRegion"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)
QCDMuonIsoLooseBControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDMuonIsoControlRegion.cuts))
QCDMuonIsoLooseBControlRegion.cuts.insert(9,jet_csvl_cut)


######################################################################
################  basic bb + no-iso muon selection    ################
######################################################################

QCDMuonNoIsoDisplacedControlRegion = cms.PSet(
    name = cms.string("QCDMuonNoIsoDisplacedControlRegion"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)
QCDMuonNoIsoDisplacedControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDMuonDisplacedControlRegion.cuts))
for cut in QCDMuonNoIsoDisplacedControlRegion.cuts:
    if "pfdBetaIsoCorr" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        QCDMuonNoIsoDisplacedControlRegion.cuts.remove(cut)

#######################################################################################
################bb + non-iso displaced muon selection with various B WP ###############
#######################################################################################

QCDMuonDisplacedControlRegionTightB = cms.PSet(
    name = cms.string("QCDMuonDisplacedControlRegionTightB"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)

QCDMuonDisplacedControlRegionTightB.cuts = cms.VPSet (copy.deepcopy(QCDMuonDisplacedControlRegion.cuts))
for cut in QCDMuonDisplacedControlRegionTightB.cuts:
    if "pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.800" in str(cut.cutString) and "jets" in str(cut.inputCollection):
        cut.cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.935")

QCDMuonDisplacedControlRegionLooseB = cms.PSet(
    name = cms.string("QCDMuonDisplacedControlRegionLooseB"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)
QCDMuonDisplacedControlRegionLooseB.cuts = cms.VPSet (copy.deepcopy(QCDMuonDisplacedControlRegion.cuts))
for cut in QCDMuonDisplacedControlRegionLooseB.cuts:
    if "pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.800" in str(cut.cutString) and "bjets" in str(cut.inputCollection):
        cut.cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.460")

######################################################################
################  basic bb + non-iso ele selection    ################
######################################################################

QCDElectronControlRegion = cms.PSet(
    name = cms.string("QCDElectronControlRegion"),
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
    cuts = cms.VPSet ()
)

QCDElectronControlRegion.cuts.extend(electron_basic_selection_cuts)
QCDElectronControlRegion.cuts.append(electron_inverted_iso_corr_cut)
QCDElectronControlRegion.cuts.extend(jet_basic_selection_cuts)
QCDElectronControlRegion.cuts.extend(bjet_basic_selection_cuts)
QCDElectronControlRegion.cuts.append(bjet_csvt_cut)
QCDElectronControlRegion.cuts.append(dijet_cut)
QCDElectronControlRegion.cuts.append(electronjet_cut)
QCDElectronControlRegion.cuts.append(electron_veto_cut)
for cut in QCDElectronControlRegion.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > -1" in str(cut.cutString) and "jets" in str(cut.inputCollection):
        QCDElectronControlRegion.cuts.remove(cut)

##################################################################################
################  basic bb + non-iso displaced ele selection      ################
##################################################################################

QCDElectronDisplacedControlRegion = cms.PSet(
    name = cms.string("QCDElectronDisplacedControlRegion"),
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
    cuts = cms.VPSet ()
)
QCDElectronDisplacedControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDElectronControlRegion.cuts))
QCDElectronDisplacedControlRegion.cuts.insert(5,electron_dxy_cut)

###############################################################################
################  basic bb + iso displaced ele selection      ################
###############################################################################

QCDElectronIsoControlRegion = cms.PSet(
    name = cms.string("QCDElectronIsoControlRegion"),
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
    cuts = cms.VPSet ()
)
QCDElectronIsoControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDElectronDisplacedControlRegion.cuts))
for cut in QCDElectronIsoControlRegion.cuts:
    if "pfdRhoIsoCorr" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("(pfdRhoIsoCorr <= 0.0646 && isEE) | \
        (pfdRhoIsoCorr <= 0.0354  && isEB)")
        cut.alias = cms.string("electron isolation corrected")

###############################################################################
################  basic bb + iso displaced ele selection various B WP #########
###############################################################################

QCDElectronIsoTightBControlRegion = cms.PSet(
    name = cms.string("QCDElectronIsoTightBControlRegion"),
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
    cuts = cms.VPSet ()
)

QCDElectronIsoTightBControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDElectronIsoControlRegion.cuts))
QCDElectronIsoTightBControlRegion.cuts.insert(9,jet_csvt_cut)

QCDElectronIsoMediumBControlRegion = cms.PSet(
    name = cms.string("QCDElectronIsoMediumBControlRegion"),
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
    cuts = cms.VPSet ()
)

QCDElectronIsoMediumBControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDElectronIsoControlRegion.cuts))
QCDElectronIsoMediumBControlRegion.cuts.insert(9,jet_csvm_cut)

QCDElectronIsoLooseBControlRegion = cms.PSet(
    name = cms.string("QCDElectronIsoLooseBControlRegion"),
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
    cuts = cms.VPSet ()
)

QCDElectronIsoLooseBControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDElectronIsoControlRegion.cuts))
QCDElectronIsoLooseBControlRegion.cuts.insert(9,jet_csvl_cut)

###################################################################################
################  basic bb + non-iso displaced ele selection various B WP #########
###################################################################################

QCDElectronDisplacedControlRegionMediumB = cms.PSet(
    name = cms.string("QCDElectronDisplacedControlRegionMediumB"),
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
    cuts = cms.VPSet ()
)

QCDElectronDisplacedControlRegionMediumB.cuts = cms.VPSet (copy.deepcopy(QCDElectronDisplacedControlRegion.cuts))
for cut in QCDElectronDisplacedControlRegionMediumB.cuts:
    if "pfCombinedInclusiveSecondaryVertexV2BJetTags" in str(cut.cutString) and "bjets" in str(cut.inputCollection):
        cut.cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.800")

QCDElectronDisplacedControlRegionLooseB = cms.PSet(
    name = cms.string("QCDElectronDisplacedControlRegionLooseB"),
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
    cuts = cms.VPSet ()
)

QCDElectronDisplacedControlRegionLooseB.cuts = cms.VPSet (copy.deepcopy(QCDElectronDisplacedControlRegion.cuts))
for cut in QCDElectronDisplacedControlRegionLooseB.cuts:
    if "pfCombinedInclusiveSecondaryVertexV2BJetTags" in str(cut.cutString) and "bjets" in str(cut.inputCollection):
        cut.cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.460")

##################################################################################
################  basic bb + iso ele selection(no trigger)        ################
##################################################################################

QCDElectronNoTriggerControlRegion = cms.PSet(
    name = cms.string("QCDElectronNoTriggerControlRegion"),
    #triggers = cms.vstring("HLT_Photon90_v","HLT_Photon120_v","HLT_Photon175_v","HLT_Photon165_HE10_v","HLT_Photon22_R9Id90_HE10_IsoM_v","HLT_Photon30_R9Id90_HE10_IsoM_v","HLT_Photon36_R9Id90_HE10_IsoM_v","HLT_Photon50_R9Id90_HE10_IsoM_v","HLT_Photon75_R9Id90_HE10_IsoM_v","HLT_Photon90_R9Id90_HE10_IsoM_v","HLT_Photon120_R9Id90_HE10_IsoM_v","HLT_Photon165_R9Id90_HE10_IsoM_v","HLT_Photon90_CaloIdL_PFHT500_v","HLT_Photon90_CaloIdL_PFHT600_v","HLT_Photon500_v","HLT_Photon600_v","HLT_Photon135_PFMET100_v","HLT_Photon250_NoHE_v","HLT_Photon300_NoHE_v","HLT_Photon22_v","HLT_Photon30_v","HLT_Photon36_v","HLT_Photon50_v","HLT_Photon75_v"),
    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)

QCDElectronNoTriggerControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDElectronControlRegion.cuts))
QCDElectronNoTriggerControlRegion.cuts.triggers = cms.vstring() 


QCDElectronDisplacedNoTriggerControlRegion = cms.PSet(
    name = cms.string("QCDElectronDisplacedNoTriggerControlRegion"),
    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)
QCDElectronDisplacedNoTriggerControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDElectronDisplacedControlRegion.cuts))
QCDElectronDisplacedNoTriggerControlRegion.triggers = cms.vstring()

########################################################################################
################  basic bb + no-iso displaced ele selection(no trigger) ################
########################################################################################

QCDElectronNoIsoDisplacedControlRegion = cms.PSet(
    name = cms.string("QCDElectronNoIsoDisplacedControlRegion"),
    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
    cuts = cms.VPSet ()
)
QCDElectronNoIsoDisplacedControlRegion.cuts = cms.VPSet (copy.deepcopy(QCDElectronDisplacedControlRegion.cuts))
for cut in QCDElectronNoIsoDisplacedControlRegion.cuts:
    if "pfdRhoIsoCorr" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        QCDElectronNoIsoDisplacedControlRegion.cuts.remove(cut)
