import FWCore.ParameterSet.Config as cms
import copy




##########################################################################
######## Set up the preselection for the displaced SUSY analysis #########
##########################################################################

Preselection = cms.PSet(
    name = cms.string("Preselection"),
#    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
#        # EVENT CLEANING
#        cms.PSet (
#            inputCollection = cms.vstring("events"),
#            cutString = cms.string("FilterOutScraping > 0"),
#            numberRequired = cms.string(">= 1")
#        ),
#        # EVENT HAS GOOD PV
        cms.PSet (
            inputCollection = cms.vstring("primaryvertexs"),
            cutString = cms.string("ndof > 4 & abs(z) < 15 & rho < 2"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string(">= 1 good primary vertex")
        ),
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
            cutString = cms.string("pt > 25"),
            numberRequired = cms.string(">= 1")
        ),
        # ELECTRON ID
#        cms.PSet (
#            inputCollection = cms.vstring("electrons"),
#            cutString = cms.string("                              \
#              (pt > 7 && pt < 10                                  \
#                && ((abs (scEta) < 0.8 && mvaNonTrigV0 > 0.47)    \
#                || (abs (scEta) >= 0.8 && abs (scEta) < 1.479 && mvaNonTrigV0 > 0.004) \
#                || (abs (scEta) >= 1.479 && abs (scEta) < 2.5 && mvaNonTrigV0 > 0.295))) \
#           || (pt >= 10                                           \
#                && ((abs (scEta) < 0.8 && mvaNonTrigV0 > -0.34)   \
#                || (abs (scEta) >= 0.8 && abs (scEta) < 1.479 && mvaNonTrigV0 > -0.65) \
#                || (abs (scEta) >= 1.479 && abs (scEta) < 2.5 && mvaNonTrigV0 > 0.60)))  \
#           "),
#            numberRequired = cms.string(">= 1"),
#            alias = cms.string("electron ID")
#        ),
        # PHOTON CONVERSION VETO
#        cms.PSet (
#            inputCollection = cms.vstring("electrons"),
#            cutString = cms.string("passConversionVeto > 0 && numberOfLostHits = 0"),
#            numberRequired = cms.string(">= 1"),
#            alias = cms.string("electron conversion rejection")
#        ),
#        # ELECTRON ISOLATION
#        cms.PSet (
#            inputCollection = cms.vstring("electrons"),
#            cutString = cms.string("((chargedHadronIsoDR03 + max (0.0, neutralHadronIsoDR03 + photonIsoDR03 - AEffDr03 * rhoPrime)) / pt) < 0.1"),
#            numberRequired = cms.string(">= 1"),
#            alias = cms.string("electron isolation")
#        ),
        # MUON ETA CUT
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("abs(eta) < 2.5"),
            numberRequired = cms.string(">= 1")
        ),
        # MUON PT CUT
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > 25"),
            numberRequired = cms.string(">= 1")
        ),
        # MUON ID
#        cms.PSet (
#            inputCollection = cms.vstring("muons"),
#            cutString = cms.string("               \
#               isGlobalMuon                        \
#            && isPFMuon                            \
#            && (normChi2 < 10.0)             \
#            && (numberOfValidMuonHits > 0)         \
#            && (numberOfMatchedStations > 1)       \
#            && (numberOfValidPixelHits > 0)        \
#            && (numberOfLayersWithMeasurement > 5) \
#            "),
#            numberRequired = cms.string(">= 1"),
#            alias = cms.string("muon ID")
#        ),
#        # MUON ISOLATION
#        cms.PSet (
#            inputCollection = cms.vstring("muons"),
#            cutString = cms.string("((pfIsoR04SumChargedHadronPt + max (0.0, pfIsoR04SumNeutralHadronEt + pfIsoR04SumPhotonEt - 0.5 * pfIsoR04SumPUPt)) / pt) < 0.12"),
#            numberRequired = cms.string(">= 1"),
#            alias = cms.string("muon isolation")
#        ),
        # VETO EVENTS WITH EXTRA ELECTRON
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("== 1"),
            alias = cms.string("extra electron veto")
        ),
        # VETO EVENTS WITH EXTRA MUON
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("== 1"),
            alias = cms.string("extra muon veto")
        ),
        # OPPOSITE SIGN E-MU PAIR
        cms.PSet (
            inputCollection = cms.vstring("electrons", "muons"),
            cutString = cms.string("electron.charge * muon.charge < 0"),
            numberRequired = cms.string("== 1")
        ),
        # ELECTRON AND MUON ARE NOT OVERLAPPING
        cms.PSet (
            inputCollection = cms.vstring("electrons", "muons"),
            cutString = cms.string("deltaR(electron, muon) > 0.5"),
            numberRequired = cms.string("== 1")
        ),
        #########START OF ADDITIONAL CUTS TO REQUIRE LEPTON IS NOT IN A JET
#        # ONLY CONSIDER 30 GEV JETS
#        cms.PSet (
#            inputCollection = cms.vstring("jets"),
#            cutString = cms.string("pt > 10"),
#            numberRequired = cms.string(">= 0")
#        ),
#        # ELECTRON NOT OVERLAPPING WITH JET
#        cms.PSet (
#            inputCollection = cms.vstring("electrons", "jets"),
#            cutString = cms.string("deltaR(electron, jet) < 0.5"),
#            numberRequired = cms.string("== 0"),
#            isVeto = cms.bool(True),
#            alias = cms.string("electron near jet veto"),
#        ),
#        # MUON NOT OVERLAPPING WITH JET
#        cms.PSet (
#            inputCollection = cms.vstring("muons", "jets"),
#            cutString = cms.string("deltaR(muon, jet) < 0.5"),
#            numberRequired = cms.string("== 0"),
#            isVeto = cms.bool(True),
#            alias = cms.string("muon near jet veto"),
#        ),
        ########### END OF ADDITIONAL CUTS TO REQUIRE LEPTON IS NOT IN A JET

#        # RESTRICT ELECTRONS TO RECONSTRUCTION ACCEPTANCE
#        cms.PSet (
#            inputCollection = cms.vstring("electrons"),
#            cutString = cms.string("abs(correctedD0) < 2"),
#            numberRequired = cms.string("== 1")
#        ),
#        # RESTRICT MUONS TO TRIGGER ACCEPTANCE
#        cms.PSet (
#            inputCollection = cms.vstring("muons"),
#            cutString = cms.string("abs(correctedD0) < 2"),
#            numberRequired = cms.string("== 1")
#        ),
    )
)

##########################################################################




