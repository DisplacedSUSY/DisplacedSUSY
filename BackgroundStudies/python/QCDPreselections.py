import FWCore.ParameterSet.Config as cms
import copy

##################################################
##### Set up the event selections (channels) #####
##################################################

from DisplacedSUSY.StandardAnalysis.EMuPreselection import *
from DisplacedSUSY.StandardAnalysis.CutDefinitions import *

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

