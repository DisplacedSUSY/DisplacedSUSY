import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *
from DisplacedSUSY.StandardAnalysis.Triggers import *


###############################################################################
### Set up the trigger efficiency selection for the displaced SUSY analysis ###
###############################################################################

TriggerMuonPhoton38 = cms.PSet(
    name = cms.string("TriggerMuonPhoton38"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"),
    cuts = cms.VPSet()
)


TriggerDisplacedMuonPhoton28 = cms.PSet(
    name = cms.string("TriggerDisplacedMuonPhoton28"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"),
    cuts = cms.VPSet()
)


TriggerMuonPhoton38orDisplacedMuonPhoton28 = cms.PSet(
    name = cms.string("TriggerMuonPhoton38orDisplacedMuonPhoton28"),
    triggers = cms.vstring(triggersMuonPhoton),
    cuts = cms.VPSet()
)
