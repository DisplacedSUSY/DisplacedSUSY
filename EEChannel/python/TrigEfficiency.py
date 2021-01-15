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
### at least 2 good electrons
TrigEffDen.cuts.append(electron_eta_cut)
TrigEffDen.cuts.append(electron_gap_veto)
TrigEffDen.cuts.append(electron_id_cut)

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
