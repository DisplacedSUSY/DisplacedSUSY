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

OSAntiIso = cms.PSet(
    name = cms.string("OSAntiIso"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
OSAntiIso.cuts.extend(jet_basic_selection_cuts)
OSAntiIso.cuts.extend(electron_basic_selection_cuts)
OSAntiIso.cuts.append(electron_inverted_iso_cut)
OSAntiIso.cuts.extend(muon_basic_selection_cuts)
OSAntiIso.cuts.append(muon_inverted_iso_cut)
OSAntiIso.cuts.extend(preselection_emu_cuts)
OSAntiIso.cuts.append(os_emu_cut)

for cut in OSAntiIso.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

#################################################################

OSAntiIsoMuIsoEle = cms.PSet(
    name = cms.string("OSAntiIsoMuIsoEle"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
OSAntiIsoMuIsoEle.cuts.extend(jet_basic_selection_cuts)
OSAntiIsoMuIsoEle.cuts.extend(electron_basic_selection_cuts)
OSAntiIsoMuIsoEle.cuts.append(electron_iso_cut)
OSAntiIsoMuIsoEle.cuts.append(electron_jet_deltaR_cut)
OSAntiIsoMuIsoEle.cuts.extend(muon_basic_selection_cuts)
OSAntiIsoMuIsoEle.cuts.append(muon_inverted_iso_cut)
OSAntiIsoMuIsoEle.cuts.extend(preselection_emu_cuts)
OSAntiIsoMuIsoEle.cuts.append(os_emu_cut)

for cut in OSAntiIsoMuIsoEle.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

#################################################################

OSIsoMuAntiIsoEle = cms.PSet(
    name = cms.string("OSIsoMuAntiIsoEle"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
OSIsoMuAntiIsoEle.cuts.extend(jet_basic_selection_cuts)
OSIsoMuAntiIsoEle.cuts.extend(electron_basic_selection_cuts)
OSIsoMuAntiIsoEle.cuts.append(electron_inverted_iso_cut)
OSIsoMuAntiIsoEle.cuts.extend(muon_basic_selection_cuts)
OSIsoMuAntiIsoEle.cuts.append(muon_iso_cut)
OSIsoMuAntiIsoEle.cuts.append(muon_jet_deltaR_cut)
OSIsoMuAntiIsoEle.cuts.extend(preselection_emu_cuts)
OSIsoMuAntiIsoEle.cuts.append(os_emu_cut)

for cut in OSIsoMuAntiIsoEle.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

#################################################################

SSAntiIso = cms.PSet(
    name = cms.string("SSAntiIso"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
SSAntiIso.cuts.extend(jet_basic_selection_cuts)
SSAntiIso.cuts.extend(electron_basic_selection_cuts)
SSAntiIso.cuts.append(electron_inverted_iso_cut)
SSAntiIso.cuts.extend(muon_basic_selection_cuts)
SSAntiIso.cuts.append(muon_inverted_iso_cut)
SSAntiIso.cuts.extend(preselection_emu_cuts)
SSAntiIso.cuts.append(ss_emu_cut)

for cut in SSAntiIso.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

#################################################################

SSIso = cms.PSet(
    name = cms.string("SSIso"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
SSIso.cuts.extend(jet_basic_selection_cuts)
SSIso.cuts.extend(electron_basic_selection_cuts)
SSIso.cuts.append(electron_iso_cut)
SSIso.cuts.extend(muon_basic_selection_cuts)
SSIso.cuts.append(muon_iso_cut)
SSIso.cuts.extend(preselection_emu_cuts)
SSIso.cuts.append(ss_emu_cut)

for cut in SSIso.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

#################################################################
muon_near_jet_cut = cms.PSet (
    inputCollection = cms.vstring("muons","jets"),
    cutString = cms.string("deltaR(muon,jet) < 0.5"),
    numberRequired = cms.string(">= 0"),
    alias = cms.string("jets near muons")
)
electron_near_bjet_cut = cms.PSet (
    inputCollection = cms.vstring("electrons","bjets"),
    cutString = cms.string("deltaR(electron,bjet) < 0.5"),
    numberRequired = cms.string(">= 1"),
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

AntiIsoBlinded = cms.PSet(
    name = cms.string("AntiIsoBlinded"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
AntiIsoBlinded.cuts.extend(jet_basic_selection_cuts)
AntiIsoBlinded.cuts.extend(bjet_basic_selection_cuts)
AntiIsoBlinded.cuts.extend(electron_basic_selection_cuts)
AntiIsoBlinded.cuts.append(electron_inverted_iso_cut)
AntiIsoBlinded.cuts.extend(muon_basic_selection_cuts)
AntiIsoBlinded.cuts.append(muon_inverted_iso_cut)
AntiIsoBlinded.cuts.append(muon_near_jet_cut)
AntiIsoBlinded.cuts.append(jet_csv_cut)
AntiIsoBlinded.cuts.append(electron_near_bjet_cut)
AntiIsoBlinded.cuts.append(bjet_csv_cut)
AntiIsoBlinded.cuts.extend(blinded_control_region_cuts)

for cut in AntiIsoBlinded.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoBlindedOS = cms.PSet(
    name = cms.string("AntiIsoBlindedOS"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
AntiIsoBlindedOS.cuts.extend(jet_basic_selection_cuts)
AntiIsoBlindedOS.cuts.extend(bjet_basic_selection_cuts)
AntiIsoBlindedOS.cuts.extend(electron_basic_selection_cuts)
AntiIsoBlindedOS.cuts.append(electron_inverted_iso_cut)
AntiIsoBlindedOS.cuts.extend(muon_basic_selection_cuts)
AntiIsoBlindedOS.cuts.append(muon_inverted_iso_cut)
AntiIsoBlindedOS.cuts.append(muon_near_jet_cut)
AntiIsoBlindedOS.cuts.append(electron_near_bjet_cut)
AntiIsoBlindedOS.cuts.extend(blinded_control_region_cuts)
AntiIsoBlindedOS.cuts.append(os_emu_cut)

for cut in AntiIsoBlindedOS.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoBlindedSS = cms.PSet(
    name = cms.string("AntiIsoBlindedSS"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
AntiIsoBlindedSS.cuts.extend(jet_basic_selection_cuts)
AntiIsoBlindedSS.cuts.extend(bjet_basic_selection_cuts)
AntiIsoBlindedSS.cuts.extend(electron_basic_selection_cuts)
AntiIsoBlindedSS.cuts.append(electron_inverted_iso_cut)
AntiIsoBlindedSS.cuts.extend(muon_basic_selection_cuts)
AntiIsoBlindedSS.cuts.append(muon_inverted_iso_cut)
AntiIsoBlindedSS.cuts.append(muon_near_jet_cut)
AntiIsoBlindedSS.cuts.append(electron_near_bjet_cut)
AntiIsoBlindedSS.cuts.extend(blinded_control_region_cuts)
AntiIsoBlindedSS.cuts.append(ss_emu_cut)

for cut in AntiIsoBlindedSS.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoNotBlinded = cms.PSet(
    name = cms.string("AntiIsoNotBlinded"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
AntiIsoNotBlinded.cuts.extend(jet_basic_selection_cuts)
AntiIsoNotBlinded.cuts.extend(bjet_basic_selection_cuts)
AntiIsoNotBlinded.cuts.extend(electron_basic_selection_cuts)
AntiIsoNotBlinded.cuts.append(electron_inverted_iso_cut)
AntiIsoNotBlinded.cuts.extend(muon_basic_selection_cuts)
AntiIsoNotBlinded.cuts.append(muon_inverted_iso_cut)
AntiIsoNotBlinded.cuts.append(muon_near_jet_cut)
AntiIsoNotBlinded.cuts.append(electron_near_bjet_cut)
AntiIsoNotBlinded.cuts.extend(preselection_emu_cuts)

for cut in AntiIsoNotBlinded.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoDisplacedBlinded = cms.PSet(
    name = cms.string("AntiIsoDisplacedBlinded"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
AntiIsoDisplacedBlinded.cuts.extend(jet_basic_selection_cuts)
AntiIsoDisplacedBlinded.cuts.extend(bjet_basic_selection_cuts)
AntiIsoDisplacedBlinded.cuts.extend(electron_basic_selection_cuts)
AntiIsoDisplacedBlinded.cuts.append(electron_inverted_iso_cut)
AntiIsoDisplacedBlinded.cuts.extend(muon_basic_selection_cuts)
AntiIsoDisplacedBlinded.cuts.append(muon_inverted_iso_cut)
AntiIsoDisplacedBlinded.cuts.append(muon_near_jet_cut)
AntiIsoDisplacedBlinded.cuts.append(electron_near_bjet_cut)
AntiIsoDisplacedBlinded.cuts.append(bjet_csv_cut)
AntiIsoDisplacedBlinded.cuts.extend(displaced_blinded_control_region_cuts)

for cut in AntiIsoDisplacedBlinded.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoLooseDisplacedBlinded = cms.PSet(
    name = cms.string("AntiIsoLooseDisplacedBlinded"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)
AntiIsoLooseDisplacedBlinded.cuts.extend(jet_basic_selection_cuts)
AntiIsoLooseDisplacedBlinded.cuts.extend(bjet_basic_selection_cuts)
AntiIsoLooseDisplacedBlinded.cuts.extend(electron_basic_selection_cuts)
AntiIsoLooseDisplacedBlinded.cuts.append(electron_inverted_iso_cut)
AntiIsoLooseDisplacedBlinded.cuts.extend(muon_basic_selection_cuts)
AntiIsoLooseDisplacedBlinded.cuts.append(muon_inverted_iso_cut)
AntiIsoLooseDisplacedBlinded.cuts.append(muon_near_jet_cut)
AntiIsoLooseDisplacedBlinded.cuts.append(electron_near_bjet_cut)
AntiIsoLooseDisplacedBlinded.cuts.append(bjet_csv_cut)
AntiIsoLooseDisplacedBlinded.cuts.extend(loose_displaced_blinded_control_region_cuts)

for cut in AntiIsoLooseDisplacedBlinded.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")
