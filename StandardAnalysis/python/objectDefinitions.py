import FWCore.ParameterSet.Config as cms
import copy
import string
import os
from OSUT3Analysis.Configuration.cutUtilities import *

### This file contains the official POG  object definitions, for use in object selection


### BEGIN OBJECT ISOLATION DEFINITIONS

##########################################################################

# TIGHT ELECTRON ISOLATION
# taken from here: https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2
# now included in versioned ID in OSUT3Analysis

##########################################################################

# TIGHT MUON ISOLATION

# taken from here: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Isolation
# pfdBetaIsoCorr -> isolation variables recalculated wrt the closest PV to the electron
# calculation found here: https://github.com/OSU-CMS/OSUT3Analysis/blob/master/Collections/plugins/OSUMuonProducer.cc#L124
# muon isolation is so far the same for 2016 and 2017 data

muon_iso_cutstring = cutString = cms.string("pfdBetaIsoCorr <= 0.15")

muon_iso_alias = cms.string(">=1 muons with tight isolation")

##########################################################################

# INVERTED TIGHT MUON ISOLATION

muon_antiiso_cutstring = cutString = cms.string("pfdBetaIsoCorr > 0.15")

muon_antiiso_alias = cms.string(">=1 muons with inverted tight isolation")

##########################################################################

# INVERTED LOOSE MUON ISOLATION

muon_loose_antiiso_cutstring = cutString = cms.string("pfdBetaIsoCorr > 0.25")

muon_loose_antiiso_alias = cms.string(">=1 muons with inverted loose isolation")

##########################################################################






### BEGIN OBJECT IDENTIFICATION DEFINITIONS

##########################################################################

# JET ID AGAINST LEPTONS (tight lepton veto)

# N.B.: JET ID VALID FOR ETA < 2.4

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
# taken from here: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID13TeVRun2017
    jet_id_cutstring = cms.string("neutralHadronEnergyFraction < 0.90 & \
                                              chargedEmEnergyFraction < 0.80 & \
                                              neutralEmEnergyFraction < 0.90 & \
                                              numberOfDaughters > 1 & \
                                              chargedHadronEnergyFraction > 0.0 & \
                                              chargedMultiplicity > 0.0 & \
                                              muonEnergyFraction < 0.8")
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
# taken from here: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID13TeVRun2016
    jet_id_cutstring = cms.string("neutralHadronEnergyFraction < 0.90 & \
                                              chargedEmEnergyFraction < 0.90 & \
                                              neutralEmEnergyFraction < 0.90 & \
                                              numberOfDaughters > 1 & \
                                              chargedHadronEnergyFraction > 0.0 & \
                                              chargedMultiplicity > 0.0 & \
                                              muonEnergyFraction < 0.8")

jet_id_alias = cms.string(">=0 jets with ID against leptons")

jet_loose_id_cutstring = cms.string("neutralHadronEnergyFraction < 0.99 & \
                                              chargedEmEnergyFraction < 0.99 & \
                                              neutralEmEnergyFraction < 0.99 & \
                                              numberOfDaughters > 1 & \
                                              chargedHadronEnergyFraction > 0.0 & \
                                              chargedMultiplicity > 0.0")

jet_loose_id_alias = cms.string("loose Jet ID")

jet_ttbar_paper_loose_id_cutstring = cms.string("neutralHadronEnergyFraction < 0.99 & \
                                              chargedEmEnergyFraction < 0.99 & \
                                              neutralEmEnergyFraction < 0.99 & \
                                              chargedHadronEnergyFraction > 0.0")

jet_ttbar_paper_loose_id_alias = cms.string("loose jet ID from ttbar paper")

##########################################################################
#B-JET CombinedSecondaryVertexv2 
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
    btag_tightCSVv2_cutstring = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.9693")

    btag_mediumCSVv2_cutstring = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.8838")

    btag_looseCSVv2_cutstring = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.5803")

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
    btag_tightCSVv2_cutstring = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.9535")

    btag_mediumCSVv2_cutstring = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.8484")

    btag_looseCSVv2_cutstring = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.5426")


##########################################################################

# TIGHT ELECTRON ID
# without impact parameter cuts
# taken from here: https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2
# now included in versioned ID

##########################################################################

# ELECTRON ID IMPACT PARAMETER CUTS 
# impact parameter cuts are the same in 2016 and 2017

electron_id_impact_parameter_cutstring = cms.string("(isEB & \
                                             abs("+electronD0WRTPV+") < 0.05 & \
                                             abs("+electronDZWRTPV+") < 0.10) | \
                                             (isEE & \
                                             abs("+electronD0WRTPV+") < 0.10 & \
                                             abs("+electronDZWRTPV+") < 0.20)")

electron_id_impact_parameter_alias = cms.string(">=1 electrons with tight ID impact parameter cuts")


##########################################################################

# TIGHT MUON ID, part one
# done separately because some other cuts access members that only exist for global muons
# tight muon ID is so far the same for 2016 and 2017 data

muon_global_cutstring = cms.string("isGlobalMuon & isPFMuon")

muon_global_alias = cms.string(">=1 global PF muons")

##########################################################################

# TIGHT MUON ID, part two
# taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideMuonIdRun2#Tight_Muon
# we don't include d0/dz inside the ID so that we can control it more explicitly

muon_id_cutstring = cms.string("globalTrack.normalizedChi2 < 10 & \
                                globalTrack.hitPattern_.numberOfValidMuonHits > 0 & \
                                numberOfMatchedStations > 1 & \
                                innerTrack.hitPattern_.numberOfValidPixelHits > 0 & \
                                innerTrack.hitPattern_.trackerLayersWithMeasurement > 5")

muon_id_alias = cms.string(">=1 muons with tight ID")

##########################################################################

# MUON ID IMPACT PARAMETER CUTS

muon_id_impact_parameter_cutstring = cms.string("abs("+muonD0WRTPV+") < 0.2 & \
                                                 abs("+muonDZWRTPV+") < 0.5")

muon_id_impact_parameter_alias = cms.string(">=1 muons with tight ID impact parameter cuts")

