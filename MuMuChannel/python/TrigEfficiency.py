import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *


##########################################################################
### Set up the displaced control region for the displaced SUSY analysis #####
##########################################################################

TriggerDoubleMu33 = cms.PSet(
    name = cms.string("TriggerDoubleMu33"),
    triggers = cms.vstring("HLT_DoubleMu33NoFiltersNoVtx"),
    cuts = cms.VPSet()
)


# TriggerDoubleMu33.cuts.append(cutDummy)

TriggerDoubleMu23Displaced = cms.PSet(
    name = cms.string("TriggerDoubleMu23Displaced"),
    triggers = cms.vstring("HLT_DoubleMu23NoFiltersNoVtxDisplaced"),
    cuts = cms.VPSet()
)

# TriggerDoubleMu23Displaced.cuts.append(cutDummy)

TriggerDoubleMu33ORDoubleMu23Displaced = cms.PSet(
    name = cms.string("TriggerDoubleMu33ORDoubleMu23Displaced"),
    triggers = cms.vstring("HLT_DoubleMu33NoFiltersNoVtx","HLT_DoubleMu23NoFiltersNoVtxDisplaced"),
    cuts = cms.VPSet()
)

# Trigger_DoubleMu33_OR_DoubleMu23Displaced.cuts.append(cutDummy)
