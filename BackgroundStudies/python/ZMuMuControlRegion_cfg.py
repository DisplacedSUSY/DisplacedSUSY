import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import math
import os

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('OSUAnalysis')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source ('PoolSource',
  fileNames = cms.untracked.vstring (
    #'file:miniAODSample.root'
    #'root://cmsxrootd.fnal.gov//store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU4bx50_PHYS14_25_V1-v1/00000/080957A7-C36E-E411-A5BC-00266CF327C4.root',
    #'root://cmsxrootd.fnal.gov//store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v3/10000/009D49A5-7314-E511-84EF-0025905A605E.root',
    'file:/data/users/bing/condor/ZControl2015_Aug27th/DoubleMu_2015B/zMuMu/skim_1.root'
    #'root://cmsxrootd.fnal.gov//store/mc/RunIISpring15DR74/DisplacedSUSY_StopToBL_M-900_CTau-10_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/260D284B-3C09-E511-A0C5-008CFA002028.root',
    #'root://cmsxrootd.fnal.gov//store/user/ahart/DisplacedSUSY_StopToBL_M-700_CTau-100_TuneCUETP8M1_13TeV_pythia8/Phys14DR-AVE20BX25_PHYS14_25_V3-v1/150530_130628/0000/EXO-Phys14DR-00001_step4_1.root',
    #'/store/user/ahart/36224FE2-0571-E411-9664-00266CFAE30C.root'
  )
)

#output file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

#process.options = cms.untracked.PSet(
#set number of threads you want
#numberOfThreads = cms.untracked.uint32(1),
#0 means numberOfStreams==numberOfThreads
#numberOfStreams = cms.untracked.uint32(0)
#)

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

###########################################################
##### Set up the analyzer #####
###########################################################

miniAOD_collections = cms.PSet (
  electrons       =  cms.InputTag  ('slimmedElectrons',               ''),
  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),
  jets            =  cms.InputTag  ('slimmedJets',                    ''),
  mcparticles     =  cms.InputTag  ('prunedGenParticles',             ''),
  mets            =  cms.InputTag  ('slimmedMETs',                    ''),
  muons           =  cms.InputTag  ('slimmedMuons',                ''),
  photons         =  cms.InputTag  ('slimmedPhotons',                 ''),
  primaryvertexs  =  cms.InputTag  ('offlineSlimmedPrimaryVertices',  ''),
  beamspots       =  cms.InputTag  ('offlineBeamSpot',                ''),
  superclusters   =  cms.InputTag  ('reducedEgamma',                  'reducedSuperClusters'),
  taus            =  cms.InputTag  ('slimmedTaus',                    ''),
  triggers        =  cms.InputTag  ('TriggerResults',                 '',  'HLT'),
  trigobjs        =  cms.InputTag  ('selectedPatTrigger',             ''),
)

zMuMu = cms.PSet(
    name = cms.string("zMuMu"),
    #triggers = cms.vstring(""), 
    triggers = cms.vstring("HLT_Mu27_TkMu8_v"),
    cuts = cms.VPSet (
      cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > 25.0"),
        numberRequired = cms.string(">= 2")
      ),
      cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 2")
      ),
      #Muon Id
      cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("    \
              isGlobalMuon & \
              isPFMuon & \
              globalTrack.normalizedChi2 < 10 & \
              numberOfMatchedStations > 1 & \
              globalTrack.hitPattern_.numberOfValidMuonHits > 0 & \
              innerTrack.hitPattern_.trackerLayersWithMeasurement > 5 & \
              innerTrack.hitPattern_.numberOfValidPixelHits > 0"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string("muon tight Id"), 
      ),
      # MUON ISOLATION
      cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("                \
              (pfIsolationR04_.sumChargedHadronPt \
              + max(0.0,                            \
              pfIsolationR04_.sumNeutralHadronEt                    \
              + pfIsolationR04_.sumPhotonEt                         \
              - 0.5*pfIsolationR04_.sumPUPt))                        \
              /pt < 0.12"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string("muon dBeta isolation < 0.12")
      ),
      # DiMUON InvMass
      cms.PSet (
        inputCollection = cms.vstring("muons","muons"),
        cutString = cms.string("invMass(muon,muon) > 80"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.vstring("muons","muons"),
        cutString = cms.string("invMass(muon,muon) < 100"),
        numberRequired = cms.string(">= 1"),
      ),
    )
)

diMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("muons","muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonInvMass"),
            title = cms.string("DiMuon invMass;DiMuon invMass [GeV]"),
            binsX = cms.untracked.vdouble(120, 0, 120),
            inputVariables = cms.vstring("invMass(muon,muon)"),
        ),
    )
)

muonHistograms = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonPt"),
            title = cms.string("Muon Transverse Momentum;muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(120, 0, 120),
            inputVariables = cms.vstring("muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonEta"),
            title = cms.string("Muon Pseudorapidity;muon #eta"),
            binsX = cms.untracked.vdouble(50, -2.5, 2.5),
            inputVariables = cms.vstring("muon.eta"),
        ),
        cms.PSet (
            name = cms.string("muonDxy"),
            title = cms.string("Muon IP;muon d_{xy}"),
            binsX = cms.untracked.vdouble(200, -0.1, 0.1),
            inputVariables = cms.vstring("(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonDbetaIsolation"),
            title = cms.string("Muon Isolation; muon d#beta Isolation"),
            binsX = cms.untracked.vdouble(15, 0, 0.15),
            inputVariables = cms.vstring("(muon.pfIsolationR04_.sumChargedHadronPt + max(0.0,muon.pfIsolationR04_.sumNeutralHadronEt + muon.pfIsolationR04_.sumPhotonEt - 0.5*muon.pfIsolationR04_.sumPUPt))/muon.pt"),
        ),
  )
)

add_channels(process,  [zMuMu],  cms.VPSet(muonHistograms, diMuonHistograms),  miniAOD_collections,[],False)
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
