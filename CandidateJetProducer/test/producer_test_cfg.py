import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import math
import os

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('DisplacedFermion')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source ('PoolSource',
  fileNames = cms.untracked.vstring (
    #'file:miniAODSample.root'
    #'root://cmsxrootd.fnal.gov//store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU4bx50_PHYS14_25_V1-v1/00000/080957A7-C36E-E411-A5BC-00266CF327C4.root',
    #'root://cmsxrootd.fnal.gov//store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v3/10000/009D49A5-7314-E511-84EF-0025905A605E.root',
    #'root://cms-xrd-global.cern.ch//store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/493/00000/323EBCB2-D428-E511-86E5-02163E01463E.root'   
    #'file:/home/bing/DisplacedFermion/CMSSW_7_4_5_ROOT5/src/OSUT3Analysis/test/condor/ZControl2015_Aug27th/DoubleMu_2015C/zMuMu/skim_10.root',
    'file:/data/users/bing/miniAOD_74X_sample.root',
    #'file:/data/users/bing/condor/ZControl2015_Aug27th/DoubleMu_2015B/zMuMu/skim_1.root'
    #'root://cmsxrootd.fnal.gov//store/mc/RunIISpring15DR74/DisplacedSUSY_StopToBL_M-900_CTau-10_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/260D284B-3C09-E511-A0C5-008CFA002028.root',
    #'root://cmsxrootd.fnal.gov//store/user/ahart/DisplacedSUSY_StopToBL_M-700_CTau-100_TuneCUETP8M1_13TeV_pythia8/Phys14DR-AVE20BX25_PHYS14_25_V3-v1/150530_130628/0000/EXO-Phys14DR-00001_step4_1.root',
    #'/store/user/ahart/36224FE2-0571-E411-9664-00266CFAE30C.root'
  )
)

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

process.customizeJet = cms.EDProducer("CandidateJetProducer",
    patJet = cms.InputTag  ("slimmedJets",           "",                ""),
)

process.output = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('Modified-MiniAOD'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('ProducerTest.root'),
    outputCommands = cms.untracked.vstring('keep *',
    'drop *_TriggerResults_*_DisplacedFermion'),
    splitLevel = cms.untracked.int32(0)
)

process.p = cms.Path(process.customizeJet)

process.e = cms.EndPath(process.output)
