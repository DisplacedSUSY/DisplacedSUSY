import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

##########################################################################
### Set up the TTbar regions for trigger efficiency plots
##########################################################################

# Opposite sign e-mu pair with >=2 jets and >= 1 b jet
# Designed to mimic the selection Bing used for trigger efficiency

##########################################################################

TTbarForTrigEff = cms.PSet(
    name = cms.string("TTbarForTrigEff"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### at least one good, isolated electron
TTbarForTrigEff.cuts.extend(atLeastOne_electron_basic_selection_cuts)
TTbarForTrigEff.cuts.append(electron_iso_cut)
### at least one good, isolated muon
TTbarForTrigEff.cuts.extend(atLeastOne_muon_basic_selection_cuts)
TTbarForTrigEff.cuts.append(muon_iso_cut)
### at least one good electron-muon pair
TTbarForTrigEff.cuts.append(emu_opposite_charge_cut)
TTbarForTrigEff.cuts.append(emu_deltaR_cut)
### at least two good jets, one medium b jet
TTbarForTrigEff.cuts.extend(atLeastTwo_jet_basic_selection_cuts)
TTbarForTrigEff.cuts.append(atLeastTwo_jet_lepton_cleaning_cut)
TTbarForTrigEff.cuts.append(jet_btag_mwp_cut)
### extra lepton vetoes
TTbarForTrigEff.cuts.append(electron_num_exactly_1_cut)
TTbarForTrigEff.cuts.append(muon_num_exactly_1_cut)
### passes MET trigger (use eventvariable so that triggers can be ANDed)
TTbarForTrigEff.cuts.append(pass_trigger)


#############2017 Triggers#############

### Basic selection with triggers
TTbarForTrigEff43 = cms.PSet(
    name = cms.string("TTbarForTrigEff43"),
    triggers = cms.vstring("HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEff.cuts))
)

TTbarForTrigEff48 = cms.PSet(
    name = cms.string("TTbarForTrigEff48"),
    triggers = cms.vstring("HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEff.cuts))
)

### Require high-pt electron
TTbarForTrigEffHighPtE = cms.PSet(
    name = cms.string("TTbarForTrigEffHighPtE"),
    triggers = copy.deepcopy(TTbarForTrigEff.triggers),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEff.cuts))
)
TTbarForTrigEffHighPtE.cuts.append(electron_pt_50_cut)

TTbarForTrigEff43HighPtE = cms.PSet(
    name = cms.string("TTbarForTrigEff43HighPtE"),
    triggers = cms.vstring("HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffHighPtE.cuts))
)

TTbarForTrigEff48HighPtE = cms.PSet(
    name = cms.string("TTbarForTrigEff48HighPtE"),
    triggers = cms.vstring("HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffHighPtE.cuts))
)

### Require high-pt muon
TTbarForTrigEffHighPtMu = cms.PSet(
    name = cms.string("TTbarForTrigEffHighPtMu"),
    triggers = copy.deepcopy(TTbarForTrigEff.triggers),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEff.cuts))
)
TTbarForTrigEffHighPtMu.cuts.append(muon_pt_50_cut)

TTbarForTrigEff43HighPtMu = cms.PSet(
    name = cms.string("TTbarForTrigEff43HighPtMu"),
    triggers = cms.vstring("HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffHighPtMu.cuts))
)

TTbarForTrigEff48HighPtMu = cms.PSet(
    name = cms.string("TTbarForTrigEff48HighPtMu"),
    triggers = cms.vstring("HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffHighPtMu.cuts))
)

#############2016 Triggers#############

### Basic selection with MET trigger
TTbarForTrigEffMet = cms.PSet(
    name = cms.string("TTbarForTrigEffMet"),
    triggers = cms.vstring("HLT_MET200_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEff.cuts))
)

### Basic selection with EMu trigger
TTbarForTrigEff38 = cms.PSet(
    name = cms.string("TTbarForTrigEff38"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEff.cuts))
)

### Require high-pt electron
TTbarForTrigEff38HighPtE = cms.PSet(
    name = cms.string("TTbarForTrigEff38HighPtE"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffHighPtE.cuts))
)

### Require high-pt muon
TTbarForTrigEff38HighPtMu = cms.PSet(
    name = cms.string("TTbarForTrigEff38HighPtMu"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffHighPtMu.cuts))
)

### Veto trigger
TTbarForTrigEffVeto38 = cms.PSet(
    name = cms.string("TTbarForTrigEffVeto38"),
    triggers = copy.deepcopy(TTbarForTrigEff.triggers),
    triggersToVeto = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffHighPtE.cuts))
)
TTbarForTrigEffVeto38.cuts.append(muon_pt_150_cut)

#######Standard 2016 Trigger##########

### Require high-pt electron
TTbarForTrigEffStandardTrigHighPtE = cms.PSet(
    name = cms.string("TTbarForTrigEffStandardTrigHighPtE"),
    triggers = cms.vstring("HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffHighPtE.cuts))
)

### Require high-pt muon
TTbarForTrigEffStandardTrigHighPtMu = cms.PSet(
    name = cms.string("TTbarForTrigEffStandardTrigHighPtMu"),
    triggers = cms.vstring("HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffHighPtMu.cuts))
)

