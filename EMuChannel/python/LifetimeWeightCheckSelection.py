import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

##########################################################################
######### Set up a dummy selection to check lifetime weights #############
##########################################################################

LifetimeWeightCheckSelection = cms.PSet(
    name = cms.string("LifetimeWeightCheckSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)

### Dummy cuts
LifetimeWeightCheckSelection.cuts.append(jet_pt_30_cut)
LifetimeWeightCheckSelection.cuts.append(electron_pt_25_dummy_cut)
LifetimeWeightCheckSelection.cuts.append(muon_pt_25_dummy_cut)
