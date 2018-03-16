import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.BackgroundStudies.CutDefinitions import *

##########################################################################
#Set up single lepton + 2 jet skims for the BBbar + lepton control regions
##########################################################################

##########################################################################
#Selections without triggers

QCDElectronSkim = cms.PSet(
    name = cms.string("QCDElectronSkim"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selections
QCDElectronSkim.cuts.extend(atLeastOne_jet_basic_selection_cuts)
QCDElectronSkim.cuts.extend(atLeastOne_bjet_basic_selection_cuts)
QCDElectronSkim.cuts.append(jet_btag_mwp_cut)
### at least one good electron
QCDElectronSkim.cuts.append(electron_eta_cut)
QCDElectronSkim.cuts.append(electron_gap_veto)
QCDElectronSkim.cuts.append(electron_pt_25_cut)
#electron id cut has low efficiency? so keep out of skim for now


QCDMuonSkim = cms.PSet(
    name = cms.string("QCDMuonSkim"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selections
QCDMuonSkim.cuts.extend(atLeastOne_jet_basic_selection_cuts)
QCDMuonSkim.cuts.extend(atLeastOne_bjet_basic_selection_cuts)
QCDMuonSkim.cuts.append(jet_btag_mwp_cut)
### at least one good muon
QCDMuonSkim.cuts.append(muon_eta_cut)
QCDMuonSkim.cuts.append(muon_pt_25_cut)
QCDMuonSkim.cuts.append(muon_global_cut)
QCDMuonSkim.cuts.append(muon_id_cut)

