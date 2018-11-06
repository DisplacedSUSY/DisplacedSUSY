import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.Preselection import Preselection as EMuPreselection
from DisplacedSUSY.EEChannel.Preselection import Preselection as EEPreselection
from DisplacedSUSY.MuMuChannel.Preselection import Preselection as MuMuPreselection

EMuEEPreselectionOverlap = cms.PSet(
    name = cms.string("EMuEEPreselectionOverlap"),
    triggers = copy.deepcopy(EMuPreselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(EMuPreselection.cuts))
)
EMuEEPreselectionOverlap.triggers.extend(copy.deepcopy(EEPreselection.triggers))
EMuEEPreselectionOverlap.cuts.extend(copy.deepcopy(EEPreselection.cuts))

EMuMuMuPreselectionOverlap = cms.PSet(
    name = cms.string("EMuMuMuPreselectionOverlap"),
    triggers = copy.deepcopy(EMuPreselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(EMuPreselection.cuts))
)
EMuMuMuPreselectionOverlap.triggers.extend(copy.deepcopy(MuMuPreselection.triggers))
EMuMuMuPreselectionOverlap.cuts.extend(copy.deepcopy(MuMuPreselection.cuts))

MuMuEEPreselectionOverlap = cms.PSet(
    name = cms.string("MuMuEEPreselectionOverlap"),
    triggers = copy.deepcopy(MuMuPreselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(MuMuPreselection.cuts))
)
MuMuEEPreselectionOverlap.triggers.extend(copy.deepcopy(EEPreselection.triggers))
MuMuEEPreselectionOverlap.cuts.extend(copy.deepcopy(EEPreselection.cuts))

