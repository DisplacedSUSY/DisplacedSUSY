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
                                 'file:/eos/uscms/store/user/alimena/StopToLB_M_1000_0p1mm_13TeV_2018MC_withCloudModel/MiniAod/210404_082325/0000/step4_1.root',
                             ),
                        )
process.TFileService = cms.Service ('TFileService',
                                    fileName = cms.string ("file:stopRHadronSimPat.root")
                                )

###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.stopRHadronSimPatAnalyzer = cms.EDAnalyzer ("StopRHadronSimPatAnalyzer",
                                                    electrons = cms.InputTag ("slimmedElectrons", ""),
                                                    muons = cms.InputTag ("slimmedMuons", ""),
                                                    beamspots = cms.InputTag ("offlineBeamSpot", ""),
                                                    genParticles = cms.InputTag ("genParticlePlusGeant", ""), #decay done in geant
                                                    #cutPythia8Flag = cms.untracked.bool (True), # genParticle.fromHardProcessBeforeFSR()
                                                )

process.myPath = cms.Path (process.stopRHadronSimPatAnalyzer)
