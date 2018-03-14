import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

#################################################################
### Set up the preselection for the displaced SUSY analysis #####
#################################################################

Preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = cms.vstring("HLT_DoubleMu33NoFiltersNoVtx_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
Preselection.cuts.append(atLeastZero_jet_eta_cut)
Preselection.cuts.append(atLeastZero_jet_pt_30_cut)
Preselection.cuts.append(atLeastZero_jet_id_cut)
### at least two good muons
Preselection.cuts.append(muon_eta_cut)
Preselection.cuts.append(muon_pt_40_cut)
Preselection.cuts.append(muon_global_cut)
Preselection.cuts.append(muon_id_cut)
Preselection.cuts.append(muon_iso_cut)

PromptControlRegion = copy.deepcopy(Preselection)
PromptControlRegion.name = cms.string("PromptControlRegion")
PromptControlRegion.cuts.append(muon_d0_lessThan100_cut)

AntiIsoPromptControlRegion = copy.deepcopy(PromptControlRegion)
AntiIsoPromptControlRegion.name = cms.string("AntiIsoPromptControlRegion")
replaceSingleCut(AntiIsoPromptControlRegion.cuts, muon_antiiso_cut, muon_iso_cut) #replace muon_iso_cut with muon_antiiso_cut in the same place

DisplacedControlRegion = copy.deepcopy(Preselection)
DisplacedControlRegion.name = cms.string("DisplacedControlRegion")
DisplacedControlRegion.cuts.append(muon_d0_100to200_cut)

AntiIsoDisplacedControlRegion = copy.deepcopy(DisplacedControlRegion)
AntiIsoDisplacedControlRegion.name = cms.string("AntiIsoDisplacedControlRegion")
replaceSingleCut(AntiIsoDisplacedControlRegion.cuts, muon_antiiso_cut, muon_iso_cut) #replace muon_iso_cut with muon_antiiso_cut in the same place

