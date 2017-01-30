import FWCore.ParameterSet.Config as cms
import copy
import string

import DisplacedSUSY.Configuration.objectDefinitions as objectDefs

##########################################################################

# BEGIN JET CUTS

jet_eta_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 0")
    )

jet_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 0")
    )

jet_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_id_cutstring,
    numberRequired = cms.string(">= 0"),
    alias = objectDefs.jet_id_alias
    )

##########################################################################

# BEGIN ELECTRON CUTS

electron_eta_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 2")
    )

electron_gap_veto = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("isEBEEGap = 0"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron ECAL crack veto")
    )

electron_pt_42_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 42"),
    numberRequired = cms.string(">= 2")
    )

electron_id_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.electron_id_alias
    )

electron_iso_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_iso_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.electron_iso_alias
    )

# diElectron Invariant Mass > 81.2GeV
diElectron_invMass_above81_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "electrons"),
    cutString = cms.string("invMass (electron,electron) > 81.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("diElectron invariant mass > 81.2GeV")
    )

# diElectron Invariant Mass < 101.2GeV
diElectron_invMass_below101_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "electrons"),
    cutString = cms.string("invMass (electron,electron) < 101.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("diElectron invariant mass < 101.2GeV")
    )

# electron d0 < 100 microns
electron_d0_lt100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string(objectDefs.electronAbsD0 + " < 100"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron d0 < 100 mum")
    )

# electron d0 > 100 microns
electron_d0_above100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string(objectDefs.electronAbsD0 + " > 100"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron d0 > 100 mum")
    )

# electron d0 < 200 microns
electron_d0_below200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string(objectDefs.electronAbsD0 + " < 200"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron d0 < 200 mum")
    )


##########################################################################

# BEGIN MUON CUTS

muon_eta_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 2")
    )

muon_pt_40_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 2")
    )

muon_global_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_global_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.muon_global_alias
    )

muon_id_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.muon_id_alias
    )

muon_iso_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_iso_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.muon_iso_alias
    )

# muon d0 < 100 microns
muon_d0_lt100_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string(objectDefs.muonAbsD0 + " < 100"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("muon d0 < 100 mum")
    )
