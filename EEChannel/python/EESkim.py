import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.EEChannel.CutDefinitions import *

EESkim = cms.PSet(
    name = cms.string("EESkim"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (
        electron_eta_cut,
        electron_pt_25_cut,
        electron_gap_veto
        )
)
