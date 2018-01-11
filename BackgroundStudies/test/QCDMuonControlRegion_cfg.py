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
  #fileNames = cms.untracked.vstring ("file:/store/user/lantonel/QCDMuonSkim/QCD_MuEnriched_50to80/QCDMuonSkim/skim_0.root"),
  fileNames = cms.untracked.vstring (
      #"file:/store/user/lantonel/QCDMuonSkim/QCD_MuEnriched_80to120/QCDMuonSkim/skim_0.root",
      #"file:/store/user/lantonel/QCDMuonSkim/QCD_MuEnriched_50to80/QCDMuonSkim/skim_0.root",
      "file:/store/user/lantonel/QCDMuonSkim/QCD_MuEnriched_50to80/QCDMuonSkim/skim_10.root",
      #"file:/store/user/lantonel/QCDMuonSkim/SingleMu_2016G/QCDMuonSkim/skim_1.root",
      #"file:/store/user/lantonel/QCDMuonSkim/SingleMu_2016H/QCDMuonSkim/skim_0.root",
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
  electrons       =  cms.InputTag  ('slimmedElectrons',''),
  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),
  jets            =  cms.InputTag  ('slimmedJets',     ''),
  bjets           =  cms.InputTag  ("objectSelector0","originalFormat","OSUAnalysisQCDMuonSkim1480532030"), # needs to be fed the exact collection from the skim being used
  generatorweights=  cms.InputTag  ('generator', ''),
  hardInteractionMcparticles  =  cms.InputTag  ('prunedGenParticles',             ''),
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
variableProducers.append('LifetimeWeightProducer')
variableProducers.append('PUScalingFactorProducer')

weights = cms.VPSet(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("lifetimeWeight")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("muonReco2016")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("muonID2016Tight")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("muonIso2016Tight")
    ),
)

scalingfactorproducers = []
ObjectScalingFactorProducer = {}

ObjectScalingFactorProducer['name'] = 'ObjectScalingFactorProducer'
ObjectScalingFactorProducer['muonFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/muonSFs.root')
ObjectScalingFactorProducer['electronFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSFs.root')

ObjectScalingFactorProducer['scaleFactors'] = cms.VPSet(
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("Reco"),
        version = cms.string("2016")
    ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("ID"),
        version = cms.string("2016"),
        wp = cms.string("Tight"),
        eras = cms.vstring("BCDEF","GH"),
        lumis = cms.vdouble(19717, 16146),
    ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("Iso"),
        version = cms.string("2016"),
        wp = cms.string("Tight"),
        eras = cms.vstring("BCDEF","GH"),
        lumis = cms.vdouble(19717, 16146),
    )
)

scalingfactorproducers.append(ObjectScalingFactorProducer)

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.BackgroundStudies.QCDMuonControlRegionSelections import *

eventSelections = [QCDMuonControlRegion]
#                   QCDMuonControlRegionPrompt,
#                   QCDMuonControlRegionDisplaced,
#                   QCDMuonControlRegionVeryDisplaced]

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from DisplacedSUSY.Configuration.histogramDefinitions import eventHistograms
from OSUT3Analysis.Configuration.histogramDefinitions import MuonHistograms
from DisplacedSUSY.Configuration.histogramDefinitions import MuonD0Histograms
from OSUT3Analysis.Configuration.histogramDefinitions import JetHistograms, MuonJetHistograms
from OSUT3Analysis.Configuration.histogramDefinitions import MetHistograms, MuonMetHistograms
from OSUT3Analysis.Configuration.histogramDefinitions import BjetHistograms, MuonBjetHistograms, JetBjetHistograms

histograms = cms.VPSet()
histograms.append(MuonHistograms)
histograms.append(MuonD0Histograms)
histograms.append(JetHistograms)
histograms.append(BjetHistograms)
histograms.append(MetHistograms)
histograms.append(MuonJetHistograms)
histograms.append(MuonMetHistograms)
histograms.append(MuonBjetHistograms)
histograms.append(JetBjetHistograms)
histograms.append(eventHistograms)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collections, variableProducers, False)


# Default values for cmsRun
process.PUScalingFactorProducer.dataset = cms.string("QCD_MuEnriched_170to300")
process.PUScalingFactorProducer.target = cms.string("MuonEG_2015D")
process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu2016.root')
process.PUScalingFactorProducer.type = cms.string("bgMC")
process.DisplacedSUSYEventVariableProducer.type = cms.string("bgMC")

#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
