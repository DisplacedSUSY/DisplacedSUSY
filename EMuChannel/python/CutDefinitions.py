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

jet_eta_real_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string('>= 2 jets w/ eta < 2.4')
    )

jet_pt_30_real_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string('>= 2 jets w/ pT > 30GeV')
    )

jet_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_id_cutstring,
    numberRequired = cms.string(">= 0"),
    alias = objectDefs.jet_id_alias
    )

jet_loose_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_loose_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.jet_loose_id_alias
    )

jet_btag_twp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.935"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 tight b tags')
    )

jet_btag_mwp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.800"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 medium b tags')
    )

jet_btag_2_mwp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.800"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string('>= 2 medium b tags')
    )

jet_btag_lwp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.5426"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 loose b tags')
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

jet_muon_deltaR_veto = cms.PSet (
        inputCollection = cms.vstring("jets", "muons"),
        cutString = cms.string("deltaR(jet, muon) < 0.4"),
        numberRequired = cms.string("== 0"),
        alias = cms.string('jet-mu deltaR veto'),
        isVeto = cms.bool(True)
    )

jet_electron_deltaR_veto = cms.PSet (
        inputCollection = cms.vstring("jets", "electrons"),
        cutString = cms.string("deltaR(jet, electron) < 0.4"),
        numberRequired = cms.string("== 0"),
        alias = cms.string('jet-e deltaR veto'),
        isVeto = cms.bool(True)
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

electron_ttbar_paper_id_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_id_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.electron_ttbar_paper_id_alias
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

electron_num_exactly_1_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("exactly 1 electron")
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

muon_d0_below2000_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string(objectDefs.muonAbsD0_cm + " < 0.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon d0 < 0.2 cm")
    )

muon_dZ_below5000_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string(objectDefs.muonAbsDz + " < 5000"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon dZ < 0.5 cm")
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

muon_num_exactly_1_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("exactly 1 muon")
    )


##########################################################################

# BEGIN ELECTRON-MUON CUTS

emu_mass_20_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("invMass(electron,muon) > 20"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("invariant mass < 20 GeV")
    )

emu_opposite_charge_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("electron.charge * muon.charge < 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("oppositely-charged e-mu pair")
    )

emu_pt_25_20_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("(electron.pt > 25 & muon.pt > 20) | (electron.pt > 20 & muon.pt > 25)"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Leading lepton 25 pT, sub-leading 20 pT")
    )


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

met_pt_40_cut = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1")
    )

met_gt60_cut =  cms.PSet (
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("pt > 60"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("met > 60")
)
