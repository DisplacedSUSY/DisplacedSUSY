import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.LifetimeWeightProducer_cff import *

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
     #'root://cmsxrootd.fnal.gov//store/data/Run2017D/JetHT/MINIAOD/PromptReco-v1/000/302/031/00000/24C14AB9-488F-E711-A2D5-02163E019D41.root'
     #'root://cmsxrootd.fnal.gov//store/data/Run2016G/MET/MINIAOD/23Sep2016-v1/100000/0659060C-C595-E611-9DFF-002590796302.root'
     'root://cmsxrootd.fnal.gov//store/mc/RunIISummer16MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/08D759B1-CBB6-E611-87B3-484D7E8DF0D3.root'
     #'file:condor/EMu_TrigEfficiency_Skim_17_10_03/JetHT_2017D/TTbarForTrigEffNoTrig/skim_0.root'
     #'file:condor/EMuSkim_Moriond17/MuonEG_2016H/EMuSkimSelection/skim_13.root'

  )
)

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# suppress jet producer errors
process.MessageLogger.categories.append ("OSUJetProducer")
process.MessageLogger.cerr.OSUJetProducer = cms.untracked.PSet(
    limit = cms.untracked.int32(0),
)

# suppress gen-matching errors
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.categories.append ("osu_GenMatchable")
process.MessageLogger.cerr.osu_GenMatchable = cms.untracked.PSet(
    limit = cms.untracked.int32 (0)
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (1000)
)

#mc_global_tag needs to be updated before MC is used
#data_global_tag = '92X_dataRun2_Prompt_v9'
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
  electrons                   =  cms.InputTag  ('slimmedElectrons',                  ''),
  genjets                     =  cms.InputTag  ('slimmedGenJets',                    ''),
  jets                        =  cms.InputTag  ('slimmedJets',                       ''),
  bjets                       =  cms.InputTag  ('slimmedJets',                       ''),
  generatorweights            =  cms.InputTag  ('generator',                         ''),
  mcparticles                 =  cms.InputTag  ('packedGenParticles',                ''),
  hardInteractionMcparticles  =  cms.InputTag  ('prunedGenParticles',                ''),
  mets                        =  cms.InputTag  ('slimmedMETs',                       ''),
  muons                       =  cms.InputTag  ('slimmedMuons',                      ''),
  photons                     =  cms.InputTag  ('slimmedPhotons',                    ''),
  primaryvertexs              =  cms.InputTag  ('offlineSlimmedPrimaryVertices',     ''),
  pileupinfos                 =  cms.InputTag  ('slimmedAddPileupInfo',              ''),
  beamspots                   =  cms.InputTag  ('offlineBeamSpot',                   ''),
  superclusters               =  cms.InputTag  ('reducedEgamma', 'reducedSuperClusters'),
  taus                        =  cms.InputTag  ('slimmedTaus',                       ''),
  triggers                    =  cms.InputTag  ('TriggerResults',             '', 'HLT'),
  trigobjs                    =  cms.InputTag  ('selectedPatTrigger',                 ''),
  #trigobjs                    =  cms.InputTag  ('slimmedPatTrigger',                 ''), # changed from selected to slimmed for 92X
)

collections = miniAOD_collections

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
variableProducers.append('DisplacedSUSYEventVariableProducer')
#variableProducers.append('LifetimeWeightProducer')
#variableProducers.append('PUScalingFactorProducer')


weights = cms.VPSet(
#    cms.PSet (
#        inputCollections = cms.vstring("eventvariables"),
#        inputVariable = cms.string("lifetimeWeight")
#    ),
#    cms.PSet (
#        inputCollections = cms.vstring("eventvariables"),
#        inputVariable = cms.string("puScalingFactor")
#    ),
#    cms.PSet (
#        inputCollections = cms.vstring("eventvariables"),
#        inputVariable = cms.string("electronReco2016")
#    ),
#    cms.PSet (
#        inputCollections = cms.vstring("eventvariables"),
#        inputVariable = cms.string("electronID2016Tight")
#    ),
#    cms.PSet (
#        inputCollections = cms.vstring("eventvariables"),
#        inputVariable = cms.string("muonReco2016")
#    ),
#    cms.PSet (
#        inputCollections = cms.vstring("eventvariables"),
#        inputVariable = cms.string("muonID2016Tight")
#    ),
#    cms.PSet (
#        inputCollections = cms.vstring("eventvariables"),
#        inputVariable = cms.string("muonIso2016Tight")
#    ),
)

scalingfactorproducers = []
ObjectScalingFactorProducer = {}

# lepton SFs can exist for triggering, tracking/reco, ID, isolation

# parameters:
# input file for each lepton type
# for each SF:
# inputCollection {electron, muon, track}
# sfType {Trigger, Reco, ID, Iso}
# version: 2015, 2016 
# optional: wp {Veto, Loose, Medium, Tight}
# optional list: eras (e.g. [BCDEF, GH])
# optional list: lumis (e.g. [19717, 16146])
# input distribution is in a histogram called $inputCollection$sfType$version$wp$eras
#    e.g. muonID2016TightBCDEF
# output weight called $inputCollection$sfType$version$wp
#    e.g. muonID2016Tight

# inputs are generally TH2Fs of pt vs eta
# sometimes they're |eta| or 1D plots

#ObjectScalingFactorProducer['name'] = 'ObjectScalingFactorProducer'
#ObjectScalingFactorProducer['muonFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/muonSFs.root')
#ObjectScalingFactorProducer['electronFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSFs.root')
#ObjectScalingFactorProducer['trackFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/trackSFs.root')

#ObjectScalingFactorProducer['scaleFactors'] = cms.VPSet(
#    cms.PSet (
#        inputCollection = cms.string("electrons"),
#        sfType = cms.string("Reco"),
#        version = cms.string("2016")
#    ),
#    cms.PSet (
#        inputCollection = cms.string("electrons"),
#        sfType = cms.string("ID"),
#        version = cms.string("2016"),
#        wp = cms.string("Tight")
#    ),
#    cms.PSet (
#        inputCollection = cms.string("muons"),
#        sfType = cms.string("Reco"),
#        version = cms.string("2016")
#    ),
#    cms.PSet (
#        inputCollection = cms.string("muons"),
#        sfType = cms.string("ID"),
#        version = cms.string("2016"),
#        wp = cms.string("Tight"),
#        eras = cms.vstring("BCDEF","GH"),
#        lumis = cms.vdouble(19717, 16146),
#    ),
#    cms.PSet (
#        inputCollection = cms.string("muons"),
#        sfType = cms.string("Iso"),
#        version = cms.string("2016"),
#        wp = cms.string("Tight"),
#        eras = cms.vstring("BCDEF","GH"),
#        lumis = cms.vdouble(19717, 16146),
#    )
#)
#
#scalingfactorproducers.append(ObjectScalingFactorProducer)

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EMuChannel.TrigEfficiency import *

eventSelections = [
                   TriggerMuonPhoton38,
                   TriggerDisplacedMuonPhoton28,
                   TriggerMuonPhoton38orDisplacedMuonPhoton28,
                   #TTbarForTrigEff,
                   #TTbarForTrigEffMet,
                   #TTbarForTrigEff38,
                   #TTbarForTrigEff43,
                   #TTbarForTrigEff48,
                   #TTbarForTrigEffHighPtE,
                   #TTbarForTrigEff38HighPtE,
                   #TTbarForTrigEff43HighPtE,
                   #TTbarForTrigEff48HighPtE,
                   #TTbarForTrigEffHighPtMu,
                   #TTbarForTrigEff38HighPtMu,
                   #TTbarForTrigEff43HighPtMu,
                   #TTbarForTrigEff48HighPtMu,
                   #TTbarForTrigEff43EFilter,
                   #TTbarForTrigEff43MuFilter,
                  ]

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from OSUT3Analysis.Configuration.histogramDefinitions import ElectronHistograms, MuonHistograms, ElectronMuonHistograms
from DisplacedSUSY.Configuration.histogramDefinitions import ElectronD0Histograms, MuonD0Histograms, ElectronMuonD0Histograms
from OSUT3Analysis.Configuration.histogramDefinitions import JetHistograms, ElectronJetHistograms, MuonJetHistograms
from OSUT3Analysis.Configuration.histogramDefinitions import MetHistograms, ElectronMetHistograms, MuonMetHistograms
from DisplacedSUSY.Configuration.histogramDefinitions import eventHistograms


histograms = cms.VPSet()
histograms.append(ElectronHistograms)
histograms.append(ElectronD0Histograms)
histograms.append(MuonHistograms)
histograms.append(MuonD0Histograms)
histograms.append(ElectronMuonD0Histograms)
histograms.append(ElectronMuonHistograms)
histograms.append(JetHistograms)
histograms.append(ElectronJetHistograms)
histograms.append(MuonJetHistograms)
histograms.append(MetHistograms)
histograms.append(ElectronMetHistograms)
histograms.append(MuonMetHistograms)
histograms.append(eventHistograms)


################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################


add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collections, variableProducers, False)


################################################################################
### Configure variable and weight producers (must be done after add_channels) ##
################################################################################

# default values, altered automatically when using osusub.py
#process.PUScalingFactorProducer.dataset = cms.string("TTJets_DiLept")
#process.PUScalingFactorProducer.target = cms.string ("data2016_GH")
#process.PUScalingFactorProducer.targetUp = cms.string ("data2016_GHUp")
#process.PUScalingFactorProducer.targetDown = cms.string ("data2016_GHDown")
#process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu2016.root')
#process.PUScalingFactorProducer.type = cms.string("bgMC")


process.DisplacedSUSYEventVariableProducer.type = cms.string("data")
process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_MET200_v")
process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.9645)
