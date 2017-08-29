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
ZControlRegion.cuts.append(electronjet_deltaR_veto)
ZControlRegion.cuts.append(electron_2electron_cut)
### invMass in Z range
ZControlRegion.cuts.append(diElectron_invMass_Z_cut)
### we don't take kindly to b-jets around these parts
#ZControlRegion.cuts.append(jet_csvm_veto)

fiducial_phi_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(abs(phi)-3.14159/2) > 0.05"),
    numberRequired = cms.string(">= 2")
    )
ZControlRegion.cuts.append(fiducial_phi_cut)







prompt_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 1")
    )
displaced_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) > 200 & 10000*abs(d0) < 1000"),
    numberRequired = cms.string(">= 1")
    )
very_displaced_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) > 1000"),
    numberRequired = cms.string(">= 1")
    )


ZControlRegionPrompt = cms.PSet(
    name = cms.string("ZControlRegionPrompt"),
    triggers = cms.vstring(),
    cuts = copy.deepcopy(ZControlRegion.cuts)
)
ZControlRegionPrompt.cuts.append(prompt_cut)

ZControlRegionDisplaced = cms.PSet(
    name = cms.string("ZControlRegionDisplaced"),
    triggers = cms.vstring(),
    cuts = copy.deepcopy(ZControlRegion.cuts)
)
ZControlRegionDisplaced.cuts.append(displaced_cut)

ZControlRegionVeryDisplaced = cms.PSet(
    name = cms.string("ZControlRegionVeryDisplaced"),
    triggers = cms.vstring(),
    cuts = copy.deepcopy(ZControlRegion.cuts)
)
ZControlRegionVeryDisplaced.cuts.append(very_displaced_cut)

