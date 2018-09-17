import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.CutDefinitions import *
from DisplacedSUSY.StandardAnalysis.Triggers import *

NoSelection = cms.PSet(
    name = cms.string("NoSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)

##########################################################################

#Gen particles selections (just for signal checks, not in analysis event selection)
GenElectronsFromStopsSelection = cms.PSet(
    name = cms.string("GenElectronsFromStopsSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet([genEleId_cut,
                      gen_motherIsStopId_cut
                      ])
    )

GenMuonsFromStopsSelection = cms.PSet(
    name = cms.string("GenMuonsFromStopsSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet([genMuId_cut,
                      gen_motherIsStopId_cut
                      ])
    )

##########################################################################

#Basic jet selections
atLeastZero_jet_basic_selection_cuts = cms.VPSet()
atLeastZero_jet_basic_selection_cuts.append(atLeastZero_jet_eta_cut)
atLeastZero_jet_basic_selection_cuts.append(atLeastZero_jet_pt_30_cut)
atLeastZero_jet_basic_selection_cuts.append(atLeastZero_jet_id_cut)

atLeastOne_jet_basic_selection_cuts = cms.VPSet()
atLeastOne_jet_basic_selection_cuts.append(atLeastOne_jet_eta_cut)
atLeastOne_jet_basic_selection_cuts.append(atLeastOne_jet_pt_30_cut)
atLeastOne_jet_basic_selection_cuts.append(atLeastOne_jet_id_cut)

atLeastTwo_jet_basic_selection_cuts = cms.VPSet()
atLeastTwo_jet_basic_selection_cuts.append(atLeastTwo_jet_eta_cut)
atLeastTwo_jet_basic_selection_cuts.append(atLeastTwo_jet_pt_30_cut)
atLeastTwo_jet_basic_selection_cuts.append(atLeastTwo_jet_id_cut)

##########################################################################

#Basic bjet selections
atLeastZero_bjet_basic_selection_cuts = cms.VPSet()
atLeastZero_bjet_basic_selection_cuts.append(atLeastZero_bjet_eta_cut)
atLeastZero_bjet_basic_selection_cuts.append(atLeastZero_bjet_pt_30_cut)
atLeastZero_bjet_basic_selection_cuts.append(atLeastZero_bjet_id_cut)

atLeastOne_bjet_basic_selection_cuts = cms.VPSet()
atLeastOne_bjet_basic_selection_cuts.append(atLeastOne_bjet_eta_cut)
atLeastOne_bjet_basic_selection_cuts.append(atLeastOne_bjet_pt_30_cut)
atLeastOne_bjet_basic_selection_cuts.append(atLeastOne_bjet_id_cut)

##########################################################################

#Basic electron selections
atLeastOne_electron_basic_selection_cuts = cms.VPSet()
atLeastOne_electron_basic_selection_cuts.append(electron_eta_cut)
atLeastOne_electron_basic_selection_cuts.append(electron_gap_veto)
atLeastOne_electron_basic_selection_cuts.append(electron_pt_25_cut)
atLeastOne_electron_basic_selection_cuts.append(electron_id_cut)

##########################################################################

#Basic muon selections
atLeastOne_muon_basic_selection_cuts = cms.VPSet()
atLeastOne_muon_basic_selection_cuts.append(muon_eta_cut)
atLeastOne_muon_basic_selection_cuts.append(muon_pt_25_cut)
atLeastOne_muon_basic_selection_cuts.append(muon_global_cut)
atLeastOne_muon_basic_selection_cuts.append(muon_id_cut)
