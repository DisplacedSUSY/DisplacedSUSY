import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.StandardAnalysis.CutDefinitions import *

#tt->emu

ttbar_control_region_cuts = cms.VPSet(
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("electron.charge * muon.charge < 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("oppositely charged e-mu pair")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("deltaR(electron, muon) > 0.5"),
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
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),

    cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 2")
    ),
    cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pt > 30"),
        numberRequired = cms.string(">= 2")
    ),
    cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("neutralHadronEnergyFraction < 0.99 & chargedEmEnergyFraction < 0.99 & neutralEmEnergyFraction < 0.99 & numberOfDaughters > 1 & chargedHadronEnergyFraction > 0.0 & chargedMultiplicity > 0.0"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string('>= 2 good jets')
    ),
    cms.PSet (
        inputCollection = cms.vstring("jets"),
        cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.89"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string('>= 1 medium b jets')
    )
)
##########################################################################

TTbarControlRegion = cms.PSet(
    name = cms.string("TTbartoEMu"),
    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)
TTbarControlRegion.cuts.extend(electron_basic_selection_cuts)
TTbarControlRegion.cuts.append(electron_iso_cut)
TTbarControlRegion.cuts.extend(muon_basic_selection_cuts)
TTbarControlRegion.cuts.append(muon_iso_cut)
TTbarControlRegion.cuts.extend(ttbar_control_region_cuts)

##########################################################################
