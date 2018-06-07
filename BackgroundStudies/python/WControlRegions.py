import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.BackgroundStudies.CutDefinitions import *

##############################################################
##### EVENT SELECTIONS FOR OUR QCD B-BBAR CONTROL REGIONS ####
##############################################################

Wjets_Muon_Selection = cms.PSet(
    name = cms.string("Wjets_Muon_Selection"),
    triggers = triggersIsoSingleMuon,
    cuts = cms.VPSet (
        FilterOutScraping_cut,
        atLeastOne_goodPV_cut,
        muon_eta_cut,
        muon_pt_35_cut,
        muon_iso_cut,
        muon_id_cut,
        muon_id_impact_parameter_cut,
        muon_num_exactly_1_cut,
        met_pt_40_cut,
        muon_mt_cut,
        atLeastZero_jet_pt_30_cut,
        )
    )

Wjets_Muon_Selection_WithBtagVeto = copy.deepcopy(Wjets_Muon_Selection)
Wjets_Muon_Selection_WithBtagVeto.name = cms.string("Wjets_Muon_Selection_WithBtagVeto")
Wjets_Muon_Selection_WithBtagVeto.cuts.append(jet_btag_lwp_veto)

Wjets_Muon_Selection_NearJetVeto = copy.deepcopy(Wjets_Muon_Selection_WithBtagVeto)
Wjets_Muon_Selection_WithBtagVeto.name = cms.string("Wjets_Muon_Selection_NearJetVeto")
Wjets_Muon_Selection_NearJetVeto.cuts.append(muon_jet_deltaR_overlap_veto)

##############################################################

Wjets_Electron_Selection = cms.PSet(
    name = cms.string("Wjets_Electron_Selection"),
    triggers = cms.vstring(), #??
    cuts = cms.VPSet (
        FilterOutScraping_cut,
        atLeastOne_goodPV_cut,
        electron_eta_cut,
        electron_gap_veto,
        electron_pt_25_cut,
        electron_id_cut, #electron vid includes isolation
        electron_id_impact_parameter_cut,
        electron_num_exactly_1_cut,
        met_pt_40_cut,
        electron_mt_cut,
        atLeastZero_jet_pt_30_cut,
    )
)


