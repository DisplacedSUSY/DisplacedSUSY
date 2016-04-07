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
    'root://cms-xrd-global.cern.ch//store/mc/RunIIFall15MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/00000/12086E80-62BC-E511-AED8-6CC2173CEC30.root'
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
variableProducers.append('DisplacedSUSYEventVariableProducer')
variableProducers.append('PUScalingFactorProducer')

weights = cms.VPSet (
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("triggerScalingFactor")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("electronScalingFactor")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("muonScalingFactor")
    ),
)

scalingfactorproducers = []
ObjectScalingFactorProducer = {}
ObjectScalingFactorProducer['name'] = 'ObjectScalingFactorProducer'
ObjectScalingFactorProducer['muonFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/muonSF.root')
ObjectScalingFactorProducer['electronFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSF.root')
ObjectScalingFactorProducer['muonWp'] = cms.string('TightID')
ObjectScalingFactorProducer['electronWp'] = cms.string('TightID')
ObjectScalingFactorProducer['doEleSF'] = cms.bool(True)
ObjectScalingFactorProducer['doMuSF'] = cms.bool(True)

scalingfactorproducers.append(ObjectScalingFactorProducer)
################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.StandardAnalysis.EMuPreselection import *

eventSelections = []
#eventSelections.append(EMuPreselectionControlTrigger)
eventSelections.append(EMuPreselectionInclusiveTrigger)

from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.histogramDefinitions import ElectronD0Histograms,MuonD0Histograms,ElectronMuonD0Histograms
from DisplacedSUSY.StandardAnalysis.HistogramsDefinitions import eventHistograms
################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################
#eventHistograms can only run over skims. 
histograms = cms.VPSet()
histograms.append(ElectronHistograms)
histograms.append(ElectronD0Histograms)
histograms.append(ElectronIPHistograms)
histograms.append(MuonHistograms)
histograms.append(MuonD0Histograms)
histograms.append(MuonIPHistograms)
histograms.append(ElectronMuonD0Histograms)
histograms.append(ElectronMuonHistograms)
histograms.append(eventHistograms)
################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collections, variableProducers, False)

process.PUScalingFactorProducer.dataset = cms.string("TTJets_DiLept")
process.PUScalingFactorProducer.target = cms.string("MuonEG_2015D")
process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu.root')
process.PUScalingFactorProducer.type = cms.string("bgMC")
#DisplacedSUSYEventVariableProducer can only run over skims.
process.DisplacedSUSYEventVariableProducer.type = cms.string("bgMC")
process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v")
process.DisplacedSUSYEventVariableProducer.triggerScalingFactor = cms.double(0.9783)

#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
