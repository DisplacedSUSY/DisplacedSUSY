import FWCore.ParameterSet.Config as cms
import copy

##################################################
##### Set up the event selections (channels) #####
##################################################

from DisplacedSUSY.StandardAnalysis.EMuPreselection import *
from DisplacedSUSY.StandardAnalysis.CutDefinitions import *

# ELECTRON DXY
electron_d0_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","beamspots"),
    cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) >= 0.01 "),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron dxy >= 0.01 cm")
)

# MUON DXY
muon_d0_cut = cms.PSet (
    inputCollection = cms.vstring("muons","beamspots"),
    cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) >= 0.01 "),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muon dxy >= 0.01 cm")
)


#################################################################
muon_near_jet_cut = cms.PSet (
    inputCollection = cms.vstring("muons","jets"),
    cutString = cms.string("deltaR(muon,jet) < 0.5"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("jets near muons")
)
electron_near_jet_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","jets"),
    cutString = cms.string("deltaR(electron,jet) < 0.5"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("jets near electrons")
)
bjet_csv_cut = cms.PSet (
    inputCollection = cms.vstring("bjets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 0"),
    arbitration = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
)
jet_csv_cut = cms.PSet (
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 0"),
    arbitration = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
)

AntiIsoElectronBlinded = cms.PSet(
    name = cms.string("AntiIsoElectronBlinded"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
AntiIsoElectronBlinded.cuts.extend(jet_basic_selection_cuts)
AntiIsoElectronBlinded.cuts.extend(electron_basic_selection_cuts)
AntiIsoElectronBlinded.cuts.append(electron_inverted_iso_corr_cut)
AntiIsoElectronBlinded.cuts.extend(muon_basic_selection_cuts)
AntiIsoElectronBlinded.cuts.append(muon_inverted_iso_corr_cut)
AntiIsoElectronBlinded.cuts.append(muon_near_jet_cut)
AntiIsoElectronBlinded.cuts.append(jet_csv_cut)
AntiIsoElectronBlinded.cuts.extend(electron_blinded_control_region_cuts)

for cut in AntiIsoElectronBlinded.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuonBlinded = cms.PSet(
    name = cms.string("AntiIsoMuonBlinded"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
AntiIsoMuonBlinded.cuts.extend(jet_basic_selection_cuts)
AntiIsoMuonBlinded.cuts.extend(electron_basic_selection_cuts)
AntiIsoMuonBlinded.cuts.append(electron_inverted_iso_corr_cut)
AntiIsoMuonBlinded.cuts.extend(muon_basic_selection_cuts)
AntiIsoMuonBlinded.cuts.append(muon_inverted_iso_corr_cut)
AntiIsoMuonBlinded.cuts.append(electron_near_jet_cut)
AntiIsoMuonBlinded.cuts.append(jet_csv_cut)
AntiIsoMuonBlinded.cuts.extend(muon_blinded_control_region_cuts)

for cut in AntiIsoMuonBlinded.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuonBlindedEleEE = cms.PSet(
    name = cms.string("AntiIsoMuonBlindedEleEE"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
AntiIsoMuonBlindedEleEE.cuts.extend(jet_basic_selection_cuts)
AntiIsoMuonBlindedEleEE.cuts.extend(electron_basic_selection_ee_cuts)
AntiIsoMuonBlindedEleEE.cuts.append(electron_inverted_iso_corr_cut)
AntiIsoMuonBlindedEleEE.cuts.extend(muon_basic_selection_cuts)
AntiIsoMuonBlindedEleEE.cuts.append(muon_inverted_iso_corr_cut)
AntiIsoMuonBlindedEleEE.cuts.append(electron_near_jet_cut)
AntiIsoMuonBlindedEleEE.cuts.append(jet_csv_cut)
AntiIsoMuonBlindedEleEE.cuts.extend(muon_blinded_control_region_cuts)

for cut in AntiIsoMuonBlindedEleEE.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuonBlindedEleEB = cms.PSet(
    name = cms.string("AntiIsoMuonBlindedEleEB"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
AntiIsoMuonBlindedEleEB.cuts.extend(jet_basic_selection_cuts)
AntiIsoMuonBlindedEleEB.cuts.extend(electron_basic_selection_eb_cuts)
AntiIsoMuonBlindedEleEB.cuts.append(electron_inverted_iso_corr_cut)
AntiIsoMuonBlindedEleEB.cuts.extend(muon_basic_selection_cuts)
AntiIsoMuonBlindedEleEB.cuts.append(muon_inverted_iso_corr_cut)
AntiIsoMuonBlindedEleEB.cuts.append(electron_near_jet_cut)
AntiIsoMuonBlindedEleEB.cuts.append(jet_csv_cut)
AntiIsoMuonBlindedEleEB.cuts.extend(muon_blinded_control_region_cuts)

for cut in AntiIsoMuonBlindedEleEB.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuonBlindedElectronDisplaced = cms.PSet(
    name = cms.string("AntiIsoMuonBlindedElectronDisplaced"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
AntiIsoMuonBlindedElectronDisplaced.cuts.extend(jet_basic_selection_cuts)
AntiIsoMuonBlindedElectronDisplaced.cuts.extend(electron_basic_selection_cuts)
AntiIsoMuonBlindedElectronDisplaced.cuts.append(electron_inverted_iso_corr_cut)
AntiIsoMuonBlindedElectronDisplaced.cuts.extend(muon_basic_selection_cuts)
AntiIsoMuonBlindedElectronDisplaced.cuts.append(muon_inverted_iso_corr_cut)
AntiIsoMuonBlindedElectronDisplaced.cuts.append(electron_near_jet_cut)
AntiIsoMuonBlindedElectronDisplaced.cuts.append(electron_d0_cut)
AntiIsoMuonBlindedElectronDisplaced.cuts.append(jet_csv_cut)
AntiIsoMuonBlindedElectronDisplaced.cuts.extend(muon_blinded_control_region_cuts)

for cut in AntiIsoMuonBlindedElectronDisplaced.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoElectronBlindedMuonDisplaced = cms.PSet(
    name = cms.string("AntiIsoElectronBlindedMuonDisplaced"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
AntiIsoElectronBlindedMuonDisplaced.cuts.extend(jet_basic_selection_cuts)
AntiIsoElectronBlindedMuonDisplaced.cuts.extend(electron_basic_selection_cuts)
AntiIsoElectronBlindedMuonDisplaced.cuts.append(electron_inverted_iso_corr_cut)
AntiIsoElectronBlindedMuonDisplaced.cuts.extend(muon_basic_selection_cuts)
AntiIsoElectronBlindedMuonDisplaced.cuts.append(muon_inverted_iso_corr_cut)
AntiIsoElectronBlindedMuonDisplaced.cuts.append(muon_near_jet_cut)
AntiIsoElectronBlindedMuonDisplaced.cuts.append(muon_d0_cut)
AntiIsoElectronBlindedMuonDisplaced.cuts.append(jet_csv_cut)
AntiIsoElectronBlindedMuonDisplaced.cuts.extend(electron_blinded_control_region_cuts)

for cut in AntiIsoElectronBlindedMuonDisplaced.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")
