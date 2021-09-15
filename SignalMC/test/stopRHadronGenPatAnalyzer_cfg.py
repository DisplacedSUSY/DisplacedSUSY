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
                                 #'file:/eos/uscms/store/user/alimena/StopToLBottom_M_1000_0p1mm_13TeV_2018MC/MiniAod/200926_081352/0000/step0_1.root',

                                 "/store/relval/CMSSW_12_1_0_pre2/RelValDisplacedSUSY_14TeV/MINIAODSIM/PU_121X_mcRun3_2021_realistic_v1_TkmkFitRecoOnly-v3/10000/ce62c7b3-dd77-4023-9631-347b8e654ec7.root"

                             ),
                        )
process.TFileService = cms.Service ('TFileService',
                                    fileName = cms.string ("file:stopRHadronGen.root")
                                )

###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.stopRHadronGenPatAnalyzer = cms.EDAnalyzer ("StopRHadronGenPatAnalyzer",
                                          electrons = cms.InputTag ("slimmedElectrons", ""),
                                          muons = cms.InputTag ("slimmedMuons", ""),
                                          beamspots = cms.InputTag ("offlineBeamSpot", ""),
                                          genParticles = cms.InputTag ("prunedGenParticles", ""), #decay done in pythia, from miniaod
                                          #cutPythia8Flag = cms.untracked.bool (True), # genParticle.fromHardProcessBeforeFSR()
                                      )

process.myPath = cms.Path (process.stopRHadronGenPatAnalyzer)
