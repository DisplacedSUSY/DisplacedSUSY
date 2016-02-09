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
#    'root://cmsxrootd.fnal.gov//store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v3/10000/009D49A5-7314-E511-84EF-0025905A605E.root',
     #'file:/data/users/bing/condor/QCDElectronSkim/SingleEle_2015D_v3/QCDElectronSkim/skim_21.root',
     'file:/data/users/bing/condor/QCDElectronSkim/SingleEle_2015D_v3/QCDElectronSkim/skim_21.root',
     #'file:/data/users/bing/condor/QCDElectronSkim/QCD_EMEnriched_170to300/QCDElectronSkim/skim_79.root'
  )
)


#set_input(process, "/data/users/bing/condor/EMuSkim13TeV/TTJets_DiLept_MiniAOD/EMuSKim13TeV/")

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
  electrons       =  cms.InputTag  ('slimmedElectrons',''),
  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),
  jets            =  cms.InputTag  ('slimmedJets',                    ''),
  bjets           =  cms.InputTag  ('slimmedJets',                   ''),
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
variableProducers.append('PUScalingFactorProducer')

weights = cms.VPSet (
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor")
    ),
    #cms.PSet (
    #    inputCollections = cms.vstring("eventvariables"),
    #    inputVariable = cms.string("electronScalingFactor")
    #),
)

scalingfactorproducers = []
#ObjectScalingFactorProducer = {}
#ObjectScalingFactorProducer['name'] = 'ObjectScalingFactorProducer'
#ObjectScalingFactorProducer['muonFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/muonSF.root')
#ObjectScalingFactorProducer['electronFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSF.root')
#ObjectScalingFactorProducer['muonWp'] = cms.string('NUM_TightIDandIPCut_DEN_genTracks_PAR_pt_spliteta_bin1/abseta_vs_pt')
#ObjectScalingFactorProducer['electronWp'] = cms.string('GlobalSF')
#ObjectScalingFactorProducer['doEleSF'] = cms.bool(True)
#ObjectScalingFactorProducer['doMuSF'] = cms.bool(False)

#scalingfactorproducers.append(ObjectScalingFactorProducer)
################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.BackgroundStudies.QCDControlRegions import *

eventSelections = []
eventSelections.append(QCDElectronControlRegion)

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.histogramDefinitions import ElectronD0Histograms
from DisplacedSUSY.StandardAnalysis.HistogramsDefinitions import eventHistograms

histograms = cms.VPSet()
histograms.append(ElectronHistograms)
histograms.append(ElectronIPHistograms)
histograms.append(ElectronD0Histograms)
histograms.append(MetHistograms)
histograms.append(JetHistograms)
histograms.append(BjetHistograms)
histograms.append(JetBjetHistograms)
histograms.append(ElectronJetHistograms)
histograms.append(ElectronBjetHistograms)
histograms.append(eventHistograms)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collections, variableProducers, False)

process.PUScalingFactorProducer.dataset = cms.string("QCD_EMEnriched_170to300")
process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu.root')
process.PUScalingFactorProducer.type = cms.string("data")

#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
