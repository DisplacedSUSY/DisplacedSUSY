import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.LifetimeWeightProducer_cff import *

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
  fileNames = cms.untracked.vstring (
        '/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-200_CTau-1_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/60E5B1FC-C5CB-E611-875F-02163E019E01.root'
  )
)

# output histogram file name when running interactively
process.TFileService = cms.Service('TFileService',
     fileName = cms.string ('hist.root')
)


# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (100)
)

#mc_global_tag needs to be updated before MC is used
#data_global_tag = '92X_dataRun2_Prompt_v9'
data_global_tag = '80X_dataRun2_2016SeptRepro_v3'
mc_global_tag = '80X_mcRun2_asymptotic_2016_miniAODv2_v1'

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, mc_global_tag, '')
if osusub.batchMode and (osusub.datasetLabel in types) and (types[osusub.datasetLabel] == "data"):
    print "using global tag " + data_global_tag + "..."
    process.GlobalTag = GlobalTag(process.GlobalTag, data_global_tag, '')
else:
    print "using global tag " + mc_global_tag + "..."




################################################################################
##### Set up the 'collections' map #############################################
################################################################################

# this PSet specifies which collections to get from the input files
miniAOD_collections = cms.PSet (
  electrons                   =  cms.InputTag  ('slimmedElectrons',                  ''),
  genjets                     =  cms.InputTag  ('slimmedGenJets',                    ''),
  jets                        =  cms.InputTag  ('slimmedJets',                       ''),
  bjets                       =  cms.InputTag  ('slimmedJets',                       ''),
  generatorweights            =  cms.InputTag  ('generator',                         ''),
  mcparticles                 =  cms.InputTag  ('packedGenParticles',                ''),
  hardInteractionMcparticles  =  cms.InputTag  ('prunedGenParticles',                ''),
  mets                        =  cms.InputTag  ('slimmedMETs',                       ''),
  muons                       =  cms.InputTag  ('slimmedMuons',                      ''),
  photons                     =  cms.InputTag  ('slimmedPhotons',                    ''),
  primaryvertexs              =  cms.InputTag  ('offlineSlimmedPrimaryVertices',     ''),
  pileupinfos                 =  cms.InputTag  ('slimmedAddPileupInfo',              ''),
  beamspots                   =  cms.InputTag  ('offlineBeamSpot',                   ''),
  superclusters               =  cms.InputTag  ('reducedEgamma', 'reducedSuperClusters'),
  taus                        =  cms.InputTag  ('slimmedTaus',                       ''),
  triggers                    =  cms.InputTag  ('TriggerResults',             '', 'HLT'),
  trigobjs                    =  cms.InputTag  ('selectedPatTrigger',                 ''),
)

collections = miniAOD_collections


from DisplacedSUSY.EEChannel.TrigEfficiency import *

eventSelections = [triggerDoublePhoton30orDoublePhoton60]

histograms = cms.VPSet()
weights = cms.VPSet()
scalingfactorproducers = []
variableProducers = []

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collections, variableProducers, True)


