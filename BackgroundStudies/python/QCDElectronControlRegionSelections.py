import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.BackgroundStudies.CutDefinitions import *

##############################################################
##### EVENT SELECTIONS FOR OUR QCD B-BBAR CONTROL REGIONS ####
##############################################################

##############################################################
################  basic HF + ele selection    ################
##############################################################

QCDElectronControlRegion = cms.PSet(
    name = cms.string("QCDElectronControlRegion"),
    triggers = cms.vstring("HLT_Ele27_WPTight_Gsf_v"),
    cuts = cms.VPSet ()
)
QCDElectronControlRegion.cuts.append(atLeastOne_jet_eta_cut)
QCDElectronControlRegion.cuts.append(atLeastOne_jet_pt_30_cut)
QCDElectronControlRegion.cuts.append(atLeastOne_jet_id_cut)
QCDElectronControlRegion.cuts.append(veto_3orMore_jets)

QCDElectronControlRegion.cuts.append(atLeastOne_bjet_eta_cut)
QCDElectronControlRegion.cuts.append(atLeastOne_bjet_pt_30_cut)
QCDElectronControlRegion.cuts.append(atLeastOne_bjet_id_cut)
QCDElectronControlRegion.cuts.append(jet_btag_mwp_cut)
QCDElectronControlRegion.cuts.append(veto_3orMore_bjets)

QCDElectronControlRegion.cuts.append(electron_eta_cut)
QCDElectronControlRegion.cuts.append(electron_pt_42_cut)
QCDElectronControlRegion.cuts.append(electron_gap_veto)
QCDElectronControlRegion.cuts.append(electron_id_cut)
QCDElectronControlRegion.cuts.append(electron_num_exactly_1_cut)

QCDElectronControlRegion.cuts.append(jet_bjet_deltaPhi_cut)
QCDElectronControlRegion.cuts.append(electron_jet_deltaR_cut)

