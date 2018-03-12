import FWCore.ParameterSet.Config as cms
import copy
import string

import DisplacedSUSY.StandardAnalysis.objectDefinitions as objectDefs

##########################################################################

# BEGIN JET CUTS

two_jets_eta_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 2")
    )

two_jets_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 2")
    )

two_jets_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.jet_id_alias
    )

one_jet_eta_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 1")
    )

one_jet_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1")
    )

one_jet_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_id_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.jet_id_alias
    )

extra_jet_veto = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 2")
    )


##########################################################################

# BEGIN B-JET CUTS

bjet_eta_cut = cms.PSet(
    inputCollection = cms.vstring("bjets"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 1")
    )

bjet_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("bjets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1")
    )

bjet_id_cut = cms.PSet(
    inputCollection = cms.vstring("bjets"),
    cutString = objectDefs.jet_id_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.jet_id_alias
    )

bjet_csvm_cut = cms.PSet (
    inputCollection = cms.vstring("bjets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.800"),
    numberRequired = cms.string(">= 1"),
    )

extra_bjet_veto = cms.PSet(
    inputCollection = cms.vstring("bjets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 2")
    )


##########################################################################

# BEGIN JET - B-JET CUTS

jet_deltaPhi_cut = cms.PSet (
    inputCollection = cms.vstring("jets","bjets"),
    cutString = cms.string("abs(deltaPhi(jet,bjet)) > 2.5"),
    numberRequired = cms.string(">= 1"),
)

##########################################################################

# BEGIN ELECTRON CUTS

electron_eta_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 1")
    )

electron_gap_veto = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("isEBEEGap = 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron ECAL crack veto")
    )

electron_pt_25_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_42_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 42"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string(">= 1")
    )

electron_id_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_id_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.electron_id_alias
    )

electron_iso_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_iso_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.electron_iso_alias
    )

extra_electron_veto = cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto"),
)

##########################################################################

# BEGIN MUON CUTS

muon_eta_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_25_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_40_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_50_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_55_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 55"),
    numberRequired = cms.string(">= 1")
    )

muon_global_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_global_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.muon_global_alias
    )

muon_id_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_id_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.muon_id_alias
    )

muon_iso_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_iso_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.muon_iso_alias
    )

extra_muon_veto = cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto"),
)

##########################################################################

# BEGIN JET - B-JET CUTS

jet_bjet_deltaPhi_cut = cms.PSet (
    inputCollection = cms.vstring("jets","bjets"),
    cutString = cms.string("abs(deltaPhi(jet,bjet)) > 2.5"),
    numberRequired = cms.string(">= 1"),
)


##########################################################################

# BEGIN MUON - JET CUTS

muon_jet_deltaR_cut = cms.PSet (
    inputCollection = cms.vstring("muons","jets"),
    cutString = cms.string("deltaR(muon,jet) < 0.5"),
    numberRequired = cms.string(">= 1"),
)

##########################################################################

# BEGIN ELECTRON - JET CUTS

electron_jet_deltaR_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","jets"),
    cutString = cms.string("deltaR(electron,jet) < 0.5"),
    numberRequired = cms.string(">= 1"),
)
