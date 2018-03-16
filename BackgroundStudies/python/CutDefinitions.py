import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.CutDefinitions import *

##########################################################################

# BEGIN JET - B-JET CUTS

jet_bjet_deltaPhi_cut = cms.PSet (
    inputCollection = cms.vstring("jets","bjets"),
    cutString = cms.string("abs(deltaPhi(jet,bjet)) > 2.5"),
    numberRequired = cms.string(">= 1"),
)

##########################################################################

# BEGIN MUON - JET CUTS

muon_jet_deltaR_cut = cms.PSet (
    inputCollection = cms.vstring("muons","jets"),
    cutString = cms.string("deltaR(muon,jet) < 0.5"),
    numberRequired = cms.string(">= 1"),
)

##########################################################################

# BEGIN ELECTRON - JET CUTS

electron_jet_deltaR_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","jets"),
    cutString = cms.string("deltaR(electron,jet) < 0.5"),
    numberRequired = cms.string(">= 1"),
)

##########################################################################

FilterOutScraping_cut = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("FilterOutScraping > 0"),
    numberRequired = cms.string(">= 1")
    )

##########################################################################

atLeastOne_goodPV_cut = cms.PSet (
    inputCollection = cms.string("primaryvertexs"),
    cutString = cms.string("isGood > 0"),
    numberRequired = cms.string(">= 1")
    )
