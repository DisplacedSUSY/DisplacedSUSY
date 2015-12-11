import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import math
import os

################################################################################
##### Set up the 'process' object ##############################################
################################################################################

process = cms.Process ('OSUAnalysis')

# how often to print a log message
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.source = cms.Source ('PoolSource',
  fileNames = cms.untracked.vstring ('file:/data/users/bing/condor/CosmicMuonSkim/NoBPTX_2015D_v4/CosmicMuonSkimSelection/skim_755.root')
)
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (10000)
)


process.DisplacedSUSYCosmicMuonProducer = cms.EDProducer("DisplacedSUSYCosmicMuonProducer",
         muons = cms.InputTag('objectSelector0',''),
         maxDeltaRForGenMatching = cms.double (0.1)
)
process.DisplacedSUSYCosmicMuonProducerPoolOutputModule = cms.OutputModule("PoolOutputModule",
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('/data/users/bing/condor/CosmicMuonSelected_Dec9th/CosmicMuons.root'),
    outputCommands = cms.untracked.vstring('keep *',
    'drop *_objectSelector0_*_*',
    'drop *_TriggerResults__OSUAnalysis',
    ),
        
    splitLevel = cms.untracked.int32(0)
)
process.p = cms.Path(process.DisplacedSUSYCosmicMuonProducer)

process.endPath = cms.EndPath(process.DisplacedSUSYCosmicMuonProducerPoolOutputModule)
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
