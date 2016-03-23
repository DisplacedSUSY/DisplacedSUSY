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
#EMuPreselectionNoTrigger.cuts.append(electron_jet_deltaR_cut)
EMuPreselectionNoTrigger.cuts.extend(muon_basic_selection_cuts)
EMuPreselectionNoTrigger.cuts.append(muon_iso_cut)
#EMuPreselectionNoTrigger.cuts.append(muon_jet_deltaR_cut)
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

EMuPreselectionEBEleInclusiveTrigger = cms.PSet(
    name = cms.string("EMuPreselectionEBEleInclusiveTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
EMuPreselectionEBEleInclusiveTrigger.cuts.extend(jet_basic_selection_cuts)
EMuPreselectionEBEleInclusiveTrigger.cuts.extend(electron_basic_selection_eb_cuts)
EMuPreselectionEBEleInclusiveTrigger.cuts.append(electron_iso_cut)
EMuPreselectionEBEleInclusiveTrigger.cuts.extend(muon_basic_selection_cuts)
EMuPreselectionEBEleInclusiveTrigger.cuts.append(muon_iso_cut)
EMuPreselectionEBEleInclusiveTrigger.cuts.extend(preselection_emu_cuts)
EMuPreselectionEBEleInclusiveTrigger.cuts.append(os_emu_cut)

for cut in EMuPreselectionEBEleInclusiveTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

EMuPreselectionEEEleInclusiveTrigger = cms.PSet(
    name = cms.string("EMuPreselectionEEEleInclusiveTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
EMuPreselectionEEEleInclusiveTrigger.cuts.extend(jet_basic_selection_cuts)
EMuPreselectionEEEleInclusiveTrigger.cuts.extend(electron_basic_selection_ee_cuts)
EMuPreselectionEEEleInclusiveTrigger.cuts.append(electron_iso_cut)
EMuPreselectionEEEleInclusiveTrigger.cuts.extend(muon_basic_selection_cuts)
EMuPreselectionEEEleInclusiveTrigger.cuts.append(muon_iso_cut)
EMuPreselectionEEEleInclusiveTrigger.cuts.extend(preselection_emu_cuts)
EMuPreselectionEEEleInclusiveTrigger.cuts.append(os_emu_cut)

for cut in EMuPreselectionEEEleInclusiveTrigger.cuts:
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

EMuPreselectionPrescaleInclusiveTrigger = cms.PSet(
    name = cms.string("EMuPreselectionPrescaleInclusiveTrigger"),
    triggers = cms.vstring("HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
EMuPreselectionPrescaleInclusiveTrigger.cuts = cms.VPSet (copy.deepcopy(EMuPreselectionNoTrigger.cuts))

BlindedEMuPreselectionNoTrigger = cms.PSet(
    name = cms.string("BlindedEMuPreselectionNoTrigger"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)

BlindedEMuPreselectionNoTrigger.cuts.extend(electron_basic_selection_cuts)
BlindedEMuPreselectionNoTrigger.cuts.append(electron_iso_cut)
BlindedEMuPreselectionNoTrigger.cuts.extend(muon_basic_selection_cuts)
BlindedEMuPreselectionNoTrigger.cuts.append(muon_iso_cut)
BlindedEMuPreselectionNoTrigger.cuts.extend(blinded_control_region_cuts)
BlindedEMuPreselectionNoTrigger.cuts.append(os_emu_cut)

##########################################################################

BlindedEMuPreselectionDisplacedTrigger = cms.PSet(
    name = cms.string("BlindedEMuPreselectionDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
BlindedEMuPreselectionDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(BlindedEMuPreselectionNoTrigger.cuts))

for cut in BlindedEMuPreselectionDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")

BlindedEMuPreselectionNoIsoNoOSDisplacedTrigger = cms.PSet(
    name = cms.string("BlindedEMuPreselectionNoIsoNoOSDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
BlindedEMuPreselectionNoIsoNoOSDisplacedTrigger.cuts.extend(electron_basic_selection_cuts)
BlindedEMuPreselectionNoIsoNoOSDisplacedTrigger.cuts.append(electron_loose_iso_cut)
BlindedEMuPreselectionNoIsoNoOSDisplacedTrigger.cuts.extend(muon_basic_selection_cuts)
BlindedEMuPreselectionNoIsoNoOSDisplacedTrigger.cuts.append(muon_loose_iso_cut)
BlindedEMuPreselectionNoIsoNoOSDisplacedTrigger.cuts.extend(blinded_control_region_cuts)

for cut in BlindedEMuPreselectionNoIsoNoOSDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")

