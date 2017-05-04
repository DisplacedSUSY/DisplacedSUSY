import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

##########################################################################
### Set up the displaced control region for the displaced SUSY analysis #####
##########################################################################

AntiIsoDisplacedControlRegion = cms.PSet(
    name = cms.string("AntiIsoDisplacedControlRegion"),
    triggers = cms.vstring("HLT_DoubleMu33NoFiltersNoVtx_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
AntiIsoDisplacedControlRegion.cuts.append(jet_eta_cut)
AntiIsoDisplacedControlRegion.cuts.append(jet_pt_30_cut)
AntiIsoDisplacedControlRegion.cuts.append(jet_id_cut)
### at least two good muons
AntiIsoDisplacedControlRegion.cuts.append(muon_eta_cut)
AntiIsoDisplacedControlRegion.cuts.append(muon_pt_40_cut)
AntiIsoDisplacedControlRegion.cuts.append(muon_global_cut)
AntiIsoDisplacedControlRegion.cuts.append(muon_id_cut)
AntiIsoDisplacedControlRegion.cuts.append(muon_antiiso_cut)
### require displaced leptons
AntiIsoDisplacedControlRegion.cuts.append(muon_d0_100to200_cut)

