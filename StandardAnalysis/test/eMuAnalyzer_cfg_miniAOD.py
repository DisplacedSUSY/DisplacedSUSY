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

# input source when running interactively
# ---------------------------------------
# argument can be a ROOT file, directory, or dataset name*
# *registered dataset names are listed in 'datasets' in:
#    https://github.com/OSU-CMS/OSUT3Analysis/blob/master/Configuration/python/configurationOptions.py

# sample direcotory
#set_input(process, "/store/user/ahart/BN_stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_1/")

#set_input(process, "root://cmsxrootd.fnal.gov//store/relval/CMSSW_7_2_1/RelValZTT_13/MINIAODSIM/PU25ns_PHYS14_25_V1_Phys14-v1/00000/0A3E2293-DB5E-E411-ABE2-02163E00E7EA.root")
set_input(process, "root://cmsxrootd.fnal.gov//store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU4bx50_PHYS14_25_V1-v1/00000/080957A7-C36E-E411-A5BC-00266CF327C4.root")


# sample ROOT file
#set_input(process, "/store/user/ahart/BN_stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_1/stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_10_2_Dzw.root")

# sample dataset nickname
#set_input(process, "DYToTauTau_20")
#set_input(process, "DYToMuMu_20")

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

# this PSet specifies which collections to get from the input files
miniAOD_collections = cms.PSet (
  electrons       =  cms.InputTag  ('slimmedElectrons',               ''),
  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),
  jets            =  cms.InputTag  ('slimmedJets',                    ''),
  mcparticles     =  cms.InputTag  ('packedGenParticles',             ''),
  mets            =  cms.InputTag  ('slimmedMETs',                    ''),
  muons           =  cms.InputTag  ('slimmedMuons',                   ''),
  photons         =  cms.InputTag  ('slimmedPhotons',                 ''),
  primaryvertexs  =  cms.InputTag  ('offlineSlimmedPrimaryVertices',  ''),
  superclusters   =  cms.InputTag  ('reducedEgamma',                  'reducedSuperClusters'),
  taus            =  cms.InputTag  ('slimmedTaus',                    ''),
  triggers        =  cms.InputTag  ('TriggerResults',                 '',  'PAT'),
  trigobjs        =  cms.InputTag  ('selectedPatTrigger',             ''),
)

collections = miniAOD_collections

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
#variableProducers.append("MyVariableProducer")
#variableProducers.append("MyOtherVariableProducer")

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.StandardAnalysis.Preselection import *
#from DisplacedSUSY.StandardAnalysis.SkimSelections import *
#from OSUT3Analysis.ExampleAnalysis.MyProtoEventSelections import *

eventSelections = []
#eventSelections.append(eMuMinimalUserVariables)
eventSelections.append(Preselection)
#eventSelections.append(eMuMinimal)
#eventSelections.append(EMu_Skim)

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from OSUT3Analysis.Configuration.histogramDefinitions_miniAOD import *
histograms = []
histograms.append(MuonHistograms)
histograms.append(ElectronHistograms)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, cms.VPSet (histograms), collections, [], False)
#add_channels (process, eventSelections, cms.VPSet (MuonHistograms), collections, variableProducers, False)


# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
