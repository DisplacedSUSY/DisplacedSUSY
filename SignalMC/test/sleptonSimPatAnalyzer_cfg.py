import FWCore.ParameterSet.Config as cms

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('test')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1
#process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet (
    #input = cms.untracked.int32 (100)
    input = cms.untracked.int32 (-1)
)

process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring (
                                 'file:/uscms_data/d3/alimena/DisplacedLeptons/CMSSW_10_2_5/src/DisplacedSUSY/SignalMC/test/step4.root', #miniaod
                                 #'file:/eos/uscms/store/user/lpclonglived/DisplacedLeptons/Staus_M_500_100mm_13TeV_2018MC/MiniAod/210421_105715/0000/step4_1.root'
                             ),
                        )
process.TFileService = cms.Service ('TFileService',
                                    fileName = cms.string ("file:sleptonSimPat.root")
                                )

###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.sleptonSimPatAnalyzer = cms.EDAnalyzer ("SleptonSimPatAnalyzer",
                                                    electrons = cms.InputTag ("slimmedElectrons", ""),
                                                    muons = cms.InputTag ("slimmedMuons", ""),
                                                    beamspots = cms.InputTag ("offlineBeamSpot", ""),
                                                    genParticles = cms.InputTag ("genParticlePlusGeant", ""), #decay done in geant
                                                    #cutPythia8Flag = cms.untracked.bool (True), # genParticle.fromHardProcessBeforeFSR()
                                                )

process.myPath = cms.Path (process.sleptonSimPatAnalyzer)
