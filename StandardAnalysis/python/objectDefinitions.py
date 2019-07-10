import FWCore.ParameterSet.Config as cms
import copy
import string
import os
from OSUT3Analysis.Configuration.cutUtilities import *

### This file contains the official POG  object definitions, for use in object selection


### BEGIN OBJECT ISOLATION DEFINITIONS

##########################################################################

# TIGHT MUON ISOLATION

# taken from here: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Isolation
# pfdBetaIsoCorr -> isolation variables recalculated wrt the closest PV to the electron
# calculation found here: https://github.com/OSU-CMS/OSUT3Analysis/blob/master/Collections/plugins/OSUMuonProducer.cc#L124
# muon isolation is so far the same for 2016 and 2017 data

muon_iso_cutstring = cms.string("pfdBetaIsoCorr <= 0.15")

muon_iso_alias = cms.string(">=1 muons with tight isolation")

##########################################################################

# INVERTED TIGHT MUON ISOLATION

muon_antiiso_cutstring = cms.string("pfdBetaIsoCorr > 0.15")

muon_antiiso_alias = cms.string(">=1 muons with inverted tight isolation")

##########################################################################

# INVERTED LOOSE MUON ISOLATION

muon_loose_antiiso_cutstring = cms.string("pfdBetaIsoCorr > 0.25")

muon_loose_antiiso_alias = cms.string(">=1 muons with inverted loose isolation")

##########################################################################

# VERY LOOSE MUON ISOLATION

muon_very_loose_iso_cutstring = cms.string("pfdBetaIsoCorr <= 0.40")

muon_very_loose_iso_alias = cms.string(">=1 muons with very loose isolation")

##########################################################################






### BEGIN OBJECT IDENTIFICATION DEFINITIONS

##########################################################################

# JET ID AGAINST LEPTONS (tight lepton veto)

# N.B.: JET ID VALID FOR ETA < 2.4

if (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
# taken from here: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID13TeVRun2017
# and https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID13TeVRun2018
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

#keeping 102X the same as 94X for now. in 102X, should move to DeepCSV:
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation102X
if (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
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
# HOWEVER, we are removing the isolation from the VID (see customize.py), so that then we can
# add it back in where we want and invert it as necessary
##########################################################################

# TIGHT ELECTRON ISOLATION
# pfdRhoIsoCorr -> isolation variables recalculated wrt the closest PV to the electron
# calculation found here: https://github.com/OSU-CMS/OSUT3Analysis/blob/master/Collections/plugins/OSUElectronProducer.cc#L134
#taken from here: https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2#Working%20points%20for%2094X%20and%20later
# Since you should use Fall17v2 VID for 94X and 102X, the isolation cuts are the same in the two releases

if (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    electron_iso_cutstring = cms.string("(isEB & pfdRhoIsoCorr <= (0.0287+0.506/pt)) | \
                                     (isEE & pfdRhoIsoCorr <= (0.0445+0.963/pt))")

# taken from here: https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2#Working_points_for_2016_data_for
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    electron_iso_cutstring = cms.string("(isEB & pfdRhoIsoCorr <= 0.0588) | \
                                     (isEE & pfdRhoIsoCorr <= 0.0571)")
else:
    print "# uhhh what release are you trying to use? please use 94X for 2017 data or 80X for 2016 data"
electron_iso_alias = cms.string(">=1 electrons with tight isolation")

##########################################################################
# INVERTED TIGHT ELECTRON ISOLATION
if (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    electron_antiiso_cutstring = cms.string("(isEB & pfdRhoIsoCorr > (0.0287+0.506/pt)) | \
                                     (isEE & pfdRhoIsoCorr > (0.0445+0.963/pt))")
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    electron_antiiso_cutstring = cms.string("(isEB & pfdRhoIsoCorr > 0.0588) | \
                                     (isEE & pfdRhoIsoCorr > 0.0571)")
electron_antiiso_alias = cms.string(">=1 electrons with inverted tight isolation")

##########################################################################

# ELECTRON ID IMPACT PARAMETER CUTS
# impact parameter cuts are the same in 2016 and 2017 and 2018

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
# tight muon ID is the same for 2016 and 2017 and 2018 data

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
