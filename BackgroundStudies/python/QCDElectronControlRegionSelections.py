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
    triggers = triggersSingleElectron,
    cuts = cms.VPSet ()
)
QCDElectronControlRegion.cuts.extend(atLeastOne_jet_basic_selection_cuts)
QCDElectronControlRegion.cuts.append(veto_3orMore_jets)

QCDElectronControlRegion.cuts.extend(atLeastOne_bjet_basic_selection_cuts)
QCDElectronControlRegion.cuts.append(jet_btag_mwp_cut)
QCDElectronControlRegion.cuts.append(veto_3orMore_bjets)

QCDElectronControlRegion.cuts.append(electron_eta_cut)
QCDElectronControlRegion.cuts.append(electron_pt_42_cut)
QCDElectronControlRegion.cuts.append(electron_gap_veto)
QCDElectronControlRegion.cuts.append(electron_id_cut) #electron vid normally includes isolation, but we take it out in customize.py
QCDElectronControlRegion.cuts.append(electron_iso_cut)
QCDElectronControlRegion.cuts.append(electron_num_exactly_1_cut)

QCDElectronControlRegion.cuts.append(jet_bjet_deltaPhi_cut)
QCDElectronControlRegion.cuts.append(electron_jet_deltaR_cut)

