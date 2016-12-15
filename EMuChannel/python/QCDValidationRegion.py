import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

##########################################################################
### Set up the QCD validation region
##########################################################################

# Prompt Control Region with lepton isolation inverted

##########################################################################
#Selections without triggers

QCDValidationRegion = cms.PSet(
    name = cms.string("QCDValidationRegion"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
QCDValidationRegion.cuts.append(jet_eta_cut)
QCDValidationRegion.cuts.append(jet_pt_30_cut)
QCDValidationRegion.cuts.append(jet_id_cut)
### at least one good electron
QCDValidationRegion.cuts.append(electron_eta_cut)
QCDValidationRegion.cuts.append(electron_gap_veto)
QCDValidationRegion.cuts.append(electron_pt_42_cut)
QCDValidationRegion.cuts.append(electron_id_cut)
QCDValidationRegion.cuts.append(electron_veto_antiiso_cut)
### at least one good muon
QCDValidationRegion.cuts.append(muon_eta_cut)
QCDValidationRegion.cuts.append(muon_pt_40_cut)
QCDValidationRegion.cuts.append(muon_global_cut)
QCDValidationRegion.cuts.append(muon_id_cut)
QCDValidationRegion.cuts.append(muon_loose_antiiso_cut)
### require prompt leptons
QCDValidationRegion.cuts.append(electron_d0_lt100_cut)
QCDValidationRegion.cuts.append(muon_d0_lt100_cut)

