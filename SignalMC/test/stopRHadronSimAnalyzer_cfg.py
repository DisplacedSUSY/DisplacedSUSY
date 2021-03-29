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
                                 'file:/uscms_data/d3/alimena/DisplacedLeptons/CMSSW_10_2_0/src/DisplacedSUSY/SignalMC/test/stopToLB1800_1000mm_withCloudModel.root',
                             ),
                        )
process.TFileService = cms.Service ('TFileService',
                                    fileName = cms.string ("file:stopRHadronSim.root")
                                )

###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.stopRHadronSimAnalyzer = cms.EDAnalyzer ("StopRHadronSimAnalyzer",
                                          #tracks = cms.InputTag ("generalTracks", ""),
                                          #genParticles = cms.InputTag ("genParticles", ""), #decay done in pythia
                                          genParticles = cms.InputTag ("genParticlePlusGeant", ""), #decay done in geant
                                          simTracks = cms.InputTag ("g4SimHits", "", "SIM"),
                                          simVertexs = cms.InputTag ("g4SimHits", "", "SIM"),
                                          hepMC = cms.InputTag ("generatorSmeared", "", "SIM"),
                                          PixelBarrelHighTofSimHits = cms.InputTag("g4SimHits", "TrackerHitsPixelBarrelHighTof" ,"SIM"),
                                          PixelBarrelLowTofSimHits = cms.InputTag("g4SimHits", "TrackerHitsPixelBarrelLowTof" ,"SIM"),
                                          PixelEndcapHighTofSimHits = cms.InputTag("g4SimHits", "TrackerHitsPixelEndcapHighTof" ,"SIM"),
                                          PixelEndcapLowTofSimHits = cms.InputTag("g4SimHits", "TrackerHitsPixelEndcapLowTof" ,"SIM"),
                                          TECHighTofSimHits = cms.InputTag("g4SimHits", "TrackerHitsTECHighTof" ,"SIM"),
                                          TECLowTofSimHits = cms.InputTag("g4SimHits", "TrackerHitsTECLowTof" ,"SIM"),
                                          TIBHighTofSimHits = cms.InputTag("g4SimHits", "TrackerHitsTIBHighTof" ,"SIM"),
                                          TIBLowTofSimHits = cms.InputTag("g4SimHits", "TrackerHitsTIBLowTof" ,"SIM"),
                                          TIDHighTofSimHits = cms.InputTag("g4SimHits", "TrackerHitsTIDHighTof" ,"SIM"),
                                          TIDLowTofSimHits = cms.InputTag("g4SimHits", "TrackerHitsTIDLowTof" ,"SIM"),
                                          TOBHighTofSimHits = cms.InputTag("g4SimHits", "TrackerHitsTOBHighTof" ,"SIM"),
                                          TOBLowTofSimHits = cms.InputTag("g4SimHits", "TrackerHitsTOBLowTof" ,"SIM"),
                                          CSCSimHits = cms.InputTag("g4SimHits", "MuonCSCHits"   ,"SIM"),
                                          DTSimHits = cms.InputTag("g4SimHits", "MuonDTHits"    ,"SIM"),
                                          RPCSimHits = cms.InputTag("g4SimHits", "MuonRPCHits"   ,"SIM"),
                                          #cutPythia8Flag = cms.untracked.bool (True), # genParticle.fromHardProcessBeforeFSR()
                                      )

process.myPath = cms.Path (process.stopRHadronSimAnalyzer)
