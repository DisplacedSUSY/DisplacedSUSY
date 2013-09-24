import FWCore.ParameterSet.Config as cms
import copy

#################################################################

prompt_muon_d0_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string("== 1")
)
displaced_muon_d0_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) > 0.02"),
    numberRequired = cms.string("== 1")
)

prompt_electron_d0_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string("== 1")
)
displaced_electron_d0_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("abs(correctedD0) > 0.02"),
    numberRequired = cms.string("== 1")
)

#################################################################

from DisplacedSUSY.StandardAnalysis.Preselection import *

#################################################################

Preselection_Displaced_Electron = cms.PSet(
    name = cms.string("Preselection_Displaced_Electron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_Displaced_Electron.cuts.extend(copy.deepcopy(Preselection.cuts))
Preselection_Displaced_Electron.cuts.append(prompt_muon_d0_cut)
Preselection_Displaced_Electron.cuts.append(displaced_electron_d0_cut)

#################################################################

Preselection_Displaced_Muon = cms.PSet(
    name = cms.string("Preselection_Displaced_Muon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_Displaced_Muon.cuts.extend(copy.deepcopy(Preselection.cuts))
Preselection_Displaced_Muon.cuts.append(displaced_muon_d0_cut)
Preselection_Displaced_Muon.cuts.append(prompt_electron_d0_cut)

#################################################################
