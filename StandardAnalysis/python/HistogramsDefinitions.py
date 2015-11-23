import FWCore.ParameterSet.Config as cms
import copy
import string

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
            name = cms.string("muonPtExtended"),
            title = cms.string("Muon Transverse Momentum;muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
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
            binsX = cms.untracked.vdouble(200, -0.01, 0.01),
            inputVariables = cms.vstring("(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("absMuonDxyPrompt"),
            title = cms.string("Muon IP;|muon d_{xy}| [CM]"),
            binsX = cms.untracked.vdouble(100, 0, 0.01),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px))/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("absMuonDxyDisplaced"),
            title = cms.string("Muon IP;|muon d_{xy}| [CM]"),
            binsX = cms.untracked.vdouble(100, 0.01, 0.02),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px))/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("absMuonDxyInclusive"),
            title = cms.string("Muon IP;|muon d_{xy}| [CM]"),
            binsX = cms.untracked.vdouble(400, 0, 4),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px))/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonDz"),
            title = cms.string("Muon Dz;muon d_{z}"),
            binsX = cms.untracked.vdouble(200, -10, 10),
            inputVariables = cms.vstring("(muon.vz - beamspot.z0) - ((muon.vx - beamspot.x0)*muon.px + (muon.vy - beamspot.y0)*muon.py)/muon.pt*(muon.pz/muon.pt)"),
        ),
        cms.PSet (
            name = cms.string("muonDbetaIsolation"),
            title = cms.string("Muon Isolation; muon #Delta#beta Isolation"),
            binsX = cms.untracked.vdouble(150, 0, 1.5),
            inputVariables = cms.vstring("(muon.pfIsolationR04_.sumChargedHadronPt + max(0.0,muon.pfIsolationR04_.sumNeutralHadronEt + muon.pfIsolationR04_.sumPhotonEt - 0.5*muon.pfIsolationR04_.sumPUPt))/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonDxyPhi"),
            title = cms.string("Muon IP vs Azimuthal Angle;muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(200, -0.01, 0.01),
            inputVariables = cms.vstring("muon.phi","(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
  )
)

electronHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronPt"),
            title = cms.string("Electron Transverse Momentum;electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(120, 0, 120),
            inputVariables = cms.vstring("electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronPtExtended"),
            title = cms.string("Electron Transverse Momentum;electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            inputVariables = cms.vstring("electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronEta"),
            title = cms.string("Electron Pseudorapidity;electron #eta"),
            binsX = cms.untracked.vdouble(50, -2.5, 2.5),
            inputVariables = cms.vstring("electron.eta"),
        ),
        cms.PSet (
            name = cms.string("electronPhi"),
            title = cms.string("Electron Azimuthal Angle;electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("electron.phi"),
        ),
        cms.PSet (
            name = cms.string("electronNumberOfMissingInnerHits"),
            title = cms.string("Electron Number of Missing Inner Hits;electron #misingInnerHits"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("electron.missingInnerHits"),
        ),
        cms.PSet (
            name = cms.string("electrondeltaEtaSuperClusterTrackAtVtx"),
            title = cms.string("Electron deltaEtaSuperClusterTrackAtVtx;deltaEtaSuperClusterTrackAtVtx"),
            binsX = cms.untracked.vdouble(50, 0, 0.01),
            inputVariables = cms.vstring("abs(electron.deltaEtaSuperClusterTrackAtVtx)"),
        ),
        cms.PSet (
            name = cms.string("electrondeltaPhiSuperClusterTrackAtVtx"),
            title = cms.string("Electron deltaPhiSuperClusterTrackAtVtx;deltaPhiSuperClusterTrackAtVtx"),
            binsX = cms.untracked.vdouble(50, 0, 0.1),
            inputVariables = cms.vstring("abs(electron.deltaPhiSuperClusterTrackAtVtx)"),
        ),
        cms.PSet (
            name = cms.string("electronfull5x5_sigmaIetaIeta"),
            title = cms.string("Electron full5x5_sigmaIetaIeta;full5x5_sigmaIetaIeta"),
            binsX = cms.untracked.vdouble(50, 0, 0.1),
            inputVariables = cms.vstring("electron.full5x5_sigmaIetaIeta"),
        ),
        cms.PSet (
            name = cms.string("electronhadronicOverEm"),
            title = cms.string("Electron hadronicOverEm;hadronicOverEm"),
            binsX = cms.untracked.vdouble(50, 0, 0.1),
            inputVariables = cms.vstring("electron.hadronicOverEm"),
        ),
        cms.PSet (
            name = cms.string("electronooEmooP"),
            title = cms.string("Electron ooEmoop;ooEmoop"),
            binsX = cms.untracked.vdouble(50, 0, 0.1),
            inputVariables = cms.vstring("abs(1/electron.ecalEnergy - electron.eSuperClusterOverP/electron.ecalEnergy)"),
        ),
        cms.PSet (
            name = cms.string("electronvtxFitConversion"),
            title = cms.string("Electron vtxFitConversion;vtxFitConversion"),
            binsX = cms.untracked.vdouble(4, -2, 2),
            inputVariables = cms.vstring("electron.vtxFitConversion"),
        ),
        cms.PSet (
            name = cms.string("electronsumChargedHadronPt"),
            title = cms.string("Electron sumChargedHadronPt;sumChargedHadronPt [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("electron.pfIso_.sumChargedHadronPt"),
        ),
        cms.PSet (
            name = cms.string("electronsumNeutralHadronEt"),
            title = cms.string("Electron sumNeutralHadronEt;sumNeutralHadronEt [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("electron.pfIso_.sumNeutralHadronEt"),
        ),
        cms.PSet (
            name = cms.string("electronsumChargedHadronPt "),
            title = cms.string("Electron sumChargedHadronPt;sumChargedHadronPt [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("electron.pfIso_.sumChargedHadronPt "),
        ),
        cms.PSet (
            name = cms.string("electronRho"),
            title = cms.string("Electron Rho;#rho"),
            binsX = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("electron.rho"),
        ),
        cms.PSet (
            name = cms.string("electronEffectiveArea"),
            title = cms.string("Electron Effective Area;Effective Area"),
            binsX = cms.untracked.vdouble(50, 0, 0.5),
            inputVariables = cms.vstring("electron.AEff"),
        ),
        cms.PSet (
            name = cms.string("electronDxy"),
            title = cms.string("Electron IP;electron d_{xy}"),
            binsX = cms.untracked.vdouble(200, -0.01, 0.01),
            inputVariables = cms.vstring("(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("absElectronDxyPrompt"),
            title = cms.string("Electron IP;|electron d_{xy}| [CM]"),
            binsX = cms.untracked.vdouble(100, 0, 0.01),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px))/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("absElectronDxyDisplaced"),
            title = cms.string("Electron IP;|electron d_{xy}| [CM]"),
            binsX = cms.untracked.vdouble(100, 0.01, 0.02),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px))/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("absElectronDxyInclusive"),
            title = cms.string("Electron IP;|electron d_{xy}| [CM]"),
            binsX = cms.untracked.vdouble(400, 0, 4),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px))/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronDz"),
            title = cms.string("Electron Dz;electron d_{z}"),
            binsX = cms.untracked.vdouble(200, -10, 10),
            inputVariables = cms.vstring("(electron.vz - beamspot.z0) - ((electron.vx - beamspot.x0)*electron.px + (electron.vy - beamspot.y0)*electron.py)/electron.pt*(electron.pz/electron.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronDrhoIsolation"),
            title = cms.string("Electron Isolation; electron #Delta#rho Isolation"),
            binsX = cms.untracked.vdouble(150, 0, 1.5),
            inputVariables = cms.vstring("(electron.pfIso_.sumChargedHadronPt + max(0.0,electron.pfIso_.sumNeutralHadronEt + electron.pfIso_.sumPhotonEt - electron.rho*electron.AEff))/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronDxyPhi"),
            title = cms.string("Electron IP vs Azimuthal Angle;electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(200, -0.01, 0.01),
            inputVariables = cms.vstring("electron.phi","(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt"),
        ),
  )
)

electronMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","muons","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("InvMass"),
            title = cms.string("Electron-muon Invariant Mass;M_{e-mu} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            inputVariables = cms.vstring("invMass(electron,muon)"),
        ),
        cms.PSet (
            name = cms.string("deltaR"),
            title = cms.string("Electron-muon Spacial Separation;#DeltaR_{e-mu}"),
            binsX = cms.untracked.vdouble(50, 0, 5),
            inputVariables = cms.vstring("deltaR(electron,muon)"),
        ),
        cms.PSet (
            name = cms.string("deltaPhi"),
            title = cms.string("Electron-muon #Phi Separation ;#Delta#phi_{e-mu}"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("deltaPhi(electron,muon)"),
        ),
        cms.PSet (
            name = cms.string("deltaEta"),
            title = cms.string("Electron-muon #Eta Separation ;#Delta#eta_{e-mu}"),
            binsX = cms.untracked.vdouble(50, 0, 5),
            inputVariables = cms.vstring("abs(electron.eta - muon.eta)"),
        ),
        cms.PSet (
            name = cms.string("chargedProduct"),
            title = cms.string("Electron-muon Charged Product;q_{e}*q_{mu}"),
            binsX = cms.untracked.vdouble(4,-2,2),
            inputVariables = cms.vstring("electron.charge*muon.charge"),
        ),
        cms.PSet (
            name = cms.string("electronPtMuonPt"),
            title = cms.string("Electron Momentum vs Muon Momentum;muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(120,0,120),
            binsY = cms.untracked.vdouble(120,0,120),
            inputVariables = cms.vstring("muon.pt","electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronIpMuonIpPrompt"),
            title = cms.string("Electron abs(Ip) vs Muon abs(Ip);|d_{xy}_{mu}| [cm]"),
            binsX = cms.untracked.vdouble(100,0,0.01),
            binsY = cms.untracked.vdouble(100,0,0.01),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronIpMuonIpDisplaced"),
            title = cms.string("Electron abs(Ip) vs Muon abs(Ip);|d_{xy}_{mu}| [cm]"),
            binsX = cms.untracked.vdouble(100,0.01,0.02),
            binsY = cms.untracked.vdouble(100,0.01,0.02),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronIpMuonIpInclusive"),
            title = cms.string("Electron abs(Ip) vs Muon abs(Ip);|d_{xy}_{mu}| [cm]"),
            binsX = cms.untracked.vdouble(400,0,4),
            binsY = cms.untracked.vdouble(400,0,4),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronIsoMuonIso"),
            title = cms.string("Electron Iso vs Muon Iso;muon #Delta#beta Iso"),
            binsX = cms.untracked.vdouble(150,0,1.5),
            binsY = cms.untracked.vdouble(150,0,1.5),
            inputVariables = cms.vstring("(muon.pfIsolationR04_.sumChargedHadronPt + max(0.0,muon.pfIsolationR04_.sumNeutralHadronEt + muon.pfIsolationR04_.sumPhotonEt - 0.5*muon.pfIsolationR04_.sumPUPt))/muon.pt","(electron.pfIso_.sumChargedHadronPt + max(0.0,electron.pfIso_.sumNeutralHadronEt + electron.pfIso_.sumPhotonEt - electron.rho*electron.AEff))/electron.pt")
        ),
    )
)

eventHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("numPV"),
            title = cms.string("Number of Primary Vertex; #PV"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("numPV"),
        ),
        cms.PSet (
            name = cms.string("puScalingFactor"),
            title = cms.string("PU Scaling Factor; PU Scaling Factor"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("puScalingFactor"),
        ),
        cms.PSet (
            name = cms.string("sumJetPt"),
            title = cms.string("Sum of Jet Transverse Momentum; #Sigma p_{T}_{jet}"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            inputVariables = cms.vstring("sumJetPt"),
        ),
    )
) 

electronJetHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronJetDeltaR"),
            title = cms.string("Electron - Jet #DeltaR"),
            binsX = cms.untracked.vdouble(300, 0, 3),
            inputVariables = cms.vstring("deltaR(electron,jet)"),
        ),
    )
)

muonJetHistograms = cms.PSet(
    inputCollection = cms.vstring("muons","jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonJetDeltaR"),
            title = cms.string("Muon - Jet #DeltaR"),
            binsX = cms.untracked.vdouble(300, 0, 3),
            inputVariables = cms.vstring("deltaR(muon,jet)"),
        ),
    )
)

jetHistograms = cms.PSet(
    inputCollection = cms.vstring("jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jetPt"),
            title = cms.string("Jet Transverse Momentum;electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 300),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("jetEta"),
            title = cms.string("Jet Pseudorapidity;electron #eta"),
            binsX = cms.untracked.vdouble(50, -2.5, 2.5),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("jetPhi"),
            title = cms.string("Jet Azimuthal Angle;electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("jetCSV"),
            title = cms.string("Jet CSV;jet CSV"),
            binsX = cms.untracked.vdouble(1000, 0, 1),
            inputVariables = cms.vstring("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
        )
    )
)

metHistograms = cms.PSet(
    inputCollection = cms.vstring("mets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("metPt"),
            title = cms.string("Met Transverse Momentum;p_{T}_{jet} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("metPhi"),
            title = cms.string("Met Azumithal Angle; #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
    )
)
