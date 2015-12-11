import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.StandardAnalysis.SyncCuts import *

##########################################################################

EMuPreselectionNoTrigger = cms.PSet(
    name = cms.string("EMuPreselectionNoTrigger"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)

EMuPreselectionNoTrigger.cuts.extend(electron_basic_selection_cuts)
EMuPreselectionNoTrigger.cuts.append(electron_iso_cut)
EMuPreselectionNoTrigger.cuts.extend(muon_basic_selection_cuts)
EMuPreselectionNoTrigger.cuts.append(muon_iso_cut)
EMuPreselectionNoTrigger.cuts.extend(preselection_emu_cuts)

MuPreselectionNoTrigger = cms.PSet(
    name = cms.string("MuPreselectionNoTrigger"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)

MuPreselectionNoTrigger.cuts.extend(muon_basic_selection_cuts)
MuPreselectionNoTrigger.cuts.append(muon_iso_cut)

EPreselectionNoTrigger = cms.PSet(
    name = cms.string("EPreselectionNoTrigger"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)

EPreselectionNoTrigger.cuts.extend(electron_basic_selection_cuts)
EPreselectionNoTrigger.cuts.append(electron_iso_cut)

