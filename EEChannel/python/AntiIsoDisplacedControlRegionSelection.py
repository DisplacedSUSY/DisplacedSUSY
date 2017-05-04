import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EEChannel.CutDefinitions import *

##########################################################################
### Set up the displaced control region for the displaced SUSY analysis #####
##########################################################################

AntiIsoDisplacedControlRegion = cms.PSet(
    name = cms.string("AntiIsoDisplacedControlRegion"),
    triggers = cms.vstring("HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
AntiIsoDisplacedControlRegion.cuts.append(jet_eta_cut)
AntiIsoDisplacedControlRegion.cuts.append(jet_pt_30_cut)
AntiIsoDisplacedControlRegion.cuts.append(jet_id_cut)
### at least two good electrons
AntiIsoDisplacedControlRegion.cuts.append(electron_eta_cut)
AntiIsoDisplacedControlRegion.cuts.append(electron_gap_veto)
AntiIsoDisplacedControlRegion.cuts.append(electron_pt_42_cut)
AntiIsoDisplacedControlRegion.cuts.append(electron_id_cut)
AntiIsoDisplacedControlRegion.cuts.append(electron_antiiso_cut)
### require displaced leptons
AntiIsoDisplacedControlRegion.cuts.append(electron_d0_100to200_cut)
