import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.EMuChannel.Preselection import Preselection as EMuPreselection
EMuTriggers = copy.deepcopy(EMuPreselection.triggers)
EMuCuts = cms.VPSet (copy.deepcopy(EMuPreselection.cuts))

from DisplacedSUSY.EEChannel.Preselection import Preselection as EEPreselection
EETriggers = copy.deepcopy(EEPreselection.triggers)
EECuts = cms.VPSet (copy.deepcopy(EEPreselection.cuts))

from DisplacedSUSY.MuMuChannel.Preselection import Preselection as MuMuPreselection
MuMuTriggers = copy.deepcopy(MuMuPreselection.triggers)
MuMuCuts = cms.VPSet (copy.deepcopy(MuMuPreselection.cuts))


EMuEEPreselectionOverlap = cms.PSet(
    name = cms.string("EMuEEPreselectionOverlap"),
    triggers = EMuTriggers + EETriggers,
    cuts = EMuCuts + EECuts,
)

EMuMuMuPreselectionOverlap = cms.PSet(
    name = cms.string("EMuMuMuPreselectionOverlap"),
    triggers = EMuTriggers + MuMuTriggers,
    cuts = EMuCuts + MuMuCuts,
)

MuMuEEPreselectionOverlap = cms.PSet(
    name = cms.string("MuMuEEPreselectionOverlap"),
    triggers = MuMuTriggers + EETriggers,
    cuts = MuMuCuts + EECuts
)

