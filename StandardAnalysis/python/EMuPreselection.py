import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.StandardAnalysis.CutDefinitions import *

##########################################################################

EMuPreselectionNoTrigger = cms.PSet(
    name = cms.string("EMuPreselectionNoTrigger"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)

EMuPreselectionNoTrigger.cuts.extend(jet_basic_selection_cuts)
EMuPreselectionNoTrigger.cuts.extend(electron_basic_selection_cuts)
EMuPreselectionNoTrigger.cuts.append(electron_iso_cut)
EMuPreselectionNoTrigger.cuts.append(electron_jet_deltaR_cut)
EMuPreselectionNoTrigger.cuts.extend(muon_basic_selection_cuts)
EMuPreselectionNoTrigger.cuts.append(muon_iso_cut)
EMuPreselectionNoTrigger.cuts.append(muon_jet_deltaR_cut)
EMuPreselectionNoTrigger.cuts.extend(preselection_emu_cuts)
EMuPreselectionNoTrigger.cuts.append(os_emu_cut)

##########################################################################

EMuPreselectionInclusiveTrigger = cms.PSet(
    name = cms.string("EMuPreselectionInclusiveTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
EMuPreselectionInclusiveTrigger.cuts = cms.VPSet (copy.deepcopy(EMuPreselectionNoTrigger.cuts))

for cut in EMuPreselectionInclusiveTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

##########################################################################

EMuPreselectionDisplacedTrigger = cms.PSet(
    name = cms.string("EMuPreselectionDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
EMuPreselectionDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(EMuPreselectionNoTrigger.cuts))

for cut in EMuPreselectionDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")

##########################################################################
