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
TrigEffDen.cuts.extend(atLeastOne_electron_basic_selection_cuts)
TrigEffDen.cuts.extend(atLeastOne_muon_basic_selection_cuts)

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
