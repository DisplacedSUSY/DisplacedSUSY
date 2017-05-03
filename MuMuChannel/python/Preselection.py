import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

#################################################################
### Set up the preselection for the displaced SUSY analysis #####
#################################################################

Preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = cms.vstring("HLT_DoubleMu33NoFiltersNoVtx_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
Preselection.cuts.append(jet_eta_cut)
Preselection.cuts.append(jet_pt_30_cut)
Preselection.cuts.append(jet_id_cut)
### at least two good muons
Preselection.cuts.append(muon_eta_cut)
Preselection.cuts.append(muon_pt_40_cut)
Preselection.cuts.append(muon_global_cut)
Preselection.cuts.append(muon_id_cut)
Preselection.cuts.append(muon_iso_cut)


