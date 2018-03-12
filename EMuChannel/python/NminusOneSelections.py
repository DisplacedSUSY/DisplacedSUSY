import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

##########################################################################
### Set up the prompt control region for the displaced SUSY analysis #####
##########################################################################

##########################################################################

PromptControlRegionNoElectronIso = cms.PSet(
    name = cms.string("PromptControlRegionNoElectronIso"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
PromptControlRegionNoElectronIso.cuts.append(jet_eta_cut)
PromptControlRegionNoElectronIso.cuts.append(jet_pt_30_cut)
PromptControlRegionNoElectronIso.cuts.append(jet_id_cut)
### at least one good electron
PromptControlRegionNoElectronIso.cuts.append(electron_eta_cut)
PromptControlRegionNoElectronIso.cuts.append(electron_gap_veto)
PromptControlRegionNoElectronIso.cuts.append(electron_pt_42_cut)
PromptControlRegionNoElectronIso.cuts.append(electron_id_cut)
#PromptControlRegionNoElectronIso.cuts.append(electron_iso_cut)
### at least one good muon
PromptControlRegionNoElectronIso.cuts.append(muon_eta_cut)
PromptControlRegionNoElectronIso.cuts.append(muon_pt_40_cut)
PromptControlRegionNoElectronIso.cuts.append(muon_global_cut)
PromptControlRegionNoElectronIso.cuts.append(muon_id_cut)
PromptControlRegionNoElectronIso.cuts.append(muon_iso_cut)
### require prompt leptons
PromptControlRegionNoElectronIso.cuts.append(electron_d0_lessThan100_cut)
PromptControlRegionNoElectronIso.cuts.append(muon_d0_lessThan100_cut)

##########################################################################

PromptControlRegionNoElectronID = cms.PSet(
    name = cms.string("PromptControlRegionNoElectronID"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
PromptControlRegionNoElectronID.cuts.append(jet_eta_cut)
PromptControlRegionNoElectronID.cuts.append(jet_pt_30_cut)
PromptControlRegionNoElectronID.cuts.append(jet_id_cut)
### at least one good electron
PromptControlRegionNoElectronID.cuts.append(electron_eta_cut)
PromptControlRegionNoElectronID.cuts.append(electron_gap_veto)
PromptControlRegionNoElectronID.cuts.append(electron_pt_42_cut)
#PromptControlRegionNoElectronID.cuts.append(electron_id_cut)
PromptControlRegionNoElectronID.cuts.append(electron_iso_cut)
### at least one good muon
PromptControlRegionNoElectronID.cuts.append(muon_eta_cut)
PromptControlRegionNoElectronID.cuts.append(muon_pt_40_cut)
PromptControlRegionNoElectronID.cuts.append(muon_global_cut)
PromptControlRegionNoElectronID.cuts.append(muon_id_cut)
PromptControlRegionNoElectronID.cuts.append(muon_iso_cut)
### require prompt leptons
PromptControlRegionNoElectronID.cuts.append(electron_d0_lessThan100_cut)
PromptControlRegionNoElectronID.cuts.append(muon_d0_lessThan100_cut)

##########################################################################
##########################################################################

PromptControlRegionNoMuonIso = cms.PSet(
    name = cms.string("PromptControlRegionNoMuonIso"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
PromptControlRegionNoMuonIso.cuts.append(jet_eta_cut)
PromptControlRegionNoMuonIso.cuts.append(jet_pt_30_cut)
PromptControlRegionNoMuonIso.cuts.append(jet_id_cut)
### at least one good electron
PromptControlRegionNoMuonIso.cuts.append(electron_eta_cut)
PromptControlRegionNoMuonIso.cuts.append(electron_gap_veto)
PromptControlRegionNoMuonIso.cuts.append(electron_pt_42_cut)
PromptControlRegionNoMuonIso.cuts.append(electron_id_cut)
PromptControlRegionNoMuonIso.cuts.append(electron_iso_cut)
### at least one good muon
PromptControlRegionNoMuonIso.cuts.append(muon_eta_cut)
PromptControlRegionNoMuonIso.cuts.append(muon_pt_40_cut)
PromptControlRegionNoMuonIso.cuts.append(muon_global_cut)
PromptControlRegionNoMuonIso.cuts.append(muon_id_cut)
#PromptControlRegionNoMuonIso.cuts.append(muon_iso_cut)
### require prompt leptons
PromptControlRegionNoMuonIso.cuts.append(electron_d0_lessThan100_cut)
PromptControlRegionNoMuonIso.cuts.append(muon_d0_lessThan100_cut)


PromptControlRegionNoMuonID = cms.PSet(
    name = cms.string("PromptControlRegionNoMuonID"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
PromptControlRegionNoMuonID.cuts.append(jet_eta_cut)
PromptControlRegionNoMuonID.cuts.append(jet_pt_30_cut)
PromptControlRegionNoMuonID.cuts.append(jet_id_cut)
### at least one good electron
PromptControlRegionNoMuonID.cuts.append(electron_eta_cut)
PromptControlRegionNoMuonID.cuts.append(electron_gap_veto)
PromptControlRegionNoMuonID.cuts.append(electron_pt_42_cut)
#PromptControlRegionNoMuonID.cuts.append(electron_id_cut)
PromptControlRegionNoMuonID.cuts.append(electron_iso_cut)
### at least one good muon
PromptControlRegionNoMuonID.cuts.append(muon_eta_cut)
PromptControlRegionNoMuonID.cuts.append(muon_pt_40_cut)
PromptControlRegionNoMuonID.cuts.append(muon_global_cut)
#PromptControlRegionNoMuonID.cuts.append(muon_id_cut)
PromptControlRegionNoMuonID.cuts.append(muon_iso_cut)
### require prompt leptons
PromptControlRegionNoMuonID.cuts.append(electron_d0_lessThan100_cut)
PromptControlRegionNoMuonID.cuts.append(muon_d0_lessThan100_cut)

