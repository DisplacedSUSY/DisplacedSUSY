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
  fileNames = cms.untracked.vstring ("file:/store/user/lantonel/QCDElectronSkim/QCD_EMEnriched_50to80/QCDElectronSkim/skim_0.root",
                                     "file:/store/user/lantonel/QCDElectronSkim/QCD_EMEnriched_50to80/QCDElectronSkim/skim_1.root",
                                     "file:/store/user/lantonel/QCDElectronSkim/QCD_EMEnriched_50to80/QCDElectronSkim/skim_2.root",
                                     "file:/store/user/lantonel/QCDElectronSkim/QCD_EMEnriched_50to80/QCDElectronSkim/skim_3.root",
                                     "file:/store/user/lantonel/QCDElectronSkim/QCD_EMEnriched_50to80/QCDElectronSkim/skim_4.root",



)
)


# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (10)
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
  bjets           =  cms.InputTag  ("objectSelector1","originalFormat","OSUAnalysisQCDElectronSkim1483021621"), # needs to be fed the exact collection from the skim being used
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
        inputVariable = cms.string("triggerScaleFactor")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("electronReco2016")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("electronID2016Tight")
    ),
)

scalingfactorproducers = []
ObjectScalingFactorProducer = {}

ObjectScalingFactorProducer['name'] = 'ObjectScalingFactorProducer'
ObjectScalingFactorProducer['muonFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/muonSFs.root')
ObjectScalingFactorProducer['electronFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSFs.root')

ObjectScalingFactorProducer['scaleFactors'] = cms.VPSet(
    cms.PSet (
        inputCollection = cms.string("electrons"),
        sfType = cms.string("Reco"),
        version = cms.string("2016")
    ),
    cms.PSet (
        inputCollection = cms.string("electrons"),
        sfType = cms.string("ID"),
        version = cms.string("2016"),
        wp = cms.string("Tight")
    ),
)
scalingfactorproducers.append(ObjectScalingFactorProducer)

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.BackgroundStudies.QCDElectronControlRegionSelections import *

eventSelections = [QCDElectronControlRegion]
#                   QCDElectronControlRegionPrompt,
#                   QCDElectronControlRegionDisplaced,
#                   QCDElectronControlRegionVeryDisplaced]

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from DisplacedSUSY.Configuration.histogramDefinitions import eventHistograms
from OSUT3Analysis.Configuration.histogramDefinitions import ElectronHistograms
from DisplacedSUSY.Configuration.histogramDefinitions import ElectronD0Histograms
from OSUT3Analysis.Configuration.histogramDefinitions import JetHistograms, ElectronJetHistograms
from OSUT3Analysis.Configuration.histogramDefinitions import MetHistograms, ElectronMetHistograms
from OSUT3Analysis.Configuration.histogramDefinitions import BjetHistograms, ElectronBjetHistograms, JetBjetHistograms

histograms = cms.VPSet()
histograms.append(ElectronHistograms)
histograms.append(ElectronD0Histograms)
histograms.append(JetHistograms)
histograms.append(BjetHistograms)
histograms.append(MetHistograms)
histograms.append(ElectronJetHistograms)
histograms.append(ElectronMetHistograms)
histograms.append(ElectronBjetHistograms)
histograms.append(JetBjetHistograms)
histograms.append(eventHistograms)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers,collections, variableProducers, False)


# Default values for cmsRun
process.PUScalingFactorProducer.dataset = cms.string("QCD_MuEnriched_170to300")
process.PUScalingFactorProducer.target = cms.string ("data2016_GH")
process.PUScalingFactorProducer.targetUp = cms.string ("data2016_GHUp")
process.PUScalingFactorProducer.targetDown = cms.string ("data2016_GHDown")
process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu2016.root')
process.PUScalingFactorProducer.type = cms.string("bgMC")
process.DisplacedSUSYEventVariableProducer.type = cms.string("bgMC")
process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_MET200_v")
process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.9645)

#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
