import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

#############################################################################
### Set up the TTBar Paper LL Selection for the displaced SUSY analysis #####
#############################################################################

TTbarXsectionPaperLL = cms.PSet(
    name = cms.string("TTbarXsectionPaperLL"),
    triggers = cms.vstring(
                           "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                           "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v",
                           "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v",
                           "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v",
                           "HLT_Ele27_WPTight_Gsf_v",
                           "HLT_IsoMu24_v",
                           "HLT_IsoTkMu24_v",
                          ),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
TTbarXsectionPaperLL.cuts.append(jet_eta_cut)
TTbarXsectionPaperLL.cuts.append(jet_pt_30_cut)
TTbarXsectionPaperLL.cuts.append(jet_id_cut)
### one good electron
TTbarXsectionPaperLL.cuts.append(electron_eta_cut)
TTbarXsectionPaperLL.cuts.append(electron_gap_veto)
TTbarXsectionPaperLL.cuts.append(electron_pt_25_cut)
TTbarXsectionPaperLL.cuts.append(electron_ttbar_paper_id_cut)
TTbarXsectionPaperLL.cuts.append(electron_iso_cut)
TTbarXsectionPaperLL.cuts.append(electron_num_exactly_1_cut)
### one good muon
TTbarXsectionPaperLL.cuts.append(muon_eta_cut)
TTbarXsectionPaperLL.cuts.append(muon_pt_25_cut)
TTbarXsectionPaperLL.cuts.append(muon_global_cut)
TTbarXsectionPaperLL.cuts.append(muon_id_cut)
TTbarXsectionPaperLL.cuts.append(muon_d0_below2000_cut)
TTbarXsectionPaperLL.cuts.append(muon_dZ_below5000_cut)
TTbarXsectionPaperLL.cuts.append(muon_iso_cut)
TTbarXsectionPaperLL.cuts.append(muon_num_exactly_1_cut)
### muon-electron pair
TTbarXsectionPaperLL.cuts.append(emu_mass_20_cut)
TTbarXsectionPaperLL.cuts.append(emu_opposite_charge_cut)
