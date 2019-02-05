import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.BasicSelections import *

##########################################################################

# CHANGE ELECTRON CUTS TO >=2 ELECTRONS

electron_eta_cut.numberRequired = cms.string(">= 2")

electron_gap_veto.numberRequired = cms.string(">= 2")
electron_gap_veto.alias = cms.string(">=2 electrons surviving ECAL crack veto")

electron_pt_75_cut.numberRequired = cms.string(">= 2")
electron_pt_65_cut.numberRequired = cms.string(">= 2")
electron_pt_42_cut.numberRequired = cms.string(">= 2")
electron_pt_30_cut.numberRequired = cms.string(">= 2")
electron_pt_25_cut.numberRequired = cms.string(">= 2")

# only require >= 1 electron to cut on leading electron
electron_pt_100_cut.alias = cms.string(">=1 electrons with pT > 100")

electron_id_cut.numberRequired = cms.string(">= 2")
electron_id_cut.alias = cms.string(">=2 electrons with versioned tight ID")

electron_iso_cut.numberRequired = cms.string(">= 2")
electron_iso_cut.alias = cms.string(">=2 electrons with tight isolation")

electron_antiiso_cut.numberRequired = cms.string(">= 2")
electron_antiiso_cut.alias = cms.string(">=2 electrons with inverted tight isolation")

electron_d0_lessThan10_cut.numberRequired = cms.string(">= 2")
electron_d0_lessThan10_cut.alias = cms.string(">=2 electrons with |d_0| < 10 mum")

electron_d0_lessThan50_cut.numberRequired = cms.string(">= 2")
electron_d0_lessThan50_cut.alias = cms.string(">=2 electrons with |d_0| < 50 mum")

electron_d0_greaterThan50_cut.numberRequired = cms.string(">= 2")
electron_d0_greaterThan50_cut.alias = cms.string(">=2 electrons with |d_0| > 50 mum")

electron_d0_lessThan100_cut.numberRequired = cms.string(">= 2")
electron_d0_lessThan100_cut.alias = cms.string(">=2 electrons with |d_0| < 100 mum")

electron_d0_100to200_cut.numberRequired = cms.string(">= 2")
electron_d0_100to200_cut.alias = cms.string(">=2 electrons with 100 < |d_0| < 200 mum")

electron_d0_greaterThan100_cut.numberRequired = cms.string(">= 2")
electron_d0_greaterThan100_cut.alias = cms.string(">=2 electrons with |d_0| > 100 mum")

electron_d0_lessThan200_cut.numberRequired = cms.string(">= 2")
electron_d0_lessThan200_cut.alias = cms.string(">=2 electrons with |d_0| < 200 mum")

electron_d0_greaterThan200_cut.numberRequired = cms.string(">= 2")
electron_d0_greaterThan200_cut.alias = cms.string("electron |d_0| > 200 mum")

electron_gen_motherIsW_cut.numberRequired = cms.string(">= 2")
electron_gen_motherIsW_cut.alias = cms.string(">=2 electrons from W (electron matched to gen particle whose mother has PDG ID of 24)")

electron_fiducial_phi_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(abs(phi)-3.14159/2) > 0.05"),
    numberRequired = cms.string(">= 2")
    )

electron_2electron_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("exactly 2 electrons")
    )

diElectron_invMass_greaterThan20_cut = cms.PSet (
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

diElectron_opposite_charge_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "electrons"),
    cutString = cms.string("electron.charge * electron.charge < 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 oppositely-charged e-e pair")
)

diElectron_deltaR_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "electrons"),
    cutString = cms.string("deltaR(electron, electron) > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 well-seperated e-e pair (#DeltaR > 0.5)")
)

tagElectronExists_cut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("eventvariable.tagElectronExists"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("tag electron exists")
)

electron_opposite_charge_from_tag_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "eventvariables"),
    cutString = cms.string("electron.charge * eventvariable.tagElectronCharge < 0"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("oppositely-charged e-tage pair")
)

electron_deltaR_from_tag_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "eventvariables"),
    cutString = cms.string("sqrt(pow((electron.eta-eventvariable.tagElectronEta), 2) + pow((electron.phi-eventvariable.tagElectronPhi), 2))"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("well-seperated e-tage pair")
)
##########################################################################
