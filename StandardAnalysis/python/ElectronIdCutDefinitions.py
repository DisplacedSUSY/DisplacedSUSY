import FWCore.ParameterSet.Config as cms
import copy
import string
import os

from OSUT3Analysis.Configuration.cutUtilities import *

##########################################################################################
#USE THIS CONFIG ONLY FOR ELECTRON TIGHT ID TESTS! 
##########################################################################################

#barrel or endcap
electron_isEB_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("isEB"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons in the barrel (|eta supercluster| <= 1.479)")
    )

electron_isEE_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("isEE"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons in the endcaps (|eta supercluster| < 1.479)")
    )

##########################################################################################
#sigmaIetaIeta
electron_sigmaIetaIetaEB_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("full5x5_sigmaIetaIeta < 0.00998"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with full5x5_sigmaIetaIeta < 0.00998")
    )
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_sigmaIetaIetaEB_cut.cutString = "full5x5_sigmaIetaIeta < 0.0104"
    electron_sigmaIetaIetaEB_cut.alias = ">= 1 electrons with full5x5_sigmaIetaIeta < 0.0104"

electron_sigmaIetaIetaEE_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("full5x5_sigmaIetaIeta < 0.0292"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with full5x5_sigmaIetaIeta < 0.0292")
    )
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_sigmaIetaIetaEE_cut.cutString = "full5x5_sigmaIetaIeta < 0.0165"
    electron_sigmaIetaIetaEE_cut.alias = ">= 1 electrons with full5x5_sigmaIetaIeta < 0.0165"

##########################################################################################
#delta phi supercluster track at vtx
electron_deltaPhiSuperClusterEB_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(deltaPhiSuperClusterTrackAtVtx) < 0.0816"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with abs(deltaPhiSuperClusterTrackAtVtx) < 0.0816")
    )
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_deltaPhiSuperClusterEB_cut.cutString = "abs(deltaPhiSuperClusterTrackAtVtx) < 0.0499"
    electron_deltaPhiSuperClusterEB_cut.alias = ">= 1 electrons with abs(deltaPhiSuperClusterTrackAtVtx) < 0.0499"

electron_deltaPhiSuperClusterEE_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(deltaPhiSuperClusterTrackAtVtx) < 0.0394"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with abs(deltaPhiSuperClusterTrackAtVtx) < 0.0394")
    )
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_deltaPhiSuperClusterEE_cut.cutString = "abs(deltaPhiSuperClusterTrackAtVtx) < 0.0499"
    electron_deltaPhiSuperClusterEE_cut.alias = ">= 1 electrons with abs(deltaPhiSuperClusterTrackAtVtx) < 0.0499"

##########################################################################################
#delta eta super cluster track at vtx
electron_deltaEtaSuperClusterEB_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(deltaEtaSuperClusterTrackAtVtx) < 0.00308"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with abs(deltaEtaSuperClusterTrackAtVtx) < 0.00308")
    )
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_deltaEtaSuperClusterEB_cut.cutString = "abs(deltaEtaSuperClusterTrackAtVtx) < 0.00353"
    electron_deltaEtaSuperClusterEB_cut.alias = ">= 1 electrons with abs(deltaEtaSuperClusterTrackAtVtx) < 0.00353"

electron_deltaEtaSuperClusterEE_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(deltaEtaSuperClusterTrackAtVtx) < 0.00605"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with abs(deltaEtaSuperClusterTrackAtVtx) < 0.00605")
    )
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_deltaEtaSuperClusterEE_cut.cutString = "abs(deltaEtaSuperClusterTrackAtVtx) < 0.00567"
    electron_deltaEtaSuperClusterEE_cut.alias = ">= 1 electrons with abs(deltaEtaSuperClusterTrackAtVtx) < 0.00567"

##########################################################################################
#hadronicOverEm
electron_hadronicOverEmEB_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("hadronicOverEm < 0.0414"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with hadronicOverEm < 0.0414")
    )
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_hadronicOverEmEB_cut.cutString = "hadronicOverEm < 0.026 + 1.12/ecalEnergy + 0.0368*rho/ecalEnergy"
    electron_hadronicOverEmEB_cut.alias = ">= 1 electrons with hadronicOverEm < 0.026 + 1.12/ecalEnergy + 0.0368*rho/ecalEnergy"
    

electron_hadronicOverEmEE_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("hadronicOverEm < 0.0641"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with hadronicOverEm < 0.0641")
    )
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_hadronicOverEmEE_cut.cutString = "hadronicOverEm < 0.026 + 0.5/ecalEnergy + 0.201*rho/ecalEnergy"
    electron_hadronicOverEmEE_cut.alias = ">= 1 electrons with hadronicOverEm < 0.026 + 0.5/ecalEnergy + 0.201*rho/ecalEnergy"

##########################################################################################
#abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy)
#same for EB and EE for 2016
electron_abs_1overE_1overP_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.0129"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.0129")
    )

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_"):
    electron_abs_1overE_1overP_EB_cut = cms.PSet(
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.0278"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string(">= 1 electrons with abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.0278")
        )
    electron_abs_1overE_1overP_EE_cut = cms.PSet(
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.0158"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string(">= 1 electrons with abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.0158")
        )

##########################################################################################
#missingInnerHits
#same for EB and EE
electron_missingInnerHits_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("missingInnerHits <= 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with missingInnerHits <= 1")
    )

##########################################################################################
#passConversionVeto
#same for EB and EE
electron_passConversionVeto_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("passConversionVeto"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons that pass conversion veto")
    )
