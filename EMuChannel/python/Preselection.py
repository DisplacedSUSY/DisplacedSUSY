import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *
from DisplacedSUSY.StandardAnalysis.ElectronIdCutDefinitions import *

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
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    Preselection.cuts.append(electron_eta_phi_veto_2017) #veto region with pixel power supply issues
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    Preselection.cuts.append(electron_eta_phi_veto_2018) #veto region with pixel power supply issues
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    Preselection.cuts.append(electron_pt_42_cut) #plateau of trigger turn on
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    Preselection.cuts.append(electron_pt_45_cut) #plateau of trigger turn on
Preselection.cuts.append(electron_id_cut) #electron vid normally includes isolation, but we take it out in customize.py
Preselection.cuts.append(electron_newIso_cut) #our custom rho-based iso
### at least one good muon
Preselection.cuts.append(muon_eta_cut)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    Preselection.cuts.append(muon_eta_phi_veto_2017) #veto region with pixel power supply issues
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    Preselection.cuts.append(muon_eta_phi_veto_2018) #veto region with pixel power supply issues
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    Preselection.cuts.append(muon_pt_40_cut) #plateau of trigger turn on
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    Preselection.cuts.append(muon_pt_45_cut) #plateau of trigger turn on
Preselection.cuts.append(muon_global_cut)
Preselection.cuts.append(muon_id_cut)
Preselection.cuts.append(muon_iso_cut) #our custom rho-based iso
Preselection.cuts.append(diMuon_cosAlpha_veto) #remove cosmics that are back-to-back
Preselection.cuts.append(diMuon_deltaTimeAtIpInOut_veto) #remove muons with delta time consistent with cosmics
Preselection.cuts.append(emu_deltaR_cut) #remove leptons from mesons that are very close to each other (loose dR>0.2)
Preselection.cuts.append(emu_noDispVtxsInMaterial_cut)

PromptControlRegion = cms.PSet(
    name = cms.string("PromptControlRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PromptControlRegion.cuts.append(electron_d0_lessThan50_cut)
PromptControlRegion.cuts.append(muon_d0_lessThan50_cut)


DisplacedControlRegion = cms.PSet(
    name = cms.string("DisplacedControlRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
DisplacedControlRegion.cuts.append(electron_d0_100to200_cut)
DisplacedControlRegion.cuts.append(muon_d0_100to200_cut)

MuonD00to40ElectronD00to100Region = copy.deepcopy(Preselection)
MuonD00to40ElectronD00to100Region.name = cms.string("MuonD00to40ElectronD00to100Region")
MuonD00to40ElectronD00to100Region.cuts.append(muon_d0_lessThan40_cut)
MuonD00to40ElectronD00to100Region.cuts.append(electron_d0_lessThan100_cut)

MuonD00to40ElectronD0100to500Region = copy.deepcopy(Preselection)
MuonD00to40ElectronD0100to500Region.name = cms.string("MuonD00to40ElectronD0100to500Region")
MuonD00to40ElectronD0100to500Region.cuts.append(muon_d0_lessThan40_cut)
MuonD00to40ElectronD0100to500Region.cuts.append(electron_d0_100to500_cut)

MuonD00to40ElectronD0500to1000Region = copy.deepcopy(Preselection)
MuonD00to40ElectronD0500to1000Region.name = cms.string("MuonD00to40ElectronD0500to1000Region")
MuonD00to40ElectronD0500to1000Region.cuts.append(muon_d0_lessThan40_cut)
MuonD00to40ElectronD0500to1000Region.cuts.append(electron_d0_500to1000_cut)

ElectronD00to40MuonD00to100Region = copy.deepcopy(Preselection)
ElectronD00to40MuonD00to100Region.name = cms.string("ElectronD00to40MuonD00to100Region")
ElectronD00to40MuonD00to100Region.cuts.append(electron_d0_lessThan40_cut)
ElectronD00to40MuonD00to100Region.cuts.append(muon_d0_lessThan100_cut)

ElectronD00to40MuonD0100to500Region = copy.deepcopy(Preselection)
ElectronD00to40MuonD0100to500Region.name = cms.string("ElectronD00to40MuonD0100to500Region")
ElectronD00to40MuonD0100to500Region.cuts.append(electron_d0_lessThan40_cut)
ElectronD00to40MuonD0100to500Region.cuts.append(muon_d0_100to500_cut)

ElectronD00to40MuonD0500to1000Region = copy.deepcopy(Preselection)
ElectronD00to40MuonD0500to1000Region.name = cms.string("ElectronD00to40MuonD0500to1000Region")
ElectronD00to40MuonD0500to1000Region.cuts.append(electron_d0_lessThan40_cut)
ElectronD00to40MuonD0500to1000Region.cuts.append(muon_d0_500to1000_cut)

ElectronD00to40MuonD00to40Region = copy.deepcopy(Preselection)
ElectronD00to40MuonD00to40Region.name = cms.string("ElectronD00to40MuonD00to40Region")
ElectronD00to40MuonD00to40Region.cuts.append(electron_d0_lessThan40_cut)
ElectronD00to40MuonD00to40Region.cuts.append(muon_d0_lessThan40_cut)

ElectronD00to40MuonD040to500Region = copy.deepcopy(Preselection)
ElectronD00to40MuonD040to500Region.name = cms.string("ElectronD00to40MuonD040to500Region")
ElectronD00to40MuonD040to500Region.cuts.append(electron_d0_lessThan40_cut)
ElectronD00to40MuonD040to500Region.cuts.append(muon_d0_40to500_cut)


InclusiveSignalRegion = cms.PSet(
    name = cms.string("InclusiveSignalRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
InclusiveSignalRegion.cuts.append(electron_d0_greaterThan100_cut)
InclusiveSignalRegion.cuts.append(muon_d0_greaterThan100_cut)
InclusiveSignalRegion.cuts.append(electron_d0_lessThan10cm_cut)
InclusiveSignalRegion.cuts.append(muon_d0_lessThan10cm_cut)

PromptLowPtControlRegion = copy.deepcopy(PromptControlRegion)
PromptLowPtControlRegion.name = cms.string("PromptLowPtControlRegion")
PromptLowPtControlRegion.cuts.append(electron_pt_100_veto)
PromptLowPtControlRegion.cuts.append(muon_pt_100_veto)

PromptHighPtControlRegion = copy.deepcopy(PromptControlRegion)
PromptHighPtControlRegion.name = cms.string("PromptHighPtControlRegion")
PromptHighPtControlRegion.cuts.append(electron_pt_100_cut)
PromptHighPtControlRegion.cuts.append(muon_pt_100_cut)

DisplacedLowPtControlRegion = copy.deepcopy(InclusiveSignalRegion)
DisplacedLowPtControlRegion.name = cms.string("DisplacedLowPtControlRegion")
DisplacedLowPtControlRegion.cuts.append(electron_pt_100_veto)
DisplacedLowPtControlRegion.cuts.append(muon_pt_100_veto)

DisplacedHighPtControlRegion = copy.deepcopy(InclusiveSignalRegion)
DisplacedHighPtControlRegion.name = cms.string("DisplacedHighPtControlRegion")
DisplacedHighPtControlRegion.cuts.append(electron_pt_100_cut)
DisplacedHighPtControlRegion.cuts.append(muon_pt_100_cut)

pfBetaIsoCorrPreselection = cms.PSet(
    name = cms.string("pfBetaIsoCorrPreselection"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
replaceSingleCut(pfBetaIsoCorrPreselection.cuts, muon_pfBetaIsoCorr_cut, muon_iso_cut)

PreselectionNoIso = cms.PSet(
    name = cms.string("PreselectionNoIso"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
removeCuts(PreselectionNoIso.cuts, [electron_newIso_cut, muon_iso_cut])


AntiIsoPreselection = cms.PSet(
    name = cms.string("AntiIsoPreselection"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
replaceSingleCut(AntiIsoPreselection.cuts, electron_antiNewIso_cut, electron_newIso_cut)
replaceSingleCut(AntiIsoPreselection.cuts, muon_antiiso_cut, muon_iso_cut)


AntiIsoPromptElectronDisplacedMuonRegion = cms.PSet(
    name = cms.string("AntiIsoPromptElectronDisplacedMuonRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
replaceSingleCut(AntiIsoPromptElectronDisplacedMuonRegion.cuts, electron_antiNewIso_cut, electron_newIso_cut)
replaceSingleCut(AntiIsoPromptElectronDisplacedMuonRegion.cuts, muon_antiiso_cut, muon_iso_cut)
AntiIsoPromptElectronDisplacedMuonRegion.cuts.append(electron_d0_lessThan200_cut)
AntiIsoPromptElectronDisplacedMuonRegion.cuts.append(muon_d0_greaterThan100_cut)


AntiIsoPromptMuonDisplacedElectronRegion = cms.PSet(
    name = cms.string("AntiIsoPromptMuonDisplacedElectronRegion"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
replaceSingleCut(AntiIsoPromptMuonDisplacedElectronRegion.cuts, electron_antiNewIso_cut, electron_newIso_cut)
replaceSingleCut(AntiIsoPromptMuonDisplacedElectronRegion.cuts, muon_antiiso_cut, muon_iso_cut)
AntiIsoPromptMuonDisplacedElectronRegion.cuts.append(muon_d0_lessThan200_cut)
AntiIsoPromptMuonDisplacedElectronRegion.cuts.append(electron_d0_greaterThan100_cut)


InvertDispVtxInMaterialPreselection = cms.PSet(
    name = cms.string("InvertDispVtxInMaterialPreselection"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
replaceSingleCut(InvertDispVtxInMaterialPreselection.cuts, emu_invertNoDispVtxsInMaterial_cut, emu_noDispVtxsInMaterial_cut)



PreselectionElectronBarrel = cms.PSet(
    name = cms.string("PreselectionElectronBarrel"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionElectronBarrel.cuts.append(electron_isEB_cut)


PreselectionElectronEndcap = cms.PSet(
    name = cms.string("PreselectionElectronEndcap"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionElectronEndcap.cuts.append(electron_isEE_cut)



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

PreselectionLeptonsFromWorZ = cms.PSet(
    name = cms.string("PreselectionLeptonsFromWorZ"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsFromWorZ.cuts.append(electron_gen_motherIsWorZ_cut)
PreselectionLeptonsFromWorZ.cuts.append(muon_gen_motherIsWorZ_cut)

PreselectionLeptonsFromTau = cms.PSet(
    name = cms.string("PreselectionLeptonsFromTau"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsFromTau.cuts.append(electron_gen_motherIsTau_cut)
PreselectionLeptonsFromTau.cuts.append(muon_gen_motherIsTau_cut)

PreselectionLeptonsNotFromTau = cms.PSet(
    name = cms.string("PreselectionLeptonsNotFromTau"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsNotFromTau.cuts.append(electron_gen_motherIsNotTau_cut)
PreselectionLeptonsNotFromTau.cuts.append(muon_gen_motherIsNotTau_cut)

PreselectionMuFromTau = cms.PSet(
    name = cms.string("PreselectionMuFromTau"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionMuFromTau.cuts.append(muon_gen_motherIsTau_cut)

PreselectionEFromTau = cms.PSet(
    name = cms.string("PreselectionEFromTau"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionEFromTau.cuts.append(electron_gen_motherIsTau_cut)

PreselectionMuFromLightMeson = cms.PSet(
    name = cms.string("PreselectionMuFromLightMeson"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionMuFromLightMeson.cuts.append(muon_gen_motherIsLightMeson_cut)

PreselectionEFromLightMeson = cms.PSet(
    name = cms.string("PreselectionEFromLightMeson"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionEFromLightMeson.cuts.append(electron_gen_motherIsLightMeson_cut)

PreselectionMuFromHeavyMeson = cms.PSet(
    name = cms.string("PreselectionMuFromHeavyMeson"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionMuFromHeavyMeson.cuts.append(muon_gen_motherIsHeavyMeson_cut)

PreselectionEFromHeavyMeson = cms.PSet(
    name = cms.string("PreselectionEFromHeavyMeson"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionEFromHeavyMeson.cuts.append(electron_gen_motherIsHeavyMeson_cut)

PreselectionEOrMuFromHeavyMeson = cms.PSet(
    name = cms.string("PreselectionEOrMuFromHeavyMeson"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionEOrMuFromHeavyMeson.cuts.append(emu_gen_motherIsHeavyMeson_cut)

PreselectionMuFromWorZ = cms.PSet(
    name = cms.string("PreselectionMuFromWorZ"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionMuFromWorZ.cuts.append(muon_gen_motherIsWorZ_cut)

PreselectionEFromWorZ = cms.PSet(
    name = cms.string("PreselectionEFromWorZ"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionEFromWorZ.cuts.append(electron_gen_motherIsWorZ_cut)

Preselection2TausFromZ = cms.PSet(
    name = cms.string("Preselection2TausFromZ"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
Preselection2TausFromZ.cuts.append(exactly2_genTau_uniqueMotherIsZ_cut)

GenEMuFromStopsSelection = cms.PSet(
    name = cms.string("GenEMuFromStopsSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet([
        exactly2_genEleOrMu_status1_uniqueMotherIsStop_cut,
        genEleMuChannel_cut,
        #atLeastTwo_genLxy_lessThan50cm_cut,
        #atLeastTwo_genEta_cut,
    ])
)
#if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    #GenEMuFromStopsSelection.cuts.append(atLeastTwo_genPt_40_cut)
#elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    #GenEMuFromStopsSelection.cuts.append(atLeastTwo_genPt_50_cut)

######
#to look at either gen ele or mu, but not both, in histograms
GenEMuFromStopsEleSelection = cms.PSet(
    name = cms.string("GenEMuFromStopsEleSelection"),
    triggers = copy.deepcopy(GenEMuFromStopsSelection.triggers),
    cuts = cms.VPSet (copy.deepcopy(GenEMuFromStopsSelection.cuts))
)
GenEMuFromStopsEleSelection.cuts.append(exactly1_genEle_cut)

GenEMuFromStopsMuSelection = cms.PSet(
    name = cms.string("GenEMuFromStopsMuSelection"),
    triggers = copy.deepcopy(GenEMuFromStopsSelection.triggers),
    cuts = cms.VPSet (copy.deepcopy(GenEMuFromStopsSelection.cuts))
)
GenEMuFromStopsMuSelection.cuts.append(exactly1_genMu_cut)

######
#HLT
GenEMuFromStopsEleAndHLTTrigSelection = cms.PSet(
    name = cms.string("GenEMuFromStopsEleAndHLTTrigSelection"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(GenEMuFromStopsEleSelection.cuts))
)

GenEMuFromStopsMuAndHLTTrigSelection = cms.PSet(
    name = cms.string("GenEMuFromStopsMuAndHLTTrigSelection"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(GenEMuFromStopsMuSelection.cuts))
)

######
#L1
GenEMuFromStopsEleAndL1TrigSelection = cms.PSet(
    name = cms.string("GenEMuFromStopsEleAndL1TrigSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (copy.deepcopy(GenEMuFromStopsEleSelection.cuts))
)
GenEMuFromStopsEleAndL1TrigSelection.cuts.append(pass_L1MuEG_Seeds)

GenEMuFromStopsMuAndL1TrigSelection = cms.PSet(
    name = cms.string("GenEMuFromStopsMuAndL1TrigSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (copy.deepcopy(GenEMuFromStopsMuSelection.cuts))
)
GenEMuFromStopsMuAndL1TrigSelection.cuts.append(pass_L1MuEG_Seeds)

######
