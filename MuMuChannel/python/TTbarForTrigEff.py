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
TTbarForTrigEffNoTrig.cuts.append(atLeastTwo_jet_eta_cut)
TTbarForTrigEffNoTrig.cuts.append(atLeastTwo_jet_pt_30_cut)
TTbarForTrigEffNoTrig.cuts.append(atLeastTwo_jet_id_cut)
TTbarForTrigEffNoTrig.cuts.append(atLeastTwo_jet_lepton_cleaning_cut)
TTbarForTrigEffNoTrig.cuts.append(jet_btag_mwp_cut)
### extra muon veto
TTbarForTrigEffNoTrig.cuts.append(muon_2muon_cut)


### Add triggers ###
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


### Veto triggers ###
TTbarForTrigEffVeto43 = cms.PSet(
    name = cms.string("TTbarForTrigEffVeto43"),
    triggers = cms.vstring(),
    triggersToVeto = cms.vstring("HLT_DoubleMu43NoFiltersNoVtx_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)
TTbarForTrigEffVeto43.cuts.append(muon_pt_70_cut)


### Use tag muon eventvariable
TTbarForTrigEffTagMuonNoTrig = cms.PSet(
    name = cms.string("TTbarForTrigEffTagMuonNoTrig"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)
for cut in TTbarForTrigEffTagMuonNoTrig.cuts:
    if "muon.charge * muon.charge < 0" in str(cut.cutString):
        TTbarForTrigEffTagMuonNoTrig.cuts.remove(cut)
    if "deltaR(muon, muon) > 0.5" in str(cut.cutString):
        TTbarForTrigEffTagMuonNoTrig.cuts.remove(cut)
TTbarForTrigEffTagMuonNoTrig.cuts.append(tagMuonExists_cut)
TTbarForTrigEffTagMuonNoTrig.cuts.append(muon_opposite_charge_from_tag_cut)
TTbarForTrigEffTagMuonNoTrig.cuts.append(muon_deltaR_from_tag_cut)

TTbarForTrigEffTagMuon43 = cms.PSet(
    name = cms.string("TTbarForTrigEffTagMuon43"),
    triggers = cms.vstring("HLT_DoubleMu43NoFiltersNoVtx_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffTagMuonNoTrig.cuts))
)

TTbarForTrigEffTagMuon48 = cms.PSet(
    name = cms.string("TTbarForTrigEffTagMuon48"),
    triggers = cms.vstring("HLT_DoubleMu48NoFiltersNoVtx_v"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffTagMuonNoTrig.cuts))
)

