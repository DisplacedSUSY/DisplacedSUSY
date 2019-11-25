import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.BasicSelections import *

diMuon_cosAlpha_veto = cms.PSet (
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("cosAlpha(muon, muon) < -0.99"),
    numberRequired = cms.string("== 0"),
    alias = cms.string("veto back-to-back muons (0 pairs with cos(3D angle) < -0.99)")
    )
