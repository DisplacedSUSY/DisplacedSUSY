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

################################################################################
##### Set up the Message Logger ################################################
################################################################################

# how often to print a log message
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10
# suppress gen-matching errors
process.MessageLogger.categories.append ("osu_GenMatchable")
process.MessageLogger.cerr.osu_GenMatchable = cms.untracked.PSet(
    limit = cms.untracked.int32 (0)
)

################################################################################
##### Set up the input files, output files, ####################################
##### max number of events (when run interactively) ############################
################################################################################

if os.environ["CMSSW_VERSION"].startswith("CMSSW_8_0_"):
    process.source = cms.Source ('PoolSource',
      fileNames = cms.untracked.vstring (
            #input MINIAOD files
            #'/store/data/Run2016G/MuonEG/MINIAOD/07Aug17-v1/10000/04360562-9C92-E711-A8A3-4C79BA180B5D.root'
            #'/store/data/Run2016G/DoubleEG/MINIAOD/07Aug17-v1/00000/1EF72C1E-DFB3-E711-A459-0242AC110005.root'
            #'/store/data/Run2016G/DoubleMuon/MINIAOD/07Aug17-v1/10000/00448C94-C19A-E711-BC4C-A4BF01125660.root'
            '/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/04F61242-90BA-E611-B842-001E67DFF7CB.root'

            #initial skim files
            #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EMuInitialSkim_2016Analysis_11July2018/MuonEG_2016G/EMuSkim/skim_0.root'
            #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EMuInitialSkim_2016Analysis_11July2018/DYJetsToLL_50/EMuSkim/skim_0.root'
            #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EEInitialSkim_2016Analysis_17July2018/DoubleEG_2016G/EESkim/skim_0.root'
            #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EEInitialSkim_2016Analysis_17July2018/DYJetsToLL_50/EESkim/skim_0.root'
      )
    )
elif os.environ["CMSSW_VERSION"].startswith("CMSSW_9_4_"):
    process.source = cms.Source ('PoolSource',
      fileNames = cms.untracked.vstring (
            #input MINIAOD files
            '/store/data/Run2017D/MuonEG/MINIAOD/31Mar2018-v1/100000/CC4BAF57-C437-E811-81E1-B496910A9A9C.root'
            #'/store/data/Run2017D/DoubleMuon/MINIAOD/31Mar2018-v1/100000/00915A1A-C937-E811-B03A-009C02AAB484.root'
            #'/store/data/Run2017D/DoubleEG/MINIAOD/31Mar2018-v1/00000/002F7CD1-9D37-E811-A03E-B499BAABCF1A.root'
            #'/store/mc/RunIIFall17MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/143D9394-AF60-E811-96DC-0025904C641E.root'

            #initial skim files
            #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EMuInitialSkim_2017Analysis_11July2018/MuonEG_2017C/EMuSkim/skim_0.root'
            #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EMuInitialSkim_2017Analysis_11July2018/DYJetsToLL_50/EMuSkim/skim_0.root'
            #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EEInitialSkim_2017Analysis_19July2018/DoubleEG_2017D/EESkim/skim_0.root'
            #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EEInitialSkim_2017Analysis_19July2018/DYJetsToLL_50/EESkim/skim_0.root'
      )
    )
else:
    print "What CMSSW release are you in? We expect to be in 80X or 94X"

#drop collections that we don't need, and only screw things up
process.source.inputCommands = cms.untracked.vstring(["keep *", "drop osu*_*_originalFormat_*"])

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (100)
)

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')

################################################################################
##### Set up the global tags ###################################################
################################################################################

#from https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    data_global_tag = '80X_dataRun2_2016LegacyRepro_v4'
    mc_global_tag = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    data_global_tag = '94X_dataRun2_v6'
    mc_global_tag = '94X_mc2017_realistic_v14'

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

# Import MiniAOD collection map from OSUT3Analysis
from OSUT3Analysis.AnaTools.osuAnalysis_cfi import collectionMap

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
variableProducers.append('DisplacedSUSYEventVariableProducer')
variableProducers.append('LifetimeWeightProducer')
variableProducers.append('PUScalingFactorProducer')

################################################################################
##### Set up event weights #####################################################
################################################################################

from DisplacedSUSY.StandardAnalysis.EventWeights import *

################################################################################
##### Set up scale factors #####################################################
################################################################################

from DisplacedSUSY.StandardAnalysis.LeptonScaleFactors import *

# These will look for framework object producers, meaning if you don't apply any
# cuts on say electrons it will throw a product-not-found error for osu::electrons
# Meaning, only use these if they make sense to use
scalingfactorproducers = []
scalingfactorproducers.append(ElectronScaleFactorProducer)
scalingfactorproducers.append(MuonScaleFactorProducer)
