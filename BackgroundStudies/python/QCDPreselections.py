import FWCore.ParameterSet.Config as cms
import copy

##################################################
##### Set up the event selections (channels) #####
##################################################

from DisplacedSUSY.StandardAnalysis.EMuPreselection import *
from DisplacedSUSY.StandardAnalysis.CutDefinitions import *

##########################################################################
#Blinded control region specific cuts
electron_blinded_cuts = cms.VPSet(
    #ELECTRON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("electrons","beamspots"),
        cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) <= 0.02"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron blinding cuts")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("deltaR(electron, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
    )
)

electron_blinded_control_region_os_cuts = cms.VPSet()
electron_blinded_control_region_os_cuts.extend(electron_blinded_cuts)
electron_blinded_control_region_os_cuts.append(os_emu_cut)
electron_blinded_control_region_os_cuts.append(muon_veto_cut)
electron_blinded_control_region_os_cuts.append(electron_veto_cut)

electron_blinded_control_region_cuts = cms.VPSet()
electron_blinded_control_region_cuts.extend(electron_blinded_cuts)
electron_blinded_control_region_cuts.append(muon_veto_cut)
electron_blinded_control_region_cuts.append(electron_veto_cut)

muon_blinded_cuts = cms.VPSet(
    #MUON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("muons","beamspots"),
        cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) <= 0.02"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("muon blinding cuts")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("deltaR(electron, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
    )
)

muon_blinded_control_region_os_cuts = cms.VPSet()
muon_blinded_control_region_os_cuts.extend(muon_blinded_cuts)
muon_blinded_control_region_os_cuts.append(os_emu_cut)
muon_blinded_control_region_os_cuts.append(muon_veto_cut)
muon_blinded_control_region_os_cuts.append(electron_veto_cut)

muon_blinded_control_region_cuts = cms.VPSet()
muon_blinded_control_region_cuts.extend(muon_blinded_cuts)
muon_blinded_control_region_cuts.append(muon_veto_cut)
muon_blinded_control_region_cuts.append(electron_veto_cut)

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
AntiIsoElectronBlinded.cuts.extend(electron_blinded_control_region_os_cuts)

for cut in AntiIsoElectronBlinded.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoElectronBlindedNoOS = cms.PSet(
    name = cms.string("AntiIsoElectronBlindedNoOS"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)

AntiIsoElectronBlindedNoOS.cuts = cms.VPSet (copy.deepcopy(AntiIsoElectronBlinded.cuts))
for cut in AntiIsoElectronBlindedNoOS.cuts:
    if "electron.charge" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        AntiIsoElectronBlindedNoOS.cuts.remove(cut)

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
AntiIsoMuonBlinded.cuts.extend(muon_blinded_control_region_os_cuts)

for cut in AntiIsoMuonBlinded.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuonBlindedNoOS = cms.PSet(
    name = cms.string("AntiIsoMuonBlindedNoOS"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)

AntiIsoMuonBlindedNoOS.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuonBlinded.cuts))
for cut in AntiIsoMuonBlindedNoOS.cuts:
    if "electron.charge" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        AntiIsoMuonBlindedNoOS.cuts.remove(cut)


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
AntiIsoMuonBlindedElectronDisplaced.cuts.extend(muon_blinded_control_region_os_cuts)

for cut in AntiIsoMuonBlindedElectronDisplaced.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuonBlindedElectronDisplacedNoOS = cms.PSet(
    name = cms.string("AntiIsoMuonBlindedElectronDisplacedNoOS"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)

AntiIsoMuonBlindedElectronDisplacedNoOS.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuonBlindedElectronDisplaced.cuts))
for cut in AntiIsoMuonBlindedElectronDisplacedNoOS.cuts:
    if "electron.charge" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        AntiIsoMuonBlindedElectronDisplacedNoOS.cuts.remove(cut)

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
AntiIsoElectronBlindedMuonDisplaced.cuts.extend(electron_blinded_control_region_os_cuts)

for cut in AntiIsoElectronBlindedMuonDisplaced.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoElectronBlindedMuonDisplacedNoOS = cms.PSet(
    name = cms.string("AntiIsoElectronBlindedMuonDisplacedNoOS"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), 
    cuts = cms.VPSet ()
)

AntiIsoElectronBlindedMuonDisplacedNoOS.cuts = cms.VPSet (copy.deepcopy(AntiIsoElectronBlindedMuonDisplaced.cuts))
for cut in AntiIsoElectronBlindedMuonDisplacedNoOS.cuts:
    if "electron.charge" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        AntiIsoElectronBlindedMuonDisplacedNoOS.cuts.remove(cut)
