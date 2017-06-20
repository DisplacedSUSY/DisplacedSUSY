import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

#############################################################################
### Set up the TTBar Paper MET Selection for the displaced SUSY analysis #####
#############################################################################

TTbarXsectionPaperMET = cms.PSet(
    name = cms.string("TTbarXsectionPaperMET"),
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
### jet selection
TTbarXsectionPaperMET.cuts.append(jet_eta_real_cut)
TTbarXsectionPaperMET.cuts.append(jet_pt_30_real_cut)
TTbarXsectionPaperMET.cuts.append(jet_loose_id_cut)
TTbarXsectionPaperMET.cuts.append(jet_electron_deltaR_cut)
TTbarXsectionPaperMET.cuts.append(jet_muon_deltaR_cut)
### one good electron
TTbarXsectionPaperMET.cuts.append(electron_eta_cut)
TTbarXsectionPaperMET.cuts.append(electron_gap_veto)
TTbarXsectionPaperMET.cuts.append(electron_pt_25_cut)
TTbarXsectionPaperMET.cuts.append(electron_ttbar_paper_id_cut)
TTbarXsectionPaperMET.cuts.append(electron_iso_cut)
TTbarXsectionPaperMET.cuts.append(electron_num_exactly_1_cut)
### one good muon
TTbarXsectionPaperMET.cuts.append(muon_eta_cut)
TTbarXsectionPaperMET.cuts.append(muon_pt_25_cut)
TTbarXsectionPaperMET.cuts.append(muon_global_cut)
TTbarXsectionPaperMET.cuts.append(muon_id_cut)
TTbarXsectionPaperMET.cuts.append(muon_d0_below2000_cut)
TTbarXsectionPaperMET.cuts.append(muon_dZ_below5000_cut)
TTbarXsectionPaperMET.cuts.append(muon_iso_cut)
TTbarXsectionPaperMET.cuts.append(muon_num_exactly_1_cut)
### muon-electron pair
TTbarXsectionPaperMET.cuts.append(emu_mass_20_cut)
TTbarXsectionPaperMET.cuts.append(emu_opposite_charge_cut)
## Met
TTbarXsectionPaperMET.cuts.append(met_pt_40_cut)
