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
atLeastOne_electron_basic_selection_cuts.append(electron_id_cut)

##########################################################################

#Basic muon selections
atLeastOne_muon_basic_selection_cuts = cms.VPSet()
atLeastOne_muon_basic_selection_cuts.append(muon_eta_cut)
atLeastOne_muon_basic_selection_cuts.append(muon_global_cut)
atLeastOne_muon_basic_selection_cuts.append(muon_id_cut)

##########################################################################

#Basic photon selections
atLeastZero_photon_basic_selection_cuts = cms.VPSet()
atLeastZero_photon_basic_selection_cuts.append(photon_lwp_id_cut)
atLeastZero_photon_basic_selection_cuts.append(photon_noPixelSeed_cut)
#atLeastZero_photon_basic_selection_cuts.append(photon_genMatched_cut)

##########################################################################

#L1 prefiring check selections
L1PrefiringCheck_cuts = cms.VPSet()
L1PrefiringCheck_cuts.append(zero_jet_pt_100_cut)
L1PrefiringCheck_cuts.append(zero_jet_eta_greaterThan2p25_cut)
L1PrefiringCheck_cuts.append(zero_jet_eta_lessThan3_cut)

##########################################################################


bothStopRhadronsAre1000612 = cms.PSet(
    name = cms.string("bothStopRhadronsAre1000612"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
bothStopRhadronsAre1000612.cuts.append(cutDummy)
bothStopRhadronsAre1000612.cuts.append(bothStopRhadronsAre1000612_cut)

bothStopRhadronsAre1000622 = cms.PSet(
    name = cms.string("bothStopRhadronsAre1000622"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
bothStopRhadronsAre1000622.cuts.append(cutDummy)
bothStopRhadronsAre1000622.cuts.append(bothStopRhadronsAre1000622_cut)

bothStopRhadronsAre1000632 = cms.PSet(
    name = cms.string("bothStopRhadronsAre1000632"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
bothStopRhadronsAre1000632.cuts.append(cutDummy)
bothStopRhadronsAre1000632.cuts.append(bothStopRhadronsAre1000632_cut)

stopRhadron1000612or1000622 = cms.PSet(
    name = cms.string("stopRhadron1000612or1000622"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
stopRhadron1000612or1000622.cuts.append(cutDummy)
stopRhadron1000612or1000622.cuts.append(stopRhadron_1000612_or_1000622_cut)

stopRhadron1000612or1000632 = cms.PSet(
    name = cms.string("stopRhadron1000612or1000632"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
stopRhadron1000612or1000632.cuts.append(cutDummy)
stopRhadron1000612or1000632.cuts.append(stopRhadron_1000612_or_1000632_cut)

stopRhadron1000622or1000632 = cms.PSet(
    name = cms.string("stopRhadron1000622or1000632"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
stopRhadron1000622or1000632.cuts.append(cutDummy)
stopRhadron1000622or1000632.cuts.append(stopRhadron_1000622_or_1000632_cut)


stopRhadronEverythingElse = cms.PSet(
    name = cms.string("stopRhadronEverythingElse"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
stopRhadronEverythingElse.cuts.append(cutDummy)
stopRhadronEverythingElse.cuts.append(stopRhadronEverythingElse_cut)
