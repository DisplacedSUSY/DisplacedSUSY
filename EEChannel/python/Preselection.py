import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EEChannel.CutDefinitions import *

#################################################################
### Set up the preselection for the displaced SUSY analysis #####
#################################################################

Preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = cms.vstring("HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
Preselection.cuts.append(jet_eta_cut)
Preselection.cuts.append(jet_pt_30_cut)
Preselection.cuts.append(jet_id_cut)
### at least two good electrons
Preselection.cuts.append(electron_eta_cut)
Preselection.cuts.append(electron_gap_veto)
Preselection.cuts.append(electron_pt_42_cut)
Preselection.cuts.append(electron_id_cut)
Preselection.cuts.append(electron_iso_cut)
