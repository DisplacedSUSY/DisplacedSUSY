import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.StandardAnalysis.CutDefinitions import *


##########################################################################

MuMuPreselection = cms.PSet(
    name = cms.string("MuMuPreselection"),
    triggers = cms.vstring("HLT_DoubleMu33NoFiltersNoVtx_v"), # TRIGGER
    cuts = cms.VPSet ()
)

muon_basic_selection_cuts = cms.VPSet(
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 2")
    ),
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > 35"),
        numberRequired = cms.string(">= 2")
    ),
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("isGlobalMuon & \
        isPFMuon & \
        globalTrack.hitPattern_.numberOfValidMuonHits > 0 & \
        globalTrack.normalizedChi2 < 10 & \
        numberOfMatchedStations > 1 & \
        innerTrack.hitPattern_.numberOfValidPixelHits > 0 & \
        innerTrack.hitPattern_.trackerLayersWithMeasurement > 5"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string("muon tight displaced ID")
    ),
)

muon_iso_cut = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("                \
        (pfIsolationR04_.sumChargedHadronPt \
        + max(0.0,                          \
        pfIsolationR04_.sumNeutralHadronEt  \
        + pfIsolationR04_.sumPhotonEt       \
        - 0.5*pfIsolationR04_.sumPUPt))     \
        /pt <= 0.15                         \
       "),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("muon isolation")
)


preselection_mumu_cuts = cms.VPSet(
    cms.PSet (
        inputCollection = cms.vstring("muons", "muons"),
        cutString = cms.string("deltaR(muon, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated (DeltaR > 0.5) mu-mu pair")
    ),
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 2"),
        alias = cms.string("extra muon veto")
    ),
    cms.PSet (
        inputCollection = cms.vstring("muons", "muons"),
        cutString = cms.string("muon.charge * muon.charge < 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("oppositely-charged mu-mu pair")
    )
)

MuMuPreselection.cuts.extend(jet_basic_selection_cuts)
MuMuPreselection.cuts.extend(muon_basic_selection_cuts)
MuMuPreselection.cuts.append(muon_iso_cut)
MuMuPreselection.cuts.append(muon_jet_deltaR_cut)
MuMuPreselection.cuts.extend(preselection_mumu_cuts)

##########################################################################
