import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *
from DisplacedSUSY.StandardAnalysis.ElectronIdCutDefinitions import *

##########################################################################################
#USE THIS CONFIG ONLY FOR ELECTRON TIGHT ID TESTS!
##########################################################################################

PreselectionWithExplicitEleIdBarrel = cms.PSet(
    name = cms.string("PreselectionWithExplicitEleIdBarrel"),
    triggers = triggersMuonPhoton,
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
PreselectionWithExplicitEleIdBarrel.cuts.extend(atLeastZero_jet_basic_selection_cuts)
### at least one good electron
PreselectionWithExplicitEleIdBarrel.cuts.append(electron_eta_cut)
PreselectionWithExplicitEleIdBarrel.cuts.append(electron_gap_veto)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    PreselectionWithExplicitEleIdBarrel.cuts.append(electron_pt_42_cut)
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    PreselectionWithExplicitEleIdBarrel.cuts.append(electron_pt_50_cut)
PreselectionWithExplicitEleIdBarrel.cuts.append(electron_isEB_cut)
PreselectionWithExplicitEleIdBarrel.cuts.append(electron_sigmaIetaIetaEB_cut)
PreselectionWithExplicitEleIdBarrel.cuts.append(electron_deltaPhiSuperClusterEB_cut)
PreselectionWithExplicitEleIdBarrel.cuts.append(electron_deltaEtaSuperClusterEB_cut)
PreselectionWithExplicitEleIdBarrel.cuts.append(electron_hadronicOverEmEB_cut)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    PreselectionWithExplicitEleIdBarrel.cuts.append(electron_abs_1overE_1overP_cut)
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    PreselectionWithExplicitEleIdBarrel.cuts.append(electron_abs_1overE_1overP_EB_cut)
PreselectionWithExplicitEleIdBarrel.cuts.append(electron_missingInnerHits_cut)
PreselectionWithExplicitEleIdBarrel.cuts.append(electron_passConversionVeto_cut)
### at least one good muon
PreselectionWithExplicitEleIdBarrel.cuts.append(muon_eta_cut)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    PreselectionWithExplicitEleIdBarrel.cuts.append(muon_pt_40_cut)
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    PreselectionWithExplicitEleIdBarrel.cuts.append(muon_pt_50_cut)
PreselectionWithExplicitEleIdBarrel.cuts.append(muon_global_cut)
PreselectionWithExplicitEleIdBarrel.cuts.append(muon_id_cut)
PreselectionWithExplicitEleIdBarrel.cuts.append(muon_iso_cut)

PreselectionWithExplicitEleIdEndcap = cms.PSet(
    name = cms.string("PreselectionWithExplicitEleIdEndcap"),
    triggers = triggersMuonPhoton,
    cuts = cms.VPSet()
)
### jet selection (just for plotting purposes, doesn't make event cuts)
PreselectionWithExplicitEleIdEndcap.cuts.extend(atLeastZero_jet_basic_selection_cuts)
### at least one good electron
PreselectionWithExplicitEleIdEndcap.cuts.append(electron_eta_cut)
PreselectionWithExplicitEleIdEndcap.cuts.append(electron_gap_veto)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    PreselectionWithExplicitEleIdEndcap.cuts.append(electron_pt_42_cut)
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    PreselectionWithExplicitEleIdEndcap.cuts.append(electron_pt_50_cut)
PreselectionWithExplicitEleIdEndcap.cuts.append(electron_isEE_cut)
PreselectionWithExplicitEleIdEndcap.cuts.append(electron_sigmaIetaIetaEE_cut)
PreselectionWithExplicitEleIdEndcap.cuts.append(electron_deltaPhiSuperClusterEE_cut)
PreselectionWithExplicitEleIdEndcap.cuts.append(electron_deltaEtaSuperClusterEE_cut)
PreselectionWithExplicitEleIdEndcap.cuts.append(electron_hadronicOverEmEE_cut)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    PreselectionWithExplicitEleIdEndcap.cuts.append(electron_abs_1overE_1overP_cut)
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    PreselectionWithExplicitEleIdEndcap.cuts.append(electron_abs_1overE_1overP_EE_cut)
PreselectionWithExplicitEleIdEndcap.cuts.append(electron_missingInnerHits_cut)
PreselectionWithExplicitEleIdEndcap.cuts.append(electron_passConversionVeto_cut)
### at least one good muon
PreselectionWithExplicitEleIdEndcap.cuts.append(muon_eta_cut)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    PreselectionWithExplicitEleIdEndcap.cuts.append(muon_pt_40_cut)
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    PreselectionWithExplicitEleIdEndcap.cuts.append(muon_pt_50_cut)
PreselectionWithExplicitEleIdEndcap.cuts.append(muon_global_cut)
PreselectionWithExplicitEleIdEndcap.cuts.append(muon_id_cut)
PreselectionWithExplicitEleIdEndcap.cuts.append(muon_iso_cut)
