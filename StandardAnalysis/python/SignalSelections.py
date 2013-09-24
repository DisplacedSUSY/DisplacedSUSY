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
    )
)



