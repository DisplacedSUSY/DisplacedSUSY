import FWCore.ParameterSet.Config as cms

process = cms.Process("testParticle")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #80X single top, miniAOD
        #'/store/mc/RunIISummer16MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/04F61242-90BA-E611-B842-001E67DFF7CB.root',

        #80X single top, e-mu preselection skim
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/SingleTop_tW/Preselection/skim_0.root',

        #80X diboson, e-mu preselection skim
        'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/WG/Preselection/skim_1.root',
        )
)

process.printTree1 = cms.EDAnalyzer("ParticleListDrawer",
    #src = cms.InputTag("genParticles"), #AOD
    src = cms.InputTag("prunedGenParticles"), #MINIAOD, skim files
    maxEventsToPrint  = cms.untracked.int32(-1),
    printVertex = cms.untracked.bool(True),
)

process.printTree2 = cms.EDAnalyzer("ParticleTreeDrawer",
    #src = cms.InputTag("genParticles"), #AOD
    src = cms.InputTag("prunedGenParticles"), #MINIAOD, skim files
    printP4 = cms.untracked.bool(False),
    printPtEtaPhi = cms.untracked.bool(True),
    printVertex = cms.untracked.bool(False),
    printStatus = cms.untracked.bool(False),
    printIndex  = cms.untracked.bool(False)
)

process.printEventNumber = cms.OutputModule("AsciiOutputModule")

process.p = cms.Path(process.printTree1*process.printTree2)
#process.p = cms.Path(process.printTree1)
process.outpath = cms.EndPath(process.printEventNumber)
process.MessageLogger.destinations = cms.untracked.vstring('cout','cerr')
