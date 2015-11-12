import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.StandardAnalysis.CutDefinitions_13TeV import *

#tt->emu

ttbar_control_region_cuts = cms.VPSet(
    cms.PSet (
        inputCollection = cms.vstring("candeles", "muons"),
        cutString = cms.string("candele.charge * muon.charge < 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("oppositely charged e-mu pair")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("candeles", "muons"),
        cutString = cms.string("deltaR(candele, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
    ),
    #Extra Lepton Veto
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
    ),
    # ELECTRON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("candeles"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),

    cms.PSet (
        inputCollection = cms.vstring("candjets"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 2")
    ),
    cms.PSet (
        inputCollection = cms.vstring("candjets"),
        cutString = cms.string("pt > 30"),
        numberRequired = cms.string(">= 2")
    ),
    cms.PSet (
        inputCollection = cms.vstring("candjets"),
        cutString = cms.string("neutralHadronEnergyFraction < 0.99 & chargedEmEnergyFraction < 0.99 & neutralEmEnergyFraction < 0.99 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0"),
        numberRequired = cms.string(">= 2")
    ),
    cms.PSet (
        inputCollection = cms.vstring("candjets"),
        cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.89"),
        numberRequired = cms.string(">= 1")
    )
)
##########################################################################

TTbarControlRegion_13TeV = cms.PSet(
    name = cms.string("TTbartoEMu13TeV"),
    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)
TTbarControlRegion_13TeV.cuts.extend(electron_basic_selection_cuts)
TTbarControlRegion_13TeV.cuts.append(electron_iso_cut)
TTbarControlRegion_13TeV.cuts.extend(muon_basic_selection_cuts)
TTbarControlRegion_13TeV.cuts.append(muon_iso_cut)
TTbarControlRegion_13TeV.cuts.extend(ttbar_control_region_cuts)

##########################################################################
