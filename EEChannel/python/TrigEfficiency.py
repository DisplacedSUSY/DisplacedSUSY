import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EEChannel.CutDefinitions import *

# Denominator: basic 2 electron selection+(MET triggers)
TrigEffDen = cms.PSet(
    name = cms.string("TrigEffDen"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### passes OR of unprescaled MET triggers (use eventvariable so that OR of MET triggers can be ANDed with analysis trigger)
TrigEffDen.cuts.append(pass_HLTMET_paths)
### at least two good electrons
TrigEffDen.cuts.append(electron_eta_cut)
TrigEffDen.cuts.append(electron_gap_veto)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    TrigEffDen.cuts.append(electron_eta_phi_veto_2017) #veto region with pixel power supply issues
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    TrigEffDen.cuts.append(electron_eta_phi_veto_2018) #veto region with pixel power supply issues
TrigEffDen.cuts.append(electron_id_cut) #electron vid normally includes isolation, but we take it out in customize.py
TrigEffDen.cuts.append(electron_newIso_cut) #our custom rho-based iso

# Numerator: basic 2 electron selection+(MET triggers)+(analysis trigger)
TrigEffNum = cms.PSet(
    name = cms.string("TrigEffNum"),
    triggers = triggersDoublePhoton,
    cuts = cms.VPSet(copy.deepcopy(TrigEffDen.cuts))
)


#######################################
# apply pt cut and apply trigger scale factors, to look at trigger efficiency as a function of d0
TrigEffDenInPtPlateau = cms.PSet(
    name = cms.string("TrigEffDenInPtPlateau"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TrigEffDen.cuts))
)
TrigEffDenInPtPlateau.cuts.append(electron_pt_75_cut) #measure only in pt plateau

TrigEffNumInPtPlateau = cms.PSet(
    name = cms.string("TrigEffNumInPtPlateau"),
    triggers = triggersDoublePhoton,
    cuts = cms.VPSet(copy.deepcopy(TrigEffDenInPtPlateau.cuts))
)

#######################################
# add d0 cut to get closer to signal region
TrigEffDenD0GreaterThan10 = cms.PSet(
    name = cms.string("TrigEffDenD0GreaterThan10"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(TrigEffDen.cuts))
)
TrigEffDenD0GreaterThan10.cuts.append(electron_d0_greaterThan10_cut)

TrigEffNumD0GreaterThan10 = cms.PSet(
    name = cms.string("TrigEffNumD0GreaterThan10"),
    triggers = triggersDoublePhoton,
    cuts = cms.VPSet(copy.deepcopy(TrigEffDenD0GreaterThan10.cuts))
)
