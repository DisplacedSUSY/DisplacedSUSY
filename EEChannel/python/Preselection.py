import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EEChannel.CutDefinitions import *

#################################################################
### Set up the preselection for the displaced SUSY analysis #####
#################################################################

Preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = triggersDoublePhoton,
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
Preselection.cuts.extend(atLeastZero_jet_basic_selection_cuts)
### at least two good electrons
Preselection.cuts.append(electron_eta_cut)
Preselection.cuts.append(electron_gap_veto)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    Preselection.cuts.append(electron_eta_phi_veto_2017) #veto region with pixel power supply issues
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    Preselection.cuts.append(electron_eta_phi_veto_2018) #veto region with pixel power supply issues
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    Preselection.cuts.append(electron_pt_65_cut)
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    Preselection.cuts.append(electron_pt_75_cut)
Preselection.cuts.append(electron_id_cut) #electron vid normally includes isolation, but we take it out in customize.py
Preselection.cuts.append(electron_newIso_cut) #our custom rho-based iso
Preselection.cuts.append(diElectron_deltaR_cut) # remove hypothetical electrons from mesons that are close to each other (loose dR>0.2)
Preselection.cuts.append(ee_noDispVtxsInMaterial_cut)
### remove events with displaced muons that would pass the emu preselection
Preselection.cuts.append(muon_emu_preselection_filter_part1)
Preselection.cuts.append(muon_emu_preselection_filter_part2)
Preselection.cuts.append(muon_d0_greaterThan100_veto)


#worry about the barrel only in the id cuts
DenMissingInnerHitsSel = cms.PSet(
    name = cms.string("DenMissingInnerHitsSel"),
    triggers = triggersDoublePhoton,
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
DenMissingInnerHitsSel.cuts.extend(atLeastZero_jet_basic_selection_cuts)
### at least two good electrons
DenMissingInnerHitsSel.cuts.append(electron_eta_cut)
DenMissingInnerHitsSel.cuts.append(electron_gap_veto)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    DenMissingInnerHitsSel.cuts.append(electron_eta_phi_veto_2017) #veto region with pixel power supply issues
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    DenMissingInnerHitsSel.cuts.append(electron_eta_phi_veto_2018) #veto region with pixel power supply issues
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    DenMissingInnerHitsSel.cuts.append(electron_pt_65_cut)
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    DenMissingInnerHitsSel.cuts.append(electron_pt_75_cut)
DenMissingInnerHitsSel.cuts.append(electron_isEB_cut)
DenMissingInnerHitsSel.cuts.append(electron_sigmaIetaIetaEB_cut)
DenMissingInnerHitsSel.cuts.append(electron_deltaPhiSuperClusterEB_cut)
DenMissingInnerHitsSel.cuts.append(electron_deltaEtaSuperClusterEB_cut)
DenMissingInnerHitsSel.cuts.append(electron_hadronicOverEmEB_cut)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    DenMissingInnerHitsSel.cuts.append(electron_abs_1overE_1overP_cut)
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    DenMissingInnerHitsSel.cuts.append(electron_abs_1overE_1overP_EB_cut)
DenMissingInnerHitsSel.cuts.append(electron_passConversionVeto_cut)
DenMissingInnerHitsSel.cuts.append(electron_newIso_cut) #our custom rho-based iso
DenMissingInnerHitsSel.cuts.append(diElectron_deltaR_cut) # remove hypothetical electrons from mesons that are close to each other (loose dR>0.2)
DenMissingInnerHitsSel.cuts.append(ee_noDispVtxsInMaterial_cut)
### remove events with displaced muons that would pass the emu preselection
DenMissingInnerHitsSel.cuts.append(muon_emu_preselection_filter_part1)
DenMissingInnerHitsSel.cuts.append(muon_emu_preselection_filter_part2)
DenMissingInnerHitsSel.cuts.append(muon_d0_greaterThan100_veto)

NumMissingInnerHitsSel = cms.PSet(
    name = cms.string("NumMissingInnerHitsSel"),
    triggers = copy.deepcopy(DenMissingInnerHitsSel.triggers),
    cuts = cms.VPSet (copy.deepcopy(DenMissingInnerHitsSel.cuts))
)
NumMissingInnerHitsSel.cuts.append(electron_missingInnerHits_cut)

ElectronD00to40ElectronD0Above100Region = copy.deepcopy(Preselection)
ElectronD00to40ElectronD0Above100Region.name = cms.string("ElectronD00to40ElectronD0Above100Region")
ElectronD00to40ElectronD0Above100Region.cuts.append(electron_onePrompt_oneDisplaced_cut)

ElectronD00to40ElectronD00to100Region = copy.deepcopy(Preselection)
ElectronD00to40ElectronD00to100Region.name = cms.string("ElectronD00to40ElectronD00to100Region")
ElectronD00to40ElectronD00to100Region.cuts.append(electron_onePrompt_0to40_one_lessThan100_cut)

ElectronD00to40ElectronD0100to500Region = copy.deepcopy(Preselection)
ElectronD00to40ElectronD0100to500Region.name = cms.string("ElectronD00to40ElectronD0100to500Region")
ElectronD00to40ElectronD0100to500Region.cuts.append(electron_onePrompt_0to40_oneDisplaced_100to500_cut)

ElectronD00to40ElectronD0500to1000Region = copy.deepcopy(Preselection)
ElectronD00to40ElectronD0500to1000Region.name = cms.string("ElectronD00to40ElectronD0500to1000Region")
ElectronD00to40ElectronD0500to1000Region.cuts.append(electron_onePrompt_0to40_oneDisplaced_500to1000_cut)


#################################################################

PromptControlRegion = copy.deepcopy(Preselection)
PromptControlRegion.name = cms.string("PromptControlRegion")
PromptControlRegion.cuts.append(electron_d0_lessThan50_cut)

#################################################################

DisplacedControlRegion = copy.deepcopy(Preselection)
DisplacedControlRegion.name = cms.string("DisplacedControlRegion")
#DisplacedControlRegion.cuts.append(electron_d0_100to200_cut)
DisplacedControlRegion.cuts.append(electron_d0_10to20_cut)


DisplacedGreaterThan100 = copy.deepcopy(Preselection)
DisplacedGreaterThan100.name = cms.string("DisplacedGreaterThan100")
DisplacedGreaterThan100.cuts.append(electron_d0_greaterThan100_cut)


#################################################################

ZControlRegion = copy.deepcopy(Preselection)
ZControlRegion.name = cms.string("ZControlRegion")
ZControlRegion.cuts.append(electron_jet_deltaR_overlap_veto)
ZControlRegion.cuts.append(electron_2electron_cut)
ZControlRegion.cuts.append(diElectron_invMass_Z_cut) ### invMass in Z range
ZControlRegion.cuts.append(electron_fiducial_phi_cut)

#################################################################

InclusiveSignalRegion = copy.deepcopy(Preselection)
InclusiveSignalRegion.name = cms.string("InclusiveSignalRegion")
InclusiveSignalRegion.cuts.append(electron_d0_greaterThan100_cut)
InclusiveSignalRegion.cuts.append(electron_d0_lessThan10cm_cut)

#################################################################

PromptLowPtControlRegion = copy.deepcopy(PromptControlRegion)
PromptLowPtControlRegion.name = cms.string("PromptLowPtControlRegion")
PromptLowPtControlRegion.cuts.append(electron_pt_100_veto)

#################################################################

PromptHighPtControlRegion = copy.deepcopy(PromptControlRegion)
PromptHighPtControlRegion.name = cms.string("PromptHighPtControlRegion")
PromptHighPtControlRegion.cuts.append(electron_pt_100_cut)

#################################################################

DisplacedLowPtControlRegion = copy.deepcopy(InclusiveSignalRegion)
DisplacedLowPtControlRegion.name = cms.string("DisplacedLowPtControlRegion")
DisplacedLowPtControlRegion.cuts.append(electron_pt_100_veto)

#################################################################

DisplacedHighPtControlRegion = copy.deepcopy(InclusiveSignalRegion)
DisplacedHighPtControlRegion.name = cms.string("DisplacedHighPtControlRegion")
DisplacedHighPtControlRegion.cuts.append(electron_pt_100_cut)

#################################################################

DisplacedHighPtL1PrefiringCheck = copy.deepcopy(DisplacedHighPtControlRegion)
DisplacedHighPtL1PrefiringCheck.name = cms.string("DisplacedHighPtL1PrefiringCheck")
DisplacedHighPtL1PrefiringCheck.cuts.extend(L1PrefiringCheck_cuts)

PreselectionLeptonsFromW = cms.PSet(
    name = cms.string("PreselectionLeptonsFromW"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsFromW.cuts.append(electron_gen_motherIsW_cut)

PreselectionLeptonsFromWorZ = cms.PSet(
        name = cms.string("PreselectionLeptonsFromWorZ"),
        triggers = copy.deepcopy(Preselection.triggers),
        cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
    )
PreselectionLeptonsFromWorZ.cuts.append(electron_gen_motherIsWorZ_cut)

PreselectionLeptonsFromTau = cms.PSet(
    name = cms.string("PreselectionLeptonsFromTau"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsFromTau.cuts.append(electron_gen_motherIsTau_cut)

PreselectionLeptonsNotFromTau = cms.PSet(
    name = cms.string("PreselectionLeptonsNotFromTau"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsNotFromTau.cuts.append(electron_gen_motherIsNotTau_cut)

Preselection2TausFromZ = cms.PSet(
    name = cms.string("Preselection2TausFromZ"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
Preselection2TausFromZ.cuts.append(exactly2_genTau_uniqueMotherIsZ_cut)

PreselectionEleFromLightMeson = cms.PSet(
    name = cms.string("PreselectionEleFromLightMeson"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionEleFromLightMeson.cuts.append(electron_gen_motherIsLightMeson_cut)

PreselectionEleFromHeavyMeson = cms.PSet(
    name = cms.string("PreselectionEleFromHeavyMeson"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionEleFromHeavyMeson.cuts.append(electron_gen_motherIsHeavyMeson_cut)



InvertDispVtxInMaterialPreselection = cms.PSet(
    name = cms.string("InvertDispVtxInMaterialPreselection"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
replaceSingleCut(InvertDispVtxInMaterialPreselection.cuts, ee_invertNoDispVtxsInMaterial_cut, ee_noDispVtxsInMaterial_cut)
#################################################################

GenEEFromStopsSelection = cms.PSet(
    name = cms.string("GenEEFromStopsSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet([exactly2_genEle_status1_uniqueMotherIsStop_cut,
                      #atLeastTwo_genLxy_lessThan50cm_cut,
                      #atLeastTwo_genLxy_lessThan1cm_cut,
                      #atLeastTwo_genEta_cut,
                ])
)
#if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    #GenEEFromStopsSelection.cuts.append(atLeastTwo_genPt_65_cut)
#elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    #GenEEFromStopsSelection.cuts.append(atLeastTwo_genPt_75_cut)
#GenEEFromStopsSelection.cuts.append(cutDummyElectron)

#HLT
GenEEFromStopsAndHLTTrigSelection = cms.PSet(
    name = cms.string("GenEEFromStopsAndHLTTrigSelection"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(GenEEFromStopsSelection.cuts))
)

#L1
GenEEFromStopsAndL1TrigSelection = cms.PSet(
    name = cms.string("GenEEFromStopsAndL1TrigSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)
GenEEFromStopsAndL1TrigSelection.cuts.append(pass_L1EG_OR_L1Jet_Seeds) #need L1 cut first and then gen cuts, otherwise hardIntMcpart hists get screwed up!
GenEEFromStopsAndL1TrigSelection.cuts.extend(copy.deepcopy(GenEEFromStopsSelection.cuts))

#################################################################

PreselectionD0Pull50um = cms.PSet(
    name = cms.string("PreselectionD0Pull50um"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionD0Pull50um.cuts.append(electron_absD0Pull_lessThan50_cut)
