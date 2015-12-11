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
    'file:/data/users/bing/condor/CosmicMuonSkim/NoBPTX_2015D_v3/CosmicMuonSkimSelection/skim_146.root',
  )
)

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

# this PSet specifies which collections to get from the input files
miniAOD_collections = cms.PSet (
  electrons       =  cms.InputTag  ('slimmedElectrons',''),
  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),
  jets            =  cms.InputTag  ('slimmedJets',                    ''),
  generatorweights=  cms.InputTag  ('generator', ''), 
  mcparticles     =  cms.InputTag  ('packedGenParticles',             ''),
  mets            =  cms.InputTag  ('slimmedMETs',                    ''),
  muons           =  cms.InputTag  ('DisplacedSUSYCosmicMuonProducer',   '',                'OSUAnalysis'),
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
#variableProducers.append("DisplacedSUSYCosmicMuonProducer")

weights = cms.VPSet (
)
################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.DisplacedTrackingStudies.CosmicMuonSelection import *

eventSelections = []
eventSelections.append(CosmicMuonSTASelection)
eventSelections.append(CosmicMuonGLBSelection)

from DisplacedSUSY.DisplacedTrackingStudies.CosmicHistogramsDefinitions import *

add_channels (process, eventSelections, cms.VPSet(cosmicMuonHistograms),weights, collections,variableProducers, False)
#process.DisplacedSUSYCosmicMuonProducer.muons = cms.InputTag('objectSelector0','')
#process.DisplacedSUSYCosmicMuonProducer.maxDeltaRForGenMatching = cms.double (0.1)

#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
