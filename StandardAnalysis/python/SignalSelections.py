import FWCore.ParameterSet.Config as cms
import copy

###########################################################
##### Set up the event selections (channels) #####
###########################################################

##### List of valid input collections #####   
# jets, muons, electrons, taus, photons, mets,
# events, tracks, primaryvertexs,
# genjets, mcparticles,
# bxlumis, superclusters



# abs(genMatchedPdgGrandmotherId) = 1000006 covers the stop->Bl matching
# abs(genMatchedPdgGrandmotherId) = 24 covers the stop->Tnu matching

SignalGenMatching = cms.PSet(
    name = cms.string("SignalGenMatching"),
    cuts = cms.VPSet (
      #at least one electron
      cms.PSet (
        inputCollection = cms.string("mcparticles"),
        cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 | abs(genMatchedPdgGrandmotherId) = 24 & abs(id) = 11"),
        numberRequired = cms.string(">= 1")
      ),
      #at least one muon
      cms.PSet (
        inputCollection = cms.string("secondary mcparticles"),
        cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 | abs(genMatchedPdgGrandmotherId) = 24 & abs(id) = 13"),
        numberRequired = cms.string(">= 1")
      ),
))


SignalSelection = cms.PSet(
    name = cms.string("SignalSelection"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"),
    cuts = cms.VPSet (
      cms.PSet (
        inputCollection = cms.string("events"),
        cutString = cms.string("FilterOutScraping > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("primaryvertexs"),
        cutString = cms.string("isGood > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),    
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("mvaNonTrigV0 > 0.9"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("passConvVeto > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("relPFrhoIso < 0.1"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),    
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("tightIDdisplaced > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("relPFdBetaIso < 0.12"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
      ),
      cms.PSet (
        inputCollection = cms.string("electron-muon pairs"),
        cutString = cms.string("deltaR > 0.5"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.string("electron-muon pairs"),
        cutString = cms.string("chargeProduct < 0"),
        numberRequired = cms.string("== 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(correctedD0) > 0.02"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(correctedD0) > 0.02"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string(">= 1"),
      ),
   )   
)



SignalSelectionWithGenMatching = cms.PSet(
        name = cms.string("SignalSelectionWithGenMatching"),
            triggers = copy.deepcopy(SignalSelection.triggers),
            cuts = cms.VPSet ()
        )
SignalSelectionWithGenMatching.cuts.extend(copy.deepcopy(SignalGenMatching.cuts))
SignalSelectionWithGenMatching.cuts.extend(copy.deepcopy(SignalSelection.cuts))
