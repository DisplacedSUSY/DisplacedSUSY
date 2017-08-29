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

# CSV WPs taken from here: https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
jet_csvl_veto = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.5426"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True)
    )

jet_csvm_veto = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.8484"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True)
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

electron_pt_20_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 2")
    )

electron_pt_25_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1")
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

electron_id_TTpaper_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_ttbar_paper_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.electron_ttbar_paper_id_alias
    )

electron_iso_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_iso_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.electron_iso_alias
    )

electron_antiiso_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_antiiso_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.electron_antiiso_alias
    )

electron_2electron_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("extra electron veto")
    )

diElectron_invMass_above20_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "electrons"),
    cutString = cms.string("invMass (electron,electron) > 20.0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("diElectron invariant mass > 20.0 GeV")
    )

diElectron_invMass_OutsideZWindow_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "electrons"),
    cutString = cms.string("abs(invMass (electron,electron) - 91 > 15)"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("diElectron invariant mass < 76 GeV OR > 106 GeV")
    )

diElectron_invMass_Z_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "electrons"),
    cutString = cms.string("abs(invMass(electron,electron) - 91.2) < 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("abs(mass_ee - mass_Z) < 10")
    )

electron_d0_lt100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) < 100"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron d0 < 100 mum")
    )

electron_d0_100to200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) > 100 & " + "10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron 100 < d0 < 200 mum")
    )

electron_d0_above100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) > 100"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron d0 > 100 mum")
    )

electron_d0_below200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron d0 < 200 mum")
    )

electron_d0_above200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) > 200"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron d0 > 200 mum")
    )

electron_num_exactly2_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 0"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Exactly 2 electrons")
    )

##########################################################################

# BEGIN ELECTRON-JET CUTS

electronjet_deltaR_veto = cms.PSet(
    inputCollection = cms.vstring("electrons","jets"),
    cutString = cms.string("deltaR(electron, jet) < 0.5"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True)
    )
