import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

#################################################################
### Set up the preselection for the displaced SUSY analysis #####
#################################################################

Preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = triggersDoubleMuon,
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
Preselection.cuts.extend(atLeastZero_jet_basic_selection_cuts)
### at least two good muons
Preselection.cuts.append(muon_eta_cut)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    Preselection.cuts.append(muon_eta_phi_veto_2017) #veto region with pixel power supply issues
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    Preselection.cuts.append(muon_eta_phi_veto_2018) #veto region with pixel power supply issues
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    Preselection.cuts.append(muon_pt_35_cut) #plateau of trigger turn on
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    Preselection.cuts.append(muon_pt_45_cut) #pleateau of trigger turn on
Preselection.cuts.append(muon_global_cut)
Preselection.cuts.append(muon_id_cut)
Preselection.cuts.append(muon_iso_cut) #our custom rho-based iso
Preselection.cuts.append(diMuon_cosAlpha_veto) #remove cosmics that are back-to-back
Preselection.cuts.append(diMuon_deltaTimeAtIpInOut_veto) #remove muons with delta time consistent with cosmics
Preselection.cuts.append(diMuon_deltaR_cut) #remove muons from heavy mesons that are very close to each other (loose dR>0.2)
Preselection.cuts.append(mumu_noDispVtxsInMaterial_cut)
### remove events with displaced electrons that would pass the emu preselection
Preselection.cuts.append(electron_emu_preselection_filter)
Preselection.cuts.append(electron_d0_greaterThan100_veto)




PreselectionPt75 = copy.deepcopy(Preselection)
PreselectionPt75.name = cms.string("PreselectionPt75")
PreselectionPt75.cuts.append(muon_pt_75_cut)

# selection with tighter muon eta and pT cuts to facilitate comparison with ee channel
PreselectionMimicEE = copy.deepcopy(Preselection)
PreselectionMimicEE.name = cms.string("PreselectionMimicEE")
PreselectionMimicEE.cuts.append(muon_eta1p9_cut)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    PreselectionMimicEE.cuts.append(muon_pt_65_cut)
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    PreselectionMimicEE.cuts.append(muon_pt_75_cut)

PromptControlRegion = copy.deepcopy(Preselection)
PromptControlRegion.name = cms.string("PromptControlRegion")
PromptControlRegion.cuts.append(muon_d0_lessThan50_cut)

GenPromptRegion = copy.deepcopy(Preselection)
GenPromptRegion.name = cms.string("GenPromptRegion")
GenPromptRegion.cuts.append(gen_muon_d0_lessThan30_cut)

etaLessThan1GenPromptRegion = copy.deepcopy(GenPromptRegion)
etaLessThan1GenPromptRegion.name = cms.string("etaLessThan1GenPromptRegion")
etaLessThan1GenPromptRegion.cuts.append(muon_eta_lessThan1_cut)

pT50to60GenPromptRegion = copy.deepcopy(GenPromptRegion)
pT50to60GenPromptRegion.name = cms.string("pT50to60GenPromptRegion")
pT50to60GenPromptRegion.cuts.append(muon_pt_50to60_cut)

pTGreaterThan150GenPromptRegion = copy.deepcopy(GenPromptRegion)
pTGreaterThan150GenPromptRegion.name = cms.string("pTGreaterThan150GenPromptRegion")
pTGreaterThan150GenPromptRegion.cuts.append(muon_pt_150_cut)

#################################################################




MuonD00to40MuonD00to100Region = copy.deepcopy(Preselection)
MuonD00to40MuonD00to100Region.name = cms.string("MuonD00to40MuonD00to100Region")
MuonD00to40MuonD00to100Region.cuts.append(muon_onePrompt_0to40_one_lessThan100_cut)

MuonD00to40MuonD0100to500Region = copy.deepcopy(Preselection)
MuonD00to40MuonD0100to500Region.name = cms.string("MuonD00to40MuonD0100to500Region")
MuonD00to40MuonD0100to500Region.cuts.append(muon_onePrompt_0to40_oneDisplaced_100to500_cut)

MuonD00to40MuonD0500to1000Region = copy.deepcopy(Preselection)
MuonD00to40MuonD0500to1000Region.name = cms.string("MuonD00to40MuonD0500to1000Region")
MuonD00to40MuonD0500to1000Region.cuts.append(muon_onePrompt_0to40_oneDisplaced_500to1000_cut)

#################################################################

### to find negative valued bins in abcd method closure test
lifetimeWeightNegative = copy.deepcopy(Preselection)
lifetimeWeightNegative.name = cms.string("lifetimeWeightNegative")
lifetimeWeightNegative.cuts.append(lifetimeWeight_negative)

puScalingFactorNegative = copy.deepcopy(Preselection)
puScalingFactorNegative.name = cms.string("puScalingFactorNegative")
puScalingFactorNegative.cuts.append(puScalingFactor_negative)

#################################################################

PreselectionNoIsoCut = copy.deepcopy(Preselection)
PreselectionNoIsoCut.name = cms.string("PreselectionNoIsoCut")
removeCuts(PreselectionNoIsoCut.cuts, [muon_iso_cut])

pfBetaIsoCorrPreselection = copy.deepcopy(Preselection)
pfBetaIsoCorrPreselection.name = cms.string("pfBetaIsoCorrPreselection")
replaceSingleCut(pfBetaIsoCorrPreselection.cuts, muon_pfBetaIsoCorr_cut, muon_iso_cut)

PreselectionBTagVeto = copy.deepcopy(Preselection)
PreselectionBTagVeto.name = cms.string("PreselectionBTagVeto")
PreselectionBTagVeto.cuts.append(jet_btag_lwp_veto)

PreselectionOneBJet = copy.deepcopy(Preselection)
PreselectionOneBJet.name = cms.string("PreselectionOneBJet")
PreselectionOneBJet.cuts.append(atLeastOne_bjet_eta_cut)
PreselectionOneBJet.cuts.append(atLeastOne_bjet_pt_30_cut)
PreselectionOneBJet.cuts.append(atLeastOne_bjet_id_cut)
PreselectionOneBJet.cuts.append(jet_btag_mwp_cut)

PreselectionLowEta = copy.deepcopy(Preselection)
PreselectionLowEta.name = cms.string("PreselectionLowEta")
PreselectionLowEta.cuts.append(muon_eta_lessThan1_cut)

PreselectionHighEta = copy.deepcopy(Preselection)
PreselectionHighEta.name = cms.string("PreselectionHighEta")
PreselectionHighEta.cuts.append(muon_eta_greaterThan1_cut)

PreselectionInvertedIso= copy.deepcopy(Preselection)
PreselectionInvertedIso.name = cms.string("PreselectionInvertedIso")
replaceSingleCut(PreselectionInvertedIso.cuts, muon_antiiso_cut, muon_iso_cut)

PreselectionInvertedIsoDeltaR = copy.deepcopy(Preselection)
PreselectionInvertedIsoDeltaR.name = cms.string("PreselectionInvertedIsoDeltaR")
replaceSingleCut(PreselectionInvertedIsoDeltaR.cuts, muon_antiiso_cut, muon_iso_cut)
replaceSingleCut(PreselectionInvertedIsoDeltaR.cuts, diMuon_invertedDeltaR_cut, diMuon_deltaR_cut)

PromptControlRegion = copy.deepcopy(Preselection)
PromptControlRegion.name = cms.string("PromptControlRegion")
PromptControlRegion.cuts.append(muon_d0_lessThan50_cut)

PromptControlRegionNoIsoCut = copy.deepcopy(PreselectionNoIsoCut)
PromptControlRegionNoIsoCut.name = cms.string("PromptControlRegionNoIsoCut")
PromptControlRegionNoIsoCut.cuts.append(muon_d0_lessThan50_cut)

PromptControlRegionLowEta = copy.deepcopy(PreselectionLowEta)
PromptControlRegionLowEta.name = cms.string("PromptControlRegionLowEta")
PromptControlRegionLowEta.cuts.append(muon_d0_lessThan50_cut)

PromptControlRegionHighEta = copy.deepcopy(PreselectionHighEta)
PromptControlRegionHighEta.name = cms.string("PromptControlRegionHighEta")
PromptControlRegionHighEta.cuts.append(muon_d0_lessThan50_cut)

AntiIsoPromptControlRegion = copy.deepcopy(PromptControlRegion)
AntiIsoPromptControlRegion.name = cms.string("AntiIsoPromptControlRegion")
replaceSingleCut(AntiIsoPromptControlRegion.cuts, muon_antiiso_cut, muon_iso_cut) #replace muon_iso_cut with muon_antiiso_cut in the same place

DisplacedControlRegion = copy.deepcopy(Preselection)
DisplacedControlRegion.name = cms.string("DisplacedControlRegion")
#DisplacedControlRegion.cuts.append(muon_d0_100to200_cut)
DisplacedControlRegion.cuts.append(muon_d0_10to20_cut)

AntiIsoDisplacedControlRegion = copy.deepcopy(DisplacedControlRegion)
AntiIsoDisplacedControlRegion.name = cms.string("AntiIsoDisplacedControlRegion")
replaceSingleCut(AntiIsoDisplacedControlRegion.cuts, muon_antiiso_cut, muon_iso_cut) #replace muon_iso_cut with muon_antiiso_cut in the same place

InclusiveSignalRegion = copy.deepcopy(Preselection)
InclusiveSignalRegion.name = cms.string("InclusiveSignalRegion")
InclusiveSignalRegion.cuts.append(muon_d0_greaterThan100_cut)
InclusiveSignalRegion.cuts.append(muon_d0_lessThan10cm_cut)

InclusiveSignalRegionNoIsoCut = copy.deepcopy(PreselectionNoIsoCut)
InclusiveSignalRegionNoIsoCut.name = cms.string("InclusiveSignalRegionNoIsoCut")
InclusiveSignalRegionNoIsoCut.cuts.append(muon_d0_greaterThan100_cut)
InclusiveSignalRegionNoIsoCut.cuts.append(muon_d0_lessThan10cm_cut)

InclusiveSignalRegionLowEta = copy.deepcopy(PreselectionLowEta)
InclusiveSignalRegionLowEta.name = cms.string("InclusiveSignalRegionLowEta")
InclusiveSignalRegionLowEta.cuts.append(muon_d0_greaterThan100_cut)
InclusiveSignalRegionLowEta.cuts.append(muon_d0_lessThan10cm_cut)

InclusiveSignalRegionHighEta = copy.deepcopy(PreselectionHighEta)
InclusiveSignalRegionHighEta.name = cms.string("InclusiveSignalRegionHighEta")
InclusiveSignalRegionHighEta.cuts.append(muon_d0_greaterThan100_cut)
InclusiveSignalRegionHighEta.cuts.append(muon_d0_lessThan10cm_cut)

InclusiveSignalRegionAtLeast2PixelHits = copy.deepcopy(InclusiveSignalRegion)
InclusiveSignalRegionAtLeast2PixelHits.name = cms.string("InclusiveSignalRegionAtLeast2PixelHits")
InclusiveSignalRegionAtLeast2PixelHits.cuts.append(muon_2PixelHit_cut)



InvertDispVtxInMaterialPreselection = cms.PSet(
    name = cms.string("InvertDispVtxInMaterialPreselection"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
replaceSingleCut(InvertDispVtxInMaterialPreselection.cuts, mumu_invertNoDispVtxsInMaterial_cut, mumu_noDispVtxsInMaterial_cut)

CosmicPreselection = cms.PSet(
    name = cms.string("CosmicPreselection"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
replaceSingleCut(CosmicPreselection.cuts, diMuon_cosAlpha_invertVeto, diMuon_cosAlpha_veto)
replaceSingleCut(CosmicPreselection.cuts, diMuon_deltaTimeAtIpInOut_invertVeto, diMuon_deltaTimeAtIpInOut_veto)
CosmicPreselection.cuts.append(muon_d0_greaterThan100_cut)



PreselectionForCosmics = cms.PSet(
    name = cms.string("PreselectionForCosmics"),
    triggers = triggersNoBPTX,
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
PreselectionForCosmics.cuts.extend(atLeastZero_jet_basic_selection_cuts)
### at least two good muons
PreselectionForCosmics.cuts.append(muon_eta_cut)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    PreselectionForCosmics.cuts.append(muon_eta_phi_veto_2017) #veto region with pixel power supply issues
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    PreselectionForCosmics.cuts.append(muon_eta_phi_veto_2018) #veto region with pixel power supply issues
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    PreselectionForCosmics.cuts.append(muon_pt_35_cut) #plateau of trigger turn on
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    PreselectionForCosmics.cuts.append(muon_pt_45_cut) #pleateau of trigger turn on
PreselectionForCosmics.cuts.append(muon_global_cut)
PreselectionForCosmics.cuts.append(muon_id_cut)
PreselectionForCosmics.cuts.append(muon_iso_cut) #our custom rho-based iso
PreselectionForCosmics.cuts.append(diMuon_deltaR_cut) #remove muons from heavy mesons that are very close to each other (loose dR>0.2)
PreselectionForCosmics.cuts.append(mumu_noDispVtxsInMaterial_cut)
### remove events with displaced electrons that would pass the emu preselection
PreselectionForCosmics.cuts.append(electron_emu_preselection_filter)
PreselectionForCosmics.cuts.append(electron_d0_greaterThan100_veto)
PreselectionForCosmics.cuts.append(diMuon_cosAlpha_veto) #remove cosmics that are back-to-back
PreselectionForCosmics.cuts.append(diMuon_deltaTimeAtIpInOut_veto) #remove muons with delta time consistent with cosmics



Den1PixelHitSelWithCosmics = cms.PSet(
    name = cms.string("Den1PixelHitSelWithCosmics"),
    #triggers = triggersNoBPTX,
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
Den1PixelHitSelWithCosmics.cuts.extend(atLeastZero_jet_basic_selection_cuts)
### at least two good muons
Den1PixelHitSelWithCosmics.cuts.append(muon_eta_lessThan1_cut)
Den1PixelHitSelWithCosmics.cuts.append(muon_pt_25_cut)
Den1PixelHitSelWithCosmics.cuts.append(muon_global_cut)
Den1PixelHitSelWithCosmics.cuts.append(muon_idExcept1PixelHit_cut)
#Den1PixelHitSelWithCosmics.cuts.append(muon_iso_cut) #our custom rho-based iso
Den1PixelHitSelWithCosmics.cuts.append(diMuon_deltaR_cut) #remove muons from heavy mesons that are very close to each other (loose dR>0.2)
Den1PixelHitSelWithCosmics.cuts.append(mumu_noDispVtxsInMaterial_cut)
Den1PixelHitSelWithCosmics.cuts.append(muon_dZ_lessThan15cm_cut)

Num1PixelHitSelWithCosmics = cms.PSet(
    name = cms.string("Num1PixelHitSelWithCosmics"),
    triggers = copy.deepcopy(Den1PixelHitSelWithCosmics.triggers),
    cuts = cms.VPSet (copy.deepcopy(Den1PixelHitSelWithCosmics.cuts))
)
Num1PixelHitSelWithCosmics.cuts.append(muon_1PixelHit_cut)

#################################################################

ZControlRegion = copy.deepcopy(Preselection)
ZControlRegion.name = cms.string("ZControlRegion")
ZControlRegion.cuts.append(muon_jet_deltaR_overlap_veto)
ZControlRegion.cuts.append(muon_2muon_cut)
ZControlRegion.cuts.append(diMuon_invMass_Z_cut) ### invMass in Z range
ZControlRegion.cuts.append(muon_fiducial_phi_cut)

#################################################################

PromptLowPtControlRegion = copy.deepcopy(PromptControlRegion)
PromptLowPtControlRegion.name = cms.string("PromptLowPtControlRegion")
PromptLowPtControlRegion.cuts.append(muon_pt_100_veto)

PromptHighPtControlRegion = copy.deepcopy(PromptControlRegion)
PromptHighPtControlRegion.name = cms.string("PromptHighPtControlRegion")
PromptHighPtControlRegion.cuts.append(muon_pt_100_cut)

DisplacedLowPtControlRegion = copy.deepcopy(InclusiveSignalRegion)
DisplacedLowPtControlRegion.name = cms.string("DisplacedLowPtControlRegion")
DisplacedLowPtControlRegion.cuts.append(muon_pt_100_veto)

DisplacedHighPtControlRegion = copy.deepcopy(InclusiveSignalRegion)
DisplacedHighPtControlRegion.name = cms.string("DisplacedHighPtControlRegion")
DisplacedHighPtControlRegion.cuts.append(muon_pt_100_cut)

PromptLowPtControlRegionNoIsoCut = copy.deepcopy(PromptControlRegionNoIsoCut)
PromptLowPtControlRegionNoIsoCut.name = cms.string("PromptLowPtControlRegionNoIsoCut")
PromptLowPtControlRegionNoIsoCut.cuts.append(muon_pt_100_veto)

PromptHighPtControlRegionNoIsoCut = copy.deepcopy(PromptControlRegionNoIsoCut)
PromptHighPtControlRegionNoIsoCut.name = cms.string("PromptHighPtControlRegionNoIsoCut")
PromptHighPtControlRegionNoIsoCut.cuts.append(muon_pt_100_cut)

DisplacedLowPtControlRegionNoIsoCut = copy.deepcopy(InclusiveSignalRegionNoIsoCut)
DisplacedLowPtControlRegionNoIsoCut.name = cms.string("DisplacedLowPtControlRegionNoIsoCut")
DisplacedLowPtControlRegionNoIsoCut.cuts.append(muon_pt_100_veto)

DisplacedHighPtControlRegionNoIsoCut = copy.deepcopy(InclusiveSignalRegionNoIsoCut)
DisplacedHighPtControlRegionNoIsoCut.name = cms.string("DisplacedHighPtControlRegionNoIsoCut")
DisplacedHighPtControlRegionNoIsoCut.cuts.append(muon_pt_100_cut)

PromptLowPtControlRegionLowEta = copy.deepcopy(PromptControlRegionLowEta)
PromptLowPtControlRegionLowEta.name = cms.string("PromptLowPtControlRegionLowEta")
PromptLowPtControlRegionLowEta.cuts.append(muon_pt_100_veto)

PromptHighPtControlRegionLowEta = copy.deepcopy(PromptControlRegionLowEta)
PromptHighPtControlRegionLowEta.name = cms.string("PromptHighPtControlRegionLowEta")
PromptHighPtControlRegionLowEta.cuts.append(muon_pt_100_cut)

DisplacedLowPtControlRegionLowEta = copy.deepcopy(InclusiveSignalRegionLowEta)
DisplacedLowPtControlRegionLowEta.name = cms.string("DisplacedLowPtControlRegionLowEta")
DisplacedLowPtControlRegionLowEta.cuts.append(muon_pt_100_veto)

DisplacedHighPtControlRegionLowEta = copy.deepcopy(InclusiveSignalRegionLowEta)
DisplacedHighPtControlRegionLowEta.name = cms.string("DisplacedHighPtControlRegionLowEta")
DisplacedHighPtControlRegionLowEta.cuts.append(muon_pt_100_cut)

PromptLowPtControlRegionHighEta = copy.deepcopy(PromptControlRegionHighEta)
PromptLowPtControlRegionHighEta.name = cms.string("PromptLowPtControlRegionHighEta")
PromptLowPtControlRegionHighEta.cuts.append(muon_pt_100_veto)

PromptHighPtControlRegionHighEta = copy.deepcopy(PromptControlRegionHighEta)
PromptHighPtControlRegionHighEta.name = cms.string("PromptHighPtControlRegionHighEta")
PromptHighPtControlRegionHighEta.cuts.append(muon_pt_100_cut)

DisplacedLowPtControlRegionHighEta = copy.deepcopy(InclusiveSignalRegionHighEta)
DisplacedLowPtControlRegionHighEta.name = cms.string("DisplacedLowPtControlRegionHighEta")
DisplacedLowPtControlRegionHighEta.cuts.append(muon_pt_100_veto)

DisplacedHighPtControlRegionHighEta = copy.deepcopy(InclusiveSignalRegionHighEta)
DisplacedHighPtControlRegionHighEta.name = cms.string("DisplacedHighPtControlRegionHighEta")
DisplacedHighPtControlRegionHighEta.cuts.append(muon_pt_100_cut)

#################################################################

PreselectionLeptonsFromBorCQuark = cms.PSet(
    name = cms.string("PreselectionLeptonsFromBorCQuark"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsFromBorCQuark.cuts.append(muon_gen_motherIsBorCQuark_cut)

PreselectionLeptonsFromW = cms.PSet(
    name = cms.string("PreselectionLeptonsFromW"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsFromW.cuts.append(muon_gen_motherIsW_cut)

PreselectionLeptonsFromWorZ = cms.PSet(
    name = cms.string("PreselectionLeptonsFromWorZ"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsFromWorZ.cuts.append(muon_gen_motherIsWorZ_cut)

PreselectionLeptonsFromTau = cms.PSet(
    name = cms.string("PreselectionLeptonsFromTau"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsFromTau.cuts.append(muon_gen_motherIsTau_cut)

PreselectionLeptonsNotFromTau = cms.PSet(
    name = cms.string("PreselectionLeptonsNotFromTau"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionLeptonsNotFromTau.cuts.append(muon_gen_motherIsNotTau_cut)

PreselectionLowEtaLeptonsNotFromTau = cms.PSet(
    name = cms.string("PreselectionLowEtaLeptonsNotFromTau"),
    triggers = copy.deepcopy(PreselectionLowEta.triggers),
    cuts = cms.VPSet (copy.deepcopy(PreselectionLowEta.cuts))
)
PreselectionLowEtaLeptonsNotFromTau.cuts.append(muon_gen_motherIsNotTau_cut)

PreselectionHighEtaLeptonsNotFromTau = cms.PSet(
    name = cms.string("PreselectionHighEtaLeptonsNotFromTau"),
    triggers = copy.deepcopy(PreselectionHighEta.triggers),
    cuts = cms.VPSet (copy.deepcopy(PreselectionHighEta.cuts))
)
PreselectionHighEtaLeptonsNotFromTau.cuts.append(muon_gen_motherIsNotTau_cut)

Preselection1LeptonFromTau = cms.PSet(
    name = cms.string("Preselection1LeptonFromTau"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
Preselection1LeptonFromTau.cuts.append(exactly1muon_gen_motherIsTau_cut)

Preselection2LeptonsFromTau = cms.PSet(
    name = cms.string("Preselection2LeptonsFromTau"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
Preselection2LeptonsFromTau.cuts.append(exactly2muon_gen_motherIsTau_cut)

Preselection2TausFromZ = cms.PSet(
    name = cms.string("Preselection2TausFromZ"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
Preselection2TausFromZ.cuts.append(exactly2_genTau_uniqueMotherIsZ_cut)

PreselectionMuFromLightMeson = cms.PSet(
    name = cms.string("PreselectionMuFromLightMeson"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionMuFromLightMeson.cuts.append(muon_gen_motherIsLightMeson_cut)

PreselectionMuFromHeavyMeson = cms.PSet(
    name = cms.string("PreselectionMuFromHeavyMeson"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionMuFromHeavyMeson.cuts.append(muon_gen_motherIsHeavyMeson_cut)
#################################################################

GenMuMuFromStopsSelection = cms.PSet(
    name = cms.string("GenMuMuFromStopsSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet([exactly2_genMu_status1_uniqueMotherIsStop_cut,
                      #atLeastTwo_genLxy_lessThan50cm_cut,
                      #atLeastTwo_genEta_cut,
                  ])
)
#if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    #GenMuMuFromStopsSelection.cuts.append(atLeastTwo_genPt_40_cut)
#elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    #GenMuMuFromStopsSelection.cuts.append(atLeastTwo_genPt_50_cut)

GenMuMuFromZSelection = cms.PSet(
    name = cms.string("GenMuMuFromZSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet([exactly2_genMu_status1_uniqueMotherIsZ_cut])
)

#HLT
GenMuMuFromStopsAndHLTTrigSelection = cms.PSet(
    name = cms.string("GenMuMuFromStopsAndHLTTrigSelection"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(GenMuMuFromStopsSelection.cuts))
)

#L1
GenMuMuFromStopsAndL1TrigSelection = cms.PSet(
    name = cms.string("GenMuMuFromStopsAndL1TrigSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet ()
)
GenMuMuFromStopsAndL1TrigSelection.cuts.append(pass_L1DoubleMu_Seeds) #need L1 cut first and then gen cuts, otherwise hardIntMcpart hists get screwed up!
GenMuMuFromStopsAndL1TrigSelection.cuts.extend(copy.deepcopy(GenMuMuFromStopsSelection.cuts))
#################################################################

# to check if cloud model turned on
GenMuSelection = cms.PSet(
    name = cms.string("GenMuSelection"),
    triggers = cms.vstring(),
    cuts = cms.VPSet([atLeastZero_genMu_cut,
                  ])
)
#################################################################


PreselectionOneLessThan40umOneGreaterThan100um = cms.PSet(
    name = cms.string("PreselectionOneLessThan40umOneGreaterThan100um"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionOneLessThan40umOneGreaterThan100um.cuts.append(muon_onePrompt_oneDisplaced_cut)

PreselectionPromptMuonDisplacedTagMuon100um = cms.PSet(
    name = cms.string("PreselectionPromptMuonDisplacedTagMuon100um"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionPromptMuonDisplacedTagMuon100um.cuts.append(muon_d0_lessThan40_cut) # only requires >=1
PreselectionPromptMuonDisplacedTagMuon100um.cuts.append(tagMuonExists_cut)
PreselectionPromptMuonDisplacedTagMuon100um.cuts.append(tagMuon_d0_greaterThan100_cut)

PreselectionPromptMuonDisplacedTagMuon500um = copy.deepcopy(PreselectionPromptMuonDisplacedTagMuon100um)
PreselectionPromptMuonDisplacedTagMuon500um.name = cms.string("PreselectionPromptMuonDisplacedTagMuon500um")
replaceSingleCut(PreselectionPromptMuonDisplacedTagMuon500um.cuts,
                 tagMuon_d0_greaterThan500_cut, tagMuon_d0_greaterThan100_cut)

PreselectionPromptTagMuonDisplacedMuon100um = cms.PSet(
    name = cms.string("PreselectionPromptTagMuonDisplacedMuon100um"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet (copy.deepcopy(Preselection.cuts))
)
PreselectionPromptTagMuonDisplacedMuon100um.cuts.append(muon_d0_greaterThan100_exactly1_cut)
PreselectionPromptTagMuonDisplacedMuon100um.cuts.append(tagMuonExists_cut)
PreselectionPromptTagMuonDisplacedMuon100um.cuts.append(tagMuon_d0_lessThan40_cut)
