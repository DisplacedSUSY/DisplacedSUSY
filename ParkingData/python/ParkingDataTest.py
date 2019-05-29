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
        ),
    )

closeMuons = copy.deepcopy(ParkingDataTest)
closeMuons.name = cms.string("closeMuons")
closeMuons.cuts.append(diMuon_deltaR_lessThanP5_cut)

farMuons = copy.deepcopy(ParkingDataTest)
farMuons.name = cms.string("farMuons")
farMuons.cuts.append(diMuon_deltaR_greaterThanP5_cut)

promptMuons = copy.deepcopy(ParkingDataTest)
promptMuons.name = cms.string("promptMuons")
promptMuons.cuts.append(muon_d0_lessThan50_cut)

displacedMuons = copy.deepcopy(ParkingDataTest)
displacedMuons.name = cms.string("displacedMuons")
displacedMuons.cuts.append(muon_d0_greaterThan50_cut)
