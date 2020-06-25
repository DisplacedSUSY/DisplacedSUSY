import FWCore.ParameterSet.Config as cms
import os
from OSUT3Analysis.Configuration.cutUtilities import *
from OSUT3Analysis.Configuration.pdgIdBins import *
import DisplacedSUSY.StandardAnalysis.objectDefinitions as objectDefs


###############################################
##### Set up the histograms to be plotted #####
###############################################

muonGenVertexIsOriginD0WRTBeamspot = "((muon.genMatchedParticleOfSameType.noFlags.vx - beamspot.x0) * muon.genMatchedParticleOfSameType.noFlags.py - (muon.genMatchedParticleOfSameType.noFlags.vy - beamspot.y0) * muon.genMatchedParticleOfSameType.noFlags.px) / muon.genMatchedParticleOfSameType.noFlags.pt"

electronGenVertexIsOriginD0WRTBeamspot = "((electron.genMatchedParticleOfSameType.noFlags.vx - beamspot.x0) * electron.genMatchedParticleOfSameType.noFlags.py - (electron.genMatchedParticleOfSameType.noFlags.vy - beamspot.y0) * electron.genMatchedParticleOfSameType.noFlags.px) / electron.genMatchedParticleOfSameType.noFlags.pt"


##############################################################################################

MuonHistograms = cms.PSet(
    inputCollection = cms.vstring("muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("numMuons"),
            title = cms.string("Number of Selected Muons;# muons"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("number(muon)"),
        ),
        cms.PSet (
            name = cms.string("muonPt"),
            title = cms.string("Muon Transverse Momentum;Muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("muonLeadingPt"),
            title = cms.string("Muon Transverse Momentum;Muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("muonSubleadingPt"),
            title = cms.string("Muon Transverse Momentum;Muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            indexX = cms.untracked.int32(1),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("muonPt[0]_vs_muonPt[1]"),
            title = cms.string("Leading Transverse Momentum vs Subleading Transverse Momentum; Subleading Muon p_{T} [GeV]; Leading Muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            binsY = cms.untracked.vdouble(500, 0, 500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("pt", "pt"),
        ),
        cms.PSet (
            name = cms.string("muonPt_ext"),
            title = cms.string("Muon Transverse Momentum;Muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 3000),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("muonEta"),
            title = cms.string("Muon Eta;Muon #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("muonEtaPt"),
            title = cms.string("Muon Eta vs. Muon p_{T};Muon p_{T} [GeV];Muon #eta"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(25, 0, 2.5),
            inputVariables = cms.vstring("pt","eta"),
        ),
        cms.PSet (
            name = cms.string("muonPhi"),
            title = cms.string("Muon Phi;Muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("muonPVIndex"),
            title = cms.string("Muon PV Index;Muon PV Index"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("muonPVIndex"),
        ),
        cms.PSet (
            name = cms.string("muonCharge"),
            title = cms.string("Muon Charge;Muon charge"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("charge"),
        ),
        cms.PSet (
            name = cms.string("muonEtaPhi"),
            title = cms.string("Muon Eta vs. Muon Phi;Muon #phi;Muon #eta"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("phi","eta"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfMissingInnerHits"),
            title = cms.string("Muon Number of Missing Inner Hits;Muon number of missing inner silicon hits"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingInnerHits"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfMissingMiddleHits"),
            title = cms.string("Muon Number of Missing Middle Hits;Muon number of missing middle silicon hits"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingMiddleHits"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfMissingOuterHits"),
            title = cms.string("Muon Number of Missing Outer Hits;Muon number of missing outer silicon hits"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("missingOuterHits"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfValidHits"),
            title = cms.string("Muon Number of Valid Hits;Muon number of valid hits"),
            binsX = cms.untracked.vdouble(40, 0, 40),
            inputVariables = cms.vstring("numberOfValidHits"),
        ),
        cms.PSet (
            name = cms.string("muonNormalizedChi2"),
            title = cms.string("Muon Chi Squared;Muon #chi^{2}/ndf"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("globalTrack.normalizedChi2"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfMatchedStations"),
            title = cms.string("Muon Track Number of Matched Stations;Muon number of matched stations"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("numberOfMatchedStations"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfValidPixelHits"),
            title = cms.string("Muon Number of Valid Pixel Hits;Muon number of valid pixel hits"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("innerTrack.hitPattern_.numberOfValidPixelHits"),
        ),
        cms.PSet (
            name = cms.string("muonTrackerLayersWithMeasurement"),
            title = cms.string("Muon Number of Tracker Layer with Measurement;Muon tracker layers with measurement"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("innerTrack.hitPattern_.trackerLayersWithMeasurement"),
            ),
        cms.PSet (
            name = cms.string("muonIsGlobalMuon"),
            title = cms.string("Muon isGlobalMuon;Muon is global"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("isGlobalMuon"),
        ),
        cms.PSet (
            name = cms.string("muonIsPFMuon"),
            title = cms.string("Muon isPFMuon;Muon is PF"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("isPFMuon"),
        ),
        cms.PSet (
            name = cms.string("muonIsTightMuonWRTVtx"),
            title = cms.string("Muon isTightMuon;Muon passes tight ID"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("isTightMuonWRTVtx"),
        ),
        cms.PSet (
            name = cms.string("muonIsSoftMuonWRTVtx"),
            title = cms.string("Muon isSoftMuon;Muon passes soft ID"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("isSoftMuonWRTVtx"),
        ),
        cms.PSet (
            name = cms.string("muonRhoBasedIsolation"),
            title = cms.string("Muon rho-based Isolation;Muon rho-based isolation"),
            binsX = cms.untracked.vdouble(100, 0, 1.0),
            inputVariables = cms.vstring(objectDefs.muon_iso_string),
        ),
        cms.PSet (
            name = cms.string("muonPFdBetaIsolation"),
            title = cms.string("Muon PF-based #Delta#beta Isolation;Muon PF-based #Delta#beta isolation"),
            binsX = cms.untracked.vdouble(100, 0, 5.0),
            inputVariables = cms.vstring("(pfIsolationR04_.sumChargedHadronPt + max(0.0,pfIsolationR04_.sumNeutralHadronEt + pfIsolationR04_.sumPhotonEt - 0.5*pfIsolationR04_.sumPUPt))/pt"),
        ),
        cms.PSet (
            name = cms.string("muonPFdBetaIsolationCorr"),
            title = cms.string("Muon PF-based #Delta#beta Isolation Corrected;Muon PF-based #Delta#beta Isolation Corrected"),
            binsX = cms.untracked.vdouble(100, 0, 5.0),
            inputVariables = cms.vstring("pfdBetaIsoCorr"),
        ),
        cms.PSet (
            name = cms.string("muonPFdBetaIsolationDiff"),
            title = cms.string("Muon PF-based #Delta#beta Isolation Discrepancy;Muon PF-based Iso_{default} - Iso_{customized}"),
            binsX = cms.untracked.vdouble(100, -1, 1),
            inputVariables = cms.vstring("(pfIsolationR04_.sumChargedHadronPt + max(0.0,pfIsolationR04_.sumNeutralHadronEt + pfIsolationR04_.sumPhotonEt - 0.5*pfIsolationR04_.sumPUPt))/pt - pfdBetaIsoCorr"),
        ),
        cms.PSet (
            name = cms.string("muonVx"),
            title = cms.string("Muon track reference point x value;Muon track reference point x value [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*vx"),
        ),
        cms.PSet (
            name = cms.string("muonVy"),
            title = cms.string("Muon track reference point y value;Muon track reference point y value [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*vy"),
        ),
        cms.PSet (
            name = cms.string("muonVy_vs_muonVx"),
            title = cms.string("Muon track reference point y value vs. muon track reference point x value;Muon track reference point x value [#mum];Muon track reference point y value [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            binsY = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*vx","10000*vy"),
        ),
        cms.PSet (
            name = cms.string("muonV0"),
            title = cms.string("Muon track reference point transverse distance from CMS center;Muon track reference point transverse distance from CMS center [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*hypot(vx,vy)"),
        ),
        cms.PSet (
            name = cms.string("muonPx"),
            title = cms.string("Muon track reference point x momentum;Muon track reference point x momentum [GeV]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("px"),
        ),
        cms.PSet (
            name = cms.string("muonPy"),
            title = cms.string("Muon track reference point y momentum;Muon track reference point y momentum [GeV]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("py"),
        ),
        cms.PSet (
            name = cms.string("muonPy_vs_muonPx"),
            title = cms.string("Muon track reference point y momentum vs. muon track reference point x momentum;Muon track reference point x momentum [GeV];Muon track reference point y momentum [GeV]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("px","py"),
        ),

        #gen
        cms.PSet (
            name = cms.string("muonGenVx"),
            title = cms.string("Gen muon track reference point x value;Gen muon track reference point x value [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*genVx"),
        ),
        cms.PSet (
            name = cms.string("muonGenVy"),
            title = cms.string("Gen muon track reference point y value;Gen muon track reference point y value [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*genVy"),
        ),
        cms.PSet (
            name = cms.string("muonGenVy_vs_muonGenVx"),
            title = cms.string("Gen muon track reference point y value vs. gen muon track reference point x value;Gen muon track reference point x value [#mum];Gen muon track reference point y value [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            binsY = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*genVx","10000*genVy"),
        ),
        cms.PSet (
            name = cms.string("muonGenV0"),
            title = cms.string("Gen muon track reference point transverse distance from CMS center;Gen muon track reference point transverse distance from CMS center [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*hypot(genVx,genVy)"),
        ),
        cms.PSet (
            name = cms.string("muonGenPx"),
            title = cms.string("Gen muon track reference point x momentum;Gen muon track reference point x momentum [GeV]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("genPx"),
        ),
        cms.PSet (
            name = cms.string("muonGenPy"),
            title = cms.string("Gen muon track reference point y momentum;Gen muon track reference point y momentum [GeV]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("genPy"),
        ),
        cms.PSet (
            name = cms.string("muonGenPy_vs_muonGenPx"),
            title = cms.string("Gen muon track reference point y momentum vs. gen muon track reference point x momentum;Gen muon track reference point x momentum [GeV];Gen muon track reference point y momentum [GeV]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("genPx","genPy"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchPdgId"),
            title = cms.string(";|PDG ID| of generator particle matched to muon"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.noFlagsPdgId)"),
            ),
        cms.PSet (
            name = cms.string("muonGenMatchDeltaR"),
            title = cms.string(";#DeltaR between muon and generator particle matched to muon"),
            binsX = cms.untracked.vdouble(300,0,6),
            inputVariables = cms.vstring("genMatchedParticle.noFlagsDR"),
            ),
        cms.PSet (
            name = cms.string("muonGenMatchPt"),
            title = cms.string("Gen Muon Transverse Momentum;Gen muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchPt_ext"),
            title = cms.string("Gen Muon Transverse Momentum;Gen muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 3000),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchEta"),
            title = cms.string("Gen Muon Eta;Gen muon #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.eta"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchPhi"),
            title = cms.string("Gen Muon Phi;Gen muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.phi"),
        ),

        cms.PSet (
            name = cms.string("muonGenMatchOfSameTypePdgId"),
            title = cms.string(";|PDG ID| of generator particle matched to muon"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticleOfSameType.noFlagsPdgId)"),
            ),
        cms.PSet (
            name = cms.string("muonGenMatchOfSameTypeDeltaR"),
            title = cms.string(";#DeltaR between muon and generator particle matched to muon"),
            binsX = cms.untracked.vdouble(300,0,6),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlagsDR"),
            ),
        cms.PSet (
            name = cms.string("muonGenMatchOfSameTypePt"),
            title = cms.string("Gen Muon Transverse Momentum;Gen muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchOfSameTypePt_ext"),
            title = cms.string("Gen Muon Transverse Momentum;Gen muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 3000),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchOfSameTypeEta"),
            title = cms.string("Gen Muon Eta;Gen muon #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.eta"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchOfSameTypePhi"),
            title = cms.string("Gen Muon Phi;Gen muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.phi"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchMotherPdgId"),
            title = cms.string(";|PDG ID| of mother of gen muon"),
            binsX = cms.untracked.vdouble(600, 0, 600),
            inputVariables = cms.vstring("abs(genMatchedParticle.noFlags.uniqueMotherPdgId)"),
        ),
    )
)


##############################################################################################

MuonIPHistograms = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonD0Beamspot"),
            title = cms.string("Muon d_{0} wrt Beamspot;Muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.02, 0.02),
            inputVariables = cms.vstring("(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Beamspot"),
            title = cms.string("Muon |d_{0}| wrt Beamspot;Muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.02),
            inputVariables = cms.vstring("abs(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonD0SigBeamspot"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) wrt Beamspot;d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)/hypot(muon.innerTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error))"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0SigBeamspot"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})| wrt Beamspot;|d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0.0, 20),
            inputVariables = cms.vstring("abs(((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)/hypot(muon.innerTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))"),
        ),
        cms.PSet (
            name = cms.string("muonDz"),
            title = cms.string("Muon d_{z} wrt Beamspot;Muon d_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -20, 20),
            inputVariables = cms.vstring("(muon.vz - beamspot.z0) - ((muon.vx - beamspot.x0)*muon.px + (muon.vy - beamspot.y0)*muon.py)/muon.pt*(muon.pz/muon.pt)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsDz"),
            title = cms.string("Muon |d_{z}| wrt Beamspot;Muon |d_{z}| [cm]"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            inputVariables = cms.vstring("abs((muon.vz - beamspot.z0) - ((muon.vx - beamspot.x0)*muon.px + (muon.vy - beamspot.y0)*muon.py)/muon.pt*(muon.pz/muon.pt))"),
        ),
        cms.PSet (
            name = cms.string("muonDbetaIsolationVsMuonIp"),
            title = cms.string("Muon Isolation vs Ip;Muon Ip d_{xy} [cm];Muon #Delta#beta Isolation"),
            binsX = cms.untracked.vdouble(500, 0, 0.5),
            binsY = cms.untracked.vdouble(600, 0, 6.0),
            inputVariables = cms.vstring("abs(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt","(muon.pfIsolationR04_.sumChargedHadronPt + max(0.0,muon.pfIsolationR04_.sumNeutralHadronEt + muon.pfIsolationR04_.sumPhotonEt - 0.5*muon.pfIsolationR04_.sumPUPt))/muon.pt"),
        ),
    )
)

##############################################################################################

DiMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diMuonPt"),
            title = cms.string("Di-muon Tranverse Momentum;p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pT (muon, muon)"),
        ),
        cms.PSet (
            name = cms.string("diMuonInvMass"),
            title = cms.string("Di-muon Invariant Mass;M_{#mu#mu} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass (muon, muon)"),
        ),
        cms.PSet (
            name = cms.string("diMuonInvMassZmassWindow"),
            title = cms.string("Di-muon Invariant Mass;M_{#mu#mu} [GeV]"),
            binsX = cms.untracked.vdouble(100, 50, 150),
            inputVariables = cms.vstring("invMass (muon, muon)"),
        ),
        cms.PSet (
            name = cms.string("diMuonChargeProduct"),
            title = cms.string("Di-muon Charge Product;charge_{#mu}_{1}*charge_{#mu}_{2}"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("muon.charge * muon.charge"),
        ),
        cms.PSet (
            name = cms.string("diMuonDeltaPhi"),
            title = cms.string("Di-muon Phi Difference;|#Delta(#phi)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs ( deltaPhi (muon, muon) )"),
        ),
        cms.PSet (
            name = cms.string("diMuonDeltaEta"),
            title = cms.string("Di-muon Eta Difference;|#Delta(#eta)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs (muon.eta - muon.eta)"),
        ),
        cms.PSet (
            name = cms.string("diMuonDeltaR"),
            title = cms.string("Di-muon #DeltaR;#DeltaR"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR (muon, muon)"),
        ),
        cms.PSet (
            name = cms.string("diMuonCosAlpha"),
            title = cms.string("Di-muon cos(#alpha);cos(#alpha)"),
            binsX = cms.untracked.vdouble(100, -1, 1),
            inputVariables = cms.vstring("cosAlpha (muon, muon)"),
        ),
    )
)

##############################################################################################

ElectronHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("numElectrons"),
            title = cms.string("Number of Selected Electrons;# electrons"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("number(electron)"),
        ),
        cms.PSet (
            name = cms.string("electronPt"),
            title = cms.string("Electron Transverse Momentum;Electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingPt"),
            title = cms.string("Electron Transverse Momentum;Electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("electronSubleadingPt"),
            title = cms.string("Electron Transverse Momentum;Electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            indexX = cms.untracked.int32(1),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("electronPt_ext"),
            title = cms.string("Electron Transverse Momentum;Electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 3000),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("electronEta"),
            title = cms.string("Electron Eta;Electron #eta"),
            binsX = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("electronEtaPt"),
            title = cms.string("Electron Eta vs. Electron p_{T};Electron p_{T} [GeV];Electron #eta"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(25, 0, 2.5),
            inputVariables = cms.vstring("pt","eta"),
        ),
        cms.PSet (
            name = cms.string("electronPhi"),
            title = cms.string("Electron Phi;Electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("electronPVIndex"),
            title = cms.string("Electron PV Index;Electron PV Index"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("electronPVIndex"),
        ),
        cms.PSet (
            name = cms.string("electronCharge"),
            title = cms.string("Electron Charge;Electron charge"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("charge"),
        ),
        cms.PSet (
            name = cms.string("electronEtaPhi"),
            title = cms.string("Electron Eta vs. Electron Phi;Electron #phi;Electron #eta"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("phi","eta"),
        ),
        cms.PSet (
            name = cms.string("electronNumberOfMissingInnerHits"),
            title = cms.string("Electron Number of Missing Inner Hits;Electron number of missing inner hits"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingInnerHits"),
        ),
        cms.PSet (
            name = cms.string("electronNumberOfMissingMiddleHits"),
            title = cms.string("Electron Number of Missing Middle Hits;Electron number of missing middle silicon hits"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingMiddleHits"),
        ),
        cms.PSet (
            name = cms.string("electronNumberOfMissingOuterHits"),
            title = cms.string("Electron Number of Missing Outer Hits;Electron number of missing outer hits"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("missingOuterHits"),
        ),
        cms.PSet (
            name = cms.string("electronDeltaEtaSuperClusterTrackAtVtx"),
            title = cms.string("Electron deltaEtaSuperClusterTrackAtVtx;#Delta#eta(SC, track) at vertex"),
            binsX = cms.untracked.vdouble(100, 0, 0.01),
            inputVariables = cms.vstring("abs(deltaEtaSuperClusterTrackAtVtx)"),
        ),
        # N.B.: below causes a ProductNotFound of 'reco::CaloCluster' when run over skims (ahart + bfrancis)
        #cms.PSet (
        #    name = cms.string("electronDeltaEtaSeedClusterTrackAtVtx"),
        #    title = cms.string("Electron deltaEtaSeedClusterTrackAtVtx;#Delta#eta(seed, track) at vertex"),
        #    binsX = cms.untracked.vdouble(100, 0, 0.01),
        #    inputVariables = cms.vstring("abs(deltaEtaSuperClusterTrackAtVtx - superCluster.eta + superCluster.seed_.eta)"),
        #),
        cms.PSet (
            name = cms.string("electronDeltaPhiSuperClusterTrackAtVtx"),
            title = cms.string("Electron deltaPhiSuperClusterTrackAtVtx;#Delta#phi(SC, track) at vertex"),
            binsX = cms.untracked.vdouble(100, 0, 0.1),
            inputVariables = cms.vstring("abs(deltaPhiSuperClusterTrackAtVtx)"),
        ),
        cms.PSet (
            name = cms.string("electronFull5x5_sigmaIetaIeta"),
            title = cms.string("Electron full5x5_sigmaIetaIeta;#sigmai#etai#eta"),
            binsX = cms.untracked.vdouble(100, 0, 0.1),
            inputVariables = cms.vstring("full5x5_sigmaIetaIeta"),
        ),
        cms.PSet (
            name = cms.string("electronHadronicOverEm"),
            title = cms.string("Electron H/E;H/E"),
            binsX = cms.untracked.vdouble(100, 0, 0.5),
            inputVariables = cms.vstring("hadronicOverEm"),
        ),
        cms.PSet (
            name = cms.string("electronOoEmooP"),
            title = cms.string("Electron 1/E - 1/p;1/E - 1/p [GeV^{-1}]"),
            binsX = cms.untracked.vdouble(100, 0, 0.5),
            inputVariables = cms.vstring("abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy)"),
        ),
        cms.PSet (
            name = cms.string("electronVtxFitConversion"),
            title = cms.string("Electron Pass Conversion Veto;Pass Conversion Veto"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("passConversionVeto"),
        ),

#        cms.PSet (
#            name = cms.string("electronTkNormChi2"),
#            title = cms.string("Electron Track NormChi2;#chi^{2}"),
#            binsX = cms.untracked.vdouble(50, 0, 50),
#            inputVariables = cms.vstring("gsfTrack.normalizedChi2"),
#        ),
#        cms.PSet (
#            name = cms.string("electronTkValidHits"),
#            title = cms.string("Electron Track Number of Valid Hits;# Hits"),
#            binsX = cms.untracked.vdouble(20, 0, 20),
#            inputVariables = cms.vstring("gsfTrack.numberOfValidHits"),
#        ),
        cms.PSet (
            name = cms.string("ElectronNewRhoBasedIsolation"),
            title = cms.string("Electron new rho-based Isolation;Electron new rho-based isolation"),
            binsX = cms.untracked.vdouble(100, 0, 1.0),
            inputVariables = cms.vstring(objectDefs.electron_newIso_string),
        ),
        cms.PSet (
            name = cms.string("ElectronNewRhoBasedIsolation_vs_electronPt"),
            title = cms.string("Electron new rho-based Isolation vs. Electron p_{T};Electron p_{T} [GeV];Electron new rho-based isolation"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 1.0),
            inputVariables = cms.vstring("pt",objectDefs.electron_newIso_string),
        ),
        cms.PSet (
            name = cms.string("electronPFrhoIsolation"),
            title = cms.string("Electron PF-based #rho-corrected Isolation;Electron rel. iso."),
            binsX = cms.untracked.vdouble(100, 0, 1.0),
            inputVariables = cms.vstring("(pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho*AEff))/pt"),
        ),
        cms.PSet (
            name = cms.string("electronPFrhoIsolationCorr"),
            title = cms.string("Electron PF-based #rho-corrected Isolation Corrected;Electron #rho-corrected Isolation Corrected"),
            binsX = cms.untracked.vdouble(100, 0, 1.0),
            inputVariables = cms.vstring("pfdRhoIsoCorr"),
        ),
        cms.PSet (
            name = cms.string("electronPFrhoIsolationDiff"),
            title = cms.string("Electron PF-based #rho-corrected Isolation Discrepancy;Electron PF-based Iso_{default} - Iso_{customized}"),
            binsX = cms.untracked.vdouble(100, -1, 1),
            inputVariables = cms.vstring("(pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho*AEff))/pt - pfdRhoIsoCorr"),
        ),
        cms.PSet (
            name = cms.string("electronSumChargedHadronPt"),
            title = cms.string("Electron sum charged hadron transverse momentum from PV[0];Electron sum charged hadron transverse momentum from PV[0] [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 100),
            inputVariables = cms.vstring("pfIso_.sumChargedHadronPt"),
        ),
        cms.PSet (
            name = cms.string("electronSumPuPt"),
            title = cms.string("Electron sum charged hadron transverse momentum from PV[n>0];Electron sum charged hadron transverse momentum from PV[n>0] [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 100),
            inputVariables = cms.vstring("pfIso_.sumPUPt"),
        ),
        cms.PSet (
            name = cms.string("electronSumNeutralHadronEt"),
            title = cms.string("Electron sum neutral hadron transverse energy;Electron sum neutral hadron transverse energy [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 100),
            inputVariables = cms.vstring("pfIso_.sumNeutralHadronEt"),
        ),
        cms.PSet (
            name = cms.string("electronSumPhotonEt"),
            title = cms.string("Electron sum photon transverse energy;Electron sum photon transverse energy [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 100),
            inputVariables = cms.vstring("pfIso_.sumPhotonEt"),
        ),
        cms.PSet (
            name = cms.string("electonPfRhoIsoRhoTimesAEff"),
            title = cms.string("Electron PfRhoIso Rho * AEff;Electron PfRhoIso Rho * AEff [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 100),
            inputVariables = cms.vstring("rho*AEff"),
        ),
        cms.PSet (
            name = cms.string("electonSimpleRhoBasedPuCorrection"),
            title = cms.string("Electron simple rho-based PU correction;Electron simple rho-based PU correction [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 100),
            inputVariables = cms.vstring("rho*0.283"),
        ),
        cms.PSet (
            name = cms.string("electonPfRhoIsoPuCorrection"),
            title = cms.string("Electron PfRhoIso PU correction;Electron PfRhoIso PU correction [GeV]"),
            binsX = cms.untracked.vdouble(50, 0, 100),
            inputVariables = cms.vstring("rho*AEff + pfIso_.sumPUPt"),
        ),
#        cms.PSet (
#            name = cms.string("electronFbrem"),
#            title = cms.string("Electron Brem. Energy Fraction;electron fbrem"),
#            binsX = cms.untracked.vdouble(100, 0, 2),
#            inputVariables = cms.vstring("fbrem"),
#        ),
#        cms.PSet (
#            name = cms.string("electronNumberOfLostHits"),
#            title = cms.string("Electon Number of Lost Hits;# lost hits"),
#            binsX = cms.untracked.vdouble(10, 0, 10),
#            inputVariables = cms.vstring("gsfTrack.numberOfLostHits"),
#        ),
        cms.PSet (
            name = cms.string("electronVx"),
            title = cms.string("Electron track reference point x value;Electron track reference point x value [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*vx"),
        ),
        cms.PSet (
            name = cms.string("electronVy"),
            title = cms.string("Electron track reference point y value;Electron track reference point y value [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*vy"),
        ),
        cms.PSet (
            name = cms.string("electronVy_vs_electronVx"),
            title = cms.string("Electron track reference point y value vs. electron track reference point x value;Electron track reference point x value [#mum];Electron track reference point y value [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            binsY = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*vx","10000*vy"),
        ),
        cms.PSet (
            name = cms.string("electronV0"),
            title = cms.string("Electron track reference point transverse distance from CMS center;Electron track reference point transverse distance from CMS center [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*hypot(vx,vy)"),
        ),
        cms.PSet (
            name = cms.string("electronPx"),
            title = cms.string("Electron track reference point x momentum;Electron track reference point x momentum [GeV]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("px"),
        ),
        cms.PSet (
            name = cms.string("electronPy"),
            title = cms.string("Electron track reference point y momentum;Electron track reference point y momentum [GeV]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("py"),
        ),
        cms.PSet (
            name = cms.string("electronPy_vs_electronPx"),
            title = cms.string("Electron track reference point y momentum vs. electron track reference point x momentum;Electron track reference point x momentum [GeV];Electron track reference point y momentum [GeV]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("px","py"),
        ),

        #gen
        cms.PSet (
            name = cms.string("electronGenVx"),
            title = cms.string("Gen electron track reference point x value;Gen electron track reference point x value [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*genVx"),
        ),
        cms.PSet (
            name = cms.string("electronGenVy"),
            title = cms.string("Gen electron track reference point y value;Gen electron track reference point y value [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*genVy"),
        ),
        cms.PSet (
            name = cms.string("electronGenVy_vs_electronGenVx"),
            title = cms.string("Gen electron track reference point y value vs. gen electron track reference point x value;Gen electron track reference point x value [#mum];Gen electron track reference point y value [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            binsY = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*genVx","10000*GenVy"),
        ),
        cms.PSet (
            name = cms.string("electronGenV0"),
            title = cms.string("Gen electron track reference point transverse distance from CMS center;Gen electron track reference point transverse distance from CMS center [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*hypot(genVx,genVy)"),
        ),
        cms.PSet (
            name = cms.string("electronGenPx"),
            title = cms.string("Gen electron track reference point x momentum;Gen electron track reference point x momentum [GeV]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("genPx"),
        ),
        cms.PSet (
            name = cms.string("electronGenPy"),
            title = cms.string("Gen electron track reference point y momentum;Gen electron track reference point y momentum [GeV]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("GenPy"),
        ),
        cms.PSet (
            name = cms.string("electronGenPy_vs_electronGenPx"),
            title = cms.string("Gen electron track reference point y momentum vs. gen electron track reference point x momentum;Gen electron track reference point x momentum [GeV];Gen electron track reference point y momentum [GeV]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("genPx","genPy"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchPdgId"),
            title = cms.string(";|PDG ID| of generator particle matched to electron"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.noFlagsPdgId)"),
            ),
        cms.PSet (
            name = cms.string("electronGenMatchDeltaR"),
            title = cms.string(";#DeltaR between electron and generator particle matched to electron"),
            binsX = cms.untracked.vdouble(300,0,6),
            inputVariables = cms.vstring("genMatchedParticle.noFlagsDR"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchPt"),
            title = cms.string("Gen Electron Transverse Momentum;Gen electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchPt_ext"),
            title = cms.string("Gen Electron Transverse Momentum;Gen electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 3000),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchEta"),
            title = cms.string("Gen Electron Eta;Gen electron #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.eta"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchPhi"),
            title = cms.string("Gen Electron Phi;Gen electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.phi"),
        ),

        cms.PSet (
            name = cms.string("electronGenMatchOfSameTypePdgId"),
            title = cms.string(";|PDG ID| of generator particle matched to electron"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticleOfSameType.noFlagsPdgId)"),
            ),
        cms.PSet (
            name = cms.string("electronGenMatchOfSameTypeDeltaR"),
            title = cms.string(";#DeltaR between electron and generator particle matched to electron"),
            binsX = cms.untracked.vdouble(300,0,6),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlagsDR"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchOfSameTypePt"),
            title = cms.string("Gen Electron Transverse Momentum;Gen electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchOfSameTypePt_ext"),
            title = cms.string("Gen Electron Transverse Momentum;Gen electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 3000),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchOfSameTypeEta"),
            title = cms.string("Gen Electron Eta;Gen electron #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.eta"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchOfSameTypePhi"),
            title = cms.string("Gen Electron Phi;Gen electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.phi"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchMotherPdgId"),
            title = cms.string(";|PDG ID| of mother of gen electron"),
            binsX = cms.untracked.vdouble(600, 0, 600),
            inputVariables = cms.vstring("abs(genMatchedParticle.noFlags.uniqueMotherPdgId)"),
        ),
    )
)


##############################################################################################

ElectronIPHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronD0Beamspot"),
            title = cms.string("Electron d_{0} wrt Beamspot;Electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.02, 0.02),
            inputVariables = cms.vstring("(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Beamspot"),
            title = cms.string("Electron |d_{0}| wrt Beamspot;Electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.02),
            inputVariables = cms.vstring("abs(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronD0SigBeamspot"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) wrt Beamspot;d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)/hypot(electron.gsfTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error))"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0SigBeamspot"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| wrt Beamspot;|d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0.0, 20),
            inputVariables = cms.vstring("abs(((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)/hypot(electron.gsfTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))"),
        ),
        cms.PSet (
            name = cms.string("electronDz"),
            title = cms.string("Electron d_{z} wrt Beamspot;Electron d_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -20, 20),
            inputVariables = cms.vstring("(electron.vz - beamspot.z0) - ((electron.vx - beamspot.x0)*electron.px + (electron.vy - beamspot.y0)*electron.py)/electron.pt*(electron.pz/electron.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsDz"),
            title = cms.string("Electron |d_{z}| wrt Beamspot;Electron |d_{z}| [cm]"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            inputVariables = cms.vstring("abs((electron.vz - beamspot.z0) - ((electron.vx - beamspot.x0)*electron.px + (electron.vy - beamspot.y0)*electron.py)/electron.pt*(electron.pz/electron.pt))"),
        ),
        cms.PSet (
            name = cms.string("electronDbetaIsolationVsElectronIp"),
            title = cms.string("Electron Isolation vs Ip;Electron Ip d_{xy} [cm];Electron #Delta#beta Isolation"),
            binsX = cms.untracked.vdouble(500, 0, 0.5),
            binsY = cms.untracked.vdouble(300, 0, 3.0),
            inputVariables = cms.vstring("abs(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt","(electron.pfIso_.sumChargedHadronPt + max(0.0,electron.pfIso_.sumNeutralHadronEt + electron.pfIso_.sumPhotonEt - electron.rho*electron.AEff))/electron.pt"),
        ),
    )
)

##############################################################################################

DiElectronHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons", "electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diElectronPt"),
            title = cms.string("Di-electron Tranverse Momentum;p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pT (electron, electron)"),
        ),
        cms.PSet (
            name = cms.string("diElectronInvMass"),
            title = cms.string("Di-electron Invariant Mass;M_{ee} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(electron, electron)"),
        ),
        cms.PSet (
            name = cms.string("diElectronChargeProduct"),
            title = cms.string("Di-electron Charge Product;charge_{e}_{1}*charge_{e}_{2}"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("electron.charge * electron.charge"),
        ),
        cms.PSet (
            name = cms.string("diElectronDeltaPhi"),
            title = cms.string("Di-electron Phi Difference;|#Delta(#phi)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(electron, electron))"),
        ),
        cms.PSet (
            name = cms.string("diElectronDeltaEta"),
            title = cms.string("Di-electron Eta Difference;|#Delta(#eta)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(electron.eta - electron.eta)"),
        ),
        cms.PSet (
            name = cms.string("diElectronDeltaR"),
            title = cms.string("Di-electron #DeltaR;#DeltaR"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(electron, electron)"),
        ),
        cms.PSet (
            name = cms.string("diElectronDeltaZ"),
            title = cms.string("Di-electron #DeltaZ;#DeltaZ"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            inputVariables = cms.vstring("abs(electron.vz - electron.vz)"),
        ),
   )
)

##############################################################################################

ElectronMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronPtMuonPt"),
            title = cms.string("Electron Momentum vs Muon Momentum;Muon p_{T} [GeV];Electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring("muon.pt","electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronEtaMuonEta"),
            title = cms.string("Electron Eta vs Muon Eta;Muon #eta;Electron #eta"),
            binsX = cms.untracked.vdouble(25,0,2.5),
            binsY = cms.untracked.vdouble(25,0,2.5),
            inputVariables = cms.vstring("abs(muon.eta)","abs(electron.eta)"),
        ),
        cms.PSet (
            name = cms.string("electronMuonPt"),
            title = cms.string("Momentum of Electron-Muon System;electron-muon p_{T} [GeV];"),
            binsX = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring("pT(electron, muon)"),
        ),
        cms.PSet (
            name = cms.string("electronMuonInvMass"),
            title = cms.string("Electron-muon Invariant Mass;M_{e#mu} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(electron, muon)"),
        ),
        cms.PSet (
            name = cms.string("electronMuonChargeProduct"),
            title = cms.string("Electron-muon Charge Product;charge_{e}*charge_{#mu}"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("electron.charge * muon.charge"),
        ),
        cms.PSet (
            name = cms.string("electronMuonDeltaPhi"),
            title = cms.string("Electron-muon Phi Difference;|#Delta(#phi)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(electron, muon))"),
        ),
        cms.PSet (
            name = cms.string("electronMuonDeltaEta"),
            title = cms.string("Electron-muon Eta Difference;|#Delta(#eta)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(electron.eta - muon.eta)"),
        ),
        cms.PSet (
            name = cms.string("electronMuonDeltaR"),
            title = cms.string("Electron-muon #DeltaR;#DeltaR"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(electron, muon)"),
        ),
        cms.PSet (
            name = cms.string("electronMuonDeltaZ"),
            title = cms.string("Electron-muon #DeltaZ;#DeltaZ [cm]"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("electron.vz - muon.vz"),
        ),
        cms.PSet (
            name = cms.string("electronRhoIsoVsMuonDbetaIso"),
            title = cms.string("Electron #rho-corrected Isolation vs. Muon #Delta#beta-corrected Isolation;Muon rel. iso.;Electron rel. iso."),
            binsX = cms.untracked.vdouble(300, 0, 3),
            binsY = cms.untracked.vdouble(300, 0, 3),
            inputVariables = cms.vstring("(muon.pfIsolationR04_.sumChargedHadronPt + max(0.0,muon.pfIsolationR04_.sumNeutralHadronEt + muon.pfIsolationR04_.sumPhotonEt - 0.5*muon.pfIsolationR04_.sumPUPt))/muon.pt","(electron.pfIso_.sumChargedHadronPt + max(0.0,electron.pfIso_.sumNeutralHadronEt + electron.pfIso_.sumPhotonEt - electron.rho*electron.AEff))/electron.pt"),
        ),
    )
)

##############################################################################################

ElectronMuonIPHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","muons","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronD0vsMuonD0Beamspot"),
            title = cms.string("Electron d_{0} wrt Beamspot vs. Muon d_{0} wrt Beamspot;Muon d_{0} [cm];Electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.02, 0.02),
            binsY = cms.untracked.vdouble(100, -0.02, 0.02),
            inputVariables = cms.vstring("(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt","(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsMuonAbsD0Beamspot"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Muon |d_{0}| wrt Beamspot;Muon |d_{0}| [cm];Electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 0.02),
            binsY = cms.untracked.vdouble(100, 0, 0.02),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
    )
)


##############################################################################################

ElectronMetHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","mets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronMetMT"),
            title = cms.string("Transverse Mass of Electron-E_{T}^{miss} System;m_{T}(e,E_{T}^{miss}) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("sqrt(2 * met.pt * electron.pt * (1.0 - cos(deltaPhi(electron,met))))"),
        ),
    )
)

##############################################################################################

MuonMetHistograms = cms.PSet(
    inputCollection = cms.vstring("muons","mets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonMetMT"),
            title = cms.string("Transverse Mass of Muon-E_{T}^{miss} System;m_{T}(#mu,E_{T}^{miss}) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("sqrt(2 * met.pt * muon.pt * (1.0 - cos(deltaPhi(muon,met))))"),
        ),
    )
)

##############################################################################################

JetHistograms = cms.PSet(
    inputCollection = cms.vstring("jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("numJets"),
            title = cms.string("Number of Selected Jets;# jets"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("number(jet)"),
        ),
        cms.PSet (
            name = cms.string("jetPt"),
            title = cms.string("Jet Transverse Momentum;jet p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("jetEta"),
            title = cms.string("Jet Eta;jet #eta"),
            binsX = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("jetPhi"),
            title = cms.string("Jet Phi;jet #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("jetCharge"),
            title = cms.string("Jet Charge;jet charge"),
            binsX = cms.untracked.vdouble(41, -20.5, 20.5),
            inputVariables = cms.vstring("charge"),
        ),
        cms.PSet (
            name = cms.string("jetMass"),
            title = cms.string("Jet Mass;jet mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("mass"),
        ),
        cms.PSet (
            name = cms.string("jetEtaPhi"),
            title = cms.string("Jet Eta vs. Jet Phi;jet #phi;jet #eta"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("phi","eta"),
        ),
        cms.PSet (
            name = cms.string("jetChargedHadronEnergyFraction"),
            title = cms.string("Jet Charged Hadron Fraction;jet charged hadron energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("chargedHadronEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("jetNeutralHadronEnergyFraction"),
            title = cms.string("Jet Neutral Hadron Fraction;jet neutral hadron energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("neutralHadronEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("jetNeutralEMEnergyFraction"),
            title = cms.string("Jet Neutral EM Fraction;jet neutral EM energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("neutralEmEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("jetChargedEMEnergyFraction"),
            title = cms.string("Jet Charged EM Fraction;jet charged EM energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("chargedEmEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("jetCSV"),
            title = cms.string("Jet Combined Secondary Vertex B-tagging Discriminant"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
        ),
        cms.PSet (
            name = cms.string("jetPileUpId"),
            title = cms.string("Jet PileUp Id"),
            binsX = cms.untracked.vdouble(200, -1, 1),
            inputVariables = cms.vstring("pileupJetId"),
        ),
    )
)

#####################################################################################

BjetHistograms = cms.PSet(
    inputCollection = cms.vstring("bjets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("numBjets"),
            title = cms.string("Number of Selected Bjets;# bjets"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("number(bjet)"),
        ),
        cms.PSet (
            name = cms.string("bjetPt"),
            title = cms.string("Bjet Transverse Momentum;bjet p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("bjetEta"),
            title = cms.string("Bjet Eta;bjet #eta"),
            binsX = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("bjetPhi"),
            title = cms.string("Bjet Phi;bjet #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("bjetCharge"),
            title = cms.string("Bjet Charge;bjet charge"),
            binsX = cms.untracked.vdouble(41, -20.5, 20.5),
            inputVariables = cms.vstring("charge"),
        ),
        cms.PSet (
            name = cms.string("bjetEtaPhi"),
            title = cms.string("Bjet Eta vs. Bjet Phi;bjet #phi;bjet #eta"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("phi","eta"),
        ),
        cms.PSet (
            name = cms.string("bjetChargedHadronEnergyFraction"),
            title = cms.string("Bjet Charged Hadron Fraction;bjet charged hadron energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("chargedHadronEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("bjetNeutralHadronEnergyFraction"),
            title = cms.string("Bjet Neutral Hadron Fraction;bjet neutral hadron energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("neutralHadronEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("bjetNeutralEMEnergyFraction"),
            title = cms.string("Bjet Neutral EM Fraction;bjet neutral EM energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("neutralEmEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("bjetChargedEMEnergyFraction"),
            title = cms.string("Bjet Charged EM Fraction;bjet charged EM energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("chargedEmEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("bjetCSV"),
            title = cms.string("Bjet Combined Secondary Vertex B-tagging Discriminant"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
        ),
        cms.PSet (
            name = cms.string("bjetPileUpId"),
            title = cms.string("BJet PileUp Id"),
            binsX = cms.untracked.vdouble(200, -1, 1),
            inputVariables = cms.vstring("pileupJetId"),
        ),
    )
)

#####################################################################################

JetIsoHistograms = cms.PSet(
    inputCollection = cms.vstring("jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jetChargedHadronEnergy"),
            title = cms.string("Charged Hadron Energy Deposited Within the Jet;E [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("chargedHadronEnergy"),
        ),
        cms.PSet (
            name = cms.string("jetNeutralHadronEnergy"),
            title = cms.string("Neutral Hadron Energy Deposited Within the Jet;E [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("neutralHadronEnergy"),
        ),
        cms.PSet (
            name = cms.string("jetChargedEmEnergy"),
            title = cms.string("Charged Em Energy Deposited Near the Jet;E [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("chargedEmEnergy"),
        ),
        cms.PSet (
            name = cms.string("jetNeutralEmEnergy"),
            title = cms.string("Neutral Em Energy Deposited Near the Jet;E [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("neutralEmEnergy"),
        ),
    )
)

##########################################################################################

JetBjetHistograms = cms.PSet(
    inputCollection = cms.vstring("jets","bjets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jetBjetInvMass"),
            title = cms.string("Jet-bjet Invariant Mass;M(jet,bjet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(jet,bjet)"),
        ),
        cms.PSet (
            name = cms.string("jetBjetDeltaPhi"),
            title = cms.string("Jet-bjet Phi Difference;|#Delta#phi(jet,bjet)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(jet,bjet))"),
        ),
        cms.PSet (
            name = cms.string("jetBjetDeltaEta"),
            title = cms.string("Jet-bjet Eta Difference;|#Delta#eta(jet,bjet)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(jet.eta - bjet.eta)"),
        ),
        cms.PSet (
            name = cms.string("jetBjetDeltaR"),
            title = cms.string("Jet-bjet #DeltaR;#DeltaR(jet,bjet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(jet,bjet)"),
        ),
        cms.PSet (
            name = cms.string("jetBjetDeltaZ"),
            title = cms.string("Jet-bjet Z Difference;|#Deltaz(jet,bjet)| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(jet.vz - bjet.vz)"),
        ),
        cms.PSet (
            name = cms.string("jetBjetDeltaRvsjetBjetDeltaEta"),
            title = cms.string("Jet-bjet #DeltaR vs #Delta#eta;|#Delta#eta(jet,bjet)|;#DeltaR(jet,bjet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            binsY = cms.untracked.vdouble(60, 0 ,6),
            inputVariables = cms.vstring("abs(jet.eta - bjet.eta)","deltaR(jet,bjet)"),
        ),
        cms.PSet (
            name = cms.string("jetBjetDeltaRvsjetBjetDeltaPhi"),
            title = cms.string("Jet-bjet #DeltaR vs #Delta#phi;|#Delta#phi(jet,bjet)|;#DeltaR(jet,bjet)"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            binsY = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(deltaPhi(jet,bjet))","deltaR(jet,bjet)"),
        ),
        cms.PSet (
            name = cms.string("jetEtavsBjetEta"),
            title = cms.string("Jet Eta.vs Bjet Eta;Bjet #eta;Jet #eta"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            binsY = cms.untracked.vdouble(120, -6 ,6),
            inputVariables = cms.vstring("bjet.eta","jet.eta"),
        ),
        cms.PSet (
            name = cms.string("jetPhivsBjetPhi"),
            title = cms.string("Jet Phi.vs Bjet Phi;Bjet #phi;Jet #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(64, -3.2 ,3.2),
            inputVariables = cms.vstring("bjet.phi","jet.phi"),
        ),
    )
)

##########################################################################################
##########################################################################################

MuonJetHistograms = cms.PSet(
    inputCollection = cms.vstring("muons","jets","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonAbsIPvsJetCSV"),
            title = cms.string("Muon Abs IP vs Jet CSV;Jet CSV"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            binsY = cms.untracked.vdouble(500, 0, 0.5),
            inputVariables = cms.vstring("jet.pfCombinedInclusiveSecondaryVertexV2BJetTags","abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)",),
        ),
        cms.PSet (
            name = cms.string("muonJetInvMass"),
            title = cms.string("Muon-jet Invariant Mass;M(#mu,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(muon,jet)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaPt"),
            title = cms.string("Muon-jet p_{T} Difference;|#Deltap_{T}(#mu,jet)|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs(muon.pt - jet.pt)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaPhi"),
            title = cms.string("Muon-jet Phi Difference;|#Delta#phi(#mu,jet)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(muon,jet))"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaEta"),
            title = cms.string("Muon-jet Eta Difference;|#Delta#eta(#mu,jet)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(muon.eta - jet.eta)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaR"),
            title = cms.string("Muon-jet #DeltaR;#DeltaR(#mu,jet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(muon,jet)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaZ"),
            title = cms.string("Muon-jet Z Difference;|#Deltaz(#mu,jet)| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(muon.vz - jet.vz)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaRvsmuonJetDeltaEta"),
            title = cms.string("Muon-jet #DeltaR vs #Delta#eta;|#Delta#eta(#mu,jet)|;#DeltaR(#mu,jet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            binsY = cms.untracked.vdouble(60, 0 ,6),
            inputVariables = cms.vstring("abs(muon.eta - jet.eta)","deltaR(muon,jet)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaRvsmuonJetDeltaPhi"),
            title = cms.string("Muon-jet #DeltaR vs #Delta#phi;|#Delta#phi(#mu,jet)|;#DeltaR(#mu,jet)"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            binsY = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(deltaPhi(muon,jet))","deltaR(muon,jet)"),
        ),
        cms.PSet (
            name = cms.string("muonEtavsJetEta"),
            title = cms.string("Muon Eta.vs Jet Eta;Jet #eta;Muon #eta"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            binsY = cms.untracked.vdouble(120, -6 ,6),
            inputVariables = cms.vstring("jet.eta","muon.eta"),
        ),
        cms.PSet (
            name = cms.string("muonPhivsJetPhi"),
            title = cms.string("Muon Phi.vs Jet Phi;Jet #phi;Muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(64, -3.2 ,3.2),
            inputVariables = cms.vstring("jet.phi","muon.phi"),
        ),
    )
)

##########################################################################################
##########################################################################################

ElectronJetHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","jets","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronAbsIPvsJetCSV"),
            title = cms.string("Electron Abs IP vs Jet CSV;Jet CSV"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            binsY = cms.untracked.vdouble(500, 0, 0.5),
            inputVariables = cms.vstring("jet.pfCombinedInclusiveSecondaryVertexV2BJetTags","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)",),
        ),
        cms.PSet (
            name = cms.string("electronJetInvMass"),
            title = cms.string("Electron-jet Invariant Mass;M(e,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(electron,jet)"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaPt"),
            title = cms.string("Electron-jet p_{T} Difference;|#Deltap_{T}(e,jet)|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs(electron.pt - jet.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaPhi"),
            title = cms.string("Electron-jet Phi Difference;|#Delta#phi(e,jet)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(electron,jet))"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaEta"),
            title = cms.string("Electron-jet Eta Difference;|#Delta#eta(e,jet)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(electron.eta - jet.eta)"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaR"),
            title = cms.string("Electron-jet #DeltaR;#DeltaR(e,jet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(electron,jet)"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaZ"),
            title = cms.string("Electron-jet Z Difference;|#Deltaz(e,jet)| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(electron.vz - jet.vz)"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaRvselectronJetDeltaEta"),
            title = cms.string("Electron-jet #DeltaR vs #Delta#eta;|#Delta#eta(e,jet)|;#DeltaR(e,jet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            binsY = cms.untracked.vdouble(60, 0 ,6),
            inputVariables = cms.vstring("abs(electron.eta - jet.eta)","deltaR(electron,jet)"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaRvselectronJetDeltaPhi"),
            title = cms.string("Electron-jet #DeltaR vs #Delta#phi;|#Delta#phi(e,jet)|;#DeltaR(e,jet)"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            binsY = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(deltaPhi(electron,jet))","deltaR(electron,jet)"),
        ),
        cms.PSet (
            name = cms.string("electronEtavsJetEta"),
            title = cms.string("Electron Eta.vs Jet Eta;Jet #eta;Electron #eta"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            binsY = cms.untracked.vdouble(120, -6 ,6),
            inputVariables = cms.vstring("jet.eta","electron.eta"),
        ),
        cms.PSet (
            name = cms.string("electronPhivsJetPhi"),
            title = cms.string("Electron Phi.vs Jet Phi;Jet #phi;Electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(64, -3.2 ,3.2),
            inputVariables = cms.vstring("jet.phi","electron.phi"),
        ),
    )
)

##########################################################################################

MuonBjetHistograms = cms.PSet(
    inputCollection = cms.vstring("muons","bjets","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonAbsIPvsBjetCSV"),
            title = cms.string("Muon Abs IP vs Bjet CSV;Bjet CSV"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            binsY = cms.untracked.vdouble(500, 0, 0.5),
            inputVariables = cms.vstring("bjet.pfCombinedInclusiveSecondaryVertexV2BJetTags","abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)",),
        ),
        cms.PSet (
            name = cms.string("muonBjetInvMass"),
            title = cms.string("Muon-bjet Invariant Mass;M(#mu,bjet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(muon,bjet)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaPt"),
            title = cms.string("Muon-jet p_{T} Difference;|#Deltap_{T}(#mu,bjet)|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs(muon.pt - bjet.pt)"),
        ),
        cms.PSet (
            name = cms.string("muonBjetDeltaPhi"),
            title = cms.string("Muon-bjet Phi Difference;|#Delta#phi(#mu,bjet)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(muon,bjet))"),
        ),
        cms.PSet (
            name = cms.string("muonBjetDeltaEta"),
            title = cms.string("Muon-bjet Eta Difference;|#Delta#eta(#mu,bjet)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(muon.eta - bjet.eta)"),
        ),
        cms.PSet (
            name = cms.string("muonBjetDeltaR"),
            title = cms.string("Muon-bjet #DeltaR;#DeltaR(#mu,bjet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(muon,bjet)"),
        ),
        cms.PSet (
            name = cms.string("muonBjetDeltaZ"),
            title = cms.string("Muon-bjet Z Difference;|#Deltaz(#mu,bjet)| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(muon.vz - bjet.vz)"),
        ),
        cms.PSet (
            name = cms.string("muonBjetDeltaRvsmuonBjetDeltaEta"),
            title = cms.string("Muon-bjet #DeltaR vs #Delta#eta;|#Delta#eta(#mu,bjet)|;#DeltaR(#mu,bjet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            binsY = cms.untracked.vdouble(60, 0 ,6),
            inputVariables = cms.vstring("abs(muon.eta - bjet.eta)","deltaR(muon,bjet)"),
        ),
        cms.PSet (
            name = cms.string("muonBjetDeltaRvsmuonBjetDeltaPhi"),
            title = cms.string("Muon-bjet #DeltaR vs #Delta#phi;|#Delta#phi(#mu,bjet)|;#DeltaR(#mu,bjet)"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            binsY = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(deltaPhi(muon,bjet))","deltaR(muon,bjet)"),
        ),
        cms.PSet (
            name = cms.string("muonEtavsBjetEta"),
            title = cms.string("Muon Eta.vs Bjet Eta;Bjet #eta;Muon #eta"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            binsY = cms.untracked.vdouble(120, -6 ,6),
            inputVariables = cms.vstring("bjet.eta","muon.eta"),
        ),
        cms.PSet (
            name = cms.string("muonPhivsBjetPhi"),
            title = cms.string("Muon Phi.vs Bjet Phi;Bjet #phi;Muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(64, -3.2 ,3.2),
            inputVariables = cms.vstring("bjet.phi","muon.phi"),
        ),
    )
)

##########################################################################
ElectronBjetHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","bjets","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronAbsIPvsBjetCSV"),
            title = cms.string("Electron Abs IP vs Bjet CSV;Bjet CSV"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            binsY = cms.untracked.vdouble(500, 0, 0.5),
            inputVariables = cms.vstring("bjet.pfCombinedInclusiveSecondaryVertexV2BJetTags","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)",),
        ),
        cms.PSet (
            name = cms.string("electronBjetInvMass"),
            title = cms.string("Electron-bjet Invariant Mass;M(#mu,bjet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(electron,bjet)"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaPt"),
            title = cms.string("Electron-bjet p_{T} Difference;|#Deltap_{T}(e,bjet)|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs(electron.pt - bjet.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaPhi"),
            title = cms.string("Electron-bjet Phi Difference;|#Delta#phi(#mu,bjet)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(electron,bjet))"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaEta"),
            title = cms.string("Electron-bjet Eta Difference;|#Delta#eta(#mu,bjet)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(electron.eta - bjet.eta)"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaR"),
            title = cms.string("Electron-bjet #DeltaR;#DeltaR(#mu,bjet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(electron,bjet)"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaZ"),
            title = cms.string("Electron-bjet Z Difference;|#Deltaz(#mu,bjet)| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(electron.vz - bjet.vz)"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaRvselectronBjetDeltaEta"),
            title = cms.string("Electron-bjet #DeltaR vs #Delta#eta;|#Delta#eta(#mu,bjet)|;#DeltaR(#mu,bjet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            binsY = cms.untracked.vdouble(60, 0 ,6),
            inputVariables = cms.vstring("abs(electron.eta - bjet.eta)","deltaR(electron,bjet)"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaRvselectronBjetDeltaPhi"),
            title = cms.string("Electron-bjet #DeltaR vs #Delta#phi;|#Delta#phi(#mu,bjet)|;#DeltaR(#mu,bjet)"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            binsY = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(deltaPhi(electron,bjet))","deltaR(electron,bjet)"),
        ),
        cms.PSet (
            name = cms.string("electronEtavsBjetEta"),
            title = cms.string("Electron Eta.vs Bjet Eta;Bjet #eta;Electron #eta"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            binsY = cms.untracked.vdouble(120, -6 ,6),
            inputVariables = cms.vstring("bjet.eta","electron.eta"),
        ),
        cms.PSet (
            name = cms.string("electronPhivsBjetPhi"),
            title = cms.string("Electron Phi.vs Bjet Phi;Bjet #phi;Electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(64, -3.2 ,3.2),
            inputVariables = cms.vstring("bjet.phi","electron.phi"),
        ),
    )
)

##########################################################################
PhotonHistograms = cms.PSet(
    inputCollection = cms.vstring("photons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("photonPt"),
            title = cms.string("Photon Transverse Momentum;p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("photonEta"),
            title = cms.string("Photon Eta;#eta"),
            binsX = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("photonPhi"),
            title = cms.string("Photon Phi;#phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("photonEtaPhi"),
            title = cms.string("Photon Eta vs. Photon Phi;#phi;#eta"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("phi","eta"),
        ),
        cms.PSet (
            name = cms.string("photonGenMatchPdgId"),
            title = cms.string(";|PDG ID| of generator particle matched to photon"),
            binsX = cms.untracked.vdouble(600, 0, 600),
            inputVariables = cms.vstring("abs (genMatchedParticle.noFlagsPdgId)"),
            ),
        cms.PSet (
            name = cms.string("photonGenMatchPt"),
            title = cms.string("Gen Photon Transverse Momentum;Gen photon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("photonGenMatchEta"),
            title = cms.string("Gen Photon Eta;Gen photon #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.eta"),
        ),
        cms.PSet (
            name = cms.string("photonGenMatchPhi"),
            title = cms.string("Gen Photon Phi;Gen photon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.phi"),
        ),
        cms.PSet (
            name = cms.string("photonGenMatchMotherPdgId"),
            title = cms.string(";|PDG ID| of mother of gen photon"),
            binsX = cms.untracked.vdouble(600, 0, 600),
            inputVariables = cms.vstring("abs(genMatchedParticle.noFlags.uniqueMotherPdgId)"),
        ),
    )
)



##############################################################################################

MetHistograms = cms.PSet(
    inputCollection = cms.vstring("mets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("metPt"),
            title = cms.string("Missing E_{T};E_{T}^{miss} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("metPhi"),
            title = cms.string("Phi of Missing E_{T};#phi(E_{T}^{miss})"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
    )
)

##############################################################################################

TrackHistograms = cms.PSet(
     inputCollection = cms.vstring("tracks"),
     histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackPt"),
            title = cms.string("Track Transverse Momentum;track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 10, 510),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
             name = cms.string("trackEta"),
             title = cms.string("Track Eta;track #eta"),
             binsX = cms.untracked.vdouble(60, -3, 3),
             inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
             name = cms.string("trackEtaMag"),
             title = cms.string("Track Eta;track |#eta|"),
             binsX = cms.untracked.vdouble(30, 0, 3),
             inputVariables = cms.vstring("fabs(eta)"),
        ),
        cms.PSet (
             name = cms.string("trackPhi"),
             title = cms.string("Track Phi;track #phi"),
             binsX = cms.untracked.vdouble(64, -3.2, 3.2),
             inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("trackEtaVsPhi"),
            title = cms.string("#eta vs #phi;track #eta;track #phi"),
            binsX = cms.untracked.vdouble(60, -3, 3),
            binsY = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("eta", "phi"),
        ),
        cms.PSet (
            name = cms.string("trackd0"),
            title = cms.string("Track d_{0};track d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("d0"),
        ),
        cms.PSet (
            name = cms.string("trackd0Mag"),
            title = cms.string("Track d_{0};track |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(50, 0.0, 0.5),
            inputVariables = cms.vstring("fabs(d0)"),
        ),
        cms.PSet (
            name = cms.string("trackdz"),
            title = cms.string("Track d_{z};track d_{z} [cm]"),
            binsX = cms.untracked.vdouble(60, -30, 30),
            inputVariables = cms.vstring("dz"),
        ),
        cms.PSet (
            name = cms.string("trackdzMag"),
            title = cms.string("Track d_{z};track |d_{z}| [cm]"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("fabs(dz)"),
        ),
        cms.PSet (
            name = cms.string("trackNumValidPixelHits"),
            title = cms.string("Track Number of Valid Pixel Hits;number of valid pixel hits"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("hitPattern_.numberOfValidPixelHits"),
        ),
        cms.PSet (
            name = cms.string("trackNumValidHits"),
            title = cms.string("Track Number of Valid Hits;number of valid hits"),
            binsX = cms.untracked.vdouble(100, -0.5, 99.5),
            inputVariables = cms.vstring("hitPattern_.numberOfValidHits"),
        ),
        cms.PSet (
            name = cms.string("trackNumLayersWithMeasurement"),
            title = cms.string("Track Number of Layers with Measurement;number of layers with measurement"),
            binsX = cms.untracked.vdouble(20, -0.5, 19.5),
            inputVariables = cms.vstring("hitPattern_.trackerLayersWithMeasurement"),
        ),
        cms.PSet (
            name = cms.string("trackChi2"),
            title = cms.string("Track Reduced Chi2;track #chi^{2}/ndf"),
            binsX = cms.untracked.vdouble(50, 0, 10),
            inputVariables = cms.vstring("normalizedChi2"),
        ),
        cms.PSet (
            name = cms.string("trackCharge"),
            title = cms.string("Track Charge;track charge"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("charge"),
        ),
        cms.PSet (
            name = cms.string("noFlagsPdgId"),
            title = cms.string(";|PDG ID| of generator particle matched to track"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.noFlagsPdgId)"),
            ),
        cms.PSet (
            name = cms.string("genMatchedPromptFinalStateIsMatched"),
            title = cms.string(";track is matched to generator particle"),
            binsX = cms.untracked.vdouble(2.0, -0.5, 1.5),
            inputVariables = cms.vstring("genMatchedParticle.promptFinalState.isNonnull"),
        ),
        cms.PSet (
            name = cms.string("genMatchedPromptFinalStatePdgId"),
            title = cms.string(";|PDG ID| of matched generator particle"),
            binsX = cms.untracked.vdouble(getPdgBins(["quarks", "leptons", "bosons", "hadrons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.promptFinalState.pdgId)"),
        ),
        cms.PSet (
            name = cms.string("genMatchedPromptFinalStatePdgIdNoHadrons"),
            title = cms.string(";|PDG ID| of matched generator particle"),
            binsX = cms.untracked.vdouble(getPdgBins(["quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.promptFinalState.pdgId)"),
        ),
        cms.PSet (
            name = cms.string("genMatchedDirectPromptTauDecayProductFinalStateIsMatched"),
            title = cms.string(";track is matched to generator #tau decay product"),
            binsX = cms.untracked.vdouble(2.0, -0.5, 1.5),
            inputVariables = cms.vstring("genMatchedParticle.directPromptTauDecayProductFinalState.isNonnull"),
        ),
        cms.PSet (
            name = cms.string("genMatchedDirectPromptTauDecayProductFinalStatePdgId"),
            title = cms.string(";|PDG ID| of matched generator #tau decay product"),
            binsX = cms.untracked.vdouble(getPdgBins(["quarks", "leptons", "bosons", "hadrons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.directPromptTauDecayProductFinalState.pdgId)"),
        ),
        cms.PSet (
            name = cms.string("genMatchedDirectPromptTauDecayProductFinalStatePdgIdNoHadrons"),
            title = cms.string(";|PDG ID| of matched generator #tau decay product"),
            binsX = cms.untracked.vdouble(getPdgBins(["quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.directPromptTauDecayProductFinalState.pdgId)"),
        ),
    )
)

##############################################################################################

TrackBeamspotHistograms = cms.PSet(
     inputCollection = cms.vstring("tracks", "beamspots"),
     histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackd0"),
            title = cms.string("Track d_{0};track d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring(trackD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("trackd0Mag"),
            title = cms.string("Track d_{0};track |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(50, 0, 0.5),
            inputVariables = cms.vstring("fabs ( " + trackD0WRTBeamspot + " )"),
        ),
        cms.PSet (
            name = cms.string("trackdz"),
            title = cms.string("Track d_{z};track d_{z} [cm]"),
            binsX = cms.untracked.vdouble(60, -30, 30),
            inputVariables = cms.vstring("(track.vz - beamspot.z0) - ((track.vx - beamspot.x0) * track.px + (track.vy - beamspot.y0) * track.py) / track.pt * (track.pz / track.pt)"),
        ),
        cms.PSet (
            name = cms.string("trackdzMag"),
            title = cms.string("Track d_{z};track |d_{z}| [cm]"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("fabs((track.vz - beamspot.z0) - ((track.vx - beamspot.x0) * track.px + (track.vy - beamspot.y0) * track.py) / track.pt * (track.pz / track.pt))"),
        ),
    )
)


##############################################################################################

TrackEventVarHistograms = cms.PSet(
    # To produce these histograms, include in your PSet:
    # variableProducers.append("PrimaryVtxVarProducer")
     inputCollection = cms.vstring("tracks", "eventvariables"),
     histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackd0WRTPV"),
            title = cms.string("Track d_{0} wrt leading PV;track d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring(trackD0WRTPV),
        ),
        cms.PSet (
            name = cms.string("trackd0WRTPV_Zoom"),
            title = cms.string("Track d_{0} wrt leading PV;track d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.1, 0.1),
            inputVariables = cms.vstring(trackD0WRTPV),
        ),
        cms.PSet (
            name = cms.string("trackd0WRTPVMag"),
            title = cms.string("Track d_{0} wrt leading PV;track |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(50, 0, 0.5),
            inputVariables = cms.vstring("fabs ( " + trackD0WRTPV + " )"),
        ),
        cms.PSet (
            name = cms.string("trackdzWRTPV"),
            title = cms.string("Track d_{z} wrt leading PV;track d_{z} [cm]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring(trackDZWRTPV),
        ),
        cms.PSet (
            name = cms.string("trackdzWRTPV_Zoom"),
            title = cms.string("Track d_{z} wrt leading PV;track d_{z} [cm]"),
            binsX = cms.untracked.vdouble(100, -2, 2),
            inputVariables = cms.vstring(trackDZWRTPV),
        ),
        cms.PSet (
            name = cms.string("trackdzWRTPVMag"),
            title = cms.string("Track d_{z} wrt leading PV;track |d_{z}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("fabs( " + trackDZWRTPV + " )" ),
        ),
    )
)
##############################################################################################

TrackMCParticleHistograms = cms.PSet(
    inputCollection = cms.vstring("track-mcparticle pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("TrackMCPartDeltaEta"),
            title = cms.string("Track-MCParticle Eta Difference;|#Delta(#eta)|"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("deltaEta"),
            ),
        cms.PSet (
            name = cms.string("TrackMCPartDeltaPhi"),
            title = cms.string("Track-MCParticle Phi Difference;|#Delta(#phi)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("deltaPhi"),
            ),
        cms.PSet (
            name = cms.string("TrackMCPartDeltaR"),
            title = cms.string("Track-MCParticle #DeltaR;#DeltaR"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("deltaR"),
            ),
        cms.PSet (
            name = cms.string("TrackMCPartDeltaRZoom"),
            title = cms.string("Track-MCParticle #DeltaR;#DeltaR"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaR"),
            ),
        cms.PSet (
            name = cms.string("TrackMCPart3DAngle"),
            title = cms.string("Track-MCParticle 3D Angle;3D angle"),
            binsX = cms.untracked.vdouble(100, 0, 4),
            inputVariables = cms.vstring("threeDAngle"),
            ),
        )
    )

##############################################################################################

EventVariablePVHistograms = cms.PSet(
    # EventVariable quantities associated with primary vertices
    # To produce these variables, include in your PSet:
    # variableProducers.append("PrimaryVtxVarProducer")
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("numPVReco"),
            title = cms.string(";Number of Primary Vertices"),
            binsX = cms.untracked.vdouble(50, 0.0, 50.0),
            inputVariables = cms.vstring("numPVReco"),
        ),
        cms.PSet (
            name = cms.string("leadingPV_x"),
            title = cms.string(";X Position of Leading Primary Vertex"),
            binsX = cms.untracked.vdouble(50, -1.0, 1.0),
            inputVariables = cms.vstring("leadingPV_x"),
        ),
        cms.PSet (
            name = cms.string("leadingPV_y"),
            title = cms.string(";Y Position of Leading Primary Vertex"),
            binsX = cms.untracked.vdouble(50, -1.0, 1.0),
            inputVariables = cms.vstring("leadingPV_y"),
        ),
        cms.PSet (
            name = cms.string("leadingPV_z"),
            title = cms.string(";Z Position of Leading Primary Vertex"),
            binsX = cms.untracked.vdouble(50, -20.0, 20.0),
            inputVariables = cms.vstring("leadingPV_z"),
        ),
    )
)

##############################################################################################

#####################################
##### Define variable bin lists #####
#####################################

import math
def variableBins(nBins,lower,upper):
    original_bin_size = (upper - lower)/float(nBins)
    number_of_sections = 4
    bins_per_section = math.floor(nBins/number_of_sections)
    multipliers = [2**n for n in range(number_of_sections)]
    last = 0
    variableBins = [0]
    for multiplier in multipliers:
        bins = [last + multiplier*original_bin_size*n for n in range(1,int(math.ceil(bins_per_section/multiplier))+1)]
        last = bins[-1]
        variableBins.extend(bins)
    return variableBins

# create list of bin edges for 10cm d0 TH2s
# 10um bins from 0-2mm, then 100um bins from 2mm to 10cm so TH2 isn't too large
fine_100000um_bins = range(0, 2000, 10) + range(2000, 100001, 100)

###############################################
##### Set up the histograms to be plotted #####
###############################################

ElectronD0Histograms = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    histograms = cms.VPSet (

        ###################################################################
        # track d0 error histogram
        cms.PSet (
            name = cms.string("electronTrackD0Error"),
            title = cms.string("Electron track #sigma(d_{0});Electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*"+electronD0WRTBeamspotErr),
            ),
        cms.PSet (
            name = cms.string("electronDz_500um"),
            title = cms.string("Electron d_{z};Electron d_{z} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*"+electronDZWRTBeamspot),
            ),

        ###################################################################
        # d0 calculation histograms
        cms.PSet (
            name = cms.string("electronVxWrtBeamspot_100um"),
            title = cms.string("Electron track reference point x value wrt beamspot;Electron track reference point x value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("10000*(electron.vx-beamspot.x0)"),
        ),
        cms.PSet (
            name = cms.string("electronVyWrtBeamspot_100um"),
            title = cms.string("Electron track reference point y value wrt beamspot;Electron track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("10000*(electron.vy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("electronVyWrtBeamspot[0]_vs_electronVxWrtBeamspot[0]_100um"),
            title = cms.string("Leading electron track reference point y value wrt beamspot vs. leading electron track reference point x value wrt beamspot;Leading electron track reference point x value wrt beamspot [#mum];Leading electron track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(200, -100, 100),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*(electron.vx-beamspot.x0)","10000*(electron.vy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("electronVyWrtBeamspot[1]_vs_electronVxWrtBeamspot[1]_100um"),
            title = cms.string("Subleading electron track reference point y value wrt beamspot vs. subleading electron track reference point x value wrt beamspot;Subleading electron track reference point x value wrt beamspot [#mum];Subleading electron track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(200, -100, 100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*(electron.vx-beamspot.x0)","10000*(electron.vy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("electronV0WrtBeamspot_100um"),
            title = cms.string("Electron track reference point v0 wrt beamspot;Electron track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*hypot((electron.vx-beamspot.x0), (electron.vy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("electronV0WrtBeamspot[1]_vs_electronV0WrtBeamspot[0]_100um"),
            title = cms.string("Subleading electron track reference point v0 wrt beamspot vs leading electron track reference point v0 wrt beamspot;Leading electron track reference point v0 wrt beamspot [#mum];Subleading electron track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((electron.vx-beamspot.x0), (electron.vy-beamspot.y0))","10000*hypot((electron.vx-beamspot.x0), (electron.vy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronV0WrtBeamspot[0]_100um"),
            title = cms.string("Leading electron |d_{0}| vs leading electron track reference point v0 wrt beamspot;Leading electron track reference point v0 wrt beamspot [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*hypot((electron.vx-beamspot.x0), (electron.vy-beamspot.y0))", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[1]_vs_electronV0WrtBeamspot[1]_100um"),
            title = cms.string("Subleading electron |d_{0}| vs subleading electron track reference point v0 wrt beamspot;Subleading electron track reference point v0 wrt beamspot [#mum];Subleading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((electron.vx-beamspot.x0), (electron.vy-beamspot.y0))", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronVxWrtBeamspot_10000um"),
            title = cms.string("Electron track reference point x value wrt beamspot;Electron track reference point x value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            inputVariables = cms.vstring("10000*(electron.vx-beamspot.x0)"),
        ),
        cms.PSet (
            name = cms.string("electronVyWrtBeamspot_10000um"),
            title = cms.string("Electron track reference point y value wrt beamspot;Electron track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            inputVariables = cms.vstring("10000*(electron.vy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("electronVyWrtBeamspot[0]_vs_electronVxWrtBeamspot[0]_10000um"),
            title = cms.string("Leading electron track reference point y value wrt beamspot vs. leading electron track reference point x value wrt beamspot;Leading electron track reference point x value wrt beamspot [#mum];Leading electron track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            binsY = cms.untracked.vdouble(200, -10000, 10000),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*(electron.vx-beamspot.x0)","10000*(electron.vy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("electronVyWrtBeamspot[1]_vs_electronVxWrtBeamspot[1]_10000um"),
            title = cms.string("Subleading electron track reference point y value wrt beamspot vs. subleading electron track reference point x value wrt beamspot;Subleading electron track reference point x value wrt beamspot [#mum];Subleading electron track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            binsY = cms.untracked.vdouble(200, -10000, 10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*(electron.vx-beamspot.x0)","10000*(electron.vy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("electronV0WrtBeamspot_10000um"),
            title = cms.string("Electron track reference point v0 wrt beamspot;Electron track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("10000*hypot((electron.vx-beamspot.x0), (electron.vy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("electronV0WrtBeamspot[1]_vs_electronV0WrtBeamspot[0]_10000um"),
            title = cms.string("Subleading electron track reference point v0 wrt beamspot vs leading electron track reference point v0 wrt beamspot;Leading electron track reference point v0 wrt beamspot [#mum];Subleading electron track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((electron.vx-beamspot.x0), (electron.vy-beamspot.y0))","10000*hypot((electron.vx-beamspot.x0), (electron.vy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronV0WrtBeamspot[0]_10000um"),
            title = cms.string("Leading electron |d_{0}| vs leading electron track reference point v0 wrt beamspot;Leading electron track reference point v0 wrt beamspot [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*hypot((electron.vx-beamspot.x0), (electron.vy-beamspot.y0))", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[1]_vs_electronV0WrtBeamspot[1]_10000um"),
            title = cms.string("Subleading electron |d_{0}| vs subleading electron track reference point v0 wrt beamspot;Subleading electron track reference point v0 wrt beamspot [#mum];Subleading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((electron.vx-beamspot.x0), (electron.vy-beamspot.y0))", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronGenVxWrtBeamspot_100um"),
            title = cms.string("Gen electron track reference point x value wrt beamspot;Gen electron track reference point x value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("10000*(electron.genVx-beamspot.x0)"),
        ),
        cms.PSet (
            name = cms.string("electronGenVyWrtBeamspot_100um"),
            title = cms.string("Gen electron track reference point y value wrt beamspot;Gen electron track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("10000*(electron.genVy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("electronGenVyWrtBeamspot[0]_vs_electronGenVxWrtBeamspot[0]_100um"),
            title = cms.string("Leading gen Electron track reference point y value wrt beamspot vs. leading gen electron track reference point x value wrt beamspot;Leading gen electron track reference point x value wrt beamspot [#mum];Leading gen electron track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(200, -100, 100),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*(electron.genVx-beamspot.x0)","10000*(electron.genVy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("electronGenVyWrtBeamspot[1]_vs_electronGenVxWrtBeamspot[1]_100um"),
            title = cms.string("Subleading gen Electron track reference point y value wrt beamspot vs. subleading gen electron track reference point x value wrt beamspot;Subleading gen electron track reference point x value wrt beamspot [#mum];Subleading gen electron track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(200, -100, 100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*(electron.genVx-beamspot.x0)","10000*(electron.genVy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("electronGenV0WrtBeamspot_100um"),
            title = cms.string("Gen electron track reference point v0 wrt beamspot;Gen electron track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*hypot((electron.genVx-beamspot.x0), (electron.genVy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("electronGenV0WrtBeamspot[1]_vs_electronGenV0WrtBeamspot[0]_100um"),
            title = cms.string("Subleading gen electron track reference point v0 wrt beamspot vs leading gen electron track reference point v0 wrt beamspot;Leading gen electron track reference point v0 wrt beamspot [#mum];Subleading gen electron track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((electron.genVx-beamspot.x0), (electron.genVy-beamspot.y0))","10000*hypot((electron.genVx-beamspot.x0), (electron.genVy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0[0]_vs_electronGenV0WrtBeamspot[0]_100um"),
            title = cms.string("Leading gen electron d_{0} vs leading gen electron track reference point v0 wrt beamspot;Leading gen electron track reference point v0 wrt beamspot [#mum];Leading gen electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*hypot((electron.genVx-beamspot.x0), (electron.genVy-beamspot.y0))", "10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0[1]_vs_electronGenV0WrtBeamspot[1]_100um"),
            title = cms.string("Subleading gen electron d_{0} vs subleading gen electron track reference point v0 wrt beamspot;Subleading gen electron track reference point v0 wrt beamspot [#mum];Subleading gen electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((electron.genVx-beamspot.x0), (electron.genVy-beamspot.y0))", "10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenVxWrtBeamspot_10000um"),
            title = cms.string("Gen electron track reference point x value wrt beamspot;Gen electron track reference point x value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            inputVariables = cms.vstring("10000*(electron.genVx-beamspot.x0)"),
        ),
        cms.PSet (
            name = cms.string("electronGenVyWrtBeamspot_10000um"),
            title = cms.string("Gen electron track reference point y value wrt beamspot;Gen electron track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            inputVariables = cms.vstring("10000*(electron.genVy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("electronGenVyWrtBeamspot[0]_vs_electronGenVxWrtBeamspot[0]_10000um"),
            title = cms.string("Gen electron track reference point y value wrt beamspot vs. gen electron track reference point x value wrt beamspot;Gen electron track reference point x value wrt beamspot [#mum];Gen electron track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            binsY = cms.untracked.vdouble(200, -10000, 10000),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*(electron.genVx-beamspot.x0)","10000*(electron.genVy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("electronGenVyWrtBeamspot[1]_vs_electronGenVxWrtBeamspot[1]_10000um"),
            title = cms.string("Gen electron track reference point y value wrt beamspot vs. gen electron track reference point x value wrt beamspot;Gen electron track reference point x value wrt beamspot [#mum];Gen electron track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            binsY = cms.untracked.vdouble(200, -10000, 10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*(electron.genVx-beamspot.x0)","10000*(electron.genVy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("electronGenV0WrtBeamspot_10000um"),
            title = cms.string("Gen electron track reference point v0 wrt beamspot;Gen electron track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("10000*hypot((electron.genVx-beamspot.x0), (electron.genVy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("electronGenV0WrtBeamspot[1]_vs_electronGenV0WrtBeamspot[0]_10000um"),
            title = cms.string("Subleading gen electron track reference point v0 wrt beamspot vs leading gen electron track reference point v0 wrt beamspot;Leading gen electron track reference point v0 wrt beamspot [#mum];Subleading gen electron track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((electron.genVx-beamspot.x0), (electron.genVy-beamspot.y0))","10000*hypot((electron.genVx-beamspot.x0), (electron.genVy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0[0]_vs_electronGenV0WrtBeamspot[0]_10000um"),
            title = cms.string("Leading gen electron d_{0} vs leading gen electron track reference point v0 wrt beamspot;Leading gen electron track reference point v0 wrt beamspot [#mum];Leading gen electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*hypot((electron.genVx-beamspot.x0), (electron.genVy-beamspot.y0))", "10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0[1]_vs_electronGenV0WrtBeamspot[1]_10000um"),
            title = cms.string("Subleading gen electron d_{0} vs subleading gen electron track reference point v0 wrt beamspot;Subleading gen electron track reference point v0 wrt beamspot [#mum];Subleading gen electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((electron.genVx-beamspot.x0), (electron.genVy-beamspot.y0))", "10000*electron.genD0"),
        ),

        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("electronD0_10um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_50um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_100um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_200um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_500um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_1000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_2000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -2000, 2000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_5000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_10000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1, 10000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_20000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -2, 20000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_50000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5, 50000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_100000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(1000, -10, 100000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_200000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -20, 200000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),

        ###################################################################
        # d0 smearing histograms
        cms.PSet (
            name = cms.string("electronUnsmearedD0_50um"),
            title = cms.string("Unsmeared Electron d_{0};Unsmeared Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*"+electronD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0SmearingVal"),
            title = cms.string("Electron d_{0} Smearing Value;Electron d_{0} Smearing Value [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*electron.d0SmearingVal"),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("electronAbsD0_10um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,10)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_50um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_50um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,50)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_100um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_100um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,200)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_500um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_500um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,500)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,1000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1000um_variableBins_coarse"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,1000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingAbsD0_1000um"),
            title = cms.string("Electron |d_{0}|;Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_2000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 2000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_2000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,2000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,5000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,10000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10000um_variableBins_coarse"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,10000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingAbsD0_10000um"),
            title = cms.string("Electron |d_{0}|;Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_20000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 20000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_20000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,20000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_50000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_50000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,50000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_100000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_100000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_100000um_variableBins_coarse"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,100000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingAbsD0_100000um"),
            title = cms.string("Electron |d_{0}|;Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingAbsD0_100000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100000)),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingAbsD0_100000um_variableBins_coarse"),
            title = cms.string("Electron |d_{0}|;Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,100000)),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,200000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        ###################################################################
        # sig(d0) histograms
        cms.PSet (
            name = cms.string("electronD0Sig_5"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_10"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_20"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_50"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_100"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_200"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_500"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),

        ###################################################################
        # abs(sig(d0)) histograms
        cms.PSet (
            name = cms.string("electronAbsD0Sig_5"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_10"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_20"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_50"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_100"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_200"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_500"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),

        ###################################################################
        # 2D plots
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_10um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_50um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_100um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_200um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_500um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_1000um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,1000),
            binsY = cms.untracked.vdouble(100,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_10000um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10000),
            binsY = cms.untracked.vdouble(100,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_100000um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_10um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10),
            binsY = cms.untracked.vdouble(10,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_50um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,50),
            binsY = cms.untracked.vdouble(10,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_100um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,100),
            binsY = cms.untracked.vdouble(10,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_200um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200),
            binsY = cms.untracked.vdouble(10,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_500um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,500),
            binsY = cms.untracked.vdouble(10,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_1000um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,1000),
            binsY = cms.untracked.vdouble(10,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_10000um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10000),
            binsY = cms.untracked.vdouble(10,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_5"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,5),
            binsY = cms.untracked.vdouble(100,0,5),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_10"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_20"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,20),
            binsY = cms.untracked.vdouble(100,0,20),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_50"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_100"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_200"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_500"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),

        ###################################################################
        # 2D abs(d0) vs. abs(sig(d0))
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_ElectronAbsD0Sig_50"),
            title = cms.string("Electron |d_{0}| vs. Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5000um_vs_ElectronAbsD0Sig_500"),
            title = cms.string("Electron |d_{0}| vs. Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        ###################################################################
        # 2D abs(d0) vs. d0 error
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_ElectronTrackD0Error_500"),
            title = cms.string("Electron |d_{0}| vs. Electron #sigma(d_{0});Electron #sigma(d_{0}) [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*"+electronD0WRTBeamspotErr, "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        ###################################################################
        # 2D d0 vs. pt
        cms.PSet (
            name = cms.string("electronD0_vs_electronPt"),
            title = cms.string("Electron d_{0} vs. Electron p_{T};Electron p_{T} [GeV];Electron d_{0} [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.pt", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        ###################################################################
        # 2D abs(d0) vs. pt
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_electronPt_200"),
            title = cms.string("Electron |d_{0}| vs. Electron p_{T};Electron p_{T} [GeV];Electron |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1000um_vs_electronPt_500"),
            title = cms.string("Electron |d_{0}| vs. Electron p_{T};Electron p_{T} [GeV];Electron |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10000um_vs_electronPt_1000"),
            title = cms.string("Electron |d_{0}| vs. Electron p_{T};Electron p_{T} [GeV];Electron |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_electronPt_200_coarse"),
            title = cms.string("Electron |d_{0}| vs. Electron p_{T};Electron p_{T} [GeV];Electron |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(20, 0, 200),
            binsY = cms.untracked.vdouble(20, 0, 500),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1000um_vs_electronPt_500_coarse"),
            title = cms.string("Electron |d_{0}| vs. Electron p_{T};Electron p_{T} [GeV];Electron |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(20, 0, 500),
            binsY = cms.untracked.vdouble(20, 0, 1000),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10000um_vs_electronPt_1000_coarse"),
            title = cms.string("Electron |d_{0}| vs. Electron p_{T};Electron p_{T} [GeV];Electron |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(20, 0, 1000),
            binsY = cms.untracked.vdouble(20, 0, 10000),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        ###################################################################
        # 2D sig(d0) vs. pt
        cms.PSet (
            name = cms.string("electronD0Sig_vs_electronPt"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) vs. Electron p_{T};Electron p_{T} [GeV];Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("electron.pt", electronD0WRTBeamspotSig),
        ),
        ###################################################################
        # 2D track d0 error vs. pt
        cms.PSet (
            name = cms.string("electronTrackD0Error_vs_electronPt"),
            title = cms.string("Electron track #sigma(d_{0}) vs. Electron p_{T};Electron p_{T} [GeV];Electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("electron.pt", "10000*"+electronD0WRTBeamspotErr),
        ),
        ###################################################################
        # 2D d0 vs. eta
        cms.PSet (
            name = cms.string("electronD0_vs_electronEta"),
            title = cms.string("Electron d_{0} vs. Electron #eta;Electron #eta;Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.eta", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        ###################################################################
        # 2D sig(d0) vs. eta
        cms.PSet (
            name = cms.string("electronD0Sig_vs_electronEta"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) vs. Electron #eta;Electron #eta;Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("electron.eta", electronD0WRTBeamspotSig),
        ),
        ###################################################################
        # 2D track d0 error vs. eta
        cms.PSet (
            name = cms.string("electronTrackD0Error_vs_electronEta"),
            title = cms.string("Electron track #sigma(d_{0}) vs. Electron #eta;Electron #eta;Electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("electron.eta", "10000*"+electronD0WRTBeamspotErr),
        ),
        ###################################################################
        # 2D d0 vs. phi
        cms.PSet (
            name = cms.string("electronD0_50um_vs_electronPhi"),
            title = cms.string("Electron d_{0} vs. Electron #phi;Electron #phi;Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("electron.phi", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_500um_vs_electronPhi"),
            title = cms.string("Electron d_{0} vs. Electron #phi;Electron #phi;Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.phi", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        ###################################################################
        # 2D sig(d0) vs. phi
        cms.PSet (
            name = cms.string("electronD0Sig_vs_electronPhi"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) vs. Electron #phi;Electron #phi;Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("electron.phi", electronD0WRTBeamspotSig),
        ),
        ###################################################################
        # 2D track d0 error vs. phi
        cms.PSet (
            name = cms.string("electronTrackD0Error_vs_electronPhi"),
            title = cms.string("Electron track #sigma(d_{0}) vs. Electron #phi;Electron #phi;Electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("electron.phi", "10000*"+electronD0WRTBeamspotErr),
        ),

        ###################################################################
        # 3D leading electron d0 vs subleading electron d0 vs leading electron pt
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_2000um_vs_electronPt[0]"),
            title = cms.string("Leading |d_{0}| vs Subleading |d_{0}| vs Electron Leading p_{T};Leading electron |d_{0}| [#mum];Subleading electron |d_{0}| [#mum];Leading electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            indexZ = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")","10000*abs("+electronSmearedD0WRTBeamspot+")","electron.pt"),
        ),
        # 3D leading electron d0 vs subleading electron d0 vs subleading electron pt
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_2000um_vs_electronPt[1]"),
            title = cms.string("Leading |d_{0}| vs Subleading |d_{0}| vs Electron Subleading p_{T};Leading electron |d_{0}| [#mum];Subleading electron |d_{0}| [#mum];Subleading electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            indexZ = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")","10000*abs("+electronSmearedD0WRTBeamspot+")","electron.pt"),
        ),


        ###################################################################
        ###################################################################
        # begin gen d0 histograms

        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("electronGenD0_10um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_50um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_100um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_200um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_500um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_5000um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_50000um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50000, 50000),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_100000um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(1000, -100000, 100000),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_200000um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200000, 200000),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("electronAbsGenD0_10um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_50um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_100um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_200um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_500um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_5000um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_50000um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50000),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_100000um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_200000um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200000),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),


        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_10um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_50um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_100um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_200um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_500um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_1000um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,1000),
            binsY = cms.untracked.vdouble(100,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_10000um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10000),
            binsY = cms.untracked.vdouble(100,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_100000um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("vertexIsOrigin_electronAbsGenD0[0]_vs_electronAbsGenD0[1]_100000um"),
            title = cms.string("With the vertex set to the origin (wrong d0!), Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronGenVertexIsOriginD0WRTBeamspot+")", "10000*abs("+electronGenVertexIsOriginD0WRTBeamspot+")"),
        ),


        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_10um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10),
            binsY = cms.untracked.vdouble(10,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_50um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,50),
            binsY = cms.untracked.vdouble(10,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_100um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,100),
            binsY = cms.untracked.vdouble(10,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_200um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200),
            binsY = cms.untracked.vdouble(10,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_500um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,500),
            binsY = cms.untracked.vdouble(10,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_1000um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,1000),
            binsY = cms.untracked.vdouble(10,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_10000um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10000),
            binsY = cms.untracked.vdouble(10,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),


        cms.PSet (
            name = cms.string("electronD0pull_50um"),
            title = cms.string("Electron reco d_{0} - gen d_{0}; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_100um"),
            title = cms.string("Electron reco d_{0} - gen d_{0}; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_200um"),
            title = cms.string("Electron reco d_{0} - gen d_{0}; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_500um"),
            title = cms.string("Electron reco d_{0} - gen d_{0}; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),

        cms.PSet (
            name = cms.string("electronD0pullAbs_50um"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}|; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_100um"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}|; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_200um"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}|; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_500um"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}|; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),

        #2D pull vs reco pt
        cms.PSet (
            name = cms.string("electronD0pull_50um_vs_electronPt"),
            title = cms.string("Electron reco d_{0} - gen d_{0} vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("electron.pt", "10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_100um_vs_electronPt"),
            title = cms.string("Electron reco d_{0} - gen d_{0} vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("electron.pt", "10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_200um_vs_electronPt"),
            title = cms.string("Electron reco d_{0} - gen d_{0} vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("electron.pt", "10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_500um_vs_electronPt"),
            title = cms.string("Electron reco d_{0} - gen d_{0} vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.pt", "10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),

        cms.PSet (
            name = cms.string("electronD0pullAbs_50um_vs_electronPt"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}| vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_100um_vs_electronPt"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}| vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_200um_vs_electronPt"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}| vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_500um_vs_electronPt"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}| vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),


        cms.PSet (
            name = cms.string("electronD0_10um_vs_electronGenD0_10um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            binsY = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_50um_vs_electronGenD0_50um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_100um_vs_electronGenD0_100um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_200um_vs_electronGenD0_200um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_500um_vs_electronGenD0_500um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_1000um_vs_electronGenD0_1000um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            binsY = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_5000um_vs_electronGenD0_5000um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            binsY = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),




        cms.PSet (
            name = cms.string("electronAbsD0_10um_vs_electronAbsGenD0_10um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            binsY = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_50um_vs_electronAbsGenD0_50um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_100um_vs_electronAbsGenD0_100um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200um_vs_electronAbsGenD0_200um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_electronAbsGenD0_500um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1000um_vs_electronAbsGenD0_1000um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5000um_vs_electronAbsGenD0_5000um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        #gen 3D
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_2000um_vs_electronGenPt[0]"),
            title = cms.string("Leading gen |d_{0}| vs Subleading gen |d_{0}| vs Gen Electron Leading p_{T};Leading gen electron |d_{0}| [#mum];Subleading gen electron |d_{0}| [#mum];Leading gen electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            indexZ = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)","10000*abs(electron.genD0)","electron.genMatchedParticle.noFlags.pt"),
        ),

    )
)



MuonD0Histograms = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    histograms = cms.VPSet (

        ###################################################################
        # track d0 error histogram
        cms.PSet (
            name = cms.string("muonTrackD0Error"),
            title = cms.string("Muon track #sigma(d_{0});Muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*"+muonD0WRTBeamspotErr),
        ),
        cms.PSet (
            name = cms.string("muonDz_500um"),
            title = cms.string("Muon d_{z};Muon d_{z} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*"+muonDZWRTBeamspot),
            ),

        ###################################################################
        # d0 calculation histograms
        cms.PSet (
            name = cms.string("muonVxWrtBeamspot_100um"),
            title = cms.string("Muon track reference point x value wrt beamspot;Muon track reference point x value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("10000*(muon.vx-beamspot.x0)"),
        ),
        cms.PSet (
            name = cms.string("muonVyWrtBeamspot_100um"),
            title = cms.string("Muon track reference point y value wrt beamspot;Muon track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("10000*(muon.vy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("muonVyWrtBeamspot[0]_vs_muonVxWrtBeamspot[0]_100um"),
            title = cms.string("Leading muon track reference point y value wrt beamspot vs. leading muon track reference point x value wrt beamspot;Leading muon track reference point x value wrt beamspot [#mum];Leading muon track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(200, -100, 100),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*(muon.vx-beamspot.x0)","10000*(muon.vy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("muonVyWrtBeamspot[1]_vs_muonVxWrtBeamspot[1]_100um"),
            title = cms.string("Subleading muon track reference point y value wrt beamspot vs. subleading muon track reference point x value wrt beamspot;Subleading muon track reference point x value wrt beamspot [#mum];Subleading muon track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(200, -100, 100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*(muon.vx-beamspot.x0)","10000*(muon.vy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("muonV0WrtBeamspot_100um"),
            title = cms.string("Muon track reference point v0 wrt beamspot;Muon track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*hypot((muon.vx-beamspot.x0), (muon.vy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("muonV0WrtBeamspot[1]_vs_muonV0WrtBeamspot[0]_100um"),
            title = cms.string("Subleading muon track reference point v0 wrt beamspot vs leading muon track reference point v0 wrt beamspot;Leading muon track reference point v0 wrt beamspot [#mum];Subleading muon track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((muon.vx-beamspot.x0), (muon.vy-beamspot.y0))","10000*hypot((muon.vx-beamspot.x0), (muon.vy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonV0WrtBeamspot[0]_100um"),
            title = cms.string("Leading muon |d_{0}| vs leading muon track reference point v0 wrt beamspot;Leading muon track reference point v0 wrt beamspot [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*hypot((muon.vx-beamspot.x0), (muon.vy-beamspot.y0))", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[1]_vs_muonV0WrtBeamspot[1]_100um"),
            title = cms.string("Subleading muon |d_{0}| vs subleading muon track reference point v0 wrt beamspot;Subleading muon track reference point v0 wrt beamspot [#mum];Subleading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((muon.vx-beamspot.x0), (muon.vy-beamspot.y0))", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonVxWrtBeamspot_10000um"),
            title = cms.string("Muon track reference point x value wrt beamspot;Muon track reference point x value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            inputVariables = cms.vstring("10000*(muon.vx-beamspot.x0)"),
        ),
        cms.PSet (
            name = cms.string("muonVyWrtBeamspot_10000um"),
            title = cms.string("Muon track reference point y value wrt beamspot;Muon track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            inputVariables = cms.vstring("10000*(muon.vy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("muonVyWrtBeamspot[0]_vs_muonVxWrtBeamspot[0]_10000um"),
            title = cms.string("Leading muon track reference point y value wrt beamspot vs. leading muon track reference point x value wrt beamspot;leading muon track reference point x value wrt beamspot [#mum];Leading muon track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            binsY = cms.untracked.vdouble(200, -10000, 10000),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*(muon.vx-beamspot.x0)","10000*(muon.vy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("muonVyWrtBeamspot[1]_vs_muonVxWrtBeamspot[1]_10000um"),
            title = cms.string("Subleading muon track reference point y value wrt beamspot vs. subleading muon track reference point x value wrt beamspot;Subleading muon track reference point x value wrt beamspot [#mum];Subleading muon track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            binsY = cms.untracked.vdouble(200, -10000, 10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*(muon.vx-beamspot.x0)","10000*(muon.vy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("muonV0WrtBeamspot_10000um"),
            title = cms.string("Muon track reference point v0 wrt beamspot;Muon track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("10000*hypot((muon.vx-beamspot.x0), (muon.vy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("muonV0WrtBeamspot[1]_vs_muonV0WrtBeamspot[0]_10000um"),
            title = cms.string("Subleading muon track reference point v0 wrt beamspot vs leading muon track reference point v0 wrt beamspot;Leading muon track reference point v0 wrt beamspot [#mum];Subleading muon track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((muon.vx-beamspot.x0), (muon.vy-beamspot.y0))","10000*hypot((muon.vx-beamspot.x0), (muon.vy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonV0WrtBeamspot[0]_10000um"),
            title = cms.string("Leading muon |d_{0}| vs leading muon track reference point v0 wrt beamspot;Leading muon track reference point v0 wrt beamspot [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*hypot((muon.vx-beamspot.x0), (muon.vy-beamspot.y0))", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[1]_vs_muonV0WrtBeamspot[1]_10000um"),
            title = cms.string("Subleading muon |d_{0}| vs subleading muon track reference point v0 wrt beamspot;Subleading muon track reference point v0 wrt beamspot [#mum];Subleading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((muon.vx-beamspot.x0), (muon.vy-beamspot.y0))", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonGenVxWrtBeamspot_100um"),
            title = cms.string("Gen muon track reference point x value wrt beamspot;Gen muon track reference point x value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("10000*(muon.genVx-beamspot.x0)"),
        ),
        cms.PSet (
            name = cms.string("muonGenVyWrtBeamspot_100um"),
            title = cms.string("Gen muon track reference point y value wrt beamspot;Gen muon track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("10000*(muon.genVy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("muonGenVyWrtBeamspot[0]_vs_muonGenVxWrtBeamspot[0]_100um"),
            title = cms.string("Leading gen muon track reference point y value wrt beamspot vs. leading gen muon track reference point x value wrt beamspot;Leading gen muon track reference point x value wrt beamspot [#mum];Leading gen muon track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(200, -100, 100),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*(muon.genVx-beamspot.x0)","10000*(muon.genVy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("muonGenVyWrtBeamspot[1]_vs_muonGenVxWrtBeamspot[1]_100um"),
            title = cms.string("Subleading gen muon track reference point y value wrt beamspot vs. subleading gen muon track reference point x value wrt beamspot;Subleading gen muon track reference point x value wrt beamspot [#mum];Subleading gen muon track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            binsY = cms.untracked.vdouble(200, -100, 100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*(muon.genVx-beamspot.x0)","10000*(muon.genVy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("muonGenV0WrtBeamspot_100um"),
            title = cms.string("Gen muon track reference point v0 wrt beamspot;Gen muon track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*hypot((muon.genVx-beamspot.x0), (muon.genVy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("muonGenV0WrtBeamspot[1]_vs_muonGenV0WrtBeamspot[0]_100um"),
            title = cms.string("Subleading gen muon track reference point v0 wrt beamspot vs leading gen muon track reference point v0 wrt beamspot;Leading gen muon track reference point v0 wrt beamspot [#mum];Subleading gen muon track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((muon.genVx-beamspot.x0), (muon.genVy-beamspot.y0))","10000*hypot((muon.genVx-beamspot.x0), (muon.genVy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0[0]_vs_muonGenV0WrtBeamspot[0]_100um"),
            title = cms.string("Leading gen muon d_{0} vs leading gen muon track reference point v0 wrt beamspot;Leading gen muon track reference point v0 wrt beamspot [#mum];Leading gen muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*hypot((muon.genVx-beamspot.x0), (muon.genVy-beamspot.y0))", "10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0[1]_vs_muonGenV0WrtBeamspot[1]_100um"),
            title = cms.string("Subleading gen muon d_{0} vs subleading gen muon track reference point v0 wrt beamspot;Subleading gen muon track reference point v0 wrt beamspot [#mum];Subleading gen muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((muon.genVx-beamspot.x0), (muon.genVy-beamspot.y0))", "10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenVxWrtBeamspot_10000um"),
            title = cms.string("Gen muon track reference point x value wrt beamspot;Gen muon track reference point x value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            inputVariables = cms.vstring("10000*(muon.genVx-beamspot.x0)"),
        ),
        cms.PSet (
            name = cms.string("muonGenVyWrtBeamspot_10000um"),
            title = cms.string("Gen muon track reference point y value wrt beamspot;Gen muon track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            inputVariables = cms.vstring("10000*(muon.genVy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("muonGenVyWrtBeamspot[0]_vs_muonGenVxWrtBeamspot[0]_10000um"),
            title = cms.string("Leading gen muon track reference point y value wrt beamspot vs. leading gen muon track reference point x value wrt beamspot;Leading gen muon track reference point x value wrt beamspot [#mum];Leading gen muon track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            binsY = cms.untracked.vdouble(200, -10000, 10000),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*(muon.genVx-beamspot.x0)","10000*(muon.genVy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("muonGenVyWrtBeamspot[1]_vs_muonGenVxWrtBeamspot[1]_10000um"),
            title = cms.string("Subleading gen muon track reference point y value wrt beamspot vs. subleading gen muon track reference point x value wrt beamspot;Subleading gen muon track reference point x value wrt beamspot [#mum];Subleading gen muon track reference point y value wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            binsY = cms.untracked.vdouble(200, -10000, 10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*(muon.genVx-beamspot.x0)","10000*(muon.genVy-beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("muonGenV0WrtBeamspot_10000um"),
            title = cms.string("Gen muon track reference point v0 wrt beamspot;Gen muon track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("10000*hypot((muon.genVx-beamspot.x0), (muon.genVy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("muonGenV0WrtBeamspot[1]_vs_muonGenV0WrtBeamspot[0]_10000um"),
            title = cms.string("Subleading gen muon track reference point v0 wrt beamspot vs leading gen muon track reference point v0 wrt beamspot;Leading gen muon track reference point v0 wrt beamspot [#mum];Subleading gen muon track reference point v0 wrt beamspot [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((muon.genVx-beamspot.x0), (muon.genVy-beamspot.y0))","10000*hypot((muon.genVx-beamspot.x0), (muon.genVy-beamspot.y0))"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0[0]_vs_muonGenV0WrtBeamspot[0]_10000um"),
            title = cms.string("Leading gen muon d_{0} vs leading gen muon track reference point v0 wrt beamspot;Leading gen muon track reference point v0 wrt beamspot [#mum];Leading gen muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*hypot((muon.genVx-beamspot.x0), (muon.genVy-beamspot.y0))", "10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0[1]_vs_muonGenV0WrtBeamspot[1]_10000um"),
            title = cms.string("Subleading gen muon d_{0} vs subleading gen muon track reference point v0 wrt beamspot;Subleading gen muon track reference point v0 wrt beamspot [#mum];Subleading gen muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*hypot((muon.genVx-beamspot.x0), (muon.genVy-beamspot.y0))", "10000*muon.genD0"),
        ),

        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("muonD0_10um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_50um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_100um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_200um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_500um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_1000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_2000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -2000, 2000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_5000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_10000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10000, 10000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_20000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -20000, 20000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_50000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50000, 50000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_100000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(1000, -100000, 100000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_200000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200000, 200000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),

        ###################################################################
        # d0 smearing histograms
        cms.PSet (
            name = cms.string("muonUnsmearedD0_50um"),
            title = cms.string("Unsmeared Muon d_{0};Unsmeared Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*"+muonD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0SmearingVal"),
            title = cms.string("Muon d_{0} Smearing Value;Muon d_{0} Smearing Value [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*muon.d0SmearingVal"),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("muonAbsD0_10um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,10)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_50um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_50um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,50)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_100um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_100um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,200)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_500um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_500um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,500)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,1000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1000um_variableBins_coarse"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,1000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonLeadingAbsD0_1000um"),
            title = cms.string("Muon |d_{0}|;Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_2000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 2000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_2000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,2000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,5000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,10000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10000um_variableBins_coarse"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,10000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonLeadingAbsD0_10000um"),
            title = cms.string("Muon |d_{0}|;Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_20000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 20000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_20000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,20000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_50000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_50000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,50000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_100000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_100000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_100000um_variableBins_coarse"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,100000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonLeadingAbsD0_100000um"),
            title = cms.string("Muon |d_{0}|;Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonLeadingAbsD0_100000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100000)),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonLeadingAbsD0_100000um_variableBins_coarse"),
            title = cms.string("Muon |d_{0}|;Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,100000)),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,200000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),

        ###################################################################
        # sig(d0) histograms
        cms.PSet (
            name = cms.string("muonD0Sig_5"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_10"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_20"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_50"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_100"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_200"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_500"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),

        ###################################################################
        # abs(sig(d0)) histograms
        cms.PSet (
            name = cms.string("muonAbsD0Sig_5"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_10"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_20"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_50"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_100"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_200"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_500"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),

        ###################################################################
        # 2D plots
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_10um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_50um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_100um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_200um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_500um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_1000um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,1000),
            binsY = cms.untracked.vdouble(100,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_10000um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10000),
            binsY = cms.untracked.vdouble(100,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_100000um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_10um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10),
            binsY = cms.untracked.vdouble(10,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_50um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,50),
            binsY = cms.untracked.vdouble(10,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_100um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,100),
            binsY = cms.untracked.vdouble(10,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_200um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200),
            binsY = cms.untracked.vdouble(10,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_500um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,500),
            binsY = cms.untracked.vdouble(10,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_1000um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,1000),
            binsY = cms.untracked.vdouble(10,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_10000um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10000),
            binsY = cms.untracked.vdouble(10,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_5"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,5),
            binsY = cms.untracked.vdouble(100,0,5),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_10"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_20"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,20),
            binsY = cms.untracked.vdouble(100,0,20),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_50"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_100"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_200"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_500"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),

        ###################################################################
        # 2D abs(d0) vs. abs(sig(d0))
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_MuonAbsD0Sig_50"),
            title = cms.string("Muon |d_{0}| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5000um_vs_MuonAbsD0Sig_500"),
            title = cms.string("Muon |d_{0}| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),

        ###################################################################
        # 2D abs(d0) vs. d0 error
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_MuonTrackD0Error_500"),
            title = cms.string("Muon |d_{0}| vs. Muon #sigma(d_{0});Muon #sigma(d_{0}) [#mum];Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*"+muonD0WRTBeamspotErr, "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),

        ###################################################################
        # 2D d0 vs. pt
        cms.PSet (
            name = cms.string("muonD0_vs_muonPt"),
            title = cms.string("Muon d_{0} vs. Muon p_{T};Muon p_{T} [GeV];Muon d_{0} [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.pt", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        ###################################################################
        # 2D abs(d0) vs. pt
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_muonPt_200"),
            title = cms.string("Muon |d_{0}| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1000um_vs_muonPt_500"),
            title = cms.string("Muon |d_{0}| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10000um_vs_muonPt_1000"),
            title = cms.string("Muon |d_{0}| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_muonPt_200_coarse"),
            title = cms.string("Muon |d_{0}| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(20, 0, 200),
            binsY = cms.untracked.vdouble(20, 0, 500),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1000um_vs_muonPt_500_coarse"),
            title = cms.string("Muon |d_{0}| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(20, 0, 500),
            binsY = cms.untracked.vdouble(20, 0, 1000),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10000um_vs_muonPt_1000_coarse"),
            title = cms.string("Muon |d_{0}| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(20, 0, 1000),
            binsY = cms.untracked.vdouble(20, 0, 10000),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        ###################################################################
        # 2D sig(d0) vs. pt
        cms.PSet (
            name = cms.string("muonD0Sig_vs_muonPt"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) vs. Muon p_{T};Muon p_{T} [GeV];Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("muon.pt", muonD0WRTBeamspotSig),
        ),
        ###################################################################
        # 2D abs( sig(d0) ) vs. pt
        cms.PSet (
            name = cms.string("muonAbsD0Sig_vs_muonPt"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.pt", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        ###################################################################
        # 2D track d0 error vs. pt
        cms.PSet (
            name = cms.string("muonTrackD0Error_vs_muonPt"),
            title = cms.string("Muon track #sigma(d_{0}) vs. Muon p_{T};Muon p_{T} [GeV];Muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("muon.pt", "10000*"+muonD0WRTBeamspotErr),
        ),
        ###################################################################
        # 2D d0 vs. eta
        cms.PSet (
            name = cms.string("muonD0_vs_muonEta"),
            title = cms.string("Muon d_{0} vs. Muon #eta;Muon #eta;Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.eta", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        ###################################################################
        # 2D sig(d0) vs. eta
        cms.PSet (
            name = cms.string("muonD0Sig_vs_muonEta"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) vs. Muon #eta;Muon #eta;Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("muon.eta", muonD0WRTBeamspotSig),
        ),
        ###################################################################
        # 2D track d0 error vs. eta
        cms.PSet (
            name = cms.string("muonTrackD0Error_vs_muonEta"),
            title = cms.string("Muon track #sigma(d_{0}) vs. Muon #eta;Muon #eta;Muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("muon.eta", "10000*"+muonD0WRTBeamspotErr),
        ),
        ###################################################################
        # 2D d0 vs. phi
        cms.PSet (
            name = cms.string("muonD0_50um_vs_muonPhi"),
            title = cms.string("Muon d_{0} vs. Muon #phi;Muon #phi;Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("muon.phi", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_500um_vs_muonPhi"),
            title = cms.string("Muon d_{0} vs. Muon #phi;Muon #phi;Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.phi", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        ###################################################################
        # 2D sig(d0) vs. phi
        cms.PSet (
            name = cms.string("muonD0Sig_vs_muonPhi"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) vs. Muon #phi;Muon #phi;Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("muon.phi", muonD0WRTBeamspotSig),
        ),
        ###################################################################
        # 2D track d0 error vs. phi
        cms.PSet (
            name = cms.string("muonTrackD0Error_vs_muonPhi"),
            title = cms.string("Muon track #sigma(d_{0}) vs. Muon #phi;Muon #phi;Muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("muon.phi", "10000*"+muonD0WRTBeamspotErr),
        ),

        ###################################################################
        # 3D leading muon d0 vs subleading muon d0 vs leading muon pt
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_2000um_vs_muonPt[0]"),
            title = cms.string("Leading |d_{0}| vs Subleading |d_{0}| vs Muon Leading p_{T};Leading muon |d_{0}| [#mum];Subleading muon |d_{0}| [#mum];Leading muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            indexZ = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")","10000*abs("+muonSmearedD0WRTBeamspot+")","muon.pt"),
        ),
        # 3D leading muon d0 vs subleading muon d0 vs subleading muon pt
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_2000um_vs_muonPt[1]"),
            title = cms.string("Leading |d_{0}| vs Subleading |d_{0}| vs Muon Subleading p_{T};Leading muon |d_{0}| [#mum];Subleading muon |d_{0}| [#mum];Subleading muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            indexZ = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")","10000*abs("+muonSmearedD0WRTBeamspot+")","muon.pt"),
        ),


        ###################################################################
        ###################################################################
        # begin gen d0 histograms

        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("muonGenD0_10um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_50um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_100um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_200um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_500um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_5000um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_50000um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50000, 50000),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_100000um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(1000, -100000, 100000),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_200000um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200000, 200000),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("muonAbsGenD0_10um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_50um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_100um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_200um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_500um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_5000um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_50000um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_100000um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_200000um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),


        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_10um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_50um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_100um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_200um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_500um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_1000um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,1000),
            binsY = cms.untracked.vdouble(100,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_10000um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10000),
            binsY = cms.untracked.vdouble(100,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_100000um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("vertexIsOrigin_muonAbsGenD0[0]_vs_muonAbsGenD0[1]_100000um"),
            title = cms.string("With the vertex set to the origin (wrong d0!), Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonGenVertexIsOriginD0WRTBeamspot+")", "10000*abs("+muonGenVertexIsOriginD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_10um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10),
            binsY = cms.untracked.vdouble(10,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_50um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,50),
            binsY = cms.untracked.vdouble(10,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_100um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,100),
            binsY = cms.untracked.vdouble(10,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_200um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200),
            binsY = cms.untracked.vdouble(10,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_500um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,500),
            binsY = cms.untracked.vdouble(10,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_1000um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,1000),
            binsY = cms.untracked.vdouble(10,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_10000um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10000),
            binsY = cms.untracked.vdouble(10,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        #gen 3D
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_2000um_vs_muonGenPt[0]"),
            title = cms.string("Leading gen |d_{0}| vs Subleading gen |d_{0}| vs Gen Muon Leading p_{T};Leading gen muon |d_{0}| [#mum];Subleading gen muon |d_{0}| [#mum];Leading gen muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            indexZ = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)","10000*abs(muon.genD0)","muon.genMatchedParticle.noFlags.pt"),
        ),

        cms.PSet (
            name = cms.string("muonD0pull_50um"),
            title = cms.string("Muon reco d_{0} - gen d_{0}; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_100um"),
            title = cms.string("Muon reco d_{0} - gen d_{0}; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_200um"),
            title = cms.string("Muon reco d_{0} - gen d_{0}; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_500um"),
            title = cms.string("Muon reco d_{0} - gen d_{0}; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),

        cms.PSet (
            name = cms.string("muonD0pullAbs_50um"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}|; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_100um"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}|; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_200um"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}|; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_500um"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}|; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),

        #2D pull vs reco pt
        cms.PSet (
            name = cms.string("muonD0pull_50um_vs_muonPt"),
            title = cms.string("Muon reco d_{0} - gen d_{0} vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("muon.pt", "10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_100um_vs_muonPt"),
            title = cms.string("Muon reco d_{0} - gen d_{0} vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("muon.pt", "10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_200um_vs_muonPt"),
            title = cms.string("Muon reco d_{0} - gen d_{0} vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("muon.pt", "10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_500um_vs_muonPt"),
            title = cms.string("Muon reco d_{0} - gen d_{0} vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.pt", "10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),

        cms.PSet (
            name = cms.string("muonD0pullAbs_50um_vs_muonPt"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}| vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_100um_vs_muonPt"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}| vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_200um_vs_muonPt"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}| vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_500um_vs_muonPt"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}| vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),


        cms.PSet (
            name = cms.string("muonD0_10um_vs_muonGenD0_10um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; Muon gen d_{0} [#mum]; Muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            binsY = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("10000*muon.genD0", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_100um_vs_muonGenD0_100um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; Muon gen d_{0} [#mum]; Muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*muon.genD0", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_200um_vs_muonGenD0_200um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; Muon gen d_{0} [#mum]; Muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*muon.genD0", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_500um_vs_muonGenD0_500um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; Muon gen d_{0} [#mum]; Muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*muon.genD0", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_1000um_vs_muonGenD0_1000um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; Muon gen d_{0} [#mum]; Muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            binsY = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("10000*muon.genD0", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_5000um_vs_muonGenD0_5000um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; Muon gen d_{0} [#mum]; Muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            binsY = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*muon.genD0", "10000*"+muonSmearedD0WRTBeamspot),
        ),




        cms.PSet (
            name = cms.string("muonAbsD0_10um_vs_muonAbsGenD0_10um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            binsY = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_50um_vs_muonAbsGenD0_50um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_100um_vs_muonAbsGenD0_100um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200um_vs_muonAbsGenD0_200um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_muonAbsGenD0_500um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1000um_vs_muonAbsGenD0_1000um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5000um_vs_muonAbsGenD0_5000um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
    )
)


ElectronMuonD0Histograms = cms.PSet(
    inputCollection = cms.vstring("electrons","muons","beamspots"),
    histograms = cms.VPSet (

        ###################################################################
        #
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_10um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_50um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_100um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_200um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_500um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_1000um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,1000),
            binsY = cms.untracked.vdouble(100,0,1000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_10000um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10000),
            binsY = cms.untracked.vdouble(100,0,10000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_100000um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingAbsD0_vs_muonLeadingAbsD0_100000um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Leading muon |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            indexX = cms.untracked.int32(0),
            indexy = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_200000um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200000),
            binsY = cms.untracked.vdouble(100,0,200000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_10um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10),
            binsY = cms.untracked.vdouble(10,0,10),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_50um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,50),
            binsY = cms.untracked.vdouble(10,0,50),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_100um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,100),
            binsY = cms.untracked.vdouble(10,0,100),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_200um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200),
            binsY = cms.untracked.vdouble(10,0,200),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_500um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,500),
            binsY = cms.untracked.vdouble(10,0,500),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_1000um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,1000),
            binsY = cms.untracked.vdouble(10,0,1000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_10000um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10000),
            binsY = cms.untracked.vdouble(10,0,10000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_200000um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200000),
            binsY = cms.untracked.vdouble(10,0,200000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_5"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,5),
            binsY = cms.untracked.vdouble(100,0,5),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_10"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_20"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,20),
            binsY = cms.untracked.vdouble(100,0,20),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_50"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_100"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_200"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_500"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        ###################################################################
        # 3D leading muon d0 vs leading electron d0 vs leading muon pt
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_electronAbsD0[0]_2000um_vs_muonPt[0]"),
            title = cms.string("Leading muon |d_{0}| vs Leading electron |d_{0}| vs Muon leading p_{T};Leading muon |d_{0}| [#mum];Leading electron |d_{0}| [#mum];Leading muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            indexZ = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")","10000*abs("+electronSmearedD0WRTBeamspot+")","muon.pt"),
        ),
        # 3D leading muon d0 vs leading electron d0 vs leading electron pt
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_electronAbsD0[0]_2000um_vs_electronPt[0]"),
            title = cms.string("Leading muon |d_{0}| vs Leading electron |d_{0}| vs Electron leading p_{T};Leading muon |d_{0}| [#mum];Leading electron |d_{0}| [#mum];Leading electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            indexZ = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")","10000*abs("+electronSmearedD0WRTBeamspot+")","electron.pt"),
        ),

        #gen
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_10um"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_50um"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_100um"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_200um"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_500um"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_2000um"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(2000,0,2000),
            binsY = cms.untracked.vdouble(2000,0,2000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("vertexIsOrigin_electronAbsGenD0[0]_vs_muonAbsGenD0[0]_100000um"),
            title = cms.string("With the vertex set to the origin (wrong d0!), Leading gen electron |d_{0}| vs. Leading gen muon |d_{0}|;Leading gen muon |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonGenVertexIsOriginD0WRTBeamspot+")", "10000*abs("+electronGenVertexIsOriginD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_10um_coarse"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10),
            binsY = cms.untracked.vdouble(10,0,10),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_50um_coarse"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,50),
            binsY = cms.untracked.vdouble(10,0,50),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_100um_coarse"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,100),
            binsY = cms.untracked.vdouble(10,0,100),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_200um_coarse"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200),
            binsY = cms.untracked.vdouble(10,0,200),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_500um_coarse"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,500),
            binsY = cms.untracked.vdouble(10,0,500),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_2000um_coarse"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,2000),
            binsY = cms.untracked.vdouble(10,0,2000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        #gen 3D
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_electronAbsGenD0[0]_2000um_vs_muonGenPt[0]"),
            title = cms.string("Leading muon gen |d_{0}| vs Leading electron gen |d_{0}| vs Gen Muon Leading p_{T};Leading gen muon |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum];Leading gen muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            indexZ = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)","10000*abs(electron.genD0)","muon.genMatchedParticle.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_electronAbsGenD0[0]_2000um_vs_electronGenPt[0]"),
            title = cms.string("Leading muon gen |d_{0}| vs Leading electron gen |d_{0}| vs Gen Electron Leading p_{T};Leading gen muon |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum];Leading gen electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            indexZ = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)","10000*abs(electron.genD0)","electron.genMatchedParticle.noFlags.pt"),
        ),
    )
)


ElectronPhotonHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","photons"),
    histograms = cms.VPSet (

        ###################################################################
        #
        cms.PSet (
            name = cms.string("electronPhotonDeltaPhi"),
            title = cms.string("Electron-photon Phi Difference;|#Delta(#phi)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs ( deltaPhi (electron, photon) )"),
        ),
        cms.PSet (
            name = cms.string("electronPhotonDeltaEta"),
            title = cms.string("Electron-photon Eta Difference;|#Delta(#eta)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs (electron.eta - photon.eta)"),
        ),
        cms.PSet (
            name = cms.string("electronPhotonDeltaR"),
            title = cms.string("Electron-photon #DeltaR;#DeltaR"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR (electron, photon)"),
        ),
        cms.PSet (
            name = cms.string("electronPhotonDeltaPhiZoomed"),
            title = cms.string("Electron-photon Phi Difference;|#Delta(#phi)|"),
            binsX = cms.untracked.vdouble(50, 0, 1),
            inputVariables = cms.vstring("abs ( deltaPhi (electron, photon) )"),
        ),
        cms.PSet (
            name = cms.string("electronPhotonDeltaEtaZoomed"),
            title = cms.string("Electron-photon Eta Difference;|#Delta(#eta)|"),
            binsX = cms.untracked.vdouble(20, 0, 1),
            inputVariables = cms.vstring("abs (electron.eta - photon.eta)"),
        ),
        cms.PSet (
            name = cms.string("electronPt_vs_photonPt"),
            title = cms.string("Electron p_{T} vs. Photon p_{T};Photon p_{T} [GeV];Electron p_{T} [GeV];"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("photon.pt", "electron.pt"),
        ),
    )
)


MuonPhotonHistograms = cms.PSet(
    inputCollection = cms.vstring("muons","photons"),
    histograms = cms.VPSet (

        ###################################################################
        #
        cms.PSet (
            name = cms.string("muonPhotonDeltaPhi"),
            title = cms.string("Muon-photon Phi Difference;|#Delta(#phi)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs ( deltaPhi (muon, photon) )"),
        ),
        cms.PSet (
            name = cms.string("muonPhotonDeltaEta"),
            title = cms.string("Muon-photon Eta Difference;|#Delta(#eta)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs (muon.eta - photon.eta)"),
        ),
        cms.PSet (
            name = cms.string("muonPhotonDeltaR"),
            title = cms.string("Muon-photon #DeltaR;#DeltaR"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR (muon, photon)"),
        ),
    )
)


BeamspotHistograms = cms.PSet(
    inputCollection = cms.vstring("beamspots"),
    histograms = cms.VPSet (

        ###################################################################
        #
        cms.PSet (
            name = cms.string("beamspotX0_1000um"),
            title = cms.string("Beamspot x_{0};beamspot x_{0} [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*beamspot.x0"),
        ),
        cms.PSet (
            name = cms.string("beamspotY0_1000um"),
            title = cms.string("Beamspot y_{0};beamspot y_{0} [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*beamspot.y0"),
        ),
        cms.PSet (
            name = cms.string("beamspotY0_vs_beamspotX0_1000um"),
            title = cms.string("Beamspot y_{0} vs. beamspot y_{0};beamspot x_{0} [#mum];beamspot y_{0} [#mum]"),
            binsX = cms.untracked.vdouble(200, -1000, 1000),
            binsY = cms.untracked.vdouble(200, -1000, 1000),
            inputVariables = cms.vstring("10000*beamspot.x0","10000*beamspot.y0"),
        ),
        cms.PSet (
            name = cms.string("beamspotX0_10000um"),
            title = cms.string("Beamspot x_{0};beamspot x_{0} [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            inputVariables = cms.vstring("10000*beamspot.x0"),
        ),
        cms.PSet (
            name = cms.string("beamspotY0_10000um"),
            title = cms.string("Beamspot y_{0};beamspot y_{0} [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            inputVariables = cms.vstring("10000*beamspot.y0"),
        ),
        cms.PSet (
            name = cms.string("beamspotY0_vs_beamspotX0_10000um"),
            title = cms.string("Beamspot y_{0} vs. beamspot y_{0};beamspot x_{0} [#mum];beamspot y_{0} [#mum]"),
            binsX = cms.untracked.vdouble(200, -10000, 10000),
            binsY = cms.untracked.vdouble(200, -10000, 10000),
            inputVariables = cms.vstring("10000*beamspot.x0","10000*beamspot.y0"),
        ),
        cms.PSet (
            name = cms.string("beamspotV0"),
            title = cms.string("Beamspot v_{0};beamspot v_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*hypot(beamspot.x0, beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("beamspotV0Error"),
            title = cms.string("Beamspot #sigma(v_{0});beamspot #sigma(v_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("10000*hypot(beamspot.x0Error, beamspot.y0Error)"),
        ),
        cms.PSet (
            name = cms.string("beamspotVz"),
            title = cms.string("Beamspot v_{z};beamspot v_{z} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50000),
            inputVariables = cms.vstring("10000*beamspot.z0"),
        ),
    )
)


eventHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("numPV"),
            title = cms.string("Number of Primary Vertex; #PV"),
            binsX = cms.untracked.vdouble(75, 0, 75),
            inputVariables = cms.vstring("numPV"),
        ),
        cms.PSet (
            name = cms.string("numSoftMuons"),
            title = cms.string("Number of Soft Muons; # muon passing soft ID"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("numSoftMuons"),
        ),
        cms.PSet (
            name = cms.string("numTightMuons"),
            title = cms.string("Number of Tight Muons; # muon passing tight ID"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("numTightMuons"),
        ),
        cms.PSet (
            name = cms.string("numTruePV"),
            title = cms.string("Number of True PVs; #True PVs"),
            binsX = cms.untracked.vdouble(75, 0, 75),
            inputVariables = cms.vstring("numTruePV"),
        ),
        cms.PSet (
            name = cms.string("numPV_vs_numTruePV"),
            title = cms.string("Number of Primary Vertex; #True PVs; #PV"),
            binsX = cms.untracked.vdouble(75, 0, 75),
            binsY = cms.untracked.vdouble(75, 0, 75),
            inputVariables = cms.vstring("numTruePV", "numPV"),
        ),
        cms.PSet (
            name = cms.string("puScalingFactor"),
            title = cms.string("PU Scaling Factor; log(PU Scaling Factor)"),
            binsX = cms.untracked.vdouble(200, -4, 4),
            inputVariables = cms.vstring("log10(puScalingFactor)"),
        ),
        cms.PSet (
            name = cms.string("sumJetPt"),
            title = cms.string("Sum of Jet Transverse Momentum; #Sigma p_{T}_{jet}"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("sumJetPt"),
        ),
        cms.PSet (
            name = cms.string("tagMuonPt"),
            title = cms.string("Tag Muon p_{T}; Muon p_{T}"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("tagMuonPt"),
        ),
        cms.PSet (
            name = cms.string("tagMuonEta"),
            title = cms.string("Tag Muon #eta; Muon #eta"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            inputVariables = cms.vstring("tagMuonEta"),
        ),
        cms.PSet (
            name = cms.string("tagMuonPhi"),
            title = cms.string("Tag Muon #phi; Muon #phi"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            inputVariables = cms.vstring("tagMuonPhi"),
        ),
        cms.PSet (
            name = cms.string("tagMuonCharge"),
            title = cms.string("Tag Muon Charge; Muon Charge"),
            binsX = cms.untracked.vdouble(3, -1, 1),
            inputVariables = cms.vstring("tagMuonCharge"),
        ),
        cms.PSet (
            name = cms.string("tagMuonUnsmearedAbsD0"),
            title = cms.string("Unsmeared Muon d_{0};Unsmeared Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 2000),
            inputVariables = cms.vstring("10000*abs(tagMuonUnsmearedD0)"),
        ),
        cms.PSet (
            name = cms.string("leadingMuonPt"),
            title = cms.string("Muon p_{T}; Leading muon p_{T}"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("leadingMuonPt"),
        ),
        cms.PSet (
            name = cms.string("leadingMuonEta"),
            title = cms.string("Muon #eta; Leading muon #eta"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            inputVariables = cms.vstring("leadingMuonEta"),
        ),
        cms.PSet (
            name = cms.string("leadingMuonPhi"),
            title = cms.string("Muon #phi; Leading muon #phi"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            inputVariables = cms.vstring("leadingMuonPhi"),
        ),
        cms.PSet (
            name = cms.string("leadingMuonUnsmearedAbsD0"),
            title = cms.string("Unsmeared Muon d_{0};Leading muon unsmeared d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 2000),
            inputVariables = cms.vstring("10000*abs(leadingMuonUnsmearedD0)"),
        ),
        cms.PSet (
            name = cms.string("subleadingMuonPt"),
            title = cms.string("Muon p_{T}; Subleading muon p_{T}"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("subleadingMuonPt"),
        ),
        cms.PSet (
            name = cms.string("subleadingMuonEta"),
            title = cms.string("Muon #eta; Subleading muon #eta"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            inputVariables = cms.vstring("subleadingMuonEta"),
        ),
        cms.PSet (
            name = cms.string("subleadingMuonPhi"),
            title = cms.string("Muon #phi; Subleading muon #phi"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            inputVariables = cms.vstring("subleadingMuonPhi"),
        ),
        cms.PSet (
            name = cms.string("subleadingMuonUnsmearedAbsD0"),
            title = cms.string("Unsmeared Muon d_{0};Subleading muon unsmeared d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 2000),
            inputVariables = cms.vstring("10000*abs(subleadingMuonUnsmearedD0)"),
        ),
        cms.PSet (
            name = cms.string("triggerScaleFactor"),
            title = cms.string("Trigger Scale Factor; Trigger Scale Factor"),
            binsX = cms.untracked.vdouble(10, 0, 1),
            inputVariables = cms.vstring("triggerScaleFactor"),
        ),
        cms.PSet (
            name = cms.string("electronReco2016"),
            title = cms.string("Electron Reco SF; Electron Reco SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("electronReco2016"),
        ),
        cms.PSet (
            name = cms.string("electronID2016Tight"),
            title = cms.string("Electron ID SF; Electron ID SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("electronID2016Tight"),
        ),
        cms.PSet (
            name = cms.string("muonTracking2016GH"),
            title = cms.string("Muon Tracking SF; Muon Tracking SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("muonTracking2016GH"),
        ),
        cms.PSet (
            name = cms.string("muonID2016TightGH"),
            title = cms.string("Muon ID SF; Muon ID SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("muonID2016TightGH"),
        ),
        cms.PSet (
            name = cms.string("muonIso2016TightTightIDGH"),
            title = cms.string("Muon Iso SF; Muon Iso SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("muonIso2016TightTightIDGH"),
        ),
        cms.PSet (
            name = cms.string("electronID2017Tight"),
            title = cms.string("Electron ID SF; Electron ID SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("electronID2017Tight"),
        ),
        cms.PSet (
            name = cms.string("muonID2017Tight"),
            title = cms.string("Muon ID SF; Muon ID SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("muonID2017Tight"),
        ),
        cms.PSet (
            name = cms.string("muonIso2017TightTightID"),
            title = cms.string("Muon Iso SF; Muon Iso SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("muonIso2017TightTightID"),
        ),
        cms.PSet (
            name = cms.string("lifetimeWeight"),
            title = cms.string("Lifetime Scaling Factor; Lifetime Scaling Factor"),
            binsX = cms.untracked.vdouble(200, -4, 4),
            inputVariables = cms.vstring("log10(lifetimeWeight)"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_100um"),
            title = cms.string("Stop 0 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*cTau_1000006_0"),
            ),
        cms.PSet (
            name = cms.string("ctauStop1_100um"),
            title = cms.string("Stop 1 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*cTau_1000006_1"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_1000um"),
            title = cms.string("Stop 0 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*cTau_1000006_0"),
        ),
        cms.PSet (
            name = cms.string("ctauStop1_1000um"),
            title = cms.string("Stop 1 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*cTau_1000006_1"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_10000um"),
            title = cms.string("Stop 0 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("10000*cTau_1000006_0"),
        ),
        cms.PSet (
            name = cms.string("ctauStop1_10000um"),
            title = cms.string("Stop 1 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("10000*cTau_1000006_1"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_100000um"),
            title = cms.string("Stop 0 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100000),
            inputVariables = cms.vstring("10000*cTau_1000006_0"),
            ),
        cms.PSet (
            name = cms.string("ctauStop1_100000um"),
            title = cms.string("Stop 1 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100000),
            inputVariables = cms.vstring("10000*cTau_1000006_1"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_1000000um"),
            title = cms.string("Stop 0 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000000),
            inputVariables = cms.vstring("10000*cTau_1000006_0"),
        ),
        cms.PSet (
            name = cms.string("ctauStop1_1000000um"),
            title = cms.string("Stop 1 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000000),
            inputVariables = cms.vstring("10000*cTau_1000006_1"),
        ),
        cms.PSet (
            name = cms.string("HLT_CaloMET350_HBHECleaned"),
            title = cms.string("HLT_CaloMET350_HBHECleaned"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("HLT_CaloMET350_HBHECleaned"),
        ),
        cms.PSet (
            name = cms.string("HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight"),
            title = cms.string("HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight"),
        ),
        cms.PSet (
            name = cms.string("HLT_PFMET120_PFMHT120_IDTight"),
            title = cms.string("HLT_PFMET120_PFMHT120_IDTight"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("HLT_PFMET120_PFMHT120_IDTight"),
        ),
        cms.PSet (
            name = cms.string("HLT_PFMET200_HBHE_BeamHaloCleaned"),
            title = cms.string("HLT_PFMET200_HBHE_BeamHaloCleaned"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("HLT_PFMET200_HBHE_BeamHaloCleaned"),
        ),
        cms.PSet (
            name = cms.string("HLT_PFMET250_HBHECleaned"),
            title = cms.string("HLT_PFMET250_HBHECleaned"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("HLT_PFMET250_HBHECleaned"),
        ),
        cms.PSet (
            name = cms.string("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight"),
            title = cms.string("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight"),
        ),
        cms.PSet (
            name = cms.string("L1_Mu5_EG20"),
            title = cms.string("L1_Mu5_EG20"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_Mu5_EG20"),
        ),
        cms.PSet (
            name = cms.string("L1_Mu20_EG15"),
            title = cms.string("L1_Mu20_EG15"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_Mu20_EG15"),
        ),
        cms.PSet (
            name = cms.string("L1_Mu5_EG23"),
            title = cms.string("L1_Mu5_EG23"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_Mu5_EG23"),
        ),
        cms.PSet (
            name = cms.string("L1_Mu7_EG23"),
            title = cms.string("L1_Mu7_EG23"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_Mu7_EG23"),
        ),
        cms.PSet (
            name = cms.string("L1_Mu20_EG17"),
            title = cms.string("L1_Mu20_EG17"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_Mu20_EG17"),
        ),
        cms.PSet (
            name = cms.string("L1_Mu23_EG10"),
            title = cms.string("L1_Mu23_EG10"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_Mu23_EG10"),
        ),
        cms.PSet (
            name = cms.string("L1_DoubleMu_11_4"),
            title = cms.string("L1_DoubleMu_11_4"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_DoubleMu_11_4"),
        ),
        cms.PSet (
            name = cms.string("L1_DoubleMu_12_5"),
            title = cms.string("L1_DoubleMu_12_5"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_DoubleMu_12_5"),
        ),
        cms.PSet (
            name = cms.string("L1_DoubleMu_13_6"),
            title = cms.string("L1_DoubleMu_13_6"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_DoubleMu_13_6"),
        ),
        cms.PSet (
            name = cms.string("L1_DoubleMu_15_5"),
            title = cms.string("L1_DoubleMu_15_5"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_DoubleMu_15_5"),
        ),
        cms.PSet (
            name = cms.string("L1_DoubleMu_15_7"),
            title = cms.string("L1_DoubleMu_15_7"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_DoubleMu_15_7"),
        ),
        cms.PSet (
            name = cms.string("L1_SingleEG30"),
            title = cms.string("L1_SingleEG30"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_SingleEG30"),
        ),
        cms.PSet (
            name = cms.string("L1_SingleEG40"),
            title = cms.string("L1_SingleEG40"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_SingleEG40"),
        ),
        cms.PSet (
            name = cms.string("L1_SingleEG50"),
            title = cms.string("L1_SingleEG50"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_SingleEG50"),
        ),
        cms.PSet (
            name = cms.string("L1_SingleIsoEG22er"),
            title = cms.string("L1_SingleIsoEG22er"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_SingleIsoEG22er"),
        ),
        cms.PSet (
            name = cms.string("L1_SingleIsoEG24"),
            title = cms.string("L1_SingleIsoEG24"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_SingleIsoEG24"),
        ),
        cms.PSet (
            name = cms.string("L1_SingleIsoEG28"),
            title = cms.string("L1_SingleIsoEG28"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_SingleIsoEG28"),
        ),
        cms.PSet (
            name = cms.string("L1_SingleIsoEG38"),
            title = cms.string("L1_SingleIsoEG38"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_SingleIsoEG38"),
        ),
        cms.PSet (
            name = cms.string("L1_DoubleEG_15_10"),
            title = cms.string("L1_DoubleEG_15_10"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_DoubleEG_15_10"),
        ),
        cms.PSet (
            name = cms.string("L1_DoubleEG_18_17"),
            title = cms.string("L1_DoubleEG_18_17"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_DoubleEG_18_17"),
        ),
        cms.PSet (
            name = cms.string("L1_DoubleEG_25_12"),
            title = cms.string("L1_DoubleEG_25_12"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_DoubleEG_25_12"),
        ),
        cms.PSet (
            name = cms.string("L1_SingleJet200"),
            title = cms.string("L1_SingleJet200"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_SingleJet200"),
        ),
        cms.PSet (
            name = cms.string("L1_SingleTau100er"),
            title = cms.string("L1_SingleTau100er"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_SingleTau100er"),
        ),
        cms.PSet (
            name = cms.string("L1_SingleTau100er2p1"),
            title = cms.string("L1_SingleTau100er2p1"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("L1_SingleTau100er2p1"),
        ),
    )
)


CosmicMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("MuontimeAtIpInOut"),
            title = cms.string("Muon timeAtIpInOut; timeAtIpInOut"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("time.timeAtIpInOut"),
        ),
        cms.PSet (
            name = cms.string("MuontimeAtIpOutIn"),
            title = cms.string("Muon timeAtIpOutIn; timeAtIpOutIn"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("time.timeAtIpOutIn"),
        ),
        cms.PSet (
            name = cms.string("MuontimeAtIpInOut_vs_MuontimeAtIpOutIn"),
            title = cms.string("Muon timeAtIpInOut vs. Muon timeAtIpOutIn;timeAtIpOutIn;timeAtIpInOut"),
            binsX = cms.untracked.vdouble(100,-200,200),
            binsY = cms.untracked.vdouble(100,-200,200),
            inputVariables = cms.vstring("time.timeAtIpOutIn", "time.timeAtIpInOut"),
        ),
    )
)

eventMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables", "muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonPt_vs_tagMuonPt"),
            title = cms.string("Muon p_{T} vs tag Muon p_{T}; tag Muon p_{T} [GeV]; Muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("eventvariable.tagMuonPt, muon.pt"),
        ),
    )
)

DiMuonHistogramsExtra = cms.PSet(
    inputCollection = cms.vstring("muons","muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diMuonInvMassJPsiMassWindow"),
            title = cms.string("Di-muon Invariant Mass;M_{#mu#mu} [GeV]"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("invMass (muon, muon)"),
            ),
        cms.PSet (
            name = cms.string("diMuonInvMassJPsiMassWindow_100Bins"),
            title = cms.string("Di-muon Invariant Mass;M_{#mu#mu} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("invMass (muon, muon)"),
            ),
        cms.PSet (
            name = cms.string("diMuonInvMassJPsiMassWindow_200Bins"),
            title = cms.string("Di-muon Invariant Mass;M_{#mu#mu} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 10),
            inputVariables = cms.vstring("invMass (muon, muon)"),
            ),

    )
)

GenParticleHistograms = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("GenPdgId"),
            title = cms.string("Gen PdgId;|PDG ID|"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (pdgId)"),
            ),
        cms.PSet (
            name = cms.string("GenStatus"),
            title = cms.string("Gen Status;Status"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("status"),
            ),
        cms.PSet (
            name = cms.string("GenPt"),
            title = cms.string("Gen Transverse Momentum;Gen p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("GenPt_ext"),
            title = cms.string("Gen Transverse Momentum;Gen p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 3000),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("GenEta"),
            title = cms.string("Gen Eta;Gen #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("GenPhi"),
            title = cms.string("Gen Phi;Gen #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("GenMotherPdgId"),
            title = cms.string("Unique Gen Mother PdgId;Mother |PDG ID|"),
            binsX = cms.untracked.vdouble(600, 0, 600),
            inputVariables = cms.vstring("abs (uniqueMotherPdgId)"),
            ),
        )
    )

GenParticleD0Histograms = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("GenAbsD0_100000um"),
            title = cms.string("Gen |d_{0}|;Gen |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            inputVariables = cms.vstring("10000*abs("+hardInteractionMcparticleD0WRTBeamspot+")"),
        ),
    )
)
