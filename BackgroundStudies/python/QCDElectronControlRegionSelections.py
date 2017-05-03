import FWCore.ParameterSet.Config as cms
import copy
import string

from DisplacedSUSY.StandardAnalysis.CutDefinitions import *
from DisplacedSUSY.BackgroundStudies.CutDefinitions import *

##############################################################
##### EVENT SELECTIONS FOR OUR QCD B-BBAR CONTROL REGIONS ####
##############################################################

##############################################################
################  basic HF + ele selection    ################
##############################################################

QCDElectronControlRegion = cms.PSet(
    name = cms.string("QCDElectronControlRegion"),
    triggers = cms.vstring(),
#    triggers = cms.vstring("HLT_Ele27_WPLoose_Gsf_v"),
    cuts = cms.VPSet ()
)
QCDElectronControlRegion.cuts.append(one_jet_eta_cut)
QCDElectronControlRegion.cuts.append(one_jet_pt_30_cut)
QCDElectronControlRegion.cuts.append(one_jet_id_cut)
QCDElectronControlRegion.cuts.append(extra_jet_veto)

QCDElectronControlRegion.cuts.append(bjet_eta_cut)
QCDElectronControlRegion.cuts.append(bjet_pt_30_cut)
QCDElectronControlRegion.cuts.append(bjet_id_cut)
QCDElectronControlRegion.cuts.append(bjet_csvm_cut)
QCDElectronControlRegion.cuts.append(extra_bjet_veto)

QCDElectronControlRegion.cuts.append(electron_eta_cut)
#QCDElectronControlRegion.cuts.append(electron_pt_42_cut)
# raise electron pt to get above single electron trigger threshold
QCDElectronControlRegion.cuts.append(electron_pt_100_cut)
QCDElectronControlRegion.cuts.append(electron_gap_veto)
QCDElectronControlRegion.cuts.append(electron_id_cut)
QCDElectronControlRegion.cuts.append(extra_electron_veto)

QCDElectronControlRegion.cuts.append(jet_bjet_deltaPhi_cut)
QCDElectronControlRegion.cuts.append(electron_jet_deltaR_cut)


