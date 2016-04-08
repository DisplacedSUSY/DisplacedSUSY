import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.StandardAnalysis.CutDefinitions import *


muon_d0_50um_cut = cms.PSet (
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) > 0.005"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon dxy > 0.005 cm")
    )
electron_d0_50um_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) > 0.005"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron dxy > 0.005 cm")
    )

muon_d0_100um_cut = cms.PSet (
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) > 0.01"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon dxy > 0.01 cm")
    )
electron_d0_100um_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) > 0.01"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron dxy > 0.01 cm")
    )

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

CentralValue = cms.PSet(
    name = cms.string("CentralValue"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
CentralValue.cuts = cms.VPSet (copy.deepcopy(EMuPreselectionInclusiveTrigger.cuts))


CentralValue50um = cms.PSet(
    name = cms.string("CentralValue50um"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
CentralValue50um.cuts = cms.VPSet (copy.deepcopy(CentralValue.cuts))
CentralValue50um.cuts.append(muon_d0_50um_cut)
CentralValue50um.cuts.append(electron_d0_50um_cut)

CentralValue100um = cms.PSet(
    name = cms.string("CentralValue100um"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
CentralValue100um.cuts = cms.VPSet (copy.deepcopy(CentralValue.cuts))
CentralValue100um.cuts.append(muon_d0_100um_cut)
CentralValue100um.cuts.append(electron_d0_100um_cut)

