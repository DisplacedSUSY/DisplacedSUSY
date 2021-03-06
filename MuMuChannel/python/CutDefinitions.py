import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.BasicSelections import *

##########################################################################

# BEGIN MUON CUTS


muon_eta_cut.numberRequired = cms.string(">= 2")

muon_eta1p9_cut.numberRequired = cms.string(">= 2")

muon_eta_lessThan1_cut.numberRequired = cms.string(">= 2")

muon_eta_greaterThan1_cut.numberRequired = cms.string(">= 2")

muon_eta_phi_veto_2017.numberRequired = cms.string(">= 2")
muon_eta_phi_veto_2017.alias = cms.string(">= 2 muons not in region affected by 2017 pixel power supply issues")

muon_eta_phi_veto_2018.numberRequired = cms.string(">= 2")
muon_eta_phi_veto_2018.alias = cms.string(">= 2 muons not in region affected by 2018 pixel power supply issues")

muon_pt_20_cut.numberRequired = cms.string(">= 2")

muon_pt_25_cut.numberRequired = cms.string(">= 2")

muon_pt_30_cut.numberRequired = cms.string(">= 2")

muon_pt_35_cut.numberRequired = cms.string(">= 2")

muon_pt_40_cut.numberRequired = cms.string(">= 2")

muon_pt_45_cut.numberRequired = cms.string(">= 2")

muon_pt_50_cut.numberRequired = cms.string(">= 2")

muon_pt_65_cut.numberRequired = cms.string(">= 2")

muon_pt_70_cut.numberRequired = cms.string(">= 2")

muon_pt_75_cut.numberRequired = cms.string(">= 2")

muon_pt_100_cut.numberRequired = cms.string(">= 2")

muon_pt_150_cut.numberRequired = cms.string(">= 2")

muon_pt_50to60_cut.numberRequired = cms.string(">= 2")

# only require >= 1 muon to cut on leading muon
#muon_pt_100_cut.alias = cms.string(">=1 muons with pT > 100")

muon_global_cut.numberRequired = cms.string(">= 2")
muon_global_cut.alias = cms.string(">=2 global PF muons")

muon_id_cut.numberRequired = cms.string(">= 2")
muon_id_cut.alias = cms.string(">=2 muons with tight ID")

muon_iso_cut.numberRequired = cms.string(">= 2")
muon_iso_cut.alias = cms.string(">=2 muons with tight rho-based isolation")

muon_antiiso_cut.numberRequired = cms.string(">= 2")
muon_antiiso_cut.alias = cms.string(">=2 muons with inverted tight rho-based isolation")

muon_pfBetaIsoCorr_cut.numberRequired = cms.string(">= 2")
muon_pfBetaIsoCorr_cut.alias = cms.string(">=2 muons with pfBetaIsoCorr tight isolation")

muon_d0_lessThan10_cut.numberRequired = cms.string(">= 2")
muon_d0_lessThan10_cut.alias = cms.string(">=2 muons with |d_0| < 10 mum")

muon_d0_lessThan50_cut.numberRequired = cms.string(">= 2")
muon_d0_lessThan50_cut.alias = cms.string(">=2 muons with |d_0| < 50 mum")

muon_d0_lessThan30_cut.numberRequired = cms.string(">= 2")
muon_d0_lessThan30_cut.alias = cms.string(">=2 muons with |d_0| < 30 mum")

gen_muon_d0_lessThan30_cut.numberRequired = cms.string(">= 2")
gen_muon_d0_lessThan30_cut.alias = cms.string(">=2 gen muons with |d_0| < 30 mum")

muon_d0_greaterThan50_cut.numberRequired = cms.string(">= 2")
muon_d0_greaterThan50_cut.alias = cms.string(">=2 muons with |d_0| > 50 mum")

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

muon_gen_motherIsWorZ_cut.numberRequired = cms.string(">= 2")
muon_gen_motherIsWorZ_cut.alias = cms.string(">=2 muons from W or Z (muons matched to gen particles whose mother's PDG ID is 23 or 24")

muon_gen_motherIsLightMeson_cut.numberRequired = cms.string(">= 2")
muon_gen_motherIsLightMeson_cut.alias = cms.string(">=2 muons from light mesons (muon matched to gen particle whose mother has 111 <= PDG ID < 400)")

muon_gen_motherIsHeavyMeson_cut.numberRequired = cms.string(">= 2")
muon_gen_motherIsHeavyMeson_cut.alias = cms.string(">=2 muons from heavy mesons (muon matched to gen particle whose mother has 400 < PDG ID < 600)")

#dZ cut
muon_dZ_lessThan5000_cut.numberRequired = cms.string(">= 2")
muon_dZ_lessThan5000_cut.alias = cms.string(">=2 muons with dZ < 0.5 cm")

muon_gen_motherIsBorCQuark_cut.numberRequired = cms.string(">= 2")
muon_gen_motherIsBorCQuark_cut.alias = cms.string(">=2 muons from b or c quark (muon matched to gen particle whose mother's PDG ID is 4 or 5)")

muon_gen_motherIsW_cut.numberRequired = cms.string(">= 2")
muon_gen_motherIsW_cut.alias = cms.string(">=2 muons from W (muon matched to gen particle whose mother has PDG ID of 24)")

muon_gen_motherIsTau_cut.numberRequired = cms.string(">= 2")
muon_gen_motherIsTau_cut.alias = cms.string(">=2 muons from tau (muon matched to gen particle whose mother has PDG ID of 15)")

muon_gen_motherIsNotTau_cut.numberRequired = cms.string(">= 2")
muon_gen_motherIsNotTau_cut.alias = cms.string(">=2 muons not from Tau (muon matched to gen particle whose mother's PDG ID is not 15)")

muon_fiducial_phi_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(abs(muon.phi)-3.14159/2) > 0.05"),
    numberRequired = cms.string(">= 2")
    )

muon_2muon_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("muon.pt > -1"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("exactly 2 muons")
    )

diMuon_invMass_Z_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("abs(invMass(muon,muon) - 91.2) < 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("abs(mass_mumu - mass_Z) < 10")
    )

diMuon_invMass_tightZ_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("abs(invMass(muon,muon) - 91.2) < 2.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("abs(mass_mumu - mass_Z) < 2.5")
    )

diMuon_invMass_OutsideZWindow_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("abs(invMass (muon,muon) - 91 > 15.0)"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("dimuon invariant mass < 76 GeV OR > 106 GeV")
    )

diMuon_invMass_BelowZWindow_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("invMass (muon,muon) < 76.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("dimuon invariant mass < 76.2")
    )

diMuon_invMass_AboveZWindow_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("invMass (muon,muon) > 106.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("dimuon invariant mass > 106.2")
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
    cutString = cms.string("deltaR(muon, muon) > 0.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 mu-mu pair with #DeltaR > 0.2")
    )

diMuon_invertedDeltaR_cut = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("deltaR(muon, muon) <= 0.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 mu-mu pair with #DeltaR <= 0.2")
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

tagMuon_d0_greaterThan100_cut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("10000*abs(eventvariable.tagMuonUnsmearedD0) > 100"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("tag muon |d0| > 100um")
    )

tagMuon_d0_greaterThan500_cut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("10000*abs(eventvariable.tagMuonUnsmearedD0) > 500"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("tag muon |d0| > 500um")
    )

tagMuon_d0_lessThan40_cut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("10000*abs(eventvariable.tagMuonUnsmearedD0) < 40"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("tag muon |d0| < 40um")
    )

muon_onePrompt_oneDisplaced_cut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("(10000*abs(eventvariable.leadingMuonUnsmearedD0) < 40 &   \
                           10000*abs(eventvariable.subleadingMuonUnsmearedD0) > 100)  \
                           |                                                          \
                           (10000*abs(eventvariable.subleadingMuonUnsmearedD0) < 40 & \
                           10000*abs(eventvariable.leadingMuonUnsmearedD0) > 100)"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("one muon |d0| < 40um & another muon |d0| > 100um")
    )

muon_onePrompt_0to40_one_lessThan100_cut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("(10000*abs(eventvariable.leadingMuonUnsmearedD0) < 40 &   \
                           10000*abs(eventvariable.subleadingMuonUnsmearedD0) < 100)  \
                           |                                                          \
                           (10000*abs(eventvariable.subleadingMuonUnsmearedD0) < 40 & \
                           10000*abs(eventvariable.leadingMuonUnsmearedD0) < 100)"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("one muon |d0| < 40um & another muon |d0| < 100um")
    )

muon_onePrompt_0to40_oneDisplaced_100to500_cut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("(10000*abs(eventvariable.leadingMuonUnsmearedD0) < 40 &   \
                           (10000*abs(eventvariable.subleadingMuonUnsmearedD0) > 100 & 10000*abs(eventvariable.subleadingMuonUnsmearedD0) < 500))  \
                           |                                                          \
                           (10000*abs(eventvariable.subleadingMuonUnsmearedD0) < 40 & \
                           (10000*abs(eventvariable.leadingMuonUnsmearedD0) > 100 & 10000*abs(eventvariable.leadingMuonUnsmearedD0) < 500))"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("one muon |d0| < 40um & another muon 100 < |d0| < 500um")
    )

muon_onePrompt_0to40_oneDisplaced_500to1000_cut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("(10000*abs(eventvariable.leadingMuonUnsmearedD0) < 40 &   \
                           (10000*abs(eventvariable.subleadingMuonUnsmearedD0) > 500 & 10000*abs(eventvariable.subleadingMuonUnsmearedD0) < 1000))  \
                           |                                                          \
                           (10000*abs(eventvariable.subleadingMuonUnsmearedD0) < 40 & \
                           (10000*abs(eventvariable.leadingMuonUnsmearedD0) > 500 & 10000*abs(eventvariable.leadingMuonUnsmearedD0) < 1000))"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("one muon |d0| < 40um & another muon 500 < |d0| < 1000um")
    )

##########################################################################

# build cut to filter out electrons that would not pass the emu preselection
# don't include deltaR veto
from DisplacedSUSY.EMuChannel.Preselection import Preselection as emu_preselection
from DisplacedSUSY.Configuration.helperFunctions import make_selection_filter

alias = "filter electron collection to only include those that pass emu preselection electron cuts"
electron_emu_preselection_filter = make_selection_filter('electrons', emu_preselection, alias)
