import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.ParkingData.CutDefinitions import *

#no triggers required
ParkingDataTest = cms.PSet(
    name = cms.string("ParkingDataTest"),
    #triggers = triggersParkingData,
    cuts = cms.VPSet (
        muon_softID_cut,
        muon_eta_lessThan2p4_cut,
        muon_pt_4p2_cut,
        ),
    )

promptMuons = copy.deepcopy(ParkingDataTest)
promptMuons.name = cms.string("promptMuons")
promptMuons.cuts.append(muon_d0_lessThan50_cut)

displacedMuons = copy.deepcopy(ParkingDataTest)
displacedMuons.name = cms.string("displacedMuons")
displacedMuons.cuts.append(muon_d0_greaterThan50_cut)

ParkingDataJPsi =  copy.deepcopy(ParkingDataTest)
ParkingDataJPsi.name = cms.string("ParkingDataJPsi")
ParkingDataJPsi.cuts.append(diMuon_invMass_greaterThan2p9_cut)
ParkingDataJPsi.cuts.append(diMuon_invMass_lessThan3p2_cut)

displacedHighPtJPsi =  copy.deepcopy(ParkingDataJPsi)
displacedHighPtJPsi.name =  cms.string("displacedHighPtJPsi")
#displacedHighPtJPsi.cuts.append(muon_pt_100_cut)
displacedHighPtJPsi.cuts.append(muon_pt_15_cut)
#displacedHighPtJPsi.cuts.append(muon_d0_greaterThan50_cut)
displacedHighPtJPsi.cuts.append(muon_d0_greaterThan300_cut)

displacedLowPtJPsi =  copy.deepcopy(ParkingDataJPsi)
displacedLowPtJPsi.name =  cms.string("displacedLowPtJPsi")
#displacedLowPtJPsi.cuts.append(muon_pt_100_veto)
displacedLowPtJPsi.cuts.append(muon_pt_15_veto)
#displacedLowPtJPsi.cuts.append(muon_d0_greaterThan50_cut)
displacedLowPtJPsi.cuts.append(muon_d0_greaterThan300_cut)

promptHighPtJPsi =  copy.deepcopy(ParkingDataJPsi)
promptHighPtJPsi.name =  cms.string("promptHighPtJPsi")
#promptHighPtJPsi.cuts.append(muon_pt_100_cut)
promptHighPtJPsi.cuts.append(muon_pt_15_cut)
#promptHighPtJPsi.cuts.append(muon_d0_lessThan50_cut)
promptHighPtJPsi.cuts.append(muon_d0_lessThan300_cut)

promptLowPtJPsi =  copy.deepcopy(ParkingDataJPsi)
promptLowPtJPsi.name =  cms.string("promptLowPtJPsi")
#promptLowPtJPsi.cuts.append(muon_pt_100_veto)
promptLowPtJPsi.cuts.append(muon_pt_15_veto)
#promptLowPtJPsi.cuts.append(muon_d0_lessThan50_cut)
promptLowPtJPsi.cuts.append(muon_d0_lessThan300_cut)

signalNoCuts = cms.PSet(
    name = cms.string("signalNoCuts"),
    cuts = cms.VPSet (
        muon_pt_25_dummy_cut,
        muon_softID_dummy,
        muon_tightID_dummy,
        muon_eta_lessThan2p4_dummy,
        muon_pt_4p2_dummy,
        ),
    )
