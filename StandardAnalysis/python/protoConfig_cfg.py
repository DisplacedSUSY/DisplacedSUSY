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
process.MessageLogger.cerr.FwkReport.reportEvery = 100
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

          #preselection skim files
          #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/MuMuPreselection_2016Analysis_1April2019/DoubleMu_2016G/Preselection/emptySkim_1.root'
      )
    )
elif os.environ["CMSSW_VERSION"].startswith("CMSSW_9_4_"):
    process.source = cms.Source ('PoolSource',
      fileNames = cms.untracked.vstring (
            #input MINIAOD files
            #'/store/data/Run2017D/MuonEG/MINIAOD/31Mar2018-v1/100000/CC4BAF57-C437-E811-81E1-B496910A9A9C.root'
            #'/store/data/Run2017D/DoubleMuon/MINIAOD/31Mar2018-v1/100000/00915A1A-C937-E811-B03A-009C02AAB484.root'
            #'/store/data/Run2017D/DoubleEG/MINIAOD/31Mar2018-v1/00000/002F7CD1-9D37-E811-A03E-B499BAABCF1A.root'
          #'/store/data/Run2017F/MET/MINIAOD/31Mar2018-v1/00001/804EFF7E-B338-E811-A67D-38EAA7A6DCF0.root'
            #'/store/mc/RunIIFall17MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/143D9394-AF60-E811-96DC-0025904C641E.root'
          #'/store/mc/RunIISummer16MiniAODv3/DisplacedSUSY_stopToBottom_M_1400_1mm_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/182C45DE-E6E9-E811-895B-001EC9ADC226.root'
          '/store/mc/RunIIFall17MiniAODv2/ggH_HToSSTo4l_MH-500_MS-150_ctauS-10_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/A285B521-79F5-EA11-AE5A-782BCB539A7E.root'

            #initial skim files
            #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EMuInitialSkim_2017Analysis_11July2018/MuonEG_2017C/EMuSkim/skim_0.root'
            #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EMuInitialSkim_2017Analysis_11July2018/DYJetsToLL_50/EMuSkim/skim_0.root'
            #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EEInitialSkim_2017Analysis_19July2018/DoubleEG_2017D/EESkim/skim_0.root'
            #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EEInitialSkim_2017Analysis_19July2018/DYJetsToLL_50/EESkim/skim_0.root'

            #'file:/uscms_data/d3/alimena/DisplacedLeptons/CMSSW_9_4_8/src/DisplacedSUSY/StandardAnalysis/python/MINIAODSIM_stopToLD_M_1000_1mm.root'

          #'file:/eos/uscms/store/user/alimena/DisplacedLeptons/MuMuCosmicPreselection_NoBPTX2017_1Sep2020/NoBPTX_2017B/CosmicPreselection/skim_3.root',
      )
    )
elif os.environ["CMSSW_VERSION"].startswith("CMSSW_10_2_") or os.environ["CMSSW_VERSION"].startswith("CMSSW_10_6_"):
    process.source = cms.Source ('PoolSource',
      fileNames = cms.untracked.vstring (
          #input MINIAOD files
          #"/store/data/Run2018D/MuonEG/MINIAOD/PromptReco-v2/000/325/172/00000/C31B5583-B5A6-034D-A38C-66D11A21D9A9.root"
          #"/store/data/Run2018D/DoubleMuon/MINIAOD/PromptReco-v2/000/325/175/00000/ACD8ED9B-F9B0-AE44-B0FD-E20DAB363018.root"
          #"/store/data/Run2018D/EGamma/MINIAOD/PromptReco-v1/000/320/434/00000/1858FF04-BD93-E811-A4C8-FA163E472C72.root"
          #"/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/6391FD45-7256-EC45-B6D4-3DEF9DDCCF90.root"
          #"/store/data/Run2018D/ParkingBPH5/MINIAOD/20Mar2019-v1/60003/FD6BDA2E-F9B0-1D47-B915-73614A217E25.root"
          #"/store/mc/RunIIAutumn18MiniAOD/DisplacedSUSY_stopToLD_M_1200_10mm_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/33568D74-1FF4-5E4F-A5D8-09CDFC436439.root"
          #"/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/FF8CA354-EA2A-CA48-B634-59EC7DE358E6.root"
          "/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FFDCFC59-4ABE-0646-AABE-BD5D65301169.root",
          #"/store/data/Run2018D/MET/MINIAOD/PromptReco-v2/000/325/175/00000/BB60D29A-1476-4B4C-882E-4856877B06D0.root"

          #initial skim files

          #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EMuPreselection_2018Analysis_Signal_12Aug2019/stopToLB1800_1mm/Preselection/skim_0.root'
          #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EEInitialSkim_2018Analysis_15Mar2019/EGamma_2018C/EESkim/skim_1.root'
          #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EMuInitialSkim_2018Analysis_15Mar2019/MuonEG_2018C/EMuSkim/skim_1.root'
          #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/EMuInitialSkim_2018Analysis_15Mar2019/TTJets_DiLept/EMuSkim/skim_1.root'
          #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/MuMuInitialSkim_2018Analysis_15Mar2019/DoubleMu_2018C/MuMuSkim/skim_1.root'
      )
    )
else:
    print "What CMSSW release are you in? We expect to be in 80X or 94X or 102X"

#drop collections that we don't need, and only screw things up
process.source.inputCommands = cms.untracked.vstring(["keep *", "drop osu*_*_originalFormat_*"])

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (1000)
)

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")

################################################################################
##### Set up the global tags ###################################################
################################################################################

#from https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions
#and https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVAnalysisSummaryTable
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    data_global_tag = '80X_dataRun2_2016LegacyRepro_v4'
    mc_global_tag = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    data_global_tag = '94X_dataRun2_v6'
    mc_global_tag = '94X_mc2017_realistic_v14'
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    data_global_tag = '102X_dataRun2_Sep2018ABC_v2'
    mc_global_tag = '102X_upgrade2018_realistic_v18'
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_6_"):
    data_global_tag = '102X_dataRun2_Sep2018ABC_v2' #would need an update
    #mc_global_tag = '106X_mcRun3_2021_realistic_v3'
    #mc_global_tag = '106X_mcRun3_2023_realistic_v3'
    mc_global_tag = '106X_mcRun3_2024_realistic_v4'

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

################################################################################
# Set up the collections of tree branches
################################################################################

from DisplacedSUSY.StandardAnalysis.TreeBranchDefinitions import *

emuBranchSets = cms.VPSet (
    EventVariableBranches,
    EMuEventVariableBranches,
    Electron0Branches,
    Electron0D0Branches,
    Muon0Branches,
    Muon0D0Branches,
)

eeBranchSets = cms.VPSet (
    EventVariableBranches,
    EEEventVariableBranches,
    Electron0Branches,
    Electron0D0Branches,
    Electron1Branches,
    Electron1D0Branches,
)

mumuBranchSets = cms.VPSet (
    EventVariableBranches,
    MuMuEventVariableBranches,
    Muon0Branches,
    Muon0D0Branches,
    Muon1Branches,
    Muon1D0Branches,
)
