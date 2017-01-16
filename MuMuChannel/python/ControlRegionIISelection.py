import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

##########################################################################
### Set up the prompt control region for the displaced SUSY analysis #####
##########################################################################

##########################################################################
#Selections without triggers

ControlRegionII = cms.PSet(
    name = cms.string("ControlRegionII"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
ControlRegionII.cuts.append(jet_eta_cut)
ControlRegionII.cuts.append(jet_pt_30_cut)
ControlRegionII.cuts.append(jet_id_cut)
### at least one good electron
#ControlRegionII.cuts.append(electron_eta_cut)
#ControlRegionII.cuts.append(electron_gap_veto)
#ControlRegionII.cuts.append(electron_pt_42_cut)
#ControlRegionII.cuts.append(electron_id_cut)
#ControlRegionII.cuts.append(electron_iso_cut)
### at least two good muons
ControlRegionII.cuts.append(muon_eta_cut)
ControlRegionII.cuts.append(muon_pt_40_cut)
ControlRegionII.cuts.append(muon_global_cut)
ControlRegionII.cuts.append(muon_id_cut)
ControlRegionII.cuts.append(muon_iso_cut)
### require prompt leptons
#ControlRegionII.cuts.append(electron_d0_lt100_cut)
#ControlRegionII.cuts.append(muon_d0_lt100_cut)
### require lepton d0 in CRII range
ControlRegionII.cuts.append(muon_d0_above100_cut)
ControlRegionII.cuts.append(muon_d0_below200_cut)
