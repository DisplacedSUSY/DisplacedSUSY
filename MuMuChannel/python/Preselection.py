import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

#################################################################
### Set up the preselection for the displaced SUSY analysis #####
#################################################################

Preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
Preselection.cuts.extend(atLeastZero_jet_basic_selection_cuts)
### at least two good muons
Preselection.cuts.append(muon_eta_cut)
Preselection.cuts.append(muon_pt_40_cut)
Preselection.cuts.append(muon_global_cut)
Preselection.cuts.append(muon_id_cut)
Preselection.cuts.append(muon_iso_cut)

PromptControlRegion = copy.deepcopy(Preselection)
PromptControlRegion.name = cms.string("PromptControlRegion")
#PromptControlRegion.cuts.append(muon_d0_lessThan100_cut)
PromptControlRegion.cuts.append(muon_d0_lessThan10_cut)

AntiIsoPromptControlRegion = copy.deepcopy(PromptControlRegion)
AntiIsoPromptControlRegion.name = cms.string("AntiIsoPromptControlRegion")
replaceSingleCut(AntiIsoPromptControlRegion.cuts, muon_antiiso_cut, muon_iso_cut) #replace muon_iso_cut with muon_antiiso_cut in the same place

#################################################################

DisplacedControlRegion = copy.deepcopy(Preselection)
DisplacedControlRegion.name = cms.string("DisplacedControlRegion")
#DisplacedControlRegion.cuts.append(muon_d0_100to200_cut)
DisplacedControlRegion.cuts.append(muon_d0_10to20_cut)

AntiIsoDisplacedControlRegion = copy.deepcopy(DisplacedControlRegion)
AntiIsoDisplacedControlRegion.name = cms.string("AntiIsoDisplacedControlRegion")
replaceSingleCut(AntiIsoDisplacedControlRegion.cuts, muon_antiiso_cut, muon_iso_cut) #replace muon_iso_cut with muon_antiiso_cut in the same place

#################################################################

ZControlRegion = copy.deepcopy(Preselection)
ZControlRegion.name = cms.string("ZControlRegion")
ZControlRegion.cuts.append(muon_jet_deltaR_overlap_veto)
ZControlRegion.cuts.append(muon_2muon_cut)
ZControlRegion.cuts.append(diMuon_invMass_Z_cut) ### invMass in Z range 
ZControlRegion.cuts.append(muon_fiducial_phi_cut)


#################################################################

InclusiveSignalRegion = copy.deepcopy(Preselection)
InclusiveSignalRegion.name = cms.string("InclusiveSignalRegion")
InclusiveSignalRegion.cuts.append(muon_d0_greaterThan40_cut)



PreselectionLeptonsFromW = cms.PSet(
    name = cms.string("PreselectionLeptonsFromW"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsFromW.cuts.append(muon_gen_motherIsW_cut)
