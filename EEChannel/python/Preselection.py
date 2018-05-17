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
Preselection.cuts.append(electron_pt_65_cut)
Preselection.cuts.append(electron_id_cut)
Preselection.cuts.append(electron_iso_cut)


PromptControlRegion = copy.deepcopy(Preselection)
PromptControlRegion.name = cms.string("PromptControlRegion")
#PromptControlRegion.cuts.append(electron_d0_lessThan100_cut)
PromptControlRegion.cuts.append(electron_d0_lessThan10_cut)

AntiIsoPromptControlRegion = copy.deepcopy(PromptControlRegion)
AntiIsoPromptControlRegion.name = cms.string("AntiIsoPromptControlRegion")
replaceSingleCut(AntiIsoPromptControlRegion.cuts,electron_antiiso_cut,electron_iso_cut) #replace electron_iso_cut with electron_antiiso_cut in the same place 

#################################################################

DisplacedControlRegion = copy.deepcopy(Preselection)
DisplacedControlRegion.name = cms.string("DisplacedControlRegion") 
#DisplacedControlRegion.cuts.append(electron_d0_100to200_cut)
DisplacedControlRegion.cuts.append(electron_d0_10to20_cut)

AntiIsoDisplacedControlRegion = copy.deepcopy(DisplacedControlRegion)
AntiIsoDisplacedControlRegion.name = cms.string("AntiIsoDisplacedControlRegion")
replaceSingleCut(AntiIsoDisplacedControlRegion.cuts,electron_antiiso_cut,electron_iso_cut) #replace electron_iso_cut with electron_antiiso_cut in the same place 

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
