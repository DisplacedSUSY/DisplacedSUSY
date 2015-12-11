import FWCore.ParameterSet.Config as cms
import copy
import string

cosmicMuonHistograms = cms.PSet(
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
            name = cms.string("muonDxyBS"),
            title = cms.string("Muon IP wrt BS;muon d_{xy}"),
            binsX = cms.untracked.vdouble(2000, -100, 100),
            inputVariables = cms.vstring("(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("absMuonDxyBSInclusive"),
            title = cms.string("Muon IP wrt BS;|muon d_{xy}| [CM]"),
            binsX = cms.untracked.vdouble(1000, 0, 100),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px))/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonDzBS"),
            title = cms.string("Muon Dz wrt BS;muon d_{z}"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("(muon.vz - beamspot.z0) - ((muon.vx - beamspot.x0)*muon.px + (muon.vy - beamspot.y0)*muon.py)/muon.pt*(muon.pz/muon.pt)"),
        ),
        cms.PSet (
            name = cms.string("muonDxy"),
            title = cms.string("Muon IP;muon d_{xy}"),
            binsX = cms.untracked.vdouble(2000, -100, 100),
            inputVariables = cms.vstring("(-muon.vx*muon.py + muon.vy*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("absMuonDxyInclusive"),
            title = cms.string("Muon IP;|muon d_{xy}| [CM]"),
            binsX = cms.untracked.vdouble(1000, 0, 100),
            inputVariables = cms.vstring("abs(-muon.vx*muon.py + muon.vy*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonDz"),
            title = cms.string("Muon Dz;muon d_{z}"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("muon.vz - (muon.vx*muon.px + muon.vy*muon.py)/muon.pt*(muon.pz/muon.pt)"),
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
            binsY = cms.untracked.vdouble(2000, -100, 100),
            inputVariables = cms.vstring("muon.phi","(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonDxyDz"),
            title = cms.string("Muon IP vs d_{Z};muon d_{Z} [cm]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            binsY = cms.untracked.vdouble(2000, -100, 100),
            inputVariables = cms.vstring("(muon.vz - beamspot.z0) - ((muon.vx - beamspot.x0)*muon.px + (muon.vy - beamspot.y0)*muon.py)/muon.pt*(muon.pz/muon.pt)","(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonEtaPt"),
            title = cms.string("Muon Pseudorapidity vs Transverse Momentum;muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(5, -2.5, 2.5),
            inputVariables = cms.vstring("muon.pt","muon.eta"),
        ),
  )
)

