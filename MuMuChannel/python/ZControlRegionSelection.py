import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

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
### at least two good muons
ZControlRegion.cuts.append(muon_eta_cut)
ZControlRegion.cuts.append(muon_pt_40_cut)
ZControlRegion.cuts.append(muon_global_cut)
ZControlRegion.cuts.append(muon_id_cut)
ZControlRegion.cuts.append(muon_iso_cut)
### invMass in Z range
ZControlRegion.cuts.append(diMuon_invMass_below101_cut)
ZControlRegion.cuts.append(diMuon_invMass_above81_cut)
