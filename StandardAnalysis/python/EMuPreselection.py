import FWCore.ParameterSet.Config as cms
import copy
import string
from CutDefinitions import *
#Preselection cuts
preselection_emu_cuts = cms.VPSet(
    # OPPOSITE SIGN E-MU PAIR
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("electron.charge * muon.charge < 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("oppositely charged e-mu pair")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("deltaR(electron, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
    ),
    #Extra Lepton Veto
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
    ),
    #Extra Lepton Veto
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)
EMuPreselection = cms.PSet(
    name = cms.string("EMuPreselection"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
EMuPreselection.cuts.extend(electron_basic_selection_cuts)
EMuPreselection.cuts.append(electron_iso_cut)
EMuPreselection.cuts.extend(muon_basic_selection_cuts)
EMuPreselection.cuts.append(muon_iso_cut)
EMuPreselection.cuts.extend(preselection_emu_cuts)

##########################################################################
EMuPreselectionInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("EMuPreselectionInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
EMuPreselectionInclusiveDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(EMuPreselection.cuts))

for cut in EMuPreselectionInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

EMuPreselectionDisplacedTrigger = cms.PSet(
    name = cms.string("EMuPreselectionDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
EMuPreselectionDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(EMuPreselection.cuts))

for cut in EMuPreselectionDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")
