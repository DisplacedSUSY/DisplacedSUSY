import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.ParkingData.CutDefinitions import *

#no triggers required
ParkingDataTest = cms.PSet(
    name = cms.string("ParkingDataTest"),
    cuts = cms.VPSet (
        muon_softID_cut,
        muon_eta_lessThan2p4_cut,
        muon_pt_4p2_cut,
        #diMuon_deltaR_cut
        ),
    )
