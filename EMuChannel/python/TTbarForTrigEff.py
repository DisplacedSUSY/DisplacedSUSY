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

TTbarForTrigEffNoTrig = cms.PSet(
    name = cms.string("TTbarForTrigEffNoTrig"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### at least one good electron
TTbarForTrigEffNoTrig.cuts.append(electron_eta_cut)
TTbarForTrigEffNoTrig.cuts.append(electron_gap_veto)
TTbarForTrigEffNoTrig.cuts.append(electron_pt_25_cut)
TTbarForTrigEffNoTrig.cuts.append(electron_id_cut)
TTbarForTrigEffNoTrig.cuts.append(electron_iso_cut)
### at least one good muon
TTbarForTrigEffNoTrig.cuts.append(muon_eta_cut)
TTbarForTrigEffNoTrig.cuts.append(muon_pt_25_cut)
TTbarForTrigEffNoTrig.cuts.append(muon_global_cut)
TTbarForTrigEffNoTrig.cuts.append(muon_id_cut)
TTbarForTrigEffNoTrig.cuts.append(muon_iso_cut)
### good electron, muon pair
TTbarForTrigEffNoTrig.cuts.append(emu_opposite_charge_cut)
TTbarForTrigEffNoTrig.cuts.append(emu_deltaR_cut)
### two good jets, one medium b jet
TTbarForTrigEffNoTrig.cuts.append(jet_eta_real_cut)
TTbarForTrigEffNoTrig.cuts.append(jet_pt_30_real_cut)
TTbarForTrigEffNoTrig.cuts.append(jet_id_real_cut)
TTbarForTrigEffNoTrig.cuts.append(jet_lepton_cleaning_cut)
TTbarForTrigEffNoTrig.cuts.append(jet_btag_mwp_cut)
### extra lepton vetos
TTbarForTrigEffNoTrig.cuts.append(electron_num_exactly_1_cut)
TTbarForTrigEffNoTrig.cuts.append(muon_num_exactly_1_cut)


TTbarForTrigEff43 = cms.PSet(
    name = cms.string("TTbarForTrigEff43"),
    triggers = cms.vstring("HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)

TTbarForTrigEff48 = cms.PSet(
    name = cms.string("TTbarForTrigEff48"),
    triggers = cms.vstring("HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)
