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

jet_btag_mwp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.800"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 medium b tags')
    )

jet_btag_2_lwp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.460"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string('>= 2 loose b tags')
    )

jet_btag_lwp_veto = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.460"),
        numberRequired = cms.string("== 0"),
        alias = cms.string('no loose b tags'),
        isVeto = cms.bool(True)
    )

jet_2jet_veto = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("< 2"),
        alias = cms.string('< 2 jets')
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

electron_antiiso_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_antiiso_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.electron_antiiso_alias
    )

electron_veto_antiiso_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_veto_antiiso_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.electron_veto_antiiso_alias
    )

# electron d0 < 100 microns
electron_d0_lt100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string(objectDefs.electronAbsD0_um + " < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron d0 < 100 mum")
    )

# electron d0 > 100 microns
electron_d0_gt100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string(objectDefs.electronAbsD0_um + " > 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron d0 > 100 mum")
    )

# electron 100 < d0 < 200 microns
electron_d0_100to200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string(objectDefs.electronAbsD0_um + " > 100 & " + objectDefs.electronAbsD0_um + " < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron 100 < d0 < 200 mum")
    )

electron_mt_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","mets"),
    cutString = cms.string("transMass(electron, met) < 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron m_{T} < 50 GeV")
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

muon_antiiso_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_antiiso_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.muon_antiiso_alias
    )

muon_loose_antiiso_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_loose_antiiso_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.muon_loose_antiiso_alias
    )

# muon d0 < 100 microns
muon_d0_lt100_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string(objectDefs.muonAbsD0_um + " < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon d0 < 100 mum")
    )

# muon d0 > 100 microns
muon_d0_gt100_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string(objectDefs.muonAbsD0_um + " > 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon d0 > 100 mum")
    )

# muon 100 < d0 < 200 microns
muon_d0_100to200_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string(objectDefs.muonAbsD0_um + " > 100 & " + objectDefs.muonAbsD0_um + " < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon 100 < d0 < 200 mum")
    )

muon_mt_cut = cms.PSet (
    inputCollection = cms.vstring("muons","mets"),
    cutString = cms.string("transMass(muon, met) < 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon m_{T} < 50 GeV")
    )


##########################################################################

# BEGIN ELECTRON-MUON CUTS

emu_mass_lt100_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("invMass(electron,muon) < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("invariant mass < 100GeV")
    )

emu_pt_gt50_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("pT(electron,muon) > 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("pT(e,mu) > 50")
    )


##########################################################################

# BEGIN MET CUTS

met_gt60_cut =  cms.PSet (
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("pt > 60"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("met > 60")
)
