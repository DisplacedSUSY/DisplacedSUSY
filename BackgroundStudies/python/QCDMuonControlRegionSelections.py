import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.BackgroundStudies.CutDefinitions import *

##############################################################
##### EVENT SELECTIONS FOR OUR QCD B-BBAR CONTROL REGIONS ####
##############################################################

##############################################################
################  basic HF + muon selection   ################
##############################################################

QCDMuonControlRegion = cms.PSet(
    name = cms.string("QCDMuonControlRegion"),
    triggers = cms.vstring("HLT_Mu50_v", "HLT_TkMu50_v"),
    cuts = cms.VPSet ()
)
QCDMuonControlRegion.cuts.append(atLeastOne_jet_eta_cut)
QCDMuonControlRegion.cuts.append(atLeastOne_jet_pt_30_cut)
QCDMuonControlRegion.cuts.append(atLeastOne_jet_id_cut)
QCDMuonControlRegion.cuts.append(veto_3orMore_jets)

QCDMuonControlRegion.cuts.append(atLeastOne_bjet_eta_cut)
QCDMuonControlRegion.cuts.append(atLeastOne_bjet_pt_30_cut)
QCDMuonControlRegion.cuts.append(atLeastOne_bjet_id_cut)
QCDMuonControlRegion.cuts.append(jet_btag_mwp_cut)
QCDMuonControlRegion.cuts.append(veto_3orMore_bjets)

QCDMuonControlRegion.cuts.append(muon_eta_cut)
# raise muon pt to be in plateau of single muon trig eff curve
QCDMuonControlRegion.cuts.append(muon_pt_55_cut)
QCDMuonControlRegion.cuts.append(muon_global_cut)
QCDMuonControlRegion.cuts.append(muon_id_cut)
QCDMuonControlRegion.cuts.append(muon_num_exactly_1_cut)

QCDMuonControlRegion.cuts.append(jet_bjet_deltaPhi_cut)
QCDMuonControlRegion.cuts.append(muon_jet_deltaR_cut)

prompt_muon_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 1")
    )
displaced_muon_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) > 200 & 10000*abs(d0) < 1000"),
    numberRequired = cms.string(">= 1")
    )
very_displaced_muon_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) > 1000"),
    numberRequired = cms.string(">= 1")
    )

QCDMuonControlRegionPrompt = cms.PSet(
    name = cms.string("QCDMuonControlRegionPrompt"),
    triggers = cms.vstring(),
    cuts = copy.deepcopy(QCDMuonControlRegion.cuts)
)
QCDMuonControlRegionPrompt.cuts.append(prompt_muon_cut)

QCDMuonControlRegionDisplaced = cms.PSet(
    name = cms.string("QCDMuonControlRegionDisplaced"),
    triggers = cms.vstring(),
    cuts = copy.deepcopy(QCDMuonControlRegion.cuts)
)
QCDMuonControlRegionDisplaced.cuts.append(displaced_muon_cut)

QCDMuonControlRegionVeryDisplaced = cms.PSet(
    name = cms.string("QCDMuonControlRegionVeryDisplaced"),
    triggers = cms.vstring(),
    cuts = copy.deepcopy(QCDMuonControlRegion.cuts)
)
QCDMuonControlRegionVeryDisplaced.cuts.append(very_displaced_muon_cut)
