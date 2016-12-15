import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

##########################################################################
### Set up the prompt control region for the displaced SUSY analysis #####
##########################################################################

##########################################################################

Preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
Preselection.cuts.append(jet_eta_cut)
Preselection.cuts.append(jet_pt_30_cut)
Preselection.cuts.append(jet_id_cut)
### at least one good electron
Preselection.cuts.append(electron_eta_cut)
Preselection.cuts.append(electron_gap_veto)
Preselection.cuts.append(electron_pt_42_cut)
Preselection.cuts.append(electron_id_cut)
Preselection.cuts.append(electron_iso_cut)
### at least one good muon
Preselection.cuts.append(muon_eta_cut)
Preselection.cuts.append(muon_pt_40_cut)
Preselection.cuts.append(muon_global_cut)
Preselection.cuts.append(muon_id_cut)
Preselection.cuts.append(muon_iso_cut)


DisplacedControlRegion = cms.PSet(
    name = cms.string("DisplacedControlRegion"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
DisplacedControlRegion.cuts.append(jet_eta_cut)
DisplacedControlRegion.cuts.append(jet_pt_30_cut)
DisplacedControlRegion.cuts.append(jet_id_cut)
### at least one good electron
DisplacedControlRegion.cuts.append(electron_eta_cut)
DisplacedControlRegion.cuts.append(electron_gap_veto)
DisplacedControlRegion.cuts.append(electron_pt_42_cut)
DisplacedControlRegion.cuts.append(electron_id_cut)
DisplacedControlRegion.cuts.append(electron_iso_cut)
### at least one good muon
DisplacedControlRegion.cuts.append(muon_eta_cut)
DisplacedControlRegion.cuts.append(muon_pt_40_cut)
DisplacedControlRegion.cuts.append(muon_global_cut)
DisplacedControlRegion.cuts.append(muon_id_cut)
DisplacedControlRegion.cuts.append(muon_iso_cut)
### require displaced leptons
DisplacedControlRegion.cuts.append(electron_d0_100to200_cut)
DisplacedControlRegion.cuts.append(muon_d0_100to200_cut)

