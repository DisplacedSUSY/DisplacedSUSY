import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

##########################################################################
### Set up the Ztautau validation region
##########################################################################

# Prompt Control Region with lepton-met mass < 50 and dilepton mass < 100

##########################################################################
#Selections without triggers

ZtautauValidationRegion = cms.PSet(
    name = cms.string("ZtautauValidationRegion"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
ZtautauValidationRegion.cuts.append(jet_eta_cut)
ZtautauValidationRegion.cuts.append(jet_pt_30_cut)
ZtautauValidationRegion.cuts.append(jet_id_cut)
### at least one good electron
ZtautauValidationRegion.cuts.append(electron_eta_cut)
ZtautauValidationRegion.cuts.append(electron_gap_veto)
ZtautauValidationRegion.cuts.append(electron_pt_42_cut)
ZtautauValidationRegion.cuts.append(electron_id_cut)
ZtautauValidationRegion.cuts.append(electron_iso_cut)
### at least one good muon
ZtautauValidationRegion.cuts.append(muon_eta_cut)
ZtautauValidationRegion.cuts.append(muon_pt_40_cut)
ZtautauValidationRegion.cuts.append(muon_global_cut)
ZtautauValidationRegion.cuts.append(muon_id_cut)
ZtautauValidationRegion.cuts.append(muon_iso_cut)
### require prompt leptons
ZtautauValidationRegion.cuts.append(electron_d0_lt100_cut)
ZtautauValidationRegion.cuts.append(muon_d0_lt100_cut)
### ztautau-enriching cuts
ZtautauValidationRegion.cuts.append(electron_mt_cut)
ZtautauValidationRegion.cuts.append(muon_mt_cut)
ZtautauValidationRegion.cuts.append(emu_mass_lt100_cut)
ZtautauValidationRegion.cuts.append(jet_btag_lwp_veto)

