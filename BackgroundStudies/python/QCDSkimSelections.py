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
QCDElectronSkim.cuts.append(two_jets_eta_cut)
QCDElectronSkim.cuts.append(two_jets_pt_30_cut)
QCDElectronSkim.cuts.append(two_jets_id_cut)
### at least one good electron
QCDElectronSkim.cuts.append(electron_eta_cut)
QCDElectronSkim.cuts.append(electron_gap_veto)
QCDElectronSkim.cuts.append(electron_pt_25_cut)
#QCDElectronSkim.cuts.append(electron_id_cut)  # i'm suspicious of the low efficiency for this cut... JA 11/18



QCDMuonSkim = cms.PSet(
    name = cms.string("QCDMuonSkim"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selections
QCDMuonSkim.cuts.append(two_jets_eta_cut)
QCDMuonSkim.cuts.append(two_jets_pt_30_cut)
QCDMuonSkim.cuts.append(two_jets_id_cut)
### at least one good muon
QCDMuonSkim.cuts.append(muon_eta_cut)
QCDMuonSkim.cuts.append(muon_pt_25_cut)
QCDMuonSkim.cuts.append(muon_global_cut)
QCDMuonSkim.cuts.append(muon_id_cut)

