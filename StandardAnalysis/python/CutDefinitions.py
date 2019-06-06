import FWCore.ParameterSet.Config as cms
import copy
import string

import DisplacedSUSY.StandardAnalysis.objectDefinitions as objectDefs
from OSUT3Analysis.Configuration.cutUtilities import *

#WE USE ETA 2.4 OFTEN
absEta_2p4_cutstring = cms.string("abs(eta) < 2.4")

#########################################################################
# weight selections to determine if they contribute to negative
# weighted event

lifetimeWeight_negative = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("lifetimeWeight < 0"),
    numberRequired = cms.string(">= 1"),
)

puScalingFactor_negative = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("puScalingFactor < 0"),
    numberRequired = cms.string(">= 1"),
)

##########################################################################

# BEGIN GEN PARTICLE CUTS
#just for checking signal, not used in analysis event selection
genEleId_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("abs ( pdgId ) == 11"),
    numberRequired = cms.string(">= 1"),
)

genMuId_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("abs ( pdgId ) == 13"),
    numberRequired = cms.string(">= 1"),
)

gen_motherIsStopId_cut = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    cutString = cms.string("abs (motherPdgId) == 1000006"),
    numberRequired = cms.string(">= 1"),
)

##########################################################################
# DUMMY CUT FOR PRODUCING FLOW CHART

cutDummyMet = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("noMuPt > -1"),
    numberRequired = cms.string(">= 1"),
)

cutDummy = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("No offline cuts")
)
##########################################################################

# level1 prefiring check cuts:
# https://twiki.cern.ch/twiki/bin/view/CMS/ExoPreapprovalChecklist
zero_jet_pt_100_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string("== 0")
    )

zero_jet_eta_greaterThan2p25_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) > 2.25"),
    numberRequired = cms.string("== 0")
    )

zero_jet_eta_lessThan3_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) < 3.0"),
    numberRequired = cms.string("== 0")
    )
##########################################################################

# BEGIN JET CUTS

atLeastZero_jet_eta_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = absEta_2p4_cutstring,
    numberRequired = cms.string(">= 0")
    )

atLeastZero_jet_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 0")
    )

atLeastZero_jet_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_id_cutstring,
    numberRequired = cms.string(">= 0"),
    alias = objectDefs.jet_id_alias
    )


atLeastOne_jet_eta_cut = copy.deepcopy(atLeastZero_jet_eta_cut)
atLeastOne_jet_eta_cut.numberRequired = cms.string(">= 1")

atLeastOne_jet_pt_30_cut = copy.deepcopy(atLeastZero_jet_pt_30_cut)
atLeastOne_jet_pt_30_cut.numberRequired = cms.string(">= 1")

atLeastOne_jet_id_cut = copy.deepcopy(atLeastZero_jet_id_cut)
atLeastOne_jet_id_cut.numberRequired = cms.string(">= 1")
atLeastOne_jet_id_cut.alias = cms.string(">=1 jets with ID against leptons")


atLeastTwo_jet_eta_cut = copy.deepcopy(atLeastZero_jet_eta_cut)
atLeastTwo_jet_eta_cut.numberRequired = cms.string(">= 2")

atLeastTwo_jet_pt_30_cut = copy.deepcopy(atLeastZero_jet_pt_30_cut)
atLeastTwo_jet_pt_30_cut.numberRequired = cms.string(">= 2")

atLeastTwo_jet_id_cut = copy.deepcopy(atLeastZero_jet_id_cut)
atLeastTwo_jet_id_cut.numberRequired = cms.string(">= 2")
atLeastTwo_jet_id_cut.alias = cms.string(">=2 jets with ID against leptons")

atLeastTwo_jet_loose_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_loose_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.jet_loose_id_alias
    )

atLeastTwo_jet_ttbar_paper_loose_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_ttbar_paper_loose_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.jet_ttbar_paper_loose_id_alias
    )

atLeastTwo_jet_lepton_cleaning_cut = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("matchedToLepton = 0"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string('>=2 jets not matched to leptons')
    )

veto_2orMore_jets = cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("< 2"),
        alias = cms.string('< 2 jets')
    )

veto_3orMore_jets = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 2")
    )


#BEGIN B-JET CUTS
atLeastZero_bjet_eta_cut = copy.deepcopy(atLeastZero_jet_eta_cut)
atLeastZero_bjet_eta_cut.inputCollection = cms.vstring("bjets")

atLeastZero_bjet_pt_30_cut = copy.deepcopy(atLeastZero_jet_pt_30_cut)
atLeastZero_bjet_pt_30_cut.inputCollection = cms.vstring("bjets")

atLeastZero_bjet_id_cut = copy.deepcopy(atLeastZero_jet_id_cut)
atLeastZero_bjet_id_cut.inputCollection = cms.vstring("bjets")
atLeastZero_bjet_id_cut.alias = cms.string(">=0 b-jets with ID against leptons")

atLeastOne_bjet_eta_cut = copy.deepcopy(atLeastOne_jet_eta_cut)
atLeastOne_bjet_eta_cut.inputCollection = cms.vstring("bjets")

atLeastOne_bjet_pt_30_cut = copy.deepcopy(atLeastOne_jet_pt_30_cut)
atLeastOne_bjet_pt_30_cut.inputCollection = cms.vstring("bjets")

atLeastOne_bjet_id_cut = copy.deepcopy(atLeastOne_jet_id_cut)
atLeastOne_bjet_id_cut.inputCollection = cms.vstring("bjets")
atLeastOne_bjet_id_cut.alias = cms.string(">=1 b-jets with ID against leptons")

veto_3orMore_bjets = cms.PSet(
    inputCollection = cms.vstring("bjets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 2")
    )

#BEGIN B-JET CombinedSecondaryVertexv2 CUTS
#FIXME: should be applied to "bjets" instead of "jets" ?
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
    alias = cms.string(">= 1 electrons not in ECAL crack")
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

electron_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1")
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

electron_pt_65_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 65"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_75_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 75"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string(">= 1")
    )

electron_pt_100_veto = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),
    alias = cms.string("electron pT > 100 GeV veto")
    )

electron_id_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("passesVID_tightID"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with versioned tight ID") #versioned tight ID normally includes tight isolation, but we remove it in customize.py so we can use the inverted isolation at times
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

electron_id_impact_parameter_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_id_impact_parameter_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.electron_id_impact_parameter_alias
    )

# electron d0 < 10 microns
electron_d0_lessThan10_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") < 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with |d_0| < 10 mum")
    )

# electron 10 < d0 < 20 microns
electron_d0_10to20_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 10 & 10000*abs("+electronSmearedD0WRTBeamspot+") < 20"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with 10 < |d_0| < 20 mum")
    )

# electron d0 < 20 microns
electron_d0_lessThan20_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") < 20"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| < 20 mum")
    )

# electron d0 > 20 microns
electron_d0_greaterThan20_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 20"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| > 20 mum")
    )

# electron d0 < 50 microns
electron_d0_lessThan50_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") < 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with |d_0| < 50 mum")
    )

# electron d0 > 50 microns
electron_d0_greaterThan50_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| > 50 mum")
    )

# electron d0 < 100 microns
electron_d0_lessThan100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with |d_0| < 100 mum")
    )

# electron d0 > 100 microns
electron_d0_greaterThan100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| > 100 mum")
    )

# electron 100 < d0 < 200 microns
electron_d0_100to200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 100 & 10000*abs("+electronSmearedD0WRTBeamspot+") < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with 100 < |d_0| < 200 mum")
    )

electron_d0_lessThan200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| < 200 mum")
    )

electron_d0_greaterThan100_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| > 100 mum")
    )

electron_d0_greaterThan200_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("10000*abs("+electronSmearedD0WRTBeamspot+") > 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons with |d_0| > 200 mum")
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

#####################
#BEGIN GEN ELECTRON CUTS

electron_gen_motherIsW_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(genMatchedParticle.bestMatch.mother_.pdgId) == 24"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electrons from W (electron matched to gen particle whose mother has PDG ID of 24)")
)

##########################################################################

# BEGIN MUON CUTS

muon_eta_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = absEta_2p4_cutstring,
    numberRequired = cms.string(">= 1")
    )

muon_eta_lessThan1_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(eta) < 1.0"),
    numberRequired = cms.string(">= 1")
    )

muon_eta_greaterThan1_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(eta) >= 1.0"),
    numberRequired = cms.string(">= 1")
    )

#####################################

muon_pt_20_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 20"),
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

muon_pt_30_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_35_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 35"),
    numberRequired = cms.string(">= 1")
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

muon_pt_55_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 55"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_70_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 70"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_100_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string(">= 1")
    )

muon_pt_100_veto = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),
    alias = cms.string("muon pT > 100 GeV veto")
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

muon_softID_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("isSoftMuonWRTVtx > 0"),
    numberRequired = cms.string(">= 1"),
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

# muon d0 < 10 microns
muon_d0_lessThan10_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") < 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| < 10 mum")
    )

# muon 10 < d0 < 20 microns
muon_d0_10to20_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 10 & 10000*abs("+muonSmearedD0WRTBeamspot+") < 20"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with 10 < |d_0| < 20 mum")
    )

# muon d0 < 40 microns
muon_d0_lessThan40_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") < 40"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| < 40 mum")
    )

# muon d0 > 40 microns
muon_d0_greaterThan40_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 40"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| > 40 mum")
    )

# muon d0 < 50 microns
muon_d0_lessThan50_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") < 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| < 50 mum")
    )

# muon d0 > 50 microns
muon_d0_greaterThan50_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| > 50 mum")
    )

# muon d0 < 100 microns
muon_d0_lessThan100_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| < 100 mum")
    )

# muon d0 > 100 microns
muon_d0_greaterThan100_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| > 100 mum")
    )

# muon 100 < d0 < 200 microns
muon_d0_100to200_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 100 & 10000*abs("+muonSmearedD0WRTBeamspot+") < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with 100 < |d_0| < 200 mum")
    )

muon_d0_lessThan200_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") < 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| < 200 mum")
    )

muon_d0_greaterThan200_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("10000*abs("+muonSmearedD0WRTBeamspot+") > 200"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| > 200 mum")
    )

muon_d0_lessThan2000_cut = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("abs("+muonSmearedD0WRTBeamspot+") < 0.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with |d_0| < 0.2 cm")
    )

muon_dZ_lessThan5000_cut = cms.PSet(
    inputCollection = cms.vstring("muons","primaryvertices"),
    cutString = cms.string("abs("+muonDZWRTBeamspot+") < 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons with dZ < 0.5 cm")
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

#####################
#BEGIN GEN MUON CUTS

muon_gen_motherIsW_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(genMatchedParticle.bestMatch.mother_.pdgId) == 24"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 muons from W (muon matched to gen particle whose mother has PDG ID of 24)")
)

##########################################################################

# BEGIN ELECTRON-MUON CUTS

emu_mass_20_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("invMass(electron,muon) > 20"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electron-muon pair with invariant mass > 20 GeV")
    )

emu_mass_lessThan100_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("invMass(electron,muon) < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 electron-muon pair with invariant mass < 100GeV")
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

emu_pt_greaterThan50_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("pT(electron,muon) > 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("pT(e,mu) > 50")
    )

emu_deltaR_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons"),
    cutString = cms.string("deltaR(electron,muon) > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 well separated e-mu pair (#DeltaR > 0.5)")
    )

emu_correlated_d0_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons","beamspots"),
    cutString = cms.string("abs(abs(10000*"+electronSmearedD0WRTBeamspot+") - abs(10000*"+muonSmearedD0WRTBeamspot+")) <= 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 e-mu pair w/ correlated |d0|")
    )

emu_uncorrelated_d0_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons","beamspots"),
    cutString = cms.string("abs(abs(10000*"+electronSmearedD0WRTBeamspot+") - abs(10000*"+muonSmearedD0WRTBeamspot+")) > 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 e-mu pair w/ uncorrelated |d0|")
    )

emu_correlated_genD0_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons","beamspots"),
    cutString = cms.string("abs(abs(10000*electron.genD0) - abs(10000*muon.genD0)) <= 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 e-mu pair w/ correlated |genD0|")
    )

emu_uncorrelated_genD0_cut = cms.PSet (
    inputCollection = cms.vstring("electrons", "muons","beamspots"),
    cutString = cms.string("abs(abs(10000*electron.genD0) - abs(10000*muon.genD0)) > 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">=1 e-mu pair w/ uncorrelated |genD0|")
    )


##########################################################################
# ELECTRON-JET OVERLAP VETO
electron_jet_deltaR_overlap_veto = cms.PSet (
        inputCollection = cms.vstring("electrons", "jets"),
        cutString = cms.string("deltaR(electron, jet) < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("electron near jet veto (#DeltaR < 0.5))")
)

##########################################################################
# MUON-JET OVERLAP VETO
muon_jet_deltaR_overlap_veto = cms.PSet (
        inputCollection = cms.vstring("muons", "jets"),
        cutString = cms.string("deltaR(muon, jet) < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("muon near jet veto (#DeltaR < 0.5)")
)

##########################################################################

# BEGIN MET CUTS

met_pt_40_cut = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("met > 40")
    )

met_pt_60_cut =  cms.PSet (
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

