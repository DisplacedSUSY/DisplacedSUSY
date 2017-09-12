import FWCore.ParameterSet.Config as cms
import copy
import string

### This file contains the official POG  object definitions, for use in object selection


### BEGIN OBJECT ISOLATION DEFINITIONS

##########################################################################

# TIGHT ELECTRON ISOLATION

# taken from here: https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2#Working_points_for_2016_data_for
# pfdRhoIsoCorr -> isolation variables recalculated wrt the closest PV to the electron
# calculation found here: https://github.com/OSU-CMS/OSUT3Analysis/blob/master/Collections/plugins/OSUElectronProducer.cc#L134

electron_iso_cutstring = cms.string("(isEB & pfdRhoIsoCorr <= 0.0588) | \
                                     (isEE & pfdRhoIsoCorr <= 0.0571)")

electron_iso_alias = cms.string("electron tight isolation")

##########################################################################

# INVERTED TIGHT ELECTRON ISOLATION

electron_antiiso_cutstring = cms.string("(isEB & pfdRhoIsoCorr > 0.0588) | \
                                     (isEE & pfdRhoIsoCorr > 0.0571)")

electron_antiiso_alias = cms.string("electron inverted tight isolation")

##########################################################################

# INVERTED VETO ELECTRON ISOLATION

electron_veto_antiiso_cutstring = cms.string("(isEB & pfdRhoIsoCorr > 0.175) | \
                                     (isEE & pfdRhoIsoCorr > 0.159)")

electron_veto_antiiso_alias = cms.string("electron inverted veto isolation")

##########################################################################

# TIGHT MUON ISOLATION

# taken from here: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Isolation
# pfdBetaIsoCorr -> isolation variables recalculated wrt the closest PV to the electron
# calculation found here: https://github.com/OSU-CMS/OSUT3Analysis/blob/master/Collections/plugins/OSUMuonProducer.cc#L124

muon_iso_cutstring = cutString = cms.string("pfdBetaIsoCorr <= 0.15")

muon_iso_alias = cms.string("muon tight isolation")

##########################################################################

# INVERTED TIGHT MUON ISOLATION

muon_antiiso_cutstring = cutString = cms.string("pfdBetaIsoCorr > 0.15")

muon_antiiso_alias = cms.string("muon inverted tight isolation")

##########################################################################

# INVERTED LOOSE MUON ISOLATION

muon_loose_antiiso_cutstring = cutString = cms.string("pfdBetaIsoCorr > 0.25")

muon_loose_antiiso_alias = cms.string("muon inverted loose isolation")

##########################################################################






### BEGIN OBJECT IDENTIFICATION DEFINITIONS

##########################################################################

# JET ID AGAINST LEPTONS

# N.B.: JET ID VALID FOR ETA < 2.4
# taken from here: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID#Recommendations_for_13_TeV_data

jet_id_cutstring = cms.string("neutralHadronEnergyFraction < 0.90 & \
                                              chargedEmEnergyFraction < 0.90 & \
                                              neutralEmEnergyFraction < 0.90 & \
                                              numberOfDaughters > 1 & \
                                              chargedHadronEnergyFraction > 0.0 & \
                                              chargedMultiplicity > 0.0 & \
                                              muonEnergyFraction < 0.8")

jet_id_alias = cms.string("jet ID against leptons")

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

# ELECTRON ID

# taken from here: https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2#Offline_selection_criteria

electron_id_cutstring = cms.string("(isEB & \
                            full5x5_sigmaIetaIeta < 0.00998 & \
                            abs(deltaPhiSuperClusterTrackAtVtx) < 0.0816 & \
                            abs(deltaEtaSuperClusterTrackAtVtx) < 0.00308 &\
                            hadronicOverEm < 0.0414 & \
                            abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.0129 & \
                            missingInnerHits <= 1 & \
                            passConversionVeto) | \
                            (isEE & \
                            full5x5_sigmaIetaIeta < 0.0292 & \
                            abs(deltaPhiSuperClusterTrackAtVtx) < 0.0394 & \
                            abs(deltaEtaSuperClusterTrackAtVtx) < 0.00605 &\
                            hadronicOverEm < 0.0641 & \
                            abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.0129 & \
                            missingInnerHits <= 1 & \
                            passConversionVeto)")

electron_id_alias = cms.string("electron tight ID")

##########################################################################

# MUON ID, part one
# done separately because some other cuts access members that only exist for global muons

muon_global_cutstring = cms.string("isGlobalMuon & isPFMuon")

muon_global_alias = cms.string("is global muon")

##########################################################################

# MUON ID, part two
# taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideMuonIdRun2#Tight_Muon
# we don't include d0/dz inside the ID so that we can control it more explicitly

muon_id_cutstring = cms.string("globalTrack.normalizedChi2 < 10 & \
                                globalTrack.hitPattern_.numberOfValidMuonHits > 0 & \
                                numberOfMatchedStations > 1 & \
                                innerTrack.hitPattern_.numberOfValidPixelHits > 0 & \
                                innerTrack.hitPattern_.trackerLayersWithMeasurement > 5")

muon_id_alias = cms.string("muon tight ID")


