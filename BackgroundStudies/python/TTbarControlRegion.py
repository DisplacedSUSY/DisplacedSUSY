import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.StandardAnalysis.BasicSelections import *

#tt->emu

ttbar_control_region_cuts = cms.VPSet(
    emu_opposite_charge_cut,
    emu_deltaR_cut, # ELECTRON AND MUON ARE NOT OVERLAPPING (Delta R> 0.5)
    atLeastTwo_jet_eta_cut,
    atLeastTwo_jet_pt_30_cut,
    atLeastTwo_jet_id_cut,
    muon_jet_deltaR_overlap_veto, #if deltaR(muon,jet) < 0.5, veto
    electron_jet_deltaR_overlap_veto, #if deltaR(electron,jet) < 0.5, veto
    muon_num_exactly_1_cut,
    electron_num_exactly_1_cut,
    jet_btag_mwp_cut,
)

ttbar_semileptonic_control_region_cuts = cms.VPSet(
    atLeastTwo_jet_eta_cut,
    atLeastTwo_jet_pt_30_cut,
    atLeastTwo_jet_id_cut,
    jet_btag_mwp_cut,
    muon_jet_deltaR_overlap_veto, #if deltaR(muon,jet) < 0.5, veto
)
##########################################################################

TTbarControlRegion = cms.PSet(
    name = cms.string("TTbarControlRegion"),
    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)
TTbarControlRegion.cuts.extend(atLeastOne_electron_basic_selection_cuts)
TTbarControlRegion.cuts.append(electron_iso_cut)
TTbarControlRegion.cuts.extend(atLeastOne_muon_basic_selection_cuts)
TTbarControlRegion.cuts.append(muon_iso_cut)
TTbarControlRegion.cuts.extend(ttbar_control_region_cuts)

##########################################################################

TTbarControlRegionMETTrigger = cms.PSet(
    name = cms.string("TTbarControlRegionMETTrigger"),
    triggers = cms.vstring("HLT_PFMET170_v","HLT_PFMET120_BTagCSV0p72_v","HLT_PFMET120_JetIdCleaned_BTagCSV0p72_v","HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v"),
    cuts = cms.VPSet ()
)

TTbarControlRegionMETTrigger.cuts = cms.VPSet (copy.deepcopy(TTbarControlRegion.cuts))

for cut in TTbarControlRegionMETTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

TTbarLowPtControlRegionMETTrigger = cms.PSet(
    name = cms.string("TTbarLowPtControlRegionMETTrigger"),
    triggers = cms.vstring("HLT_PFMET170_v","HLT_PFMET120_BTagCSV0p72_v","HLT_PFMET120_JetIdCleaned_BTagCSV0p72_v","HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v"),
    cuts = cms.VPSet ()
)

TTbarLowPtControlRegionMETTrigger.cuts = cms.VPSet (copy.deepcopy(TTbarControlRegion.cuts))



TTbarControlRegionMETTriggerPassEMuTrigger = cms.PSet(
    name = cms.string("TTbarControlRegionMETTriggerPassEMuTrigger"),
    triggers = cms.vstring("HLT_PFMET170_v","HLT_PFMET120_BTagCSV0p72_v","HLT_PFMET120_JetIdCleaned_BTagCSV0p72_v","HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v"),
    cuts = cms.VPSet ()
)

TTbarControlRegionMETTriggerPassEMuTrigger.cuts = cms.VPSet (copy.deepcopy(TTbarControlRegion.cuts))

for cut in TTbarControlRegionMETTriggerPassEMuTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

TTbarLowPtControlRegionMETTriggerPassEMuTrigger = cms.PSet(
    name = cms.string("TTbarLowPtControlRegionMETTriggerPassEMuTrigger"),
    triggers = cms.vstring("HLT_PFMET170_v","HLT_PFMET120_BTagCSV0p72_v","HLT_PFMET120_JetIdCleaned_BTagCSV0p72_v","HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v"),
    cuts = cms.VPSet ()
)

TTbarLowPtControlRegionMETTriggerPassEMuTrigger.cuts = cms.VPSet (copy.deepcopy(TTbarControlRegion.cuts))


TTbarMuonControlRegion = cms.PSet(
    name = cms.string("TTbarMuonControlRegion"),
    triggers = triggersIsoSingleMuon,
    cuts = cms.VPSet ()
)
TTbarMuonControlRegion.cuts.extend(atLeastOne_muon_basic_selection_cuts)
TTbarMuonControlRegion.cuts.append(muon_iso_cut)
TTbarMuonControlRegion.cuts.extend(ttbar_semileptonic_control_region_cuts)
