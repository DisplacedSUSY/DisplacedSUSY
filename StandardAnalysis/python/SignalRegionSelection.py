import FWCore.ParameterSet.Config as cms
import copy
import string
from CutDefinitions import *
##########################################################################
######## Set up the prompt control region for the displaced SUSY analysis #########
##########################################################################
##########################################################################
#Signal region specific cuts
signal_region_cuts = cms.VPSet(
    # MUON DXY 
    cms.PSet (
        inputCollection = cms.vstring("muons","beamspots"),
        cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) >= 0.02 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("muon dxy >= 0.02 cm")
    ),
    # ELECTRON DXY
    cms.PSet (
        inputCollection = cms.vstring("electrons","beamspots"),
        cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) >= 0.02 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron dxy >= 0.02 cm")
    ),
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
    # ELECTRON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)

SignalRegionSelection = cms.PSet(
    name = cms.string("SignalRegionSelection"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet ()
)

SignalRegionSelection.cuts.extend(electron_basic_selection_cuts)
SignalRegionSelection.cuts.append(electron_iso_cut)
SignalRegionSelection.cuts.extend(muon_basic_selection_cuts)
SignalRegionSelection.cuts.append(muon_iso_cut)
SignalRegionSelection.cuts.extend(signal_region_cuts)

##########################################################################
SignalRegionSelectionInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("SignalRegionSelectionInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
SignalRegionSelectionInclusiveDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(SignalRegionSelection.cuts))

for cut in SignalRegionSelectionInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

SignalRegionSelectionDisplacedTrigger = cms.PSet(
    name = cms.string("SignalRegionSelectionDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
SignalRegionSelectionDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(SignalRegionSelection.cuts))

for cut in SignalRegionSelectionDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")


