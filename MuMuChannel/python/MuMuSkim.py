import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.MuMuChannel.CutDefinitions import *

#at least two good muons
#no triggers required
MuMuSkim = cms.PSet(
    name = cms.string("MuMuSkim"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet (
        muon_eta_cut,
        muon_pt_20_cut,
        muon_global_cut
        ),
    )

