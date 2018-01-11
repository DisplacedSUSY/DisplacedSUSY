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
#        'root://cmsxrootd.fnal.gov//store/mc/RunIISpring16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/80000/4EF9F71C-0057-E611-A3FF-002590A831AA.root'
#        'root://cmsxrootd.fnal.gov//store/mc/RunIISpring16MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v4/00000/7AADCC01-EC2B-E611-886E-02163E013F02.root'
        'file:condor/EMuSkim_Moriond17/DYJetsToLL_50/EMuSkimSelection/skim_13.root'
    #    'file:condor/EMuSkim_Moriond17/MuonEG_2016H/EMuSkimSelection/skim_13.root'
#    'root://cms-xrd-global.cern.ch//store/data/Run2015D/MuonEG/MINIAOD/16Dec2015-v1/60000/66DF7966-6AAB-E511-BE9D-002590747E40.root'
    # 'file:/store/user/lantonel/EMuSkim_23Sep/MuonEG_2016D_23Sep/EMuSkimSelection/skim_0.root',
    # 'file:/store/user/lantonel/EMuSkim_23Sep/MuonEG_2016D_23Sep/EMuSkimSelection/skim_1.root',
    # 'file:/store/user/lantonel/EMuSkim_23Sep/MuonEG_2016D_23Sep/EMuSkimSelection/skim_2.root',
    # 'file:/store/user/lantonel/EMuSkim_23Sep/MuonEG_2016D_23Sep/EMuSkimSelection/skim_3.root',
    # 'file:/store/user/lantonel/EMuSkim_23Sep/MuonEG_2016D_23Sep/EMuSkimSelection/skim_4.root',
    # 'file:/store/user/lantonel/EMuSkim_23Sep/MuonEG_2016D_23Sep/EMuSkimSelection/skim_5.root',
    # 'file:/store/user/lantonel/EMuSkim_23Sep/MuonEG_2016D_23Sep/EMuSkimSelection/skim_6.root',
    # 'file:/store/user/lantonel/EMuSkim_23Sep/MuonEG_2016D_23Sep/EMuSkimSelection/skim_7.root',
    # 'file:/store/user/lantonel/EMuSkim_23Sep/MuonEG_2016D_23Sep/EMuSkimSelection/skim_8.root',
    # 'file:/store/user/lantonel/EMuSkim_23Sep/MuonEG_2016D_23Sep/EMuSkimSelection/skim_9.root'

  )
)

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# suppress gen-matching errors
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.categories.append ("osu_GenMatchable")
process.MessageLogger.cerr.osu_GenMatchable = cms.untracked.PSet(
    limit = cms.untracked.int32 (0)
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (100)
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
  trigobjs                    =  cms.InputTag  ('selectedPatTrigger',                ''),
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

ObjectScalingFactorProducer['name'] = 'ObjectScalingFactorProducer'
ObjectScalingFactorProducer['muonFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/muonSFs.root')
ObjectScalingFactorProducer['electronFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSFs.root')
ObjectScalingFactorProducer['trackFile'] = cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/trackSFs.root')

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

scalingfactorproducers.append(ObjectScalingFactorProducer)

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EMuChannel.PromptControlRegionSelection import *

eventSelections = [PromptControlRegion]

#eventSelections = [PromptControlRegion,
#                   PromptControlRegionNoElectronIso,
#                   PromptControlRegionNoElectronID,
#                   PromptControlRegionNoMuonIso,
#                   PromptControlRegionNoMuonID]

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
process.PUScalingFactorProducer.dataset = cms.string("TTJets_DiLept")
process.PUScalingFactorProducer.target = cms.string("Data2016")
process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/Configuration/data/pu2016.root')
process.PUScalingFactorProducer.type = cms.string("bgMC")


process.DisplacedSUSYEventVariableProducer.type = cms.string("bgMC")
