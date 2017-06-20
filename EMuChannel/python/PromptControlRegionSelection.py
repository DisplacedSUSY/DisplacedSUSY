import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

##########################################################################
### Set up the prompt control region for the displaced SUSY analysis #####
##########################################################################

PromptControlRegion = cms.PSet(
    name = cms.string("PromptControlRegion"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"),
#    triggers = cms.vstring("HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
PromptControlRegion.cuts.append(jet_eta_cut)
PromptControlRegion.cuts.append(jet_pt_30_cut)
PromptControlRegion.cuts.append(jet_id_cut)
### at least one good electron
PromptControlRegion.cuts.append(electron_eta_cut)
PromptControlRegion.cuts.append(electron_gap_veto)
PromptControlRegion.cuts.append(electron_pt_42_cut)
PromptControlRegion.cuts.append(electron_id_cut)
PromptControlRegion.cuts.append(electron_iso_cut)
### at least one good muon
PromptControlRegion.cuts.append(muon_eta_cut)
PromptControlRegion.cuts.append(muon_pt_40_cut)
PromptControlRegion.cuts.append(muon_global_cut)
PromptControlRegion.cuts.append(muon_id_cut)
PromptControlRegion.cuts.append(muon_iso_cut)
### require prompt leptons
PromptControlRegion.cuts.append(electron_d0_lt100_cut)
PromptControlRegion.cuts.append(muon_d0_lt100_cut)

