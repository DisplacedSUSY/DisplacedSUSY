import FWCore.ParameterSet.Config as cms
import copy
import string
from CutDefinitions_13TeV import *
#Preselection cuts
preselection_emu_cuts = cms.VPSet(
    # OPPOSITE SIGN E-MU PAIR
    cms.PSet (
        inputCollection = cms.vstring("candeles", "muons"),
        cutString = cms.string("candele.charge * muon.charge < 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("oppositely charged e-mu pair")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("candeles", "muons"),
        cutString = cms.string("deltaR(candele, muon) > 0.5"),
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
        inputCollection = cms.vstring("candeles"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)
EMuPreselection_13TeV = cms.PSet(
    name = cms.string("EMuPreselection13TeV"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
EMuPreselection_13TeV.cuts.extend(electron_basic_selection_cuts)
EMuPreselection_13TeV.cuts.append(electron_iso_cut)
EMuPreselection_13TeV.cuts.extend(muon_basic_selection_cuts)
EMuPreselection_13TeV.cuts.append(muon_iso_cut)
EMuPreselection_13TeV.cuts.extend(preselection_emu_cuts)

##########################################################################
EMuPreselectionInclusiveDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("EMuPreselectionInclusiveDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
EMuPreselectionInclusiveDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(EMuPreselection_13TeV.cuts))

for cut in EMuPreselectionInclusiveDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

EMuPreselectionDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("EMuPreselectionDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
EMuPreselectionDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(EMuPreselection_13TeV.cuts))

for cut in EMuPreselectionDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")
