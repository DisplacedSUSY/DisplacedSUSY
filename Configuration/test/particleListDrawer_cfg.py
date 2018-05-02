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
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/WG/Preselection/skim_1.root',

        #80X ttbar, e-mu preselection skim
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/TTJets_DiLept/Preselection/skim_0.root',

        #80X drell-yan, e-mu preselection skim
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/DYJetsToLL_50/Preselection/skim_0.root',

        #80X qcd 170to300, e-mu preselection skim
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_104.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_105.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_107.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_12.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_122.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_14.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_147.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_39.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_46.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_49.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_52.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_83.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_84.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_88.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_170to300/Preselection/skim_9.root',

        #80X qcd 800to1000, e-mu preselection skim
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_101.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_117.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_12.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_123.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_124.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_127.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_129.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_142.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_167.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_178.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_180.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_183.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_19.root',
        #'file:/data/users/jalimena/condor/DisplacedLeptons2016/EMuSkim_Preselection/QCD_MuEnriched_800to1000/Preselection/skim_28.root',
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
