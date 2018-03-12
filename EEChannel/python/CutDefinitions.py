import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.CutDefinitions import *

##########################################################################

# CHANGE ELECTRON CUTS TO >=2 ELECTRONS

electron_eta_cut.numberRequired = cms.string(">= 2")

electron_gap_veto.numberRequired = cms.string(">= 2")
electron_gap_veto.alias = cms.string(">=2 electrons surviving ECAL crack veto")

electron_pt_42_cut.numberRequired = cms.string(">= 2")

electron_id_cut.numberRequired = cms.string(">= 2")
electron_id_cut.alias = cms.string(">=2 electrons with tight ID")

electron_iso_cut.numberRequired = cms.string(">= 2")
electron_iso_cut.alias = cms.string(">=2 electrons with tight isolation")

electron_antiiso_cut.numberRequired = cms.string(">= 2")
electron_antiiso_cut.alias = cms.string(">=2 electrons with inverted tight isolation")

electron_d0_lt100_cut.numberRequired = cms.string(">= 2")
electron_d0_lt100_cut.alias = cms.string(">=2 electrons with d0 < 100 mum")

electron_d0_100to200_cut.numberRequired = cms.string(">= 2")
electron_d0_100to200_cut.alias = cms.string(">=2 electrons with 100 < d0 < 200 mum")

electron_d0_above100_cut.numberRequired = cms.string(">= 2")
electron_d0_above100_cut.alias = cms.string(">=2 electrons with d0 > 100 mum")

electron_d0_below200_cut.numberRequired = cms.string(">= 2")
electron_d0_below200_cut.alias = cms.string(">=2 electrons with d0 < 200 mum")

electron_d0_above200_cut.numberRequired = cms.string(">= 2")
electron_d0_above200_cut.alias = cms.string("electron d0 > 200 mum")

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

##########################################################################
