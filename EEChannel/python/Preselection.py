import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EEChannel.CutDefinitions import *

#################################################################
### Set up the preselection for the displaced SUSY analysis #####
#################################################################

Preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = triggersDoublePhoton,
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
Preselection.cuts.extend(atLeastZero_jet_basic_selection_cuts)
### at least two good electrons
Preselection.cuts.append(electron_eta_cut)
Preselection.cuts.append(electron_gap_veto)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    Preselection.cuts.append(electron_pt_65_cut)
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    Preselection.cuts.append(electron_pt_75_cut)
Preselection.cuts.append(electron_id_cut) #electron vid normally includes isolation, but we take it out in customize.py
Preselection.cuts.append(electron_iso_cut)

PromptControlRegion = copy.deepcopy(Preselection)
PromptControlRegion.name = cms.string("PromptControlRegion")
PromptControlRegion.cuts.append(electron_d0_lessThan50_cut)

#################################################################

DisplacedControlRegion = copy.deepcopy(Preselection)
DisplacedControlRegion.name = cms.string("DisplacedControlRegion")
#DisplacedControlRegion.cuts.append(electron_d0_100to200_cut)
DisplacedControlRegion.cuts.append(electron_d0_10to20_cut)

#################################################################

ZControlRegion = copy.deepcopy(Preselection)
ZControlRegion.name = cms.string("ZControlRegion")
ZControlRegion.cuts.append(electron_jet_deltaR_overlap_veto)
ZControlRegion.cuts.append(electron_2electron_cut)
ZControlRegion.cuts.append(diElectron_invMass_Z_cut) ### invMass in Z range
ZControlRegion.cuts.append(electron_fiducial_phi_cut)

#################################################################

InclusiveSignalRegion = copy.deepcopy(Preselection)
InclusiveSignalRegion.name = cms.string("InclusiveSignalRegion")
InclusiveSignalRegion.cuts.append(electron_d0_greaterThan20_cut)



PreselectionLeptonsFromW = cms.PSet(
    name = cms.string("PreselectionLeptonsFromW"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsFromW.cuts.append(electron_gen_motherIsW_cut)
