import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EEChannel.CutDefinitions import *

##########################################################################
###### Set up the Z control region for the displaced SUSY analysis #######
##########################################################################

##########################################################################
#Selections without triggers

ZControlRegion = cms.PSet(
    name = cms.string("ZControlRegion"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
ZControlRegion.cuts.append(jet_eta_cut)
ZControlRegion.cuts.append(jet_pt_30_cut)
ZControlRegion.cuts.append(jet_id_cut)
### at least two good electrons
ZControlRegion.cuts.append(electron_eta_cut)
ZControlRegion.cuts.append(electron_gap_veto)
ZControlRegion.cuts.append(electron_pt_42_cut)
ZControlRegion.cuts.append(electron_id_cut)
ZControlRegion.cuts.append(electron_iso_cut)
### invMass in Z range
ZControlRegion.cuts.append(diElectron_invMass_below101_cut)
ZControlRegion.cuts.append(diElectron_invMass_above81_cut)
