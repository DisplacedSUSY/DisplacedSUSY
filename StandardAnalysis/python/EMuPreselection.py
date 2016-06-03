import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.StandardAnalysis.CutDefinitions import *

##########################################################################
##############  e-mu preselection without triggers  ######################
##########################################################################

EMuPreselectionNoTrigger = cms.PSet(
    name = cms.string("EMuPreselectionNoTrigger"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)

EMuPreselectionNoTrigger.cuts.extend(electron_basic_selection_cuts)
EMuPreselectionNoTrigger.cuts.append(electron_iso_corr_cut)
EMuPreselectionNoTrigger.cuts.extend(muon_basic_selection_cuts)
EMuPreselectionNoTrigger.cuts.append(muon_iso_corr_cut)
EMuPreselectionNoTrigger.cuts.extend(jet_basic_selection_cuts)
EMuPreselectionNoTrigger.cuts.extend(preselection_emu_cuts)
EMuPreselectionNoTrigger.cuts.append(os_emu_cut)

##########################################################################
##############  e-mu preselection with inclusive trigger  ################
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
##############  e-mu preselection with inclusive trigger EB/EE eles ######
##########################################################################
EMuPreselectionEBEleInclusiveTrigger = cms.PSet(
    name = cms.string("EMuPreselectionEBEleInclusiveTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
EMuPreselectionEBEleInclusiveTrigger.cuts = cms.VPSet (copy.deepcopy(EMuPreselectionInclusiveTrigger.cuts))
for cut in EMuPreselectionEBEleInclusiveTrigger.cuts:
    if "abs(eta) < 2.4" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("abs(eta) < 1.5")

EMuPreselectionEEEleInclusiveTrigger = cms.PSet(
    name = cms.string("EMuPreselectionEEEleInclusiveTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
EMuPreselectionEBEleInclusiveTrigger.cuts = cms.VPSet (copy.deepcopy(EMuPreselectionInclusiveTrigger.cuts))
for cut in EMuPreselectionEEEleInclusiveTrigger.cuts:
    if "abs(eta) < 2.4" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("abs(eta) < 2.4 && abs(eta) > 1.5")
##########################################################################
#Preselctions using the displaced trigger with lower thresholds.
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
#Preselections using control triggers

EMuPreselectionControlTrigger = cms.PSet(
    name = cms.string("EMuPreselectionControlTrigger"),
    triggers = cms.vstring("HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
    )
)
EMuPreselectionControlTrigger.cuts = cms.VPSet (copy.deepcopy(EMuPreselectionNoTrigger.cuts))
for cut in EMuPreselectionControlTrigger.cuts:
    if "pt >" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 27")
    if "pt >" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 25")


EMuPreselectionControlTriggerPassSignalTrigger = cms.PSet(
    name = cms.string("EMuPreselectionControlTriggerPassSignalTrigger"),
    triggers = cms.vstring("HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
    )
)
EMuPreselectionControlTriggerPassSignalTrigger.cuts = cms.VPSet (copy.deepcopy(EMuPreselectionNoTrigger.cuts))
for cut in EMuPreselectionControlTrigger.cuts:
    if "pt >" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 27")
    if "pt >" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 25")
