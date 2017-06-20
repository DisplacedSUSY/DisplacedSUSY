import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

##########################################################################
### Set up the ZTauTau validation region
##########################################################################

# Prompt Control Region with lepton-met mass < 50 and dilepton mass < 100

##########################################################################
#Selections without triggers

ZTauTauValidationRegion = cms.PSet(
    name = cms.string("ZTauTauValidationRegion"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
ZTauTauValidationRegion.cuts.append(jet_eta_cut)
ZTauTauValidationRegion.cuts.append(jet_pt_30_cut)
ZTauTauValidationRegion.cuts.append(jet_id_cut)
### at least one good electron
ZTauTauValidationRegion.cuts.append(electron_eta_cut)
ZTauTauValidationRegion.cuts.append(electron_gap_veto)
ZTauTauValidationRegion.cuts.append(electron_pt_42_cut)
ZTauTauValidationRegion.cuts.append(electron_id_cut)
ZTauTauValidationRegion.cuts.append(electron_iso_cut)
### at least one good muon
ZTauTauValidationRegion.cuts.append(muon_eta_cut)
ZTauTauValidationRegion.cuts.append(muon_pt_40_cut)
ZTauTauValidationRegion.cuts.append(muon_global_cut)
ZTauTauValidationRegion.cuts.append(muon_id_cut)
ZTauTauValidationRegion.cuts.append(muon_iso_cut)
### require prompt leptons
ZTauTauValidationRegion.cuts.append(electron_d0_lt100_cut)
ZTauTauValidationRegion.cuts.append(muon_d0_lt100_cut)
### ztautau-enriching cuts
ZTauTauValidationRegion.cuts.append(electron_mt_cut)
ZTauTauValidationRegion.cuts.append(muon_mt_cut)
ZTauTauValidationRegion.cuts.append(emu_mass_lt100_cut)
ZTauTauValidationRegion.cuts.append(jet_btag_lwp_veto)

