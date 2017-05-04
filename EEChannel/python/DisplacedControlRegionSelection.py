import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EEChannel.CutDefinitions import *

##########################################################################
### Set up the displaced control region for the displaced SUSY analysis #####
##########################################################################

DisplacedControlRegion = cms.PSet(
    name = cms.string("DisplacedControlRegion"),
    triggers = cms.vstring("HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
DisplacedControlRegion.cuts.append(jet_eta_cut)
DisplacedControlRegion.cuts.append(jet_pt_30_cut)
DisplacedControlRegion.cuts.append(jet_id_cut)
### at least two good electrons
DisplacedControlRegion.cuts.append(electron_eta_cut)
DisplacedControlRegion.cuts.append(electron_gap_veto)
DisplacedControlRegion.cuts.append(electron_pt_42_cut)
DisplacedControlRegion.cuts.append(electron_id_cut)
DisplacedControlRegion.cuts.append(electron_iso_cut)
### require displaced leptons
DisplacedControlRegion.cuts.append(electron_d0_100to200_cut)
