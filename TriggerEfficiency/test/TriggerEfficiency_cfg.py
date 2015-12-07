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
  fileNames = cms.untracked.vstring (
    #'file:/data/users/bing/condor/EMuSkim_Nov6th/DYJetsToLL_50_MiniAOD/EMuSKim13TeV/skim_91.root', 
    #'file:/data/users/bing/condor/EMuSkim13TeV/TTJets_DiLept_MiniAOD/EMuSKim13TeV/skim_416.root',
    'file:/data/users/bing/condor/EMuSkim13TeV/MET_2015D_v4/EMuSKim13TeV/skim_107.root'
   )
)


# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (10000)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

# this PSet specifies which collections to get from the input files
miniAOD_collections = cms.PSet (
  electrons       =  cms.InputTag  ('slimmedElectrons',''),
  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),
  jets            =  cms.InputTag  ('slimmedJets',                    ''),
  generatorweights= cms.InputTag  ('generator', ''), 
  mcparticles     =  cms.InputTag  ('packedGenParticles',             ''),
  mets            =  cms.InputTag  ('slimmedMETs',                    ''),
  muons           =  cms.InputTag  ('slimmedMuons',                   ''),
  photons         =  cms.InputTag  ('slimmedPhotons',                 ''),
  primaryvertexs  =  cms.InputTag  ('offlineSlimmedPrimaryVertices',  ''),
  pileupinfos     =  cms.InputTag  ('slimmedAddPileupInfo',  ''),
  beamspots       =  cms.InputTag  ('offlineBeamSpot',                ''),
  superclusters   =  cms.InputTag  ('reducedEgamma',                  'reducedSuperClusters'),
  taus            =  cms.InputTag  ('slimmedTaus',                    ''),
  triggers        =  cms.InputTag  ('TriggerResults',                 '',  'HLT'),
  trigobjs        =  cms.InputTag  ('selectedPatTrigger',             ''),
)

collections = miniAOD_collections

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
variableProducers.append('DisplacedSUSYEventVariableProducer')
#DisplacedSUSYEventVariableProducer can only run over skims
variableProducers.append('PUScalingFactorProducer')

weights = cms.VPSet (
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor")
    ),
)

weightsWithTrigger = cms.VPSet (
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("passTrigger")
    ),
)

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.BackgroundStudies.TTbarControlRegion import *

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################
from DisplacedSUSY.StandardAnalysis.HistogramsDefinitions import *
################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################
#eventHistograms can only run over skims. 
add_channels (process, [TTbarControlRegionMETTrigger], cms.VPSet (muonHistograms,electronHistograms,electronMuonHistograms,eventHistograms, metHistograms, jetHistograms), weights, collections,variableProducers, False)
add_channels (process, [TTbarControlRegionMETTriggerPassEMuTrigger], cms.VPSet (muonHistograms,electronHistograms,electronMuonHistograms,eventHistograms, metHistograms, jetHistograms), weightsWithTrigger, collections,variableProducers, False)

process.PUScalingFactorProducer.dataset = cms.string("TTJets_DiLept_MiniAOD")
process.PUScalingFactorProducer.PU = cms.string("/data/users/bing/condor/PU2015MC/puMC.root")
#process.PUScalingFactorProducer.type = cms.string("bgMC")
process.PUScalingFactorProducer.type = cms.string("data")
#DisplacedSUSYEventVariableProducer can only run over skims.
process.DisplacedSUSYEventVariableProducer.type = cms.string("data")
process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v")
process.DisplacedSUSYEventVariableProducer.triggerScalingFactor = cms.double(1)

#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
