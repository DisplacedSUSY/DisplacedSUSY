import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.MuMuChannel.CutDefinitions import *

#at least two good muons
MuMuSkim = cms.PSet(
    name = cms.string("MuMuSkim"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet (
        muon_eta_cut,
        muon_pt_20_cut,
        muon_global_cut
        ),
    )

MuMuSkimWithoutTrigger = cms.PSet(
    name= cms.string("MuMuSkimWithoutTrigger"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet (copy.deepcopy(MuMuSkim.cuts))
)

MuMuSkimWithOnlyL1Trigger = cms.PSet(
    name = cms.string("MuMuSkimWithOnlyL1Trigger"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet (copy.deepcopy(MuMuSkim.cuts))
)
MuMuSkimWithOnlyL1Trigger.cuts.append(pass_L1DoubleMu_Seeds)
