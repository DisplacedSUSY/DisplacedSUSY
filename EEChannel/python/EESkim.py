import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.EEChannel.CutDefinitions import *

#at least two good electrons
EESkim = cms.PSet(
    name = cms.string("EESkim"),
    triggers = triggersDoublePhoton,
    cuts = cms.VPSet (
        electron_eta_cut,
        electron_pt_25_cut,
        electron_gap_veto
        )
)

EESkimWithoutTrigger = cms.PSet(
    name= cms.string("EESkimWithoutTrigger"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet (copy.deepcopy(EESkim.cuts))
)

EESkimWithOnlyL1Trigger = cms.PSet(
    name = cms.string("EESkimWithOnlyL1Trigger"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet (copy.deepcopy(EESkim.cuts))
)
EESkimWithOnlyL1Trigger.cuts.append(pass_L1EG_OR_L1Jet_Seeds)
