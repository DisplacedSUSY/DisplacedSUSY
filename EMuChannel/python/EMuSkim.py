import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

##########################################################################
##### Set up the EMu Skim Selections for the displaced SUSY analysis #####
##########################################################################

EMuSkim = cms.PSet(
    name = cms.string("EMuSkim"),
    triggers = triggersMuonPhoton,
    cuts = cms.VPSet()
)
### at least one good electron
EMuSkim.cuts.append(electron_eta_cut)
EMuSkim.cuts.append(electron_pt_20_cut)
### at least one good muon
EMuSkim.cuts.append(muon_eta_cut)
EMuSkim.cuts.append(muon_pt_20_cut)
EMuSkim.cuts.append(muon_global_cut)


EMuSkimWithoutTrigger = cms.PSet(
    name = cms.string("EMuSkimWithoutTrigger"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet (copy.deepcopy(EMuSkim.cuts))
)

EMuSkimWithOnlyL1Trigger = cms.PSet(
    name = cms.string("EMuSkimWithOnlyL1Trigger"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet (copy.deepcopy(EMuSkim.cuts))
)
EMuSkimWithOnlyL1Trigger.cuts.append(pass_L1MuEG_Seeds)

EmptySkim = cms.PSet(
    name = cms.string("EmptySkim"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet()
)
EmptySkim.cuts.append(cutDummyElectron)
EmptySkim.cuts.append(cutDummyMuon)
