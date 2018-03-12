import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.CutDefinitions import *

##########################################################################

#Basic jet selections
jet_basic_selection_cuts = cms.VPSet()
jet_basic_selection_cuts.append(jet_eta_cut)
jet_basic_selection_cuts.append(jet_pt_30_cut)
jet_basic_selection_cuts.append(jet_id_cut)

##########################################################################

#Basic bjet selections
bjet_basic_selection_cuts = cms.VPSet()
bjet_basic_selection_cuts.append(bjet_eta_cut)
bjet_basic_selection_cuts.append(bjet_pt_30_cut)
bjet_basic_selection_cuts.append(bjet_id_cut)

##########################################################################

#Basic electron selections
electron_basic_selection_cuts = cms.VPSet()
electron_basic_selection_cuts.append(electron_eta_cut)
electron_basic_selection_cuts.append(electron_gap_veto)
electron_basic_selection_cuts.append(electron_pt_25_cut)
electron_basic_selection_cuts.append(electron_id_cut)

##########################################################################

#Basic muon selections
muon_basic_selection_cuts = cms.VPSet()
muon_basic_selection_cuts.append(muon_eta_cut)
muon_basic_selection_cuts.append(muon_pt_25_cut)
muon_basic_selection_cuts.append(muon_global_cut)
muon_basic_selection_cuts.append(muon_id_cut)
