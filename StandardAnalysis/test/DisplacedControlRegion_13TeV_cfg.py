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
    #'root://cmsxrootd.fnal.gov//store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v3/10000/009D49A5-7314-E511-84EF-0025905A605E.root',
    'file:/data/users/bing/condor/EMuSkim13TeV_Oct27th/TTJets_DiLept_MiniAOD/EMuSKim13TeV/skim_82.root',
  )
)


# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (1000)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

# this PSet specifies which collections to get from the input files
miniAOD_collections = cms.PSet (
  candeles        =  cms.InputTag  ('objectSelector0',''),
  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),
  candjets        =  cms.InputTag  ('CandidateJetProducer',                    ''),
  generatorweights = cms.InputTag  ('generator', ''), 
  mcparticles     =  cms.InputTag  ('packedGenParticles',             ''),
  mets            =  cms.InputTag  ('slimmedMETs',                    ''),
  muons           =  cms.InputTag  ('slimmedMuons',                   ''),
  photons         =  cms.InputTag  ('slimmedPhotons',                 ''),
  primaryvertexs  =  cms.InputTag  ('offlineSlimmedPrimaryVertices',  ''),
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

from DisplacedSUSY.StandardAnalysis.DisplacedControlRegionSelection_13TeV import *

eventSelections = []
eventSelections.append(AntiIsoMuIsoEleDisplacedControlRegionInclusiveDisplacedTrigger_13TeV)
eventSelections.append(DisplacedControlRegionInclusiveDisplacedTrigger_13TeV)
eventSelections.append(IsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger_13TeV)
eventSelections.append(AntiIsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger_13TeV)

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################
from DisplacedSUSY.StandardAnalysis.HistogramsDefinitions_13TeV import *
################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, cms.VPSet (muonHistograms,electronHistograms,electronMuonHistograms), collections,variableProducers, False)
