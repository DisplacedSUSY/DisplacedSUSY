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
TTbarForTrigEffNoTrig.cuts.append(cutDummyMet)
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

#######################################
### Triggers used by Jamie and Bryan###
#######################################
# TTbarForTrigEff43 = cms.PSet(
#     name = cms.string("TTbarForTrigEff43"),
#     triggers = cms.vstring("HLT_DoubleMu43NoFiltersNoVtx_v"),
#     cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
# )
# 
# TTbarForTrigEff48 = cms.PSet(
#     name = cms.string("TTbarForTrigEff48"),
#     triggers = cms.vstring("HLT_DoubleMu48NoFiltersNoVtx_v"),
#     cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
# )
# 
# ### Veto triggers ###
# TTbarForTrigEffVeto43 = cms.PSet(
#     name = cms.string("TTbarForTrigEffVeto43"),
#     triggers = cms.vstring(),
#     triggersToVeto = cms.vstring("HLT_DoubleMu43NoFiltersNoVtx_v"),
#     cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
# )
# TTbarForTrigEffVeto43.cuts.append(muon_pt_70_cut)

###############################
### Triggers used for 2016 ####
###############################
TriggerDoubleMu33 = cms.PSet(
    name = cms.string("TriggerDoubleMu33"),
    triggers = cms.vstring("HLT_DoubleMu33NoFiltersNoVtx"),
    cuts = cms.VPSet()
)
TriggerDoubleMu33.cuts.append(cutDummyMet)
TriggerDoubleMu33.cuts.append(pass_trigger)

TriggerDoubleMu23Displaced = cms.PSet(
    name = cms.string("TriggerDoubleMu23Displaced"),
    triggers = cms.vstring("HLT_DoubleMu23NoFiltersNoVtxDisplaced"),
    cuts = cms.VPSet()
)
TriggerDoubleMu23Displaced.cuts.append(cutDummyMet)
TriggerDoubleMu23Displaced.cuts.append(pass_trigger)

# Trigger to be used for 2016 MuMu channel
TriggerDoubleMu33ORDoubleMu23Displaced = cms.PSet(
    name = cms.string("TriggerDoubleMu33ORDoubleMu23Displaced"),
    triggers = cms.vstring("HLT_DoubleMu33NoFiltersNoVtx","HLT_DoubleMu23NoFiltersNoVtxDisplaced"),
    cuts = cms.VPSet()
)
TriggerDoubleMu33ORDoubleMu23Displaced.cuts.append(cutDummyMet)
TriggerDoubleMu33ORDoubleMu23Displaced.cuts.append(pass_trigger)

TrigMET = cms.PSet(
    name = cms.string("TrigMET"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
TrigMET.cuts.append(cutDummyMet)
TrigMET.cuts.append(pass_trigger)

### TTbar for triggers without tag muon eventvariable ###
MuMuTrigTTbarMET = cms.PSet(
    name = cms.string("MuMuTrigTTbarMET"),
    triggers = cms.vstring("HLT_DoubleMu33NoFiltersNoVtx","HLT_DoubleMu23NoFiltersNoVtxDisplaced"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)
MuMuTrigTTbarMET.cuts.append(cutDummyMet)
MuMuTrigTTbarMET.cuts.append(pass_trigger)

TrigTTbarMET = cms.PSet(
    name = cms.string("TrigTTbarMET"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)
TrigTTbarMET.cuts.append(cutDummyMet)
TrigTTbarMET.cuts.append(pass_trigger)

DoubleMu33TTbar = cms.PSet(
    name = cms.string("DoubleMu33TTbar"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)
DoubleMu33TTbar.cuts.append(cutDummyMet)
DoubleMu33TTbar.cuts.append(pass_trigger)

DoubleMu23DisplacedTTbar = cms.PSet(
    name = cms.string("DoubleMu23DisplacedTTbar"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)
DoubleMu23DisplacedTTbar.cuts.append(cutDummyMet)
DoubleMu23DisplacedTTbar.cuts.append(pass_trigger)

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
TTbarForTrigEffTagMuonNoTrig.cuts.append(cutDummyMet)
TTbarForTrigEffTagMuonNoTrig.cuts.append(tagMuonExists_cut)
TTbarForTrigEffTagMuonNoTrig.cuts.append(muon_opposite_charge_from_tag_cut)
TTbarForTrigEffTagMuonNoTrig.cuts.append(muon_deltaR_from_tag_cut)

# TTbarForTrigEffTagMuon43 = cms.PSet(
#     name = cms.string("TTbarForTrigEffTagMuon43"),
#     triggers = cms.vstring("HLT_DoubleMu43NoFiltersNoVtx_v"),
#     cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffTagMuonNoTrig.cuts))
# )
# 
# TTbarForTrigEffTagMuon48 = cms.PSet(
#     name = cms.string("TTbarForTrigEffTagMuon48"),
#     triggers = cms.vstring("HLT_DoubleMu48NoFiltersNoVtx_v"),
#     cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffTagMuonNoTrig.cuts))
# )


TriggerDoubleMu33ORDoubleMu23DisplacedTagMuon = cms.PSet(
    name = cms.string("TriggerDoubleMu33ORDoubleMu23DisplacedTagMuon"),
    triggers = cms.vstring("HLT_DoubleMu33NoFiltersNoVtx","HLT_DoubleMu23NoFiltersNoVtxDisplaced"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffTagMuonNoTrig.cuts))
)
TriggerDoubleMu33ORDoubleMu23DisplacedTagMuon.cuts.append(cutDummyMet)
TriggerDoubleMu33ORDoubleMu23DisplacedTagMuon.cuts.append(pass_trigger)


TTbarTagMuonTrigMET = cms.PSet(
    name = cms.string("TTbarTagMuonTrigMET"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffTagMuonNoTrig.cuts))
)
TTbarTagMuonTrigMET.cuts.append(cutDummyMet)
TTbarTagMuonTrigMET.cuts.append(pass_trigger)

DoubleMu33TTbarTagMuon = cms.PSet(
    name = cms.string("DoubleMu33TTbarTagMuon"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffTagMuonNoTrig.cuts))
)
DoubleMu33TTbarTagMuon.cuts.append(cutDummyMet)
DoubleMu33TTbarTagMuon.cuts.append(pass_trigger)

DoubleMu23DisplacedTTbarTagMuon = cms.PSet(
    name = cms.string("DoubleMu23DisplacedTTbarTagMuon"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffTagMuonNoTrig.cuts))
)
DoubleMu23DisplacedTTbarTagMuon.cuts.append(cutDummyMet)
DoubleMu23DisplacedTTbarTagMuon.cuts.append(pass_trigger)


