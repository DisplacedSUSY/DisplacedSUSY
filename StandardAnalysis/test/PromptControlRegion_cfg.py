import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
from DisplacedSUSY.StandardAnalysis.PromptControlRegion import *
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
    'root://cmsxrootd.fnal.gov//store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v3/10000/009D49A5-7314-E511-84EF-0025905A605E.root',
    #'file:/home/bing/DisplacedFermion/CMSSW_7_4_5_ROOT5/src/DisplacedSUSY/CandidateElectronProducer/test/ProducerTest.root',
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
  candeles       =  cms.InputTag  ('CandidateElectronProducer',''),
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
variableProducers.append("CandidateElectronProducer")
#variableProducers.append("MyOtherVariableProducer")

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.StandardAnalysis.PromptControlRegion import *
#from DisplacedSUSY.StandardAnalysis.SkimSelections import *
#from OSUT3Analysis.ExampleAnalysis.MyProtoEventSelections import *

eventSelections = []
#eventSelections.append(eMuMinimalUserVariables)
eventSelections.append(PromptControlRegion)
#eventSelections.append(eMuMinimal)
#eventSelections.append(EMu_Skim)

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
            name = cms.string("electronDxy"),
            title = cms.string("Electron IP;electron d_{xy}"),
            binsX = cms.untracked.vdouble(200, -0.1, 0.1),
            inputVariables = cms.vstring("(-(candele.vx - beamspot.x0)*candele.py + (candele.vy - beamspot.y0)*candele.px)/candele.pt"),
        ),
        cms.PSet (
            name = cms.string("electronDbetaIsolation"),
            title = cms.string("Electron Isolation; electron d#beta Isolation"),
            binsX = cms.untracked.vdouble(15, 0, 0.15),
            inputVariables = cms.vstring("(candele.pfIso_.sumChargedHadronPt + max(0.0,candele.pfIso_.sumNeutralHadronEt + candele.pfIso_.sumPhotonEt - rho*AEff))/candele.pt"),
        ),
  )
)
################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, cms.VPSet (muonHistograms,electronHistograms), collections,variableProducers)
#add_channels (process, eventSelections, cms.VPSet (MuonHistograms), collections, variableProducers, False)
process.CandidateElectronProducer = cms.EDProducer("CandidateElectronProducer",
    electronsMiniAOD = cms.InputTag("slimmedElectrons"),
    conversions = cms.InputTag  ("reducedEgamma",    "reducedConversions",""),
    rho = cms.InputTag  ("fixedGridRhoFastjetAll",    "",                ""),
    beamSpot = cms.InputTag  ("offlineBeamSpot",           "",                "")
)
