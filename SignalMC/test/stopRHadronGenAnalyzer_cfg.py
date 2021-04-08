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
                                 'file:/eos/uscms/store/user/alimena/StopToLBottom_M_1000_0p1mm_13TeV_2018MC/MiniAod/200926_081352/0000/step0_1.root',
                             ),
                        )
process.TFileService = cms.Service ('TFileService',
                                    fileName = cms.string ("file:stopRHadronGen.root")
                                )

###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.stopRHadronGenAnalyzer = cms.EDAnalyzer ("StopRHadronGenAnalyzer",
                                          #tracks = cms.InputTag ("generalTracks", ""),
                                          genParticles = cms.InputTag ("prunedGenParticles", ""), #decay done in pythia, from miniaod
                                          #cutPythia8Flag = cms.untracked.bool (True), # genParticle.fromHardProcessBeforeFSR()
                                      )

process.myPath = cms.Path (process.stopRHadronGenAnalyzer)
