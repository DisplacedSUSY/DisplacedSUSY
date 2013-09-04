import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    comEnergy = cms.double(8000.0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
          'MSEL=0',
          'MSUB(264)=1', 
          'IMSS(1)=11',
          'IMSS(51)=1',
          'IMSS(52)=1',
          'RMSS(51)=3',
          'RMSS(52)=3'
        ),
        SLHAParameters = cms.vstring('SLHAFILE = data/param_card.dat'),
        parameterSets = cms.vstring(
          'pythiaUESettings',
          'processParameters',
          'SLHAParameters'
        )
    )
)

genParticlesForFilter = cms.EDProducer("GenParticleProducer",
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("generator"),
    abortOnUnknownPDGCode = cms.untracked.bool(True)
)

stopToBTFilter = cms.EDFilter("StopToBTFilter",
    genParticles = cms.InputTag("genParticlesForFilter")
)

ProductionFilterSequence = cms.Sequence (generator * (genParticlesForFilter + stopToBTFilter))
