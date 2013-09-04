import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.StandardAnalysis.Preselection import *

#tt->emu

##########################################################################

TTbarControlRegion = cms.PSet(
    name = cms.string("TTbartoEMu"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"),
    cuts = cms.VPSet ()
)
TTbarControlRegion.cuts.extend(copy.deepcopy(Preselection.cuts))

jet_eta_cut =  cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 2")
)
TTbarControlRegion.cuts.append(jet_eta_cut)

jet_pt_cut =  cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 2")
)
TTbarControlRegion.cuts.append(jet_pt_cut)

btag_cut =  cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("btagCombinedSecVertex > 0.679"),
    numberRequired = cms.string(">= 1")
)
TTbarControlRegion.cuts.append(btag_cut)

##########################################################################
