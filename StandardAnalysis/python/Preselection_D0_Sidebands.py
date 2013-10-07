import FWCore.ParameterSet.Config as cms
import copy

#################################################################

prompt_electron_d0_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string("== 1")
)

prompt_muon_d0_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string("== 1")
)

#################################################################

from DisplacedSUSY.StandardAnalysis.Preselection import *

#################################################################

Preselection_Prompt_Electron = cms.PSet(
    name = cms.string("Preselection_Prompt_Electron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_Prompt_Electron.cuts.extend(copy.deepcopy(Preselection.cuts))
Preselection_Prompt_Electron.cuts.append(prompt_electron_d0_cut)

#################################################################

Preselection_Prompt_Muon = cms.PSet(
    name = cms.string("Preselection_Prompt_Muon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_Prompt_Muon.cuts.extend(copy.deepcopy(Preselection.cuts))
Preselection_Prompt_Muon.cuts.append(prompt_muon_d0_cut)

#################################################################
