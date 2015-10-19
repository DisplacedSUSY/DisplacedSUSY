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
  fileNames = cms.untracked.vstring (
    #'root://cmsxrootd.fnal.gov//store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v3/10000/009D49A5-7314-E511-84EF-0025905A605E.root',
    #'file:/home/bing/DisplacedFermion/CMSSW_7_4_5_ROOT5/src/DisplacedSUSY/CandidateElectronProducer/test/ProducerTest.root',
    #'file:/data/users/bing/condor/EMuSkim_2015/MuonEG_2015D/EMuSKim13TeV/skim_14.root',
    'file:/data/users/bing/condor/EMuSkim_2015/DYJetsToLL_50_MiniAOD/EMuSKim13TeV/skim_6.root',
  )
)


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
  candeles       =  cms.InputTag   ('objectSelector0',''),
  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),
  jets            =  cms.InputTag  ('slimmedJets',                    ''),
  mcparticles     =  cms.InputTag  ('packedGenParticles',             ''),
  mets            =  cms.InputTag  ('slimmedMETs',                    ''),
  muons           =  cms.InputTag  ('slimmedMuons',                   ''),
  photons         =  cms.InputTag  ('slimmedPhotons',                 ''),
  primaryvertexs  =  cms.InputTag  ('offlineSlimmedPrimaryVertices',  ''),
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
#variableProducers.append("CandidateElectronProducer")
#variableProducers.append("MyOtherVariableProducer")

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.StandardAnalysis.PromptControlRegionSelection_13TeV import *
#from DisplacedSUSY.StandardAnalysis.SkimSelections import *
#from OSUT3Analysis.ExampleAnalysis.MyProtoEventSelections import *

eventSelections = []
#eventSelections.append(PromptControlRegion)
eventSelections.append(PromptControlRegionPromptTrigger)
#eventSelections.append(PromptControlRegionInclusiveDisplacedTrigger)

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################
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
            name = cms.string("muonPhi"),
            title = cms.string("Muon Azimuthal Angle;muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("muon.phi"),
        ),
        cms.PSet (
            name = cms.string("muonPFMuonFlag"),
            title = cms.string("Muon PFMuonFlas;muon isPFMuon"),
            binsX = cms.untracked.vdouble(4, -2, 2),
            inputVariables = cms.vstring("muon.isPFMuon"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfValidMuonHits"),
            title = cms.string("Muon Number of Valid Muon Hits;muon numberOfValidMuonHits"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("muon.globalTrack.hitPattern_.numberOfValidMuonHits"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfMatchedStations"),
            title = cms.string("Muon Number of Matched Stations;muon numberOfMatchedStations"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("muon.numberOfMatchedStations"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfValidPixelHits"),
            title = cms.string("Muon Number of Valid Pixel Hits;muon numberOfValidPixelHits"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("muon.innerTrack.hitPattern_.numberOfValidPixelHits"),
        ),
        cms.PSet (
            name = cms.string("muonTrackerLayersWithMeasurement"),
            title = cms.string("Muon Number of Tracker Layer with Measurement;muon trackerLayersWithMeasurement"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("muon.innerTrack.hitPattern_.trackerLayersWithMeasurement"),
        ),
        cms.PSet (
            name = cms.string("muonSumChargedHadronPt"),
            title = cms.string("Muon sumChargedHadronPt;muon sumChargedHadronPt [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("muon.pfIsolationR04_.sumChargedHadronPt"),
        ),
        cms.PSet (
            name = cms.string("muonSumNeutralHadronEt"),
            title = cms.string("Muon sumNeutralHadronEt;muon sumNeutralHadronEt [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("muon.pfIsolationR04_.sumNeutralHadronEt"),
        ),
        cms.PSet (
            name = cms.string("muonSumPhotonEt"),
            title = cms.string("Muon sumPhotonEt;muon sumPhotonEt [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("muon.pfIsolationR04_.sumPhotonEt"),
        ),
        cms.PSet (
            name = cms.string("muonSumPUPt"),
            title = cms.string("Muon sumPUPt;muon sumPUPt [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("muon.pfIsolationR04_.sumPUPt"),
        ),
        cms.PSet (
            name = cms.string("muonDxy"),
            title = cms.string("Muon IP;muon d_{xy}"),
            binsX = cms.untracked.vdouble(2000, -0.1, 0.1),
            inputVariables = cms.vstring("(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonDz"),
            title = cms.string("Muon Dz;muon d_{z}"),
            binsX = cms.untracked.vdouble(200, -10, 10),
            inputVariables = cms.vstring("(muon.vz - beamspot.z0) - ((muon.vx - beamspot.x0)*muon.px + (muon.vy - beamspot.y0)*muon.py)/muon.pt*(muon.pz/muon.pt)"),
        ),
        cms.PSet (
            name = cms.string("muonDbetaIsolation"),
            title = cms.string("Muon Isolation; muon d#beta Isolation"),
            binsX = cms.untracked.vdouble(15, 0, 0.15),
            inputVariables = cms.vstring("(muon.pfIsolationR04_.sumChargedHadronPt + max(0.0,muon.pfIsolationR04_.sumNeutralHadronEt + muon.pfIsolationR04_.sumPhotonEt - 0.5*muon.pfIsolationR04_.sumPUPt))/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonDxyPhi"),
            title = cms.string("Muon IP vs Azimuthal Angle;muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(2000, -0.1, 0.1),
            inputVariables = cms.vstring("muon.phi","(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
  )
)

electronHistograms = cms.PSet(
    inputCollection = cms.vstring("candeles","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronPt"),
            title = cms.string("Electron Transverse Momentum;electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(120, 0, 120),
            inputVariables = cms.vstring("candele.pt"),
        ),
        cms.PSet (
            name = cms.string("electronEta"),
            title = cms.string("Electron Pseudorapidity;electron #eta"),
            binsX = cms.untracked.vdouble(50, -2.5, 2.5),
            inputVariables = cms.vstring("candele.eta"),
        ),
        cms.PSet (
            name = cms.string("electronPhi"),
            title = cms.string("Electron Azimuthal Angle;electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("candele.phi"),
        ),
        cms.PSet (
            name = cms.string("electronNumberOfMissingInnerHits"),
            title = cms.string("Electron Number of Missing Inner Hits;electron #misingInnerHits"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("candele.missingInnerHits"),
        ),
        cms.PSet (
            name = cms.string("electrondeltaEtaSuperClusterTrackAtVtx"),
            title = cms.string("Electron deltaEtaSuperClusterTrackAtVtx;deltaEtaSuperClusterTrackAtVtx"),
            binsX = cms.untracked.vdouble(50, 0, 0.01),
            inputVariables = cms.vstring("abs(candele.deltaEtaSuperClusterTrackAtVtx)"),
        ),
        cms.PSet (
            name = cms.string("electrondeltaPhiSuperClusterTrackAtVtx"),
            title = cms.string("Electron deltaPhiSuperClusterTrackAtVtx;deltaPhiSuperClusterTrackAtVtx"),
            binsX = cms.untracked.vdouble(50, 0, 0.1),
            inputVariables = cms.vstring("abs(candele.deltaPhiSuperClusterTrackAtVtx)"),
        ),
        cms.PSet (
            name = cms.string("electronfull5x5_sigmaIetaIeta"),
            title = cms.string("Electron full5x5_sigmaIetaIeta;full5x5_sigmaIetaIeta"),
            binsX = cms.untracked.vdouble(50, 0, 0.1),
            inputVariables = cms.vstring("candele.full5x5_sigmaIetaIeta"),
        ),
        cms.PSet (
            name = cms.string("electronhadronicOverEm"),
            title = cms.string("Electron hadronicOverEm;hadronicOverEm"),
            binsX = cms.untracked.vdouble(50, 0, 0.1),
            inputVariables = cms.vstring("candele.hadronicOverEm"),
        ),
        cms.PSet (
            name = cms.string("electronooEmooP"),
            title = cms.string("Electron ooEmoop;ooEmoop"),
            binsX = cms.untracked.vdouble(50, 0, 0.1),
            inputVariables = cms.vstring("abs(1/candele.ecalEnergy - candele.eSuperClusterOverP/candele.ecalEnergy)"),
        ),
        cms.PSet (
            name = cms.string("electronvtxFitConversion"),
            title = cms.string("Electron vtxFitConversion;vtxFitConversion"),
            binsX = cms.untracked.vdouble(4, -2, 2),
            inputVariables = cms.vstring("candele.vtxFitConversion"),
        ),
        cms.PSet (
            name = cms.string("electronsumChargedHadronPt"),
            title = cms.string("Electron sumChargedHadronPt;sumChargedHadronPt [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("candele.pfIso_.sumChargedHadronPt"),
        ),
        cms.PSet (
            name = cms.string("electronsumNeutralHadronEt"),
            title = cms.string("Electron sumNeutralHadronEt;sumNeutralHadronEt [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("candele.pfIso_.sumNeutralHadronEt"),
        ),
        cms.PSet (
            name = cms.string("electronsumChargedHadronPt "),
            title = cms.string("Electron sumChargedHadronPt;sumChargedHadronPt [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("candele.pfIso_.sumChargedHadronPt "),
        ),
        cms.PSet (
            name = cms.string("electronRho"),
            title = cms.string("Electron Rho;#rho"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("candele.rho"),
        ),
        cms.PSet (
            name = cms.string("electronEffectiveArea"),
            title = cms.string("Electron Effective Area;Effective Area"),
            binsX = cms.untracked.vdouble(50, 0, 0.5),
            inputVariables = cms.vstring("candele.AEff"),
        ),
        cms.PSet (
            name = cms.string("electronDxy"),
            title = cms.string("Electron IP;electron d_{xy}"),
            binsX = cms.untracked.vdouble(2000, -0.1, 0.1),
            inputVariables = cms.vstring("(-(candele.vx - beamspot.x0)*candele.py + (candele.vy - beamspot.y0)*candele.px)/candele.pt"),
        ),
        cms.PSet (
            name = cms.string("electronDz"),
            title = cms.string("Electron Dz;electron d_{z}"),
            binsX = cms.untracked.vdouble(200, -10, 10),
            inputVariables = cms.vstring("(candele.vz - beamspot.z0) - ((candele.vx - beamspot.x0)*candele.px + (candele.vy - beamspot.y0)*candele.py)/candele.pt*(candele.pz/candele.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronDbetaIsolation"),
            title = cms.string("Electron Isolation; electron d#beta Isolation"),
            binsX = cms.untracked.vdouble(15, 0, 0.15),
            inputVariables = cms.vstring("(candele.pfIso_.sumChargedHadronPt + max(0.0,candele.pfIso_.sumNeutralHadronEt + candele.pfIso_.sumPhotonEt - candele.rho*candele.AEff))/candele.pt"),
        ),
        cms.PSet (
            name = cms.string("electronDxyPhi"),
            title = cms.string("Electron IP vs Azimuthal Angle;electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(2000, -0.1, 0.1),
            inputVariables = cms.vstring("candele.phi","(-(candele.vx - beamspot.x0)*candele.py + (candele.vy - beamspot.y0)*candele.px)/candele.pt"),
        ),
  )
)

electronMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("candeles","muons","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("InvMass"),
            title = cms.string("Electron-muon Invariant Mass;M_{e-mu} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            inputVariables = cms.vstring("invMass(candele,muon)"),
        ),
        cms.PSet (
            name = cms.string("deltaR"),
            title = cms.string("Electron-muon Spacial Separation;#DeltaR_{e-mu}"),
            binsX = cms.untracked.vdouble(50, 0, 5),
            inputVariables = cms.vstring("deltaR(candele,muon)"),
        ),
        cms.PSet (
            name = cms.string("deltaPhi"),
            title = cms.string("Electron-muon #Phi Separation ;#Delta#phi_{e-mu}"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("deltaPhi(candele,muon)"),
        ),
        cms.PSet (
            name = cms.string("chargedProduct"),
            title = cms.string("Electron-muon Charged Product;q_{e}*q_{mu}"),
            binsX = cms.untracked.vdouble(4,-2,2),
            inputVariables = cms.vstring("candele.charge*muon.charge"),
        ),
        cms.PSet (
            name = cms.string("muonPtElectronPt"),
            title = cms.string("Electron Momentum vs Muon Momentum;muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(120,0,120),
            binsY = cms.untracked.vdouble(120,0,120),
            inputVariables = cms.vstring("candele.pt","muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonIpElectronIp"),
            title = cms.string("Electron abs(Ip) vs Muon abs(Ip);|d_{xy}_{mu}| [cm]"),
            binsX = cms.untracked.vdouble(1000,0,0.1),
            binsY = cms.untracked.vdouble(1000,0,0.1),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)","abs((-(candele.vx - beamspot.x0)*candele.py + (candele.vy - beamspot.y0)*candele.px)/candele.pt)"),
        ),
    )
)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, cms.VPSet (muonHistograms,electronHistograms,electronMuonHistograms), collections,variableProducers, False)
#add_channels (process, eventSelections, cms.VPSet (MuonHistograms), collections, variableProducers, False)
#process.CandidateElectronProducer = cms.EDProducer("CandidateElectronProducer",
#    electronsMiniAOD = cms.InputTag("slimmedElectrons"),
#    conversions = cms.InputTag  ("reducedEgamma",    "reducedConversions",""),
#    rho = cms.InputTag  ("fixedGridRhoFastjetAll",    "",                ""),
#    beamSpot = cms.InputTag  ("offlineBeamSpot",           "",                "")
#)

# uncomment to produce a full python configuration log file
