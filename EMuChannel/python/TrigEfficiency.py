import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *
from DisplacedSUSY.StandardAnalysis.Triggers import *


# Denominator: basic selection+(MET triggers)
TrigEffDen = cms.PSet(
    name = cms.string("TrigEffDen"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### passes OR of unprescaled MET triggers (use eventvariable so that OR of MET triggers can be ANDed with analysis trigger)
TrigEffDen.cuts.append(pass_HLTMET_paths)
TrigEffDen.cuts.append(electron_eta_cut)
TrigEffDen.cuts.append(electron_gap_veto)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    TrigEffDen.cuts.append(electron_eta_phi_veto_2017) #veto region with pixel power supply issues
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    TrigEffDen.cuts.append(electron_eta_phi_veto_2018) #veto region with pixel power supply issues
TrigEffDen.cuts.append(electron_id_cut) #electron vid normally includes isolation, but we take it out in customize.py
TrigEffDen.cuts.append(electron_newIso_cut) #our custom rho-based iso
### at least one good muon
TrigEffDen.cuts.append(muon_eta_cut)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    TrigEffDen.cuts.append(muon_eta_phi_veto_2017) #veto region with pixel power supply issues
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    TrigEffDen.cuts.append(muon_eta_phi_veto_2018) #veto region with pixel power supply issues
TrigEffDen.cuts.append(muon_global_cut)
TrigEffDen.cuts.append(muon_id_cut)
TrigEffDen.cuts.append(muon_iso_cut) #our custom rho-based iso


### Require high-pt electron when looking at muon leg eff, to separate out effects
TrigEffHighPtEleDen = cms.PSet(
    name = cms.string("TrigEffHighPtEleDen"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TrigEffDen.cuts))
)
TrigEffHighPtEleDen.cuts.append(electron_pt_50_cut)


# Numerator: basic selection+high pt other leg+(MET triggers)+(analysis trigger)
TrigEffHighPtEleNum = cms.PSet(
    name = cms.string("TrigEffHighPtEleNum"),
    triggers = triggersMuonPhoton,
    cuts = cms.VPSet(copy.deepcopy(TrigEffHighPtEleDen.cuts))
)



### Require high-pt muon when looking at ele leg eff, to separate out effects
TrigEffHighPtMuDen = cms.PSet(
    name = cms.string("TrigEffHighPtMuDen"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TrigEffDen.cuts))
)
TrigEffHighPtMuDen.cuts.append(muon_pt_50_cut)

# Numerator: basic selection+high pt other leg+(MET triggers)+(analysis trigger)
TrigEffHighPtMuNum = cms.PSet(
    name = cms.string("TrigEffHighPtMuNum"),
    triggers = triggersMuonPhoton,
    cuts = cms.VPSet(copy.deepcopy(TrigEffHighPtMuDen.cuts))
)


#######################################
# apply pt cut and apply trigger scale factors, to look at trigger efficiency as a function of d0
TrigEffDenInPtPlateau = cms.PSet(
    name = cms.string("TrigEffDenInPtPlateau"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TrigEffHighPtMuDen.cuts))
)
TrigEffDenInPtPlateau.cuts.append(electron_pt_50_cut) #measure only in pt plateau

TrigEffNumInPtPlateau = cms.PSet(
    name = cms.string("TrigEffNumInPtPlateau"),
    triggers = triggersMuonPhoton,
    cuts = cms.VPSet(copy.deepcopy(TrigEffDenInPtPlateau.cuts))
)


#######################################
# add d0 cut to get closer to signal region

TrigEffHighPtEleDenD0GreaterThan20 = cms.PSet(
    name = cms.string("TrigEffHighPtEleDenD0GreaterThan20"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TrigEffHighPtEleDen.cuts))
)
TrigEffHighPtEleDenD0GreaterThan20.cuts.append(muon_d0_greaterThan20_cut)
TrigEffHighPtEleDenD0GreaterThan20.cuts.append(electron_d0_greaterThan20_cut)

TrigEffHighPtEleNumD0GreaterThan20 = cms.PSet(
    name = cms.string("TrigEffHighPtEleNumD0GreaterThan20"),
    triggers = triggersMuonPhoton,
    cuts = cms.VPSet(copy.deepcopy(TrigEffHighPtEleDenD0GreaterThan20.cuts))
)

TrigEffHighPtMuDenD0GreaterThan20 = cms.PSet(
    name = cms.string("TrigEffHighPtMuDenD0GreaterThan20"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TrigEffHighPtMuDen.cuts))
)
TrigEffHighPtMuDenD0GreaterThan20.cuts.append(muon_d0_greaterThan20_cut)
TrigEffHighPtMuDenD0GreaterThan20.cuts.append(electron_d0_greaterThan20_cut)

TrigEffHighPtMuNumD0GreaterThan20 = cms.PSet(
    name = cms.string("TrigEffHighPtMuNumD0GreaterThan20"),
    triggers = triggersMuonPhoton,
    cuts = cms.VPSet(copy.deepcopy(TrigEffHighPtMuDenD0GreaterThan20.cuts))
)
