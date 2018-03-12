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
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/00000/00F0B3DC-211B-E611-A6A0-001E67248A39.root",
#    "root://cmsxrootd.fnal.gov//store/mc/RunIISpring16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/00000/00F0B3DC-211B-E611-A6A0-001E67248A39.root",
#    "root://xrootd-cms.infn.it//store/mc/RunIISpring16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/00000/00F0B3DC-211B-E611-A6A0-001E67248A39.root",
#        "file:condor/6EDBEB11-021A-E611-AD3E-001EC9ADEA9B.root",
        "file:condor/DYSample.root",
#        "file:condor/0CB55247-0B4D-E611-AF04-02163E01419D.root",
#        "root://cmsxrootd.fnal.gov//store/data/Run2016E/MuonEG/MINIAOD/PromptReco-v2/000/276/831/00000/0CB55247-0B4D-E611-AF04-02163E01419D.root",

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

from DisplacedSUSY.MuMuChannel.MuMuSkim import *

eventSelections = []
eventSelections.append(MuMuSkim)

weights = cms.VPSet ()

scalingfactorproducers = []
################################################################################
##### Import the histograms to be plotted ######################################
################################################################################
#from DisplacedSUSY.StandardAnalysis.HistogramsDefinitions import *
#from OSUT3Analysis.Configuration.histogramDefinitions import *
#from DisplacedSUSY.Configuration.histogramDefinitions import MuonD0Histograms

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################
#eventHistograms can only run over skims.
histograms = cms.VPSet()
#histograms.append(MuonHistograms)
#histograms.append(MuonJetHistograms)
#histograms.append(MuonD0Histograms)
#histograms.append(MuonIPHistograms)


################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collections, variableProducers, True)
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
