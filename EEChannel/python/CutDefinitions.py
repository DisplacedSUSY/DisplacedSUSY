import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.BasicSelections import *
from DisplacedSUSY.StandardAnalysis.ElectronIdCutDefinitions import *

##########################################################################

# CHANGE ELECTRON CUTS TO >=2 ELECTRONS

electron_eta_cut.numberRequired = cms.string(">= 2")

electron_gap_veto.numberRequired = cms.string(">= 2")
electron_gap_veto.alias = cms.string(">=2 electrons surviving ECAL crack veto")

electron_eta_phi_veto_2017.numberRequired = cms.string(">= 2")
electron_eta_phi_veto_2017.alias = cms.string(">= 2 electrons not in region affected by 2017 pixel power supply issues")

electron_eta_phi_veto_2018.numberRequired = cms.string(">= 2")
electron_eta_phi_veto_2018.alias = cms.string(">= 2 electrons not in region affected by 2018 pixel power supply issues")

electron_pt_100_cut.numberRequired = cms.string(">= 2")
electron_pt_75_cut.numberRequired = cms.string(">= 2")
electron_pt_65_cut.numberRequired = cms.string(">= 2")
electron_pt_45_cut.numberRequired = cms.string(">= 2")
electron_pt_42_cut.numberRequired = cms.string(">= 2")
electron_pt_30_cut.numberRequired = cms.string(">= 2")
electron_pt_25_cut.numberRequired = cms.string(">= 2")

electron_id_cut.numberRequired = cms.string(">= 2")
electron_id_cut.alias = cms.string(">=2 electrons with versioned tight ID")

electron_iso_cut.numberRequired = cms.string(">= 2")
electron_iso_cut.alias = cms.string(">=2 electrons with (old) tight isolation")

electron_newIso_cut.numberRequired = cms.string(">= 2")
electron_newIso_cut.alias = cms.string(">=2 electrons with tight rho-based isolation")

electron_antiNewIso_cut.numberRequired = cms.string(">= 2")
electron_antiNewIso_cut.alias = cms.string(">=2 electrons with inverted tight rho-based isolation")

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

electron_absD0Pull_lessThan50_cut.numberRequired = cms.string(">= 2")
electron_absD0Pull_lessThan50_cut.alias = cms.string(">=2 electrons with |d_0| - |gen d_0| < 50 mum")

electron_gen_motherIsW_cut.numberRequired = cms.string(">= 2")
electron_gen_motherIsW_cut.alias = cms.string(">=2 electrons from W (electron matched to gen particle whose mother has PDG ID of 24)")

electron_gen_motherIsWorZ_cut.numberRequired = cms.string(">= 2")
electron_gen_motherIsWorZ_cut.alias = cms.string(">=2 electrons from W or Z (electron matched to gen particle whose mother's PDG ID is 23 or 24)")

electron_gen_motherIsTau_cut.numberRequired = cms.string(">= 2")
electron_gen_motherIsTau_cut.alias = cms.string(">=2 electrons from tau (electron matched to gen particle whose mother has PDG ID of 15)")

electron_gen_motherIsNotTau_cut.numberRequired = cms.string(">= 2")
electron_gen_motherIsNotTau_cut.alias = cms.string(">=2 electrons not from tau (electron matched to gen particle whose mother's PDG ID is not 15)")

electron_gen_motherIsLightMeson_cut.numberRequired = cms.string(">= 2")
electron_gen_motherIsLightMeson_cut.alias = cms.string(">=2 electrons from light mesons (electron matched to gen particle whose mother has 111 <= PDG ID < 400)")

electron_gen_motherIsHeavyMeson_cut.numberRequired = cms.string(">= 2")
electron_gen_motherIsHeavyMeson_cut.alias = cms.string(">=2 electrons from heavy mesons (electron matched to gen particle whose mother has 400 < PDG ID < 600)")

electron_fiducial_phi_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(abs(electron.phi)-3.14159/2) > 0.05"),
    numberRequired = cms.string(">= 2")
    )

electron_2electron_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("electron.pt > -1"),
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
    cutString = cms.string("deltaR(electron, electron) > 0.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 e-e pair with #DeltaR > 0.2")
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

electron_onePrompt_oneDisplaced_cut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("(10000*abs(eventvariable.leadingElectronUnsmearedD0) < 40 &   \
                           10000*abs(eventvariable.subleadingElectronUnsmearedD0) > 100)  \
                           |                                                          \
                           (10000*abs(eventvariable.subleadingElectronUnsmearedD0) < 40 & \
                           10000*abs(eventvariable.leadingElectronUnsmearedD0) > 100)"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("one electron |d0| < 40um & another electron |d0| > 100um")
    )

electron_onePrompt_0to40_one_lessThan100_cut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("(10000*abs(eventvariable.leadingElectronUnsmearedD0) < 40 &   \
                           10000*abs(eventvariable.subleadingElectronUnsmearedD0) < 100)  \
                           |                                                          \
                           (10000*abs(eventvariable.subleadingElectronUnsmearedD0) < 40 & \
                           10000*abs(eventvariable.leadingElectronUnsmearedD0) < 100)"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("one electron |d0| < 40um & another electron |d0| < 100um")
    )

electron_onePrompt_0to40_oneDisplaced_100to500_cut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("(10000*abs(eventvariable.leadingElectronUnsmearedD0) < 40 &   \
                           (10000*abs(eventvariable.subleadingElectronUnsmearedD0) > 100 & 10000*abs(eventvariable.subleadingElectronUnsmearedD0) < 500))  \
                           |                                                          \
                           (10000*abs(eventvariable.subleadingElectronUnsmearedD0) < 40 & \
                           (10000*abs(eventvariable.leadingElectronUnsmearedD0) > 100 & 10000*abs(eventvariable.leadingElectronUnsmearedD0) < 500))"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("one electron |d0| < 40um & another electron 100 < |d0| < 500um")
    )

electron_onePrompt_0to40_oneDisplaced_500to1000_cut = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("(10000*abs(eventvariable.leadingElectronUnsmearedD0) < 40 &   \
                           (10000*abs(eventvariable.subleadingElectronUnsmearedD0) > 500 & 10000*abs(eventvariable.subleadingElectronUnsmearedD0) < 1000))  \
                           |                                                          \
                           (10000*abs(eventvariable.subleadingElectronUnsmearedD0) < 40 & \
                           (10000*abs(eventvariable.leadingElectronUnsmearedD0) > 500 & 10000*abs(eventvariable.leadingElectronUnsmearedD0) < 1000))"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("one electron |d0| < 40um & another electron 500 < |d0| < 1000um")
    )

##########################################################################

# build cut to filter out muons that would not pass the emu preselection
# don't include cosmic or deltaR vetos
from DisplacedSUSY.EMuChannel.Preselection import Preselection as emu_preselection
from DisplacedSUSY.Configuration.helperFunctions import make_selection_filter

# break emu preselection into two parts because some cut attributes only exist for global muons
muon_id_cut_ix = emu_preselection.cuts.index(muon_id_cut)
cuts_part1 = emu_preselection.cuts[:muon_id_cut_ix]
cuts_part2 = emu_preselection.cuts[muon_id_cut_ix:]
emu_preselection_part1 = copy.deepcopy(emu_preselection)
emu_preselection_part2 = copy.deepcopy(emu_preselection)
removeCuts(emu_preselection_part1.cuts, cuts_part2)
removeCuts(emu_preselection_part2.cuts, cuts_part1)

alias1 = "filter muon collection to only include those that pass emu preselection muon cuts, part 1"
muon_emu_preselection_filter_part1 = make_selection_filter('muons', emu_preselection_part1, alias1)
alias2 = "filter muon collection to only include those that pass emu preselection muon cuts, part 2"
muon_emu_preselection_filter_part2 = make_selection_filter('muons', emu_preselection_part2, alias2)




#electron tight id cuts, explicitly
##########################################################################################
#barrel or endcap
electron_isEB_cut.numberRequired = cms.string(">= 2")
electron_isEB_cut.alias = cms.string(">= 2 electrons in the barrel (|eta supercluster| <= 1.479)")

electron_isEE_cut.numberRequired = cms.string(">= 2")
electron_isEE_cut.alias = cms.string(">= 1 electrons in the endcaps (|eta supercluster| > 1.479)")

##########################################################################################
#sigmaIetaIeta
electron_sigmaIetaIetaEB_cut.numberRequired = cms.string(">= 2")
electron_sigmaIetaIetaEB_cut.alias = cms.string(">= 2 electrons with full5x5_sigmaIetaIeta < 0.00998")
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_sigmaIetaIetaEB_cut.alias = ">= 2 electrons with full5x5_sigmaIetaIeta < 0.0104"

electron_sigmaIetaIetaEE_cut.numberRequired = cms.string(">= 2")
electron_sigmaIetaIetaEE_cut.alias = cms.string(">= 2 electrons with full5x5_sigmaIetaIeta < 0.0292")
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_sigmaIetaIetaEE_cut.alias = ">= 2 electrons with full5x5_sigmaIetaIeta < 0.0165"

##########################################################################################

#delta phi supercluster track at vtx
electron_deltaPhiSuperClusterEB_cut.numberRequired = cms.string(">= 1")
electron_deltaPhiSuperClusterEB_cut.alias = cms.string(">= 2 electrons with abs(deltaPhiSuperClusterTrackAtVtx) < 0.0816")
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_deltaPhiSuperClusterEB_cut.alias = ">= 2 electrons with abs(deltaPhiSuperClusterTrackAtVtx) < 0.0499"

electron_deltaPhiSuperClusterEE_cut.numberRequired = cms.string(">= 2")
electron_deltaPhiSuperClusterEE_cut.alias = cms.string(">= 2 electrons with abs(deltaPhiSuperClusterTrackAtVtx) < 0.0394")
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_deltaPhiSuperClusterEE_cut.alias = ">= 2 electrons with abs(deltaPhiSuperClusterTrackAtVtx) < 0.0499"

##########################################################################################
#delta eta super cluster track at vtx
electron_deltaEtaSuperClusterEB_cut.numberRequired = cms.string(">= 2")
electron_deltaEtaSuperClusterEB_cut.alias = cms.string(">= 2 electrons with abs(deltaEtaSuperClusterTrackAtVtx) < 0.00308")
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_deltaEtaSuperClusterEB_cut.alias = ">= 2 electrons with abs(deltaEtaSuperClusterTrackAtVtx) < 0.00353"

electron_deltaEtaSuperClusterEE_cut.numberRequired = cms.string(">= 2")
electron_deltaEtaSuperClusterEE_cut.alias = cms.string(">= 2 electrons with abs(deltaEtaSuperClusterTrackAtVtx) < 0.00605")
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_deltaEtaSuperClusterEE_cut.alias = ">= 2 electrons with abs(deltaEtaSuperClusterTrackAtVtx) < 0.00567"

##########################################################################################

#hadronicOverEm
electron_hadronicOverEmEB_cut.numberRequired = cms.string(">= 2")
electron_hadronicOverEmEB_cut.alias = cms.string(">= 2 electrons with hadronicOverEm < 0.0414")
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_hadronicOverEmEB_cut.alias = ">= 2 electrons with hadronicOverEm < 0.026 + 1.12/ecalEnergy + 0.0368*rho/ecalEnergy"

electron_hadronicOverEmEE_cut.numberRequired = cms.string(">= 2")
electron_hadronicOverEmEE_cut.alias = cms.string(">= 2 electrons with hadronicOverEm < 0.0641")
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_hadronicOverEmEE_cut.alias = ">= 2 electrons with hadronicOverEm < 0.026 + 0.5/ecalEnergy + 0.201*rho/ecalEnergy"

##########################################################################################
#abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy)
#same for EB and EE for 2016
electron_abs_1overE_1overP_cut.numberRequired = cms.string(">= 2")
electron_abs_1overE_1overP_cut.alias = cms.string(">= 2 electrons with abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.0129")

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_abs_1overE_1overP_EB_cut.numberRequired = cms.string(">= 2")
    electron_abs_1overE_1overP_EB_cut.alias = cms.string(">= 2 electrons with abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.0278")
    electron_abs_1overE_1overP_EE_cut.numberRequired = cms.string(">= 2")
    electron_abs_1overE_1overP_EE_cut.alias = cms.string(">= 2 electrons with abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.0158")

##########################################################################################
#missingInnerHits
#same for EB and EE
electron_missingInnerHits_cut.numberRequired = cms.string(">= 2")
electron_missingInnerHits_cut.alias = cms.string(">= 2 electrons with missing inner hits <= 1")

##########################################################################################
#passConversionVeto
#same for EB and EE
electron_passConversionVeto_cut.numberRequired = cms.string(">= 2")
electron_passConversionVeto_cut.alias = cms.string(">= 2 electrons that pass conversion veto")
