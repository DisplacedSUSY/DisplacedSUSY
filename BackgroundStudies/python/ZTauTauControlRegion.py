import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.StandardAnalysis.EventSelections import *

ztautau_control_region_cuts = cms.VPSet(
    electron_mt_cut,
    muon_mt_cut,
    emu_opposite_charge_cut,
    emu_deltaR_cut,
    emu_mass_lessThan100_cut,
    electron_num_exactly_1_cut,
    muon_num_exactly_1_cut,
)

ZTauTautoEMuControlRegion = cms.PSet(
    name = cms.string("ZTauTautoEMuControlRegion"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"),
    cuts = cms.VPSet ()
)
ZTauTautoEMuControlRegion.cuts.extend(electron_basic_selection_cuts)
ZTauTautoEMuControlRegion.cuts.append(electron_iso_cut)
ZTauTautoEMuControlRegion.cuts.extend(muon_basic_selection_cuts)
ZTauTautoEMuControlRegion.cuts.append(muon_iso_cut)
ZTauTautoEMuControlRegion.cuts.extend(ztautau_control_region_cuts)
