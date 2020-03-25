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
### dummy photon cuts for plotting
Preselection.cuts.extend(atLeastZero_photon_basic_selection_cuts)
### at least two good electrons
Preselection.cuts.append(electron_eta_cut)
Preselection.cuts.append(electron_gap_veto)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    Preselection.cuts.append(electron_pt_65_cut)
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    Preselection.cuts.append(electron_pt_75_cut)
Preselection.cuts.append(electron_id_cut) #electron vid normally includes isolation, but we take it out in customize.py
#Preselection.cuts.append(electron_iso_cut)
Preselection.cuts.append(electron_newIso_cut)

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
InclusiveSignalRegion.cuts.append(electron_d0_greaterThan50_cut)

#################################################################

PreselectionLooseIsoCutBTagVeto = copy.deepcopy(Preselection)
PreselectionLooseIsoCutBTagVeto.name = cms.string("PreselectionLooseIsoCutBTagVeto")
replaceSingleCut(PreselectionLooseIsoCutBTagVeto.cuts, electron_loose_iso_cut, electron_iso_cut)
PreselectionLooseIsoCutBTagVeto.cuts.append(jet_btag_lwp_veto)

#################################################################

PromptLowPtControlRegion = copy.deepcopy(PromptControlRegion)
PromptLowPtControlRegion.name = cms.string("PromptLowPtControlRegion")
PromptLowPtControlRegion.cuts.append(electron_pt_100_veto)

#################################################################

PromptHighPtControlRegion = copy.deepcopy(PromptControlRegion)
PromptHighPtControlRegion.name = cms.string("PromptHighPtControlRegion")
PromptHighPtControlRegion.cuts.append(electron_pt_100_cut)

#################################################################

DisplacedLowPtControlRegion = copy.deepcopy(InclusiveSignalRegion)
DisplacedLowPtControlRegion.name = cms.string("DisplacedLowPtControlRegion")
DisplacedLowPtControlRegion.cuts.append(electron_pt_100_veto)

#################################################################

DisplacedHighPtControlRegion = copy.deepcopy(InclusiveSignalRegion)
DisplacedHighPtControlRegion.name = cms.string("DisplacedHighPtControlRegion")
DisplacedHighPtControlRegion.cuts.append(electron_pt_100_cut)

#################################################################

DisplacedHighPtL1PrefiringCheck = copy.deepcopy(DisplacedHighPtControlRegion)
DisplacedHighPtL1PrefiringCheck.name = cms.string("DisplacedHighPtL1PrefiringCheck")
DisplacedHighPtL1PrefiringCheck.cuts.extend(L1PrefiringCheck_cuts)

PreselectionLeptonsFromW = cms.PSet(
    name = cms.string("PreselectionLeptonsFromW"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsFromW.cuts.append(electron_gen_motherIsW_cut)

#################################################################

GenEEFromStopsSelection = cms.PSet(
    name = cms.string("GenEEFromStopsSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet([exactly2_genEle_status1_uniqueMotherIsStop_cut,
                      #atLeastTwo_genLxy_lessThan50cm_cut,
                      atLeastTwo_genLxy_lessThan1cm_cut,
                      atLeastTwo_genEta_cut,
                ])
)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    GenEEFromStopsSelection.cuts.append(atLeastTwo_genPt_65_cut)
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    GenEEFromStopsSelection.cuts.append(atLeastTwo_genPt_75_cut)
GenEEFromStopsSelection.cuts.append(cutDummyElectron)

#################################################################

AdditionalPreselection = cms.PSet(
    name = cms.string("AdditionalPreselection"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet()
)
AdditionalPreselection.cuts.append(displaced_muon_emu_preselection_veto)
