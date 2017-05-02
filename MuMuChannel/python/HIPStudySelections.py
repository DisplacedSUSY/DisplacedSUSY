import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

##########################################################################
### Set up the prompt control region for the displaced SUSY analysis #####
##########################################################################

##########################################################################
#Selections without triggers

Denominator = cms.PSet(
    name = cms.string("Denominator"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)

muon_eta_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 2")
    )

muon_pt_25_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 2")
    )

muon_iso_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pfdBetaIsoCorr <= 0.15"),
    numberRequired = cms.string(">= 2")
    )

muon_extra_veto = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 2")
    )

dimuon_deltaR_cut = cms.PSet(
    inputCollection = cms.vstring("muons","muons"),
    cutString = cms.string("deltaR(muon,muon) > 0.1"),
    numberRequired = cms.string(">= 1")
    )

dimuon_os_cut = cms.PSet(
    inputCollection = cms.vstring("muons","muons"),
    cutString = cms.string("muon.charge * muon.charge < 0"),
    numberRequired = cms.string(">= 1")
    )

dimuon_onZ_cut = cms.PSet(
    inputCollection = cms.vstring("muons","muons"),
    cutString = cms.string("abs(90 - invMass(muon,muon)) < 20"),
    numberRequired = cms.string(">= 1")
    )

Denominator.cuts.append(muon_eta_cut)
Denominator.cuts.append(muon_pt_25_cut)
Denominator.cuts.append(muon_iso_cut)
Denominator.cuts.append(muon_extra_veto)
Denominator.cuts.append(dimuon_deltaR_cut)
Denominator.cuts.append(dimuon_os_cut)
Denominator.cuts.append(dimuon_onZ_cut)

Numerator = cms.PSet(
    name = cms.string("Numerator"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(Denominator.cuts))
)


muon_global_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("isGlobalMuon"),
    numberRequired = cms.string(">= 2")
    )

Numerator.cuts.append(muon_global_cut)
