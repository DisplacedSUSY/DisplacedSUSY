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


PromptControlRegion = cms.PSet(
    name = cms.string("PromptControlRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PromptControlRegion.cuts.append(electron_d0_lt100_cut)
PromptControlRegion.cuts.append(muon_d0_lt100_cut)


DisplacedControlRegion = cms.PSet(
    name = cms.string("DisplacedControlRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
DisplacedControlRegion.cuts.append(electron_d0_100to200_cut)
DisplacedControlRegion.cuts.append(muon_d0_100to200_cut)


InclusiveSignalRegion = cms.PSet(
    name = cms.string("InclusiveSignalRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
InclusiveSignalRegion.cuts.append(electron_d0_above200_cut)
InclusiveSignalRegion.cuts.append(muon_d0_above200_cut)


PreselectionPromptElectron = cms.PSet(
    name = cms.string("PreselectionPromptElectron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionPromptElectron.cuts.append(electron_d0_below200_cut)


PreselectionPromptMuon = cms.PSet(
    name = cms.string("PreselectionPromptMuon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionPromptMuon.cuts.append(muon_d0_below200_cut)


PreselectionVeryPromptElectron = cms.PSet(
    name = cms.string("PreselectionVeryPromptElectron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionVeryPromptElectron.cuts.append(electron_d0_lt100_cut)


PreselectionVeryPromptMuon = cms.PSet(
    name = cms.string("PreselectionVeryPromptMuon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionVeryPromptMuon.cuts.append(muon_d0_lt100_cut)


PreselectionIntermediateElectron = cms.PSet(
    name = cms.string("PreselectionIntermediateElectron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionIntermediateElectron.cuts.append(electron_d0_100to200_cut)


PreselectionIntermediateMuon = cms.PSet(
    name = cms.string("PreselectionIntermediateMuon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionIntermediateMuon.cuts.append(muon_d0_100to200_cut)
