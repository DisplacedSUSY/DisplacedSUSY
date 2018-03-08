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
QCDElectronSkim.cuts.append(one_jet_eta_cut)
QCDElectronSkim.cuts.append(one_jet_pt_30_cut)
QCDElectronSkim.cuts.append(one_jet_id_cut)
QCDElectronSkim.cuts.append(bjet_eta_cut)
QCDElectronSkim.cuts.append(bjet_pt_30_cut)
QCDElectronSkim.cuts.append(bjet_id_cut)
QCDElectronSkim.cuts.append(bjet_csvm_cut)
### at least one good electron
QCDElectronSkim.cuts.append(electron_eta_cut)
QCDElectronSkim.cuts.append(electron_gap_veto)
QCDElectronSkim.cuts.append(electron_pt_25_cut)



QCDMuonSkim = cms.PSet(
    name = cms.string("QCDMuonSkim"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selections
QCDMuonSkim.cuts.append(one_jet_eta_cut)
QCDMuonSkim.cuts.append(one_jet_pt_30_cut)
QCDMuonSkim.cuts.append(one_jet_id_cut)
QCDMuonSkim.cuts.append(bjet_eta_cut)
QCDMuonSkim.cuts.append(bjet_pt_30_cut)
QCDMuonSkim.cuts.append(bjet_id_cut)
QCDMuonSkim.cuts.append(bjet_csvm_cut)
### at least one good muon
QCDMuonSkim.cuts.append(muon_eta_cut)
QCDMuonSkim.cuts.append(muon_pt_25_cut)
QCDMuonSkim.cuts.append(muon_global_cut)
QCDMuonSkim.cuts.append(muon_id_cut)

