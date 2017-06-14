import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

##########################################################################
### Set up the TTbar validation regions
##########################################################################

# Prompt Control Region with at least one medium b-tag

##########################################################################
#Selections without triggers

TTbarValidationRegion = cms.PSet(
    name = cms.string("TTbarValidationRegion"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
TTbarValidationRegion.cuts.append(jet_eta_cut)
TTbarValidationRegion.cuts.append(jet_pt_30_cut)
TTbarValidationRegion.cuts.append(jet_id_cut)
### at least one good electron
TTbarValidationRegion.cuts.append(electron_eta_cut)
TTbarValidationRegion.cuts.append(electron_gap_veto)
TTbarValidationRegion.cuts.append(electron_pt_42_cut)
TTbarValidationRegion.cuts.append(electron_id_cut)
TTbarValidationRegion.cuts.append(electron_iso_cut)
### at least one good muon
TTbarValidationRegion.cuts.append(muon_eta_cut)
TTbarValidationRegion.cuts.append(muon_pt_40_cut)
TTbarValidationRegion.cuts.append(muon_global_cut)
TTbarValidationRegion.cuts.append(muon_id_cut)
TTbarValidationRegion.cuts.append(muon_iso_cut)
### require prompt leptons
TTbarValidationRegion.cuts.append(electron_d0_lt100_cut)
TTbarValidationRegion.cuts.append(muon_d0_lt100_cut)
### ttbar-enriching cuts
#TTbarValidationRegion.cuts.append(jet_btag_2_lwp_cut)
TTbarValidationRegion.cuts.append(jet_btag_mwp_cut)
