import FWCore.ParameterSet.Config as cms
import copy

##########################################################################
######## Set up the preselection for the displaced SUSY analysis #########
##########################################################################

PreselectionEMu50ns = cms.PSet(
    name = cms.string("PreselectionEMu50ns"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
        # ELECTRON ETA CUT
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("abs(eta) < 2.5"),
            numberRequired = cms.string(">= 1")
        ),
        # ELECTRON CRACK VETO
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("isEBEEGap = 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("electron ECAL crack veto")
        ),
        # ELECTRON PT CUT
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > 40"),
            numberRequired = cms.string(">= 1")
        ),
        # ELECTRON ID
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("                              \
              (isEB & \
              gsfTrack.numberOfLostHits <= 2 & \
              abs(deltaEtaSuperClusterTrackAtVtx) < 0.0095 & \
              abs(deltaPhiSuperClusterTrackAtVtx) < 0.0291 & \
              full5x5_sigmaIetaIeta < 0.0101 & \
              hadronicOverEm < 0.0372 & \
              abs(1/et - 1/pt) < 0.0174)|\
              (isEE & \
              gsfTrack.numberOfLostHits <= 1 & \
              abs(deltaEtaSuperClusterTrackAtVtx) < 0.00762 & \
              abs(deltaPhiSuperClusterTrackAtVtx) < 0.0439 & \
              full5x5_sigmaIetaIeta < 0.0287 & \
              hadronicOverEm < 0.0544 & \
              abs(1/et - 1/pt) < 0.01)"),          
            numberRequired = cms.string(">= 1"),
            alias = cms.string("electron cut-based ID")
        ),
        # ELECTRON ISOLATION
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("        \
              (pfIso_.sumChargedHadronPt    \
              + max(0.0,                    \
              pfIso_.sumNeutralHadronEt     \
              + pfIso_.sumPhotonEt          \
              - 0.5*pfIso_.sumPUPt))        \
              /pt < 0.10"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("electron dBeta isolation")
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
            cutString = cms.string("pt > 40"),
            numberRequired = cms.string(">= 1")
        ),
        # MUON ID
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("isMediumMuon"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("muon medium ID")
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
            inputCollection = cms.vstring("electrons", "muons"),
            cutString = cms.string("electron.charge * muon.charge < 0"),
            numberRequired = cms.string(">= 1")
        ),
        # ELECTRON AND MUON ARE NOT OVERLAPPING
        cms.PSet (
            inputCollection = cms.vstring("electrons", "muons"),
            cutString = cms.string("deltaR(electron, muon) > 0.5"),
            numberRequired = cms.string(">= 1")
        ),
    )
)

##########################################################################




