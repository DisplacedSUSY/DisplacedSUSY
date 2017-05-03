import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.CutDefinitions import *
from DisplacedSUSY.BackgroundStudies.CutDefinitions import *

##############################################################
##### EVENT SELECTIONS FOR OUR QCD B-BBAR CONTROL REGIONS ####
##############################################################

##############################################################
################  basic HF + muon selection   ################
##############################################################

QCDMuonControlRegion = cms.PSet(
    name = cms.string("QCDMuonControlRegion"),
    triggers = cms.vstring(),
#    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v"),
    cuts = cms.VPSet ()
)
QCDMuonControlRegion.cuts.append(one_jet_eta_cut)
QCDMuonControlRegion.cuts.append(one_jet_pt_30_cut)
QCDMuonControlRegion.cuts.append(one_jet_id_cut)
QCDMuonControlRegion.cuts.append(extra_jet_veto)

QCDMuonControlRegion.cuts.append(bjet_eta_cut)
QCDMuonControlRegion.cuts.append(bjet_pt_30_cut)
QCDMuonControlRegion.cuts.append(bjet_id_cut)
QCDMuonControlRegion.cuts.append(bjet_csvm_cut)
QCDMuonControlRegion.cuts.append(extra_bjet_veto)

QCDMuonControlRegion.cuts.append(muon_eta_cut)
#QCDMuonControlRegion.cuts.append(muon_pt_40_cut)
# raise muon pt to get above single muon trigger threshold
QCDMuonControlRegion.cuts.append(muon_pt_50_cut)
QCDMuonControlRegion.cuts.append(muon_global_cut)
QCDMuonControlRegion.cuts.append(muon_id_cut)
QCDMuonControlRegion.cuts.append(extra_muon_veto)

QCDMuonControlRegion.cuts.append(jet_bjet_deltaPhi_cut)
QCDMuonControlRegion.cuts.append(muon_jet_deltaR_cut)
