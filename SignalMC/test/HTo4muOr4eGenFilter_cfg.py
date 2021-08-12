import FWCore.ParameterSet.Config as cms

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('test')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1
#process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (100)
    #input = cms.untracked.int32 (-1)
)

process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring (
                                 "/store/user/pablom/ggH_HToSSTo4l_MH-125_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAODext/210611_113948/0000/EXO-RunIIAutumn18MiniAOD_1.root",
                             ),
                        )

process.USER = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('myPath')
    ),
    fileName = cms.untracked.string("file:HToSSTo4muOr4e_miniAod.root")
)

###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.hTo4muOr4eGenFilter = cms.EDFilter("HTo4muOr4eGenFilter",
                                         inputTag = cms.InputTag("prunedGenParticles")
                                     )

process.myPath = cms.Path (process.hTo4muOr4eGenFilter)
process.outpath = cms.EndPath(process.USER)
