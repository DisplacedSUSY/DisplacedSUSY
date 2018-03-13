import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EEChannel.Preselection import *

##########################################################################
###### Set up the Z control region for the displaced SUSY analysis #######
##########################################################################

##########################################################################

ZControlRegion = copy.deepcopy(Preselection)
ZControlRegion.name = cms.string("ZControlRegion")

ZControlRegion.cuts.append(electron_jet_deltaR_cut)
ZControlRegion.cuts.append(electron_2electron_cut)
### invMass in Z range
ZControlRegion.cuts.append(diElectron_invMass_Z_cut)

ZControlRegion.cuts.append(electron_fiducial_phi_cut)


prompt_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) < 200"),
    numberRequired = cms.string(">= 1")
    )
displaced_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("10000*abs(d0) > 200 & 10000*abs(d0) < 1000"),
    numberRequired = cms.string(">= 1")
    )
very_displaced_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
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

