import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.StandardAnalysis.CutDefinitions import *
##########################################################################
##### Set up the EMu Skim Selections for the displaced SUSY analysis #####
##########################################################################

EMuSkimSelection = cms.PSet(
    name = cms.string("EMuSkimSelection"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > 25"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > 25"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("isPFMuon & isGlobalMuon"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("Global Muon")
        ),
    ),
)

##########################################################################

EMuSkimSelectionInclusiveTrigger = cms.PSet(
    name = cms.string("EMuSkimSelectionInclusiveTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)

EMuSkimSelectionInclusiveTrigger.cuts = cms.VPSet (copy.deepcopy(EMuSkimSelection.cuts))

##########################################################################
EMuPreselectionSkim = cms.PSet(
    name = cms.string("EMuPreselectionSkim"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet ()
)

EMuPreselectionSkim.cuts.extend(electron_basic_selection_cuts)
EMuPreselectionSkim.cuts.extend(muon_basic_selection_cuts)

for cut in EMuPreselectionSkim.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")
##########################################################################

EMuTriggerStudySkimSelection = cms.PSet(
    name = cms.string("EMuTriggerStudySkimSelection"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > 10"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 1")
        ),
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > 10"),
            numberRequired = cms.string(">= 1")
        ),
    )
)

from DisplacedSUSY.StandardAnalysis.CutDefinitions import *

EMuTriggerStudySkimSelection.cuts.append(electron_id_cut)
EMuTriggerStudySkimSelection.cuts.append(muon_id_cut)
EMuTriggerStudySkimSelection.cuts.extend(preselection_emu_cuts)
