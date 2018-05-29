import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.BasicSelections import *

##########################################################################

# BEGIN MUON CUTS

muon_eta_cut.numberRequired = cms.string(">= 2")

muon_pt_20_cut.numberRequired = cms.string(">= 2")

muon_pt_25_cut.numberRequired = cms.string(">= 2")

muon_pt_40_cut.numberRequired = cms.string(">= 2")

muon_pt_70_cut.numberRequired = cms.string(">= 2")

muon_global_cut.numberRequired = cms.string(">= 2")
muon_global_cut.alias = cms.string(">=2 global PF muons")

muon_id_cut.numberRequired = cms.string(">= 2")
muon_id_cut.alias = cms.string(">=2 muons with tight ID")

muon_iso_cut.numberRequired = cms.string(">= 2")
muon_iso_cut.alias = cms.string(">=2 muons with tight isolation")

muon_antiiso_cut.numberRequired = cms.string(">= 2")
muon_antiiso_cut.alias = cms.string(">=2 muons with inverted tight isolation")

muon_d0_lessThan10_cut.numberRequired = cms.string(">= 2")
muon_d0_lessThan10_cut.alias = cms.string(">=2 muons with |d_0| < 10 mum")

muon_d0_lessThan100_cut.numberRequired = cms.string(">= 2")
muon_d0_lessThan100_cut.alias = cms.string(">=2 muons with |d_0| < 100 mum")

muon_d0_100to200_cut.numberRequired = cms.string(">= 2")
muon_d0_100to200_cut.alias = cms.string(">=2 muons with 100 < |d_0| < 200 mum")

muon_d0_greaterThan100_cut.numberRequired = cms.string(">= 2")
muon_d0_greaterThan100_cut.alias = cms.string(">=2 muons with |d_0| > 100 mum")

muon_d0_lessThan200_cut.numberRequired = cms.string(">= 2")
muon_d0_lessThan200_cut.alias = cms.string(">=2 muons with |d_0| < 200 mum")

muon_d0_lessThan2000_cut.numberRequired = cms.string(">= 2")
muon_d0_lessThan2000_cut.alias = cms.string(">=2 muons with |d_0| < 0.2 cm")

#dZ cut
muon_dZ_lessThan5000_cut.numberRequired = cms.string(">= 2")
muon_dZ_lessThan5000_cut.alias = cms.string(">=2 muons with dZ < 0.5 cm")

muon_gen_motherIsW_cut.numberRequired = cms.string(">= 2")
muon_gen_motherIsW_cut.alias = cms.string(">=2 muons from W (muon matched to gen particle whose mother has PDG ID of 24)")

muon_fiducial_phi_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(abs(phi)-3.14159/2) > 0.05"),
    numberRequired = cms.string(">= 2")
    )

muon_2muon_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("exactly 2 muons")
    )

diMuon_invMass_Z_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("abs(invMass(muon,muon) - 91.2) < 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("abs(mass_mumu - mass_Z) < 10")
    )

diMuon_invMass_OutsideZWindow_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("abs(invMass (muon,muon) - 91 > 15.0)"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("dimuon invariant mass < 76 GeV OR > 106 GeV")
    )

diMuon_invMass_greaterThan20_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("invMass (muon,muon) > 20.0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("dimuon invariant mass > 20 GeV")
    )

diMuon_opposite_charge_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("muon.charge * muon.charge < 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 oppositely-charged mu-mu pair")
    )

diMuon_deltaR_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("deltaR(muon, muon) > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 well-seperated mu-mu pair (#DeltaR > 0.5)")
    )

##########################################################################

# BEGIN EVENTVARIABLE CUTS

muon_opposite_charge_from_tag_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "eventvariables"),
    cutString = cms.string("muon.charge * eventvariable.tagMuonCharge < 0"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("oppositely-charged mu-tagmu pair")
    )

muon_deltaR_from_tag_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "eventvariables"),
    cutString = cms.string("sqrt(pow((muon.eta-eventvariable.tagMuonEta), 2) + pow((muon.phi-eventvariable.tagMuonPhi), 2))"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("well-seperated mu-tagmu pair")
    )

tagMuonExists_cut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("eventvariable.tagMuonExists"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("tag muon exists")
    )
