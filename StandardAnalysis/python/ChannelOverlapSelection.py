import FWCore.ParameterSet.Config as cms
import copy
import string
from OSUT3Analysis.Configuration.cutUtilities import *
from DisplacedSUSY.StandardAnalysis.BasicSelections import atLeastZero_jet_basic_selection_cuts

from DisplacedSUSY.EMuChannel.Preselection import Preselection as EMuPreselection
EMuTriggers = copy.deepcopy(EMuPreselection.triggers)
EMuCuts = cms.VPSet (copy.deepcopy(EMuPreselection.cuts))
removeCuts(EMuCuts,atLeastZero_jet_basic_selection_cuts)

from DisplacedSUSY.EEChannel.Preselection import Preselection as EEPreselection
EETriggers = copy.deepcopy(EEPreselection.triggers)
EECuts = cms.VPSet (copy.deepcopy(EEPreselection.cuts))
removeCuts(EECuts,atLeastZero_jet_basic_selection_cuts)

from DisplacedSUSY.MuMuChannel.Preselection import Preselection as MuMuPreselection
MuMuTriggers = copy.deepcopy(MuMuPreselection.triggers)
MuMuCuts = cms.VPSet (copy.deepcopy(MuMuPreselection.cuts))
removeCuts(MuMuCuts,atLeastZero_jet_basic_selection_cuts)

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

