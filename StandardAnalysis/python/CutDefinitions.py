import FWCore.ParameterSet.Config as cms
import copy
import string

import DisplacedSUSY.StandardAnalysis.objectDefinitions as objectDefs

absEta_2p4_cutstring = cms.string("abs(eta) < 2.4")
##########################################################################

# BEGIN JET CUTS

jet_eta_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = absEta_2p4_cutstring,
    numberRequired = cms.string(">= 0")
    )

jet_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 0")
    )

jet_eta_real_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = absEta_2p4_cutstring,
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

jet_id_real_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.jet_id_alias
    )

jet_loose_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_loose_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.jet_loose_id_alias
    )

jet_ttbar_paper_loose_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_ttbar_paper_loose_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.jet_ttbar_paper_loose_id_alias
    )

jet_2jet_veto = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("< 2"),
        alias = cms.string('< 2 jets')
    )

jet_lepton_cleaning_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("matchedToLepton = 0"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string('jet-lepton cleaning')
    )

#BEGIN B-JET CUTS
bjet_eta_cut = copy.deepcopy(jet_eta_cut)
bjet_eta_cut.inputCollection = cms.vstring("bjets")

bjet_pt_30_cut = copy.deepcopy(jet_pt_30_cut)
bjet_pt_30_cut.inputCollection = cms.vstring("bjets")

bjet_id_cut = copy.deepcopy(jet_id_cut)
bjet_id_cut.inputCollection = cms.vstring("bjets")

#BEGIN B-JET CombinedSecondaryVertexv2 CUTS
jet_btag_twp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = objectDefs.btag_tightCSVv2_cutstring,
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 tight b tags (CSVv2)')
    )

jet_btag_mwp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = objectDefs.btag_mediumCSVv2_cutstring,
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 medium b tags (CSVv2)')
    )

jet_btag_2_mwp_cut = copy.deepcopy(jet_btag_mwp_cut)
jet_btag_2_mwp_cut.numberRequired = cms.string(">= 2")
jet_btag_2_mwp_cut.alias = cms.string('>= 2 medium b tags (CSVv2)')

jet_btag_mwp_veto = copy.deepcopy(jet_btag_mwp_cut)
jet_btag_mwp_veto.numberRequired = cms.string("== 0")
jet_btag_mwp_veto.alias = cms.string('no medium b tags (CSVv2)')
jet_btag_mwp_veto.isVeto = cms.bool(True)

jet_btag_lwp_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = objectDefs.btag_looseCSVv2_cutstring,
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 loose b tags (CSVv2)')
    )

jet_btag_2_lwp_cut = copy.deepcopy(jet_btag_lwp_cut)
jet_btag_2_lwp_cut.numberRequired = cms.string(">= 2")
jet_btag_2_lwp_cut.alias = cms.string('>= 2 loose b tags (CSVv2)')

jet_btag_lwp_veto = copy.deepcopy(jet_btag_lwp_cut)
jet_btag_lwp_veto.numberRequired = cms.string("== 0")
jet_btag_lwp_veto.alias = cms.string('no loose b tags (CSVv2)')
jet_btag_lwp_veto.isVeto = cms.bool(True)


##########################################################################

# BEGIN ELECTRON CUTS

electron_eta_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = absEta_2p4_cutstring,
    numberRequired = cms.string(">= 1")
    )

electron_gap_veto = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("isEBEEGap = 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron ECAL crack veto")
    )

electron_pt_20_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_25_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_25_dummy_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 0")
    )

electron_pt_42_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 42"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_50_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1")
    )

electron_id_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_id_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.electron_id_alias
    )

electron_id_impact_parameter_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_id_impact_parameter_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.electron_id_impact_parameter_alias
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
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with d0 < 100 mum")
    )

# electron d0 > 100 microns
electron_d0_gt100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) > 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with d0 > 100 mum")
    )

# electron 100 < d0 < 200 microns
electron_d0_100to200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) > 100 & 10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with 100 < d0 < 200 mum")
    )

electron_d0_below200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with d0 < 200 mum")
    )

electron_d0_above100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) > 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with d0 > 100 mum")
    )

electron_d0_above200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) > 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with d0 > 200 mum")
    )

electron_mt_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","mets"),
    cutString = cms.string("transMass(electron, met) < 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron m_{T} < 50 GeV")
    )

electron_num_exactly_1_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("exactly 1 electron")
    )

##########################################################################

# BEGIN MUON CUTS

muon_eta_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = absEta_2p4_cutstring,
    numberRequired = cms.string(">= 1")
    )

muon_pt_25_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_25_dummy_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 0")
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

muon_pt_150_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 150"),
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

muon_id_impact_parameter_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_id_impact_parameter_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.muon_id_impact_parameter_alias
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
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with d0 < 100 mum")
    )

# muon d0 > 100 microns
muon_d0_gt100_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) > 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with d0 > 100 mum")
    )

# muon 100 < d0 < 200 microns
muon_d0_100to200_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) > 100 & 10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with 100 < d0 < 200 mum")
    )

muon_d0_below200_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with d0 < 200 mum")
    )

muon_d0_above200_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) > 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with d0 > 200 mum")
    )

muon_mt_cut = cms.PSet (
    inputCollection = cms.vstring("muons","mets"),
    cutString = cms.string("transMass(muon, met) < 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon m_{T} < 50 GeV")
    )

muon_num_exactly_1_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("exactly 1 muon")
    )


##########################################################################

# BEGIN ELECTRON-MUON CUTS

emu_mass_20_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("invMass(electron,muon) > 20"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electron-muon pair with invariant mass > 20 GeV")
    )

emu_opposite_charge_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("electron.charge * muon.charge < 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 oppositely-charged e-mu pair")
    )

emu_samesign_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("electron.charge * muon.charge > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 like-charged e-mu pair")
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
    alias = cms.string(">=1 electron-muon pair with invariant mass < 100GeV")
    )

emu_pt_gt50_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("pT(electron,muon) > 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("pT(e,mu) > 50")
    )

emu_deltaR_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("deltaR(electron,muon) > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 well separated e-mu pair")
    )

##########################################################################                                                                                 
# ELECTRON-JET OVERLAP VETO                                                                                                                                
electron_jet_deltaR_cut = cms.PSet (
        inputCollection = cms.vstring("electrons", "jets"),
        cutString = cms.string("deltaR(electron, jet) < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("electron near jet veto")
)

##########################################################################                                                                                 
# MUON-JET OVERLAP VETO                                                                                                                                    
muon_jet_deltaR_cut = cms.PSet (
        inputCollection = cms.vstring("muons", "jets"),
        cutString = cms.string("deltaR(muon, jet) < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("muon near jet veto")
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

##########################################################################

# BEGIN EVENTVARIABLE CUTS

pass_trigger = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("eventvariable.passTrigger"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("pass trigger specified in config file")
    )


