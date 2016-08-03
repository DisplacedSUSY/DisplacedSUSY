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
  fileNames = cms.untracked.vstring ("root://cms-xrd-global.cern.ch//store/mc/RunIIFall15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/00000/181E4D02-59BC-E511-A927-001EC9ADD8FD.root"),
  skipBadFiles = cms.untracked.bool (True),
)
# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (6000)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

# this PSet specifies which collections to get from the input files
miniAOD_collections = cms.PSet (
  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),
  mcparticles     =  cms.InputTag  ('packedGenParticles',             ''),
  mets            =  cms.InputTag  ('slimmedMETs',                    ''),
  muons           =  cms.InputTag  ('slimmedMuons',                   ''),
  jets            =  cms.InputTag  ('slimmedJets',                   ''),
  bjets           =  cms.InputTag  ('slimmedJets',                   ''),
  electrons       =  cms.InputTag  ('slimmedElectrons',               ''),
  photons         =  cms.InputTag  ('slimmedPhotons',                 ''),
  generatorweights = cms.InputTag  ('generator', ''),
  hardInteractionMcparticles  =  cms.InputTag  ('prunedGenParticles',             ''), 
  primaryvertexs  =  cms.InputTag  ('offlineSlimmedPrimaryVertices',  ''),
  #please notice this inputTag is different in miniAODv1 and v2.
  #pileupinfos     =  cms.InputTag  ("addPileupInfo",           ""),
  pileupinfos     =  cms.InputTag  ("slimmedAddPileupInfo",           ""),
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

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.StandardAnalysis.EMuSkimSelection import *

eventSelections = []
eventSelections.append(EMuPreselectionSkim)

weights = cms.VPSet ()

scalingfactorproducers = []
################################################################################
##### Import the histograms to be plotted ######################################
################################################################################
from DisplacedSUSY.StandardAnalysis.HistogramsDefinitions import *

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, cms.VPSet(), weights, scalingfactorproducers, collections, variableProducers, True)
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
