import FWCore.ParameterSet.Config as cms

leptonicTauDecayGenFilter = cms.EDFilter("LeptonicTauDecayGenFilter",
                                         inputTag = cms.InputTag("genParticlePlusGeant")
                                     )
