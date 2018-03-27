import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.Preselection import *

#################################################################
### Set up the updated analysis regions for the displaced SUSY analysis #####
#################################################################


NewPromptControlRegion = cms.PSet(
    name = cms.string("NewPromptControlRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
NewPromptControlRegion.cuts.append(electron_d0_lessThan10_cut)
NewPromptControlRegion.cuts.append(muon_d0_lessThan10_cut)


NewDisplacedControlRegion = cms.PSet(
    name = cms.string("NewDisplacedControlRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
NewDisplacedControlRegion.cuts.append(electron_d0_10to20_cut)
NewDisplacedControlRegion.cuts.append(muon_d0_10to20_cut)


NewInclusiveSignalRegion = cms.PSet(
    name = cms.string("NewInclusiveSignalRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
NewInclusiveSignalRegion.cuts.append(electron_d0_greaterThan20_cut)
NewInclusiveSignalRegion.cuts.append(muon_d0_greaterThan40_cut)


NewPreselectionPromptElectron = cms.PSet(
    name = cms.string("NewPreselectionPromptElectron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
NewPreselectionPromptElectron.cuts.append(electron_d0_lessThan20_cut)


NewPreselectionPromptMuon = cms.PSet(
    name = cms.string("NewPreselectionPromptMuon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
NewPreselectionPromptMuon.cuts.append(muon_d0_lessThan40_cut)


NewPreselectionVeryPromptElectron = cms.PSet(
    name = cms.string("NewPreselectionVeryPromptElectron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
NewPreselectionVeryPromptElectron.cuts.append(electron_d0_lessThan10_cut)


NewPreselectionVeryPromptMuon = cms.PSet(
    name = cms.string("NewPreselectionVeryPromptMuon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
NewPreselectionVeryPromptMuon.cuts.append(muon_d0_lessThan10_cut)


NewPreselectionIntermediateElectron = cms.PSet(
    name = cms.string("NewPreselectionIntermediateElectron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
NewPreselectionIntermediateElectron.cuts.append(electron_d0_10to20_cut)


NewPreselectionIntermediateMuon = cms.PSet(
    name = cms.string("NewPreselectionIntermediateMuon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
NewPreselectionIntermediateMuon.cuts.append(muon_d0_10to20_cut)
