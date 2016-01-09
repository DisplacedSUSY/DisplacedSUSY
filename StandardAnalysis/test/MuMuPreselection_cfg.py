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
        'root://cmsxrootd.fnal.gov//store/data/Run2015D/DoubleMuon/MINIAOD/05Oct2015-v1/30000/04008DF6-8A6F-E511-B034-0025905A6136.root'
#        'file:/data/users/bing/condor/EMuSkim13TeV/DYJetsToLL_50_MiniAOD/EMuSKim13TeV/skim_0.root',
  )
)


#set_input(process, "/data/users/bing/condor/EMuSkim13TeV/DYJetsToLL_50_MiniAOD/EMuSKim13TeV/")

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
  bjets           =  cms.InputTag  ('slimmedJets',                    ''),
  generatorweights=  cms.InputTag  ('generator', ''), 
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
#variableProducers.append('DisplacedSUSYEventVariableProducer')
#variableProducers.append('PUScalingFactorProducer')

weights = cms.VPSet (
#    cms.PSet (
#        inputCollections = cms.vstring("eventvariables"),
#        inputVariable = cms.string("puScalingFactor")
#    ),
)

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.StandardAnalysis.MuMuSkimSelection import *

eventSelections = []
eventSelections.append(MuMuPreselection)


################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.histogramDefinitions import MuonD0Histograms

histograms = cms.VPSet()
histograms.append(MuonHistograms)
histograms.append(MuonIPHistograms)
histograms.append(MuonD0Histograms)
histograms.append(MetHistograms)
histograms.append(JetHistograms)
histograms.append(MuonJetHistograms)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, collections, variableProducers, True)

#process.PUScalingFactorProducer.dataset = cms.string("DYJetsToLL_50_MiniAOD")
#process.PUScalingFactorProducer.PU = cms.string("/data/users/bing/condor/PU2015MC/puMC.root")
#process.PUScalingFactorProducer.type = cms.string("bgMC")

#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
