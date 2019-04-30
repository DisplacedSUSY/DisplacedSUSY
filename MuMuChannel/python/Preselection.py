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
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    Preselection.cuts.append(muon_pt_40_cut)
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    Preselection.cuts.append(muon_pt_50_cut)
Preselection.cuts.append(muon_global_cut)
Preselection.cuts.append(muon_id_cut)
Preselection.cuts.append(muon_iso_cut)

#################################################################

### to find negative valued bins in abcd method closure test
lifetimeWeightNegative = copy.deepcopy(Preselection)
lifetimeWeightNegative.name = cms.string("lifetimeWeightNegative")
lifetimeWeightNegative.cuts.append(lifetimeWeight_negative)

puScalingFactorNegative = copy.deepcopy(Preselection)
puScalingFactorNegative.name = cms.string("puScalingFactorNegative")
puScalingFactorNegative.cuts.append(puScalingFactor_negative)

#################################################################

PreselectionNoIsoCut = copy.deepcopy(Preselection)
PreselectionNoIsoCut.name = cms.string("PreselectionNoIsoCut")
removeCuts(PreselectionNoIsoCut.cuts, [muon_iso_cut])

PreselectionLowEta = copy.deepcopy(Preselection)
PreselectionLowEta.name = cms.string("PreselectionLowEta")
PreselectionLowEta.cuts.append(muon_eta_lessThan1_cut)

PreselectionHighEta = copy.deepcopy(Preselection)
PreselectionHighEta.name = cms.string("PreselectionHighEta")
PreselectionHighEta.cuts.append(muon_eta_greaterThan1_cut)

PromptControlRegion = copy.deepcopy(Preselection)
PromptControlRegion.name = cms.string("PromptControlRegion")
PromptControlRegion.cuts.append(muon_d0_lessThan50_cut)

PromptControlRegionNoIsoCut = copy.deepcopy(PreselectionNoIsoCut)
PromptControlRegionNoIsoCut.name = cms.string("PromptControlRegionNoIsoCut")
PromptControlRegionNoIsoCut.cuts.append(muon_d0_lessThan50_cut)

PromptControlRegionLowEta = copy.deepcopy(PreselectionLowEta)
PromptControlRegionLowEta.name = cms.string("PromptControlRegionLowEta")
PromptControlRegionLowEta.cuts.append(muon_d0_lessThan50_cut)

PromptControlRegionHighEta = copy.deepcopy(PreselectionHighEta)
PromptControlRegionHighEta.name = cms.string("PromptControlRegionHighEta")
PromptControlRegionHighEta.cuts.append(muon_d0_lessThan50_cut)

AntiIsoPromptControlRegion = copy.deepcopy(PromptControlRegion)
AntiIsoPromptControlRegion.name = cms.string("AntiIsoPromptControlRegion")
replaceSingleCut(AntiIsoPromptControlRegion.cuts, muon_antiiso_cut, muon_iso_cut) #replace muon_iso_cut with muon_antiiso_cut in the same place

DisplacedControlRegion = copy.deepcopy(Preselection)
DisplacedControlRegion.name = cms.string("DisplacedControlRegion")
#DisplacedControlRegion.cuts.append(muon_d0_100to200_cut)
DisplacedControlRegion.cuts.append(muon_d0_10to20_cut)

AntiIsoDisplacedControlRegion = copy.deepcopy(DisplacedControlRegion)
AntiIsoDisplacedControlRegion.name = cms.string("AntiIsoDisplacedControlRegion")
replaceSingleCut(AntiIsoDisplacedControlRegion.cuts, muon_antiiso_cut, muon_iso_cut) #replace muon_iso_cut with muon_antiiso_cut in the same place

InclusiveSignalRegion = copy.deepcopy(Preselection)
InclusiveSignalRegion.name = cms.string("InclusiveSignalRegion")
InclusiveSignalRegion.cuts.append(muon_d0_greaterThan50_cut)

InclusiveSignalRegionNoIsoCut = copy.deepcopy(PreselectionNoIsoCut)
InclusiveSignalRegionNoIsoCut.name = cms.string("InclusiveSignalRegionNoIsoCut")
InclusiveSignalRegionNoIsoCut.cuts.append(muon_d0_greaterThan50_cut)

InclusiveSignalRegionLowEta = copy.deepcopy(PreselectionLowEta)
InclusiveSignalRegionLowEta.name = cms.string("InclusiveSignalRegionLowEta")
InclusiveSignalRegionLowEta.cuts.append(muon_d0_greaterThan50_cut)

InclusiveSignalRegionHighEta = copy.deepcopy(PreselectionHighEta)
InclusiveSignalRegionHighEta.name = cms.string("InclusiveSignalRegionHighEta")
InclusiveSignalRegionHighEta.cuts.append(muon_d0_greaterThan50_cut)

#################################################################

ZControlRegion = copy.deepcopy(Preselection)
ZControlRegion.name = cms.string("ZControlRegion")
ZControlRegion.cuts.append(muon_jet_deltaR_overlap_veto)
ZControlRegion.cuts.append(muon_2muon_cut)
ZControlRegion.cuts.append(diMuon_invMass_Z_cut) ### invMass in Z range
ZControlRegion.cuts.append(muon_fiducial_phi_cut)

#################################################################

PromptLowPtControlRegion = copy.deepcopy(PromptControlRegion)
PromptLowPtControlRegion.name = cms.string("PromptLowPtControlRegion")
PromptLowPtControlRegion.cuts.append(muon_pt_100_veto)

PromptHighPtControlRegion = copy.deepcopy(PromptControlRegion)
PromptHighPtControlRegion.name = cms.string("PromptHighPtControlRegion")
PromptHighPtControlRegion.cuts.append(muon_pt_100_cut)

DisplacedLowPtControlRegion = copy.deepcopy(InclusiveSignalRegion)
DisplacedLowPtControlRegion.name = cms.string("DisplacedLowPtControlRegion")
DisplacedLowPtControlRegion.cuts.append(muon_pt_100_veto)

DisplacedHighPtControlRegion = copy.deepcopy(InclusiveSignalRegion)
DisplacedHighPtControlRegion.name = cms.string("DisplacedHighPtControlRegion")
DisplacedHighPtControlRegion.cuts.append(muon_pt_100_cut)

PromptLowPtControlRegionNoIsoCut = copy.deepcopy(PromptControlRegionNoIsoCut)
PromptLowPtControlRegionNoIsoCut.name = cms.string("PromptLowPtControlRegionNoIsoCut")
PromptLowPtControlRegionNoIsoCut.cuts.append(muon_pt_100_veto)

PromptHighPtControlRegionNoIsoCut = copy.deepcopy(PromptControlRegionNoIsoCut)
PromptHighPtControlRegionNoIsoCut.name = cms.string("PromptHighPtControlRegionNoIsoCut")
PromptHighPtControlRegionNoIsoCut.cuts.append(muon_pt_100_cut)

DisplacedLowPtControlRegionNoIsoCut = copy.deepcopy(InclusiveSignalRegionNoIsoCut)
DisplacedLowPtControlRegionNoIsoCut.name = cms.string("DisplacedLowPtControlRegionNoIsoCut")
DisplacedLowPtControlRegionNoIsoCut.cuts.append(muon_pt_100_veto)

DisplacedHighPtControlRegionNoIsoCut = copy.deepcopy(InclusiveSignalRegionNoIsoCut)
DisplacedHighPtControlRegionNoIsoCut.name = cms.string("DisplacedHighPtControlRegionNoIsoCut")
DisplacedHighPtControlRegionNoIsoCut.cuts.append(muon_pt_100_cut)

PromptLowPtControlRegionLowEta = copy.deepcopy(PromptControlRegionLowEta)
PromptLowPtControlRegionLowEta.name = cms.string("PromptLowPtControlRegionLowEta")
PromptLowPtControlRegionLowEta.cuts.append(muon_pt_100_veto)

PromptHighPtControlRegionLowEta = copy.deepcopy(PromptControlRegionLowEta)
PromptHighPtControlRegionLowEta.name = cms.string("PromptHighPtControlRegionLowEta")
PromptHighPtControlRegionLowEta.cuts.append(muon_pt_100_cut)

DisplacedLowPtControlRegionLowEta = copy.deepcopy(InclusiveSignalRegionLowEta)
DisplacedLowPtControlRegionLowEta.name = cms.string("DisplacedLowPtControlRegionLowEta")
DisplacedLowPtControlRegionLowEta.cuts.append(muon_pt_100_veto)

DisplacedHighPtControlRegionLowEta = copy.deepcopy(InclusiveSignalRegionLowEta)
DisplacedHighPtControlRegionLowEta.name = cms.string("DisplacedHighPtControlRegionLowEta")
DisplacedHighPtControlRegionLowEta.cuts.append(muon_pt_100_cut)

PromptLowPtControlRegionHighEta = copy.deepcopy(PromptControlRegionHighEta)
PromptLowPtControlRegionHighEta.name = cms.string("PromptLowPtControlRegionHighEta")
PromptLowPtControlRegionHighEta.cuts.append(muon_pt_100_veto)

PromptHighPtControlRegionHighEta = copy.deepcopy(PromptControlRegionHighEta)
PromptHighPtControlRegionHighEta.name = cms.string("PromptHighPtControlRegionHighEta")
PromptHighPtControlRegionHighEta.cuts.append(muon_pt_100_cut)

DisplacedLowPtControlRegionHighEta = copy.deepcopy(InclusiveSignalRegionHighEta)
DisplacedLowPtControlRegionHighEta.name = cms.string("DisplacedLowPtControlRegionHighEta")
DisplacedLowPtControlRegionHighEta.cuts.append(muon_pt_100_veto)

DisplacedHighPtControlRegionHighEta = copy.deepcopy(InclusiveSignalRegionHighEta)
DisplacedHighPtControlRegionHighEta.name = cms.string("DisplacedHighPtControlRegionHighEta")
DisplacedHighPtControlRegionHighEta.cuts.append(muon_pt_100_cut)

#################################################################

PreselectionLeptonsFromW = cms.PSet(
    name = cms.string("PreselectionLeptonsFromW"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsFromW.cuts.append(muon_gen_motherIsW_cut)
