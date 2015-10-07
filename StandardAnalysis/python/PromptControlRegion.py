import FWCore.ParameterSet.Config as cms
import copy

##########################################################################
######## Set up the prompt control region for the displaced SUSY analysis #########
##########################################################################
##########################################################################
PromptControlRegion = cms.PSet(
    name = cms.string("PromptControlRegion"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
        # ELECTRON ETA CUT
        cms.PSet (
            inputCollection = cms.vstring("candeles"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 1")
        ),
        # ELECTRON CRACK VETO
        cms.PSet (
            inputCollection = cms.vstring("candeles"),
            cutString = cms.string("isEBEEGap = 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("electron ECAL crack veto")
        ),
        # ELECTRON PT CUT
        cms.PSet (
            inputCollection = cms.vstring("candeles"),
            cutString = cms.string("pt > 25"),
            numberRequired = cms.string(">= 1")
        ),
        # ELECTRON ID
        cms.PSet (
            inputCollection = cms.vstring("candeles"),
            cutString = cms.string("                              \
              (isEB & \
              missingInnerHits <= 2 & \
              abs(deltaEtaSuperClusterTrackAtVtx) < 0.00926 & \
              abs(deltaPhiSuperClusterTrackAtVtx) < 0.0336 & \
              full5x5_sigmaIetaIeta < 0.0101 & \
              hadronicOverEm < 0.0597 & \
              abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.012 & \
              !vtxFitConversion)|\
              (isEE & \
              missingInnerHits <= 1 & \
              abs(deltaEtaSuperClusterTrackAtVtx) < 0.00724 & \
              abs(deltaPhiSuperClusterTrackAtVtx) < 0.0918 & \
              full5x5_sigmaIetaIeta < 0.0279 & \
              hadronicOverEm < 0.0615 & \
              abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.00999 & \
              !vtxFitConversion)"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("electron tight displaced ID")
        ),
        # ELECTRON ISOLATION
        cms.PSet (
            inputCollection = cms.vstring("candeles"),
            cutString = cms.string("        \
              ((pfIso_.sumChargedHadronPt    \
              + max(0.0,                    \
              pfIso_.sumNeutralHadronEt     \
              + pfIso_.sumPhotonEt          \
              - rho*AEff))        \
              /pt < 0.0646 && isEE)|\
              ((pfIso_.sumChargedHadronPt    \
              + max(0.0,                    \
              pfIso_.sumNeutralHadronEt     \
              + pfIso_.sumPhotonEt          \
              - rho*AEff))        \
              /pt < 0.0354 && isEB)"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("electron dRho isolation")
        ),
        # MUON ETA CUT
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("abs(eta) < 2.4"),
            numberRequired = cms.string(">= 1")
        ),
        # MUON PT CUT
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > 25"),
            numberRequired = cms.string(">= 1")
        ),
        # MUON ID
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("\
            isGlobalMuon & \
            isPFMuon & \
            globalTrack.hitPattern_.numberOfValidMuonHits > 0 & \
            numberOfMatchedStations > 1 & \
            innerTrack.hitPattern_.numberOfValidPixelHits > 0 & \
            innerTrack.hitPattern_.trackerLayersWithMeasurement > 5"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("muon tight displaced ID")
        ),
        # MUON ISOLATION
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("                \
              (pfIsolationR04_.sumChargedHadronPt   \
              + max(0.0,                            \
              pfIsolationR04_.sumNeutralHadronEt    \
              + pfIsolationR04_.sumPhotonEt         \
              - 0.5*pfIsolationR04_.sumPUPt))       \
              /pt < 0.12"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("muon dBeta isolation")
        ),
        # OPPOSITE SIGN E-MU PAIR
        cms.PSet (
            inputCollection = cms.vstring("candeles", "muons"),
            cutString = cms.string("candele.charge * muon.charge < 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("oppositely charged e-mu pair")
        ),
        # ELECTRON AND MUON ARE NOT OVERLAPPING
        cms.PSet (
            inputCollection = cms.vstring("candeles", "muons"),
            cutString = cms.string("deltaR(candele, muon) > 0.5"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
        ),
        # MUON DXY BLINDING
        cms.PSet (
            inputCollection = cms.vstring("muons","beamspots"),
            cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) < 0.01 "),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("muon dxy blinding cut")
        ),
        # ELECTRON DXY BLINDING
        cms.PSet (
            inputCollection = cms.vstring("candeles","beamspots"),
            cutString = cms.string("abs((-(candele.vx - beamspot.x0)*candele.py + (candele.vy - beamspot.y0)*candele.px)/candele.pt) < 0.01 "),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("electron dxy blinding cut")
        ),
    )
)
