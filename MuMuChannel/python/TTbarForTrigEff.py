import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

##########################################################################
### Set up the TTbar regions for trigger efficiency plots
##########################################################################

# Opposite sign mu-mu pair with >=2 jets and >= 1 b jet
# Designed to mimic the selection Bing used for trigger efficiency

##########################################################################

TTbarForTrigEffNoTrig = cms.PSet(
    name = cms.string("TTbarForTrigEffNoTrig"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### at least two good muons
TTbarForTrigEffNoTrig.cuts.append(muon_eta_cut)
TTbarForTrigEffNoTrig.cuts.append(muon_pt_25_cut)
TTbarForTrigEffNoTrig.cuts.append(muon_global_cut)
TTbarForTrigEffNoTrig.cuts.append(muon_id_cut)
TTbarForTrigEffNoTrig.cuts.append(muon_iso_cut)
### good muon, muon pair
TTbarForTrigEffNoTrig.cuts.append(diMuon_opposite_charge_cut)
TTbarForTrigEffNoTrig.cuts.append(diMuon_deltaR_cut)
### two good jets, one medium b jet
TTbarForTrigEffNoTrig.cuts.append(jet_eta_real_cut)
TTbarForTrigEffNoTrig.cuts.append(jet_pt_30_real_cut)
TTbarForTrigEffNoTrig.cuts.append(jet_id_real_cut)
TTbarForTrigEffNoTrig.cuts.append(jet_lepton_cleaning_cut)
TTbarForTrigEffNoTrig.cuts.append(jet_btag_mwp_cut)
### extra muon veto
TTbarForTrigEffNoTrig.cuts.append(muon_2muon_cut)


TTbarForTrigEff43 = cms.PSet(
    name = cms.string("TTbarForTrigEff43"),
    triggers = cms.vstring("HLT_DoubleMu43NoFiltersNoVtx_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)

TTbarForTrigEff48 = cms.PSet(
    name = cms.string("TTbarForTrigEff48"),
    triggers = cms.vstring("HLT_DoubleMu48NoFiltersNoVtx_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)
