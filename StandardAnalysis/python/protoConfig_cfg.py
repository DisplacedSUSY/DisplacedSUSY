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
        'file:/data/users/bcardwell/condor/EMuSkim_Moriond17/DYJetsToLL_50/EMuSkimSelection/skim_13.root'
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
else:
    print "What CMSSW release are you in? We expect to be in 80X or 94X"

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

scalingfactorproducers = []
scalingfactorproducers.append(ObjectScalingFactorProducer)




################################################################################
##### Import the channels to be run ############################################
################################################################################
from DisplacedSUSY.EMuChannel.Preselection import *
from DisplacedSUSY.MuMuChannel.Preselection import *
from DisplacedSUSY.EEChannel.Preselection import *
#others

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from OSUT3Analysis.Configuration.histogramDefinitions import ElectronHistograms, MuonHistograms, ElectronMuonHistograms
from DisplacedSUSY.Configuration.histogramDefinitions import ElectronD0Histograms, MuonD0Histograms, ElectronMuonD0Histograms, BeamspotHistograms
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
histograms.append(BeamspotHistograms)
histograms.append(eventHistograms)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################


add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers, False)


################################################################################
##### Apply PU reweighting #####################################################
################################################################################

process.PUScalingFactorProducer.dataset = cms.string("TTJets_DiLept") # default value, only used when running interactively
process.PUScalingFactorProducer.type = cms.string("bgMC")

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    process.PUScalingFactorProducer.target = cms.string ("data2016_GH")
    process.PUScalingFactorProducer.targetUp = cms.string ("data2016_GHUp")
    process.PUScalingFactorProducer.targetDown = cms.string ("data2016_GHDown")
    process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu2016.root')

#FIXME: need to update for 2017
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    process.PUScalingFactorProducer.target = cms.string ("data2016_GH")
    process.PUScalingFactorProducer.targetUp = cms.string ("data2016_GHUp")
    process.PUScalingFactorProducer.targetDown = cms.string ("data2016_GHDown")
    process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu2016.root')


################################################################################
##### Apply trigger scale factor ###############################################
################################################################################

#FIXME: need to derive trigger scale factors for ee and mumu channels as well

process.DisplacedSUSYEventVariableProducer.type = cms.string("bgMC")
process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_MET200_v")

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.9645)
#FIXME: need to update for 2017
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.9645)
