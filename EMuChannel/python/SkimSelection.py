import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

##########################################################################
##### Set up the EMu Skim Selections for the displaced SUSY analysis #####
##########################################################################

SkimSelection = cms.PSet(
    name = cms.string("SkimSelection"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet()
)
### at least one good electron
SkimSelection.cuts.append(electron_eta_cut)
SkimSelection.cuts.append(electron_pt_25_cut)
### at least one good muon
SkimSelection.cuts.append(muon_eta_cut)
SkimSelection.cuts.append(muon_pt_25_cut)
SkimSelection.cuts.append(muon_global_cut)
