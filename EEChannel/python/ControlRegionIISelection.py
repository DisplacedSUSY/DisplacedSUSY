import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

##########################################################################
####### Set up control region II for the displaced SUSY analysis #########
##########################################################################

##########################################################################
#Selections without triggers

ControlRegionII = cms.PSet(
    name = cms.string("ControlRegionII"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
PromptControlRegion.cuts.append(jet_eta_cut)
PromptControlRegion.cuts.append(jet_pt_30_cut)
PromptControlRegion.cuts.append(jet_id_cut)
### at least two good electrons
PromptControlRegion.cuts.append(electron_eta_cut)
PromptControlRegion.cuts.append(electron_gap_veto)
PromptControlRegion.cuts.append(electron_pt_42_cut)
PromptControlRegion.cuts.append(electron_id_cut)
PromptControlRegion.cuts.append(electron_iso_cut)
### at least two good muons
#PromptControlRegion.cuts.append(muon_eta_cut)
#PromptControlRegion.cuts.append(muon_pt_40_cut)
#PromptControlRegion.cuts.append(muon_global_cut)
#PromptControlRegion.cuts.append(muon_id_cut)
#PromptControlRegion.cuts.append(muon_iso_cut)
### require prompt leptons
#PromptControlRegion.cuts.append(electron_d0_lt100_cut)
#PromptControlRegion.cuts.append(muon_d0_lt100_cut)
### require lepton d0 in CRII range
PromptControlRegion.cuts.append(electron_d0_above100_cut)
PromptControlRegion.cuts.append(electron_d0_below200_cut)

