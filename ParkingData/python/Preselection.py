import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.MuMuChannel.CutDefinitions import *
from DisplacedSUSY.ParkingData.CutDefinitions import *

# Triggers with no selections
MuMuTrigger = cms.PSet(
    name = cms.string("MuMuTrigger"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet (
        ),
    )

ParkingTrigger = cms.PSet(
    name = cms.string("ParkingTrigger"),
    triggers = triggersParkingData,
    cuts = cms.VPSet (
        muon_d0Sig_greaterThan6_cut, #for 2018 signal samples b/c parking triggers are not available
        ),
    )

# MuMu Preselection as definied by the mu-mu channel
MuMuPreselection = cms.PSet(
    name = cms.string("MuMuPreselection"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet (
        muon_pt_50_cut,
        muon_eta_cut,
        muon_global_cut,
        muon_id_cut,
        muon_iso_cut,
        ),
    )

MuMuPreselectionNoPt = cms.PSet(
    name = cms.string("MuMuPreselectionNoPt"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet (
        ),
    )
MuMuPreselectionNoPt.cuts.append(muon_eta_cut)
MuMuPreselectionNoPt.cuts.append(muon_global_cut)
MuMuPreselectionNoPt.cuts.append(muon_id_cut)
MuMuPreselectionNoPt.cuts.append(muon_iso_cut)

ParkingPreselection = cms.PSet(
    name = cms.string("ParkingPreselection"),
    triggers = triggersParkingData,
    cuts = cms.VPSet (
        muon_eta_lessThan2p4_cut,
        muon_tightID_cut,
        muon_global_cut,
        diMuon_deltaR_greaterThanP2_cut,
        diMuon_cosAlpha_veto,
        ),
    )

ParkingPreselectionD0Sig = copy.deepcopy(ParkingPreselection)
ParkingPreselectionD0Sig.name = cms.string("ParkingPreselectionD0Sig")
#ParkingPreselectionD0Sig.cuts.append(muon_d0Sig_6_cut)


ParkingPreselectionNoPt = cms.PSet(
    name = cms.string("ParkingPreselectionNoPt"),
    triggers = triggersParkingData,
    cuts = cms.VPSet (
        muon_eta_lessThan2p4_cut,
        muon_softID_cut,
        ),
    )

ParkingPreselectionNoTrigger = cms.PSet(
    name = cms.string("ParkingPreselectionNoTrigger"),
    cuts = cms.VPSet (
        muon_pt_4p2_cut,
        muon_eta_lessThan2p4_cut,
        muon_softID_cut,
        ),
    )

GenMotherStopMuonTightID = cms.PSet(
    name = cms.string("GenMotherStopMuonTightID"),
    cuts = cms.VPSet (
        ),
    )
GenMotherStopMuonTightID.cuts.append(exactly2_genMu_status1_uniqueMotherIsStop_cut)
GenMotherStopMuonTightID.cuts.append(muon_tightID_cut)

GenMotherStopMuonSoftID = cms.PSet(
    name = cms.string("GenMotherStopMuonSoftID"),
    cuts = cms.VPSet (
        ),
    )
GenMotherStopMuonSoftID.cuts.append(exactly2_genMu_status1_uniqueMotherIsStop_cut)
GenMotherStopMuonSoftID.cuts.append(muon_softID_cut)

GenMotherStop = cms.PSet(
    name = cms.string("GenMotherStop"),
    cuts = cms.VPSet (
        ),
    )
GenMotherStop.cuts.append(exactly2_genMu_status1_uniqueMotherIsStop_cut)

ParkingTriggerGenMotherIsStop = cms.PSet(
    name = cms.string("ParkingTriggerGenMotherIsStop"),
    triggers = triggersParkingData,
    cuts = cms.VPSet (
        muon_d0Sig_greaterThan6_cut, #for 2018 signal samples b/c parking triggers are not available
        exactly2_genMu_status1_uniqueMotherIsStop_cut,
        ),
    )

MuMuTriggerGenMotherIsStop = cms.PSet(
    name = cms.string("MuMuTriggerGenMotherIsStop"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet (
        exactly2_genMu_status1_uniqueMotherIsStop_cut,
        ),
    )

NoSelections = cms.PSet(
    name = cms.string("NoSelections"),
    cuts = cms.VPSet (
        ),
    )
