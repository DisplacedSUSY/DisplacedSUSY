import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

# Denominator: basic 2 muon selection+(MET triggers)
TrigEffDen = cms.PSet(
    name = cms.string("TrigEffDen"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### passes OR of unprescaled MET triggers (use eventvariable so that OR of MET triggers can be ANDed with analysis trigger)
TrigEffDen.cuts.append(pass_HLTMET_paths)
### at least two good muons
TrigEffDen.cuts.append(muon_eta_cut)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    TrigEffDen.cuts.append(muon_eta_phi_veto_2017) #veto region with pixel power supply issues
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    TrigEffDen.cuts.append(muon_eta_phi_veto_2018) #veto region with pixel power supply issues
TrigEffDen.cuts.append(muon_global_cut)
TrigEffDen.cuts.append(muon_id_cut)
TrigEffDen.cuts.append(muon_iso_cut) #our custom rho-based iso

# Numerator: basic 2 muon selection+(MET triggers)+(analysis trigger)
TrigEffNum = cms.PSet(
    name = cms.string("TrigEffNum"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet(copy.deepcopy(TrigEffDen.cuts))
)

#######################################
# apply pt cut and apply trigger scale factors, to look at trigger efficiency as a function of d0
TrigEffDenInPtPlateau = cms.PSet(
    name = cms.string("TrigEffDenInPtPlateau"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TrigEffDen.cuts))
)
TrigEffDenInPtPlateau.cuts.append(muon_pt_45_cut) #measure only in pt plateau

TrigEffNumInPtPlateau = cms.PSet(
    name = cms.string("TrigEffNumInPtPlateau"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet(copy.deepcopy(TrigEffDenInPtPlateau.cuts))
)

#######################################
# add d0 cut to get closer to signal region
TrigEffDenD0GreaterThan20 = cms.PSet(
    name = cms.string("TrigEffDenD0GreaterThan20"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TrigEffDen.cuts))
)
TrigEffDenD0GreaterThan20.cuts.append(muon_d0_greaterThan20_cut)

TrigEffNumD0GreaterThan20 = cms.PSet(
    name = cms.string("TrigEffNumD0GreaterThan20"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet(copy.deepcopy(TrigEffDenD0GreaterThan20.cuts))
)
