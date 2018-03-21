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
# suppress gen-matching erros
process.MessageLogger.categories.append ("osu_GenMatchable")
process.MessageLogger.cerr.osu_GenMatchable = cms.untracked.PSet(
    limit = cms.untracked.int32 (0)
)

################################################################################
##### Set up the input files, output files, ####################################
##### max number of events (when run interactively) ############################
################################################################################

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    process.source = cms.Source ('PoolSource',
      fileNames = cms.untracked.vstring (
            '/store/data/Run2016G/MuonEG/MINIAOD/23Sep2016-v1/100000/005AB7E9-0B93-E611-AC81-848F69FD2925.root'
      )
    )
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    process.source = cms.Source ('PoolSource',
      fileNames = cms.untracked.vstring (
            '/store/data/Run2017B/MuonEG/MINIAOD/17Nov2017-v1/50000/021C1D6D-88E5-E711-9349-002590207C28.root'
      )
    )
else:
    print "What CMSSW release are you in? We expect to be in 80X or 94X"

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (100)
)

################################################################################
##### Set up the global tags ###################################################
################################################################################

#from https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    data_global_tag = '80X_dataRun2_2016SeptRepro_v6'
    mc_global_tag = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    data_global_tag = '94X_dataRun2_ReReco_EOY17_v2'
    mc_global_tag = '94X_mc2017_realistic_v12'

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
