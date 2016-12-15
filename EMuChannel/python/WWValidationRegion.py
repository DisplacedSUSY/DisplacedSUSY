import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

##########################################################################
### Set up the WW validation region
##########################################################################

# we'll look in the 0-jet bin

##########################################################################
#Selections without triggers

WWValidationRegion = cms.PSet(
    name = cms.string("WWValidationRegion"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
WWValidationRegion.cuts.append(jet_eta_cut)
WWValidationRegion.cuts.append(jet_pt_30_cut)
WWValidationRegion.cuts.append(jet_id_cut)
### at least one good electron
WWValidationRegion.cuts.append(electron_eta_cut)
WWValidationRegion.cuts.append(electron_gap_veto)
WWValidationRegion.cuts.append(electron_pt_42_cut)
WWValidationRegion.cuts.append(electron_id_cut)
WWValidationRegion.cuts.append(electron_iso_cut)
### at least one good muon
WWValidationRegion.cuts.append(muon_eta_cut)
WWValidationRegion.cuts.append(muon_pt_40_cut)
WWValidationRegion.cuts.append(muon_global_cut)
WWValidationRegion.cuts.append(muon_id_cut)
WWValidationRegion.cuts.append(muon_iso_cut)
### require prompt leptons
WWValidationRegion.cuts.append(electron_d0_lt100_cut)
WWValidationRegion.cuts.append(muon_d0_lt100_cut)
### ww-enriching cuts
#WWValidationRegion.cuts.append(jet_btag_lwp_veto)
#WWValidationRegion.cuts.append(jet_2jet_veto)
WWValidationRegion.cuts.append(jet_veto)
WWValidationRegion.cuts.append(emu_pt_gt50_cut)
WWValidationRegion.cuts.append(met_gt60_cut)
