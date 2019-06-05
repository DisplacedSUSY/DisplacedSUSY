import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.BasicSelections import *

muon_softID_cut.numberRequired = cms.string(">= 2")

muon_d0_lessThan50_cut.numberRequired = cms.string(">= 2")
muon_d0_lessThan50_cut.alias = cms.string(">=2 muons with |d_0| < 50 mum")

muon_d0_greaterThan50_cut.numberRequired = cms.string(">= 2")
muon_d0_greaterThan50_cut.alias = cms.string(">=2 muons with |d_0| > 50 mum")



muon_eta_lessThan2p4_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 2")
    )

muon_pt_4p2_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 4.2"),
    numberRequired = cms.string(">= 2")
    )

diMuon_deltaR_greaterThanP5_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("deltaR(muon, muon) > 0.5"),
    numberRequired = cms.string(">= 1"),
    )

diMuon_deltaR_lessThanP5_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("deltaR(muon, muon) < 0.5"),
    numberRequired = cms.string(">= 1"),
    )

diMuon_invMass_lessThan3p2_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("invMass(muon, muon) < 3.2"),
    numberRequired = cms.string(">= 1"),
    )

diMuon_invMass_greaterThan2p9_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("invMass(muon, muon) > 2.9"),
    numberRequired = cms.string(">= 1"),
    )
