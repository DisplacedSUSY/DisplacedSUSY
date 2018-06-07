import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *

#################################################################
### Set up the preselection for the displaced SUSY analysis #####
#################################################################

Preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = triggersMuonPhoton,
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
Preselection.cuts.extend(atLeastZero_jet_basic_selection_cuts)
### at least one good electron
Preselection.cuts.append(electron_eta_cut)
Preselection.cuts.append(electron_gap_veto)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    Preselection.cuts.append(electron_pt_42_cut)
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    Preselection.cuts.append(electron_pt_50_cut)
Preselection.cuts.append(electron_id_cut) #electron vid includes isolation
### at least one good muon
Preselection.cuts.append(muon_eta_cut)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    Preselection.cuts.append(muon_pt_40_cut)
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    Preselection.cuts.append(muon_pt_50_cut)
Preselection.cuts.append(muon_global_cut)
Preselection.cuts.append(muon_id_cut)
Preselection.cuts.append(muon_iso_cut)


PromptControlRegion = cms.PSet(
    name = cms.string("PromptControlRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PromptControlRegion.cuts.append(electron_d0_lessThan10_cut)
PromptControlRegion.cuts.append(muon_d0_lessThan10_cut)


DisplacedControlRegion = cms.PSet(
    name = cms.string("DisplacedControlRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
DisplacedControlRegion.cuts.append(electron_d0_100to200_cut)
DisplacedControlRegion.cuts.append(muon_d0_100to200_cut)


InclusiveSignalRegion = cms.PSet(
    name = cms.string("InclusiveSignalRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
InclusiveSignalRegion.cuts.append(electron_d0_greaterThan200_cut)
InclusiveSignalRegion.cuts.append(muon_d0_greaterThan200_cut)


PreselectionPromptElectron = cms.PSet(
    name = cms.string("PreselectionPromptElectron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionPromptElectron.cuts.append(electron_d0_lessThan200_cut)


PreselectionPromptMuon = cms.PSet(
    name = cms.string("PreselectionPromptMuon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionPromptMuon.cuts.append(muon_d0_lessThan200_cut)


PreselectionVeryPromptElectron = cms.PSet(
    name = cms.string("PreselectionVeryPromptElectron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionVeryPromptElectron.cuts.append(electron_d0_lessThan100_cut)


PreselectionVeryPromptMuon = cms.PSet(
    name = cms.string("PreselectionVeryPromptMuon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionVeryPromptMuon.cuts.append(muon_d0_lessThan100_cut)


PreselectionIntermediateElectron = cms.PSet(
    name = cms.string("PreselectionIntermediateElectron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionIntermediateElectron.cuts.append(electron_d0_100to200_cut)


PreselectionIntermediateMuon = cms.PSet(
    name = cms.string("PreselectionIntermediateMuon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionIntermediateMuon.cuts.append(muon_d0_100to200_cut)

PreselectionCorrelatedD0 = cms.PSet(
    name = cms.string("PreselectionCorrelatedD0"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionCorrelatedD0.cuts.append(emu_correlated_d0_cut)

PreselectionUncorrelatedD0 = cms.PSet(
    name = cms.string("PreselectionUncorrelatedD0"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionUncorrelatedD0.cuts.append(emu_uncorrelated_d0_cut)

PreselectionCorrelatedGenD0 = cms.PSet(
    name = cms.string("PreselectionCorrelatedGenD0"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionCorrelatedGenD0.cuts.append(emu_correlated_genD0_cut)

PreselectionUncorrelatedGenD0 = cms.PSet(
    name = cms.string("PreselectionUncorrelatedGenD0"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionUncorrelatedGenD0.cuts.append(emu_uncorrelated_genD0_cut)



PreselectionLeptonsFromW = cms.PSet(
    name = cms.string("PreselectionLeptonsFromW"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsFromW.cuts.append(electron_gen_motherIsW_cut)
PreselectionLeptonsFromW.cuts.append(muon_gen_motherIsW_cut)
