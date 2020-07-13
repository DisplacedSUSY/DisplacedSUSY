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
### at least 2 good muons
TrigEffDen.cuts.append(muon_eta_cut)
TrigEffDen.cuts.append(muon_global_cut)
TrigEffDen.cuts.append(muon_id_cut)

# Numerator: basic 2 muon selection+(MET triggers)+(analysis trigger)
TrigEffNum = cms.PSet(
    name = cms.string("TrigEffNum"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet(copy.deepcopy(TrigEffDen.cuts))
)
