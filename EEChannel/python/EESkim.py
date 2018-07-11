import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.EEChannel.CutDefinitions import *

#no triggers required
#at least two good electrons
EESkim = cms.PSet(
    name = cms.string("EESkim"),
    triggers = triggersDoublePhoton,
    cuts = cms.VPSet (
        electron_eta_cut,
        electron_pt_25_cut,
        electron_gap_veto
        )
)
