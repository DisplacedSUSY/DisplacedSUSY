import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.MuMuChannel.CutDefinitions import *

#no triggers required
MuMuPreselection = cms.PSet(
    name = cms.string("ParkingDataTest"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet (
        ),
    )
MuMuPreselection.cuts.append(muon_pt_50_cut)
MuMuPreselection.cuts.append(muon_eta_cut)
MuMuPreselection.cuts.append(muon_global_cut)
MuMuPreselection.cuts.append(muon_id_cut)
MuMuPreselection.cuts.append(muon_iso_cut)

from DisplacedSUSY.ParkingData.CutDefinitions import *

#no triggers required
ParkingPreselection = cms.PSet(
    name = cms.string("ParkingPreselection"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet (
        muon_pt_4p2_cut,
        muon_eta_lessThan2p4_cut,
        muon_softID_cut,
        ),
    )
