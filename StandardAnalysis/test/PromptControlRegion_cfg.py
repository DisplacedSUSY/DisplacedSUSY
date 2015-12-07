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
    #'file:./EMuSKim13TeV/skim_EMuSKim13TeV_2015_11_18_16h43m59s.root ',
    #'file:/data/users/bing/condor/EMuSkim13TeV/MuonEG_2015D_v3/EMuSKim13TeV/skim_1.root',
    'file:/data/users/bing/condor/EMuSkim13TeV/TTJets_DiLept_MiniAOD/EMuSKim13TeV/skim_416.root',
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
variableProducers.append('PUScalingFactorProducer')
#DisplacedSUSYEventVariableProducer can only run over skims
variableProducers.append('DisplacedSUSYEventVariableProducer')

weights = cms.VPSet (
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("triggerScalingFactor")
    ),
)
################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.StandardAnalysis.PromptControlRegionSelection import *

eventSelections = []
#eventSelections.append(AntiIsoMuIsoElePromptControlRegionInclusiveDisplacedTrigger)
eventSelections.append(PromptControlRegionInclusiveDisplacedTrigger)
#eventSelections.append(IsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger)
#eventSelections.append(AntiIsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger)
#eventSelections.append(AntiIsoMuIsoElePromptControlRegion)
#eventSelections.append(PromptControlRegion)
#eventSelections.append(IsoMuAntiIsoElePromptControlRegion)
#eventSelections.append(AntiIsoMuAntiIsoElePromptControlRegion)

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################
from DisplacedSUSY.StandardAnalysis.HistogramsDefinitions import *
################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################
#eventHistograms can only run over skims. 

add_channels (process, eventSelections, cms.VPSet (muonHistograms,electronHistograms,electronMuonHistograms,metHistograms,eventHistograms),weights, collections,variableProducers, False)

process.PUScalingFactorProducer.dataset = cms.string("TTJets_DiLept_MiniAOD")
process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu.root')
#process.PUScalingFactorProducer.type = cms.string("data")
process.PUScalingFactorProducer.type = cms.string("bgMC")
#DisplacedSUSYEventVariableProducer can only run over skims.
process.DisplacedSUSYEventVariableProducer.type = cms.string("bgMC")
process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v")
process.DisplacedSUSYEventVariableProducer.triggerScalingFactor = cms.double(1)

#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
