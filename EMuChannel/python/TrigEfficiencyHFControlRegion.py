import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *
from DisplacedSUSY.StandardAnalysis.Triggers import *


# Denominator: bbar selection+(MET triggers)
TrigEffHFDen = cms.PSet(
    name = cms.string("TrigEffHFDen"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### passes OR of unprescaled MET triggers (use eventvariable so that OR of MET triggers can be ANDed with analysis trigger)
TrigEffHFDen.cuts.append(pass_HLTMET_paths)

### require 1 jet (probe jet) and another jet that is b-tagged (tag jet)
### require that the probe and tag jets are back-to-back in delta phi
TrigEffHFDen.cuts.extend(atLeastOne_jet_basic_selection_cuts)
TrigEffHFDen.cuts.append(veto_3orMore_jets)
TrigEffHFDen.cuts.extend(atLeastOne_bjet_basic_selection_cuts)
TrigEffHFDen.cuts.append(veto_3orMore_bjets)
TrigEffHFDen.cuts.append(jet_btag_2_mwp_cut) #2 medium CSV v2 b-tags
TrigEffHFDen.cuts.append(jet_bjet_deltaPhi_cut)

### exactly one good muon near probe jet
TrigEffHFDen.cuts.append(muon_eta_cut)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    TrigEffHFDen.cuts.append(muon_eta_phi_veto_2017) #veto region with pixel power supply issues
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    TrigEffHFDen.cuts.append(muon_eta_phi_veto_2018) #veto region with pixel power supply issues
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    TrigEffHFDen.cuts.append(muon_pt_40_cut) #plateau of trigger turn on
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    TrigEffHFDen.cuts.append(muon_pt_45_cut) #plateau of trigger turn on
TrigEffHFDen.cuts.append(muon_global_cut)
TrigEffHFDen.cuts.append(muon_id_cut)
TrigEffHFDen.cuts.append(muon_num_exactly_1_cut)
TrigEffHFDen.cuts.append(muon_jet_deltaR_cut) #muon and jet within deltaR<0.5

TrigEffHFDenWithIso = cms.PSet(
    name = cms.string("TrigEffHFDenWithIso"),
    triggers = cms.vstring(),
    #cuts = cms.VPSet(copy.deepcopy(TrigEffHFDen.cuts))
    cuts = cms.VPSet()
)
TrigEffHFDenWithIso.cuts.append(muon_iso_cut) #our custom rho-based iso


# Numerator: bbar selection+high pt other leg+(MET triggers)+(analysis trigger)
TrigEffHFNum = cms.PSet(
    name = cms.string("TrigEffHFNum"),
    triggers = triggersMuonPhoton,
    #cuts = cms.VPSet(copy.deepcopy(TrigEffHFDen.cuts))
    cuts = cms.VPSet()
)
