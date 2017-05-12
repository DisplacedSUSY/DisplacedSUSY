import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

##########################################################################
### Set up the prompt control region for the displaced SUSY analysis #####
##########################################################################

AntiIsoPromptControlRegion = cms.PSet(
    name = cms.string("AntiIsoPromptControlRegion"),
    triggers = cms.vstring("HLT_DoubleMu33NoFiltersNoVtx_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
AntiIsoPromptControlRegion.cuts.append(jet_eta_cut)
AntiIsoPromptControlRegion.cuts.append(jet_pt_30_cut)
AntiIsoPromptControlRegion.cuts.append(jet_id_cut)
### at least two good muons
AntiIsoPromptControlRegion.cuts.append(muon_eta_cut)
AntiIsoPromptControlRegion.cuts.append(muon_pt_40_cut)
AntiIsoPromptControlRegion.cuts.append(muon_global_cut)
AntiIsoPromptControlRegion.cuts.append(muon_id_cut)
AntiIsoPromptControlRegion.cuts.append(muon_antiiso_cut)
### require prompt leptons
AntiIsoPromptControlRegion.cuts.append(muon_d0_lt100_cut)
