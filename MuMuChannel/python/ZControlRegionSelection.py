import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

##########################################################################
###### Set up the Z control region for the displaced SUSY analysis #######
##########################################################################

##########################################################################
#Selections without triggers

ZControlRegion = cms.PSet(
    name = cms.string("ZControlRegion"),
    triggers = cms.vstring("HLT_DoubleMu33NoFiltersNoVtx_v"),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
ZControlRegion.cuts.append(jet_eta_cut)
ZControlRegion.cuts.append(jet_pt_30_cut)
ZControlRegion.cuts.append(jet_id_cut)
### at least two good muons
ZControlRegion.cuts.append(muon_eta_cut)
ZControlRegion.cuts.append(muon_pt_40_cut)
ZControlRegion.cuts.append(muon_global_cut)
ZControlRegion.cuts.append(muon_id_cut)
ZControlRegion.cuts.append(muon_iso_cut)
ZControlRegion.cuts.append(muonjet_deltaR_veto)
ZControlRegion.cuts.append(muon_2muon_cut)
### invMass in Z range
ZControlRegion.cuts.append(diMuon_invMass_Z_cut)

fiducial_phi_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(abs(phi)-3.14159/2) > 0.05"),
    numberRequired = cms.string(">= 2")
    )
ZControlRegion.cuts.append(fiducial_phi_cut)


prompt_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 1")
    )
displaced_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) > 200 & 10000*abs(d0) < 1000"),
    numberRequired = cms.string(">= 1")
    )
very_displaced_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("10000*abs(d0) > 1000"),
    numberRequired = cms.string(">= 1")
    )


ZControlRegionPrompt = cms.PSet(
    name = cms.string("ZControlRegionPrompt"),
    triggers = cms.vstring(),
    cuts = copy.deepcopy(ZControlRegion.cuts)
)
ZControlRegionPrompt.cuts.append(prompt_cut)

ZControlRegionDisplaced = cms.PSet(
    name = cms.string("ZControlRegionDisplaced"),
    triggers = cms.vstring(),
    cuts = copy.deepcopy(ZControlRegion.cuts)
)
ZControlRegionDisplaced.cuts.append(displaced_cut)

ZControlRegionVeryDisplaced = cms.PSet(
    name = cms.string("ZControlRegionVeryDisplaced"),
    triggers = cms.vstring(),
    cuts = copy.deepcopy(ZControlRegion.cuts)
)
ZControlRegionVeryDisplaced.cuts.append(very_displaced_cut)

#### the following are experimental cuts aimied at rejecting fake displaced muons
# d0err_cut = cms.PSet(
#     inputCollection = cms.vstring("muons"),
#     cutString = cms.string("10000*innerTrack.d0Error < 20"),
#     numberRequired = cms.string(">= 2")
#     )
# ZControlRegion.cuts.append(d0err_cut)

# missingmiddlehits_cut = cms.PSet(
#     inputCollection = cms.vstring("muons"),
#     cutString = cms.string("missingMiddleHits < 2"),
#     numberRequired = cms.string(">= 2")
#     )
# ZControlRegion.cuts.append(missingmiddlehits_cut)

# trackhits_cut = cms.PSet(
#     inputCollection = cms.vstring("muons"),
#     cutString = cms.string("innerTrack.hitPattern_.trackerLayersWithMeasurement >= 10"),
#     numberRequired = cms.string(">= 2")
#     )
# ZControlRegion.cuts.append(trackhits_cut)

# muonhits_cut = cms.PSet(
#     inputCollection = cms.vstring("muons"),
#     cutString = cms.string("numberOfValidHits >= 12"),
#     numberRequired = cms.string(">= 2")
#     )
# ZControlRegion.cuts.append(muonhits_cut)
