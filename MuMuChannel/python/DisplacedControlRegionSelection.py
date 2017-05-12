import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

##########################################################################
### Set up the displaced control region for the displaced SUSY analysis #####
##########################################################################

DisplacedControlRegion = cms.PSet(
    name = cms.string("DisplacedControlRegion"),
    triggers = cms.vstring("HLT_DoubleMu33NoFiltersNoVtx_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
DisplacedControlRegion.cuts.append(jet_eta_cut)
DisplacedControlRegion.cuts.append(jet_pt_30_cut)
DisplacedControlRegion.cuts.append(jet_id_cut)
### at least two good muons
DisplacedControlRegion.cuts.append(muon_eta_cut)
DisplacedControlRegion.cuts.append(muon_pt_40_cut)
DisplacedControlRegion.cuts.append(muon_global_cut)
DisplacedControlRegion.cuts.append(muon_id_cut)
DisplacedControlRegion.cuts.append(muon_iso_cut)
### require displaced leptons
DisplacedControlRegion.cuts.append(muon_d0_100to200_cut)

