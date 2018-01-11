import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

#################################################################
### Set up the preselection for the displaced SUSY analysis #####
#################################################################

Preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"),
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




PreselectionPromptElectron = cms.PSet(
    name = cms.string("PreselectionPromptElectron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
PreselectionPromptElectron.cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
PreselectionPromptElectron.cuts.append(electron_d0_below200_cut)


PreselectionPromptMuon = cms.PSet(
    name = cms.string("PreselectionPromptMuon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
PreselectionPromptMuon.cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
PreselectionPromptMuon.cuts.append(muon_d0_below200_cut)


PreselectionSignalRegion = cms.PSet(
    name = cms.string("PreselectionSignalRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
PreselectionSignalRegion.cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
PreselectionSignalRegion.cuts.append(electron_d0_above200_cut)
PreselectionSignalRegion.cuts.append(muon_d0_above200_cut)
