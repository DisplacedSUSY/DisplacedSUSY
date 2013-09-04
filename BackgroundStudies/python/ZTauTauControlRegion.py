import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.StandardAnalysis.Preselection import *

#Z->tautau->emu

##########################################################################

ZTauTauControlRegion = cms.PSet(
    name = cms.string("ZTauTautoEMu"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"),
    cuts = cms.VPSet ()
)
ZTauTauControlRegion.cuts.extend(copy.deepcopy(Preselection.cuts))

e_metMT_cut =  cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("metMT < 50"),
    numberRequired = cms.string("== 1")
)
ZTauTauControlRegion.cuts.append(e_metMT_cut)

mu_metMT_cut =  cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("metMT < 50"),
    numberRequired = cms.string("== 1")
)
ZTauTauControlRegion.cuts.append(mu_metMT_cut)

deltaPhi_cut =  cms.PSet (
    inputCollection = cms.string("electron-muon pairs"),
    cutString = cms.string("deltaPhi > 2.5"),
    numberRequired = cms.string("== 1")
)
ZTauTauControlRegion.cuts.append(deltaPhi_cut)

ht_cut =  cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("unfilteredHt < 100"),
    numberRequired = cms.string("== 1")
)
ZTauTauControlRegion.cuts.append(ht_cut)


##########################################################################



