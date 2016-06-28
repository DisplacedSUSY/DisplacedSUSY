import FWCore.ParameterSet.Config as cms
import copy
import string
from CutDefinitions import *
##########################################################################
######## Set up the prompt control region for the displaced SUSY analysis #########
##########################################################################
##########################################################################
prompt_control_region_no_os_no_veto_cuts = cms.VPSet(
    # MUON DXY PROMPT
    cms.PSet (
        inputCollection = cms.vstring("muons","beamspots"),
        cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) <= 0.01 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("muon dxy <= 0.01 cm")
    ),
    # ELECTRON PROMPT
    cms.PSet (
        inputCollection = cms.vstring("electrons","beamspots"),
        cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) <= 0.01 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron dxy <= 0.01 cm")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
       cutString = cms.string("deltaR(electron, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
    ),
)
e_mu_os_cut = cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("electron.charge * muon.charge < 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("oppositely charged e-mu pair")
)
extra_mu_veto = cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
)
extra_e_veto = cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
)

prompt_control_region_cuts = cms.VPSet()
prompt_control_region_cuts.extend(prompt_control_region_no_os_no_veto_cuts)
prompt_control_region_cuts.append(e_mu_os_cut)
prompt_control_region_cuts.append(extra_mu_veto)
prompt_control_region_cuts.append(extra_e_veto)

prompt_control_region_no_os_cuts = cms.VPSet()
prompt_control_region_no_os_cuts.extend(prompt_control_region_no_os_no_veto_cuts)
prompt_control_region_no_os_cuts.append(extra_mu_veto)
prompt_control_region_no_os_cuts.append(extra_e_veto)


##########################################################################
#Selections without triggers
PromptControlRegion = cms.PSet(
    name = cms.string("PromptControlRegion"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
PromptControlRegion.cuts.extend(electron_basic_selection_cuts)
PromptControlRegion.cuts.append(electron_iso_corr_cut)
PromptControlRegion.cuts.extend(muon_basic_selection_cuts)
PromptControlRegion.cuts.append(muon_iso_corr_cut)
PromptControlRegion.cuts.extend(prompt_control_region_cuts)

##########################################################################
#Selections with prompt trigger
PromptControlRegionPromptTrigger = cms.PSet(
    name = cms.string("PromptControlRegionPromptTrigger"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
PromptControlRegionPromptTrigger.cuts = cms.VPSet (copy.deepcopy(PromptControlRegion.cuts))

##########################################################################
#Selections with inclusive displaced trigger

PromptControlRegionInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("PromptControlRegionInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
PromptControlRegionInclusiveDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(PromptControlRegion.cuts))

for cut in PromptControlRegionInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

##########################################################################
#Selections with inclusive displaced trigger, barrel/endcap electrons

PromptControlRegionEBEleInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("PromptControlRegionEBEleInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
PromptControlRegionEBEleInclusiveDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(PromptControlRegionInclusiveDisplacedTrigger.cuts))
for cut in PromptControlRegionEBEleInclusiveDisplacedTrigger.cuts:
    if "abs(eta) < 2.4" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("abs(eta) < 1.5")

PromptControlRegionEEEleInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("PromptControlRegionEEEleInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
PromptControlRegionEEEleInclusiveDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(PromptControlRegionInclusiveDisplacedTrigger.cuts))
for cut in PromptControlRegionEEEleInclusiveDisplacedTrigger.cuts:
    if "abs(eta) < 2.4" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("abs(eta) < 2.4 && abs(eta) > 1.5")

##########################################################################
#Selections with displaced trigger

PromptControlRegionDisplacedTrigger = cms.PSet(
    name = cms.string("PromptControlRegionDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
PromptControlRegionDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(PromptControlRegion.cuts))
for cut in PromptControlRegionDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")


PromptControlRegionNoIsoInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("PromptControlRegionNoIsoInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
    )
)
PromptControlRegionNoIsoInclusiveDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(PromptControlRegionInclusiveDisplacedTrigger.cuts))
for cut in PromptControlRegionNoIsoInclusiveDisplacedTrigger.cuts:
    if "pfdBetaIsoCorr" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pfdBetaIsoCorr <= 1.5")
        cut.alias = cms.string("muon isolation corrected")
    if "pfdRhoIsoCorr" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pfdRhoIsoCorr <= 1.5")
        cut.alias = cms.string("electron isolation corrected")

PromptControlRegionNoIsoNoOSInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("PromptControlRegionNoIsoNoOSInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
    )
)
PromptControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.extend(electron_basic_selection_cuts)
PromptControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.append(electron_loose_iso_corr_cut)
PromptControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.extend(muon_basic_selection_cuts)
PromptControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.append(muon_loose_iso_corr_cut)
PromptControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.extend(prompt_control_region_no_os_cuts)

for cut in PromptControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

PromptControlRegionNoOSInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("PromptControlRegionNoOSInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
    )
)
PromptControlRegionNoOSInclusiveDisplacedTrigger.cuts.extend(electron_basic_selection_cuts)
PromptControlRegionNoOSInclusiveDisplacedTrigger.cuts.append(electron_iso_corr_cut)
PromptControlRegionNoOSInclusiveDisplacedTrigger.cuts.extend(muon_basic_selection_cuts)
PromptControlRegionNoOSInclusiveDisplacedTrigger.cuts.append(muon_iso_corr_cut)
PromptControlRegionNoOSInclusiveDisplacedTrigger.cuts.extend(prompt_control_region_no_os_cuts)
for cut in PromptControlRegionNoOSInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")


PromptControlRegionNoIsoDisplacedTrigger = cms.PSet(
    name = cms.string("PromptControlRegionNoIsoDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
    )
)
PromptControlRegionNoIsoDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(PromptControlRegionNoIsoInclusiveDisplacedTrigger.cuts))
for cut in PromptControlRegionNoIsoDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")

PromptControlRegionNoIsoNoOSDisplacedTrigger = cms.PSet(
    name = cms.string("PromptControlRegionNoIsoNoOSDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
    )
)
PromptControlRegionNoIsoNoOSDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(PromptControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts))
for cut in PromptControlRegionNoIsoNoOSDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")

PromptControlRegionNoOSDisplacedTrigger = cms.PSet(
    name = cms.string("PromptControlRegionNoOSDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
    )
)
PromptControlRegionNoOSDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(PromptControlRegionNoOSInclusiveDisplacedTrigger.cuts))
for cut in PromptControlRegionNoOSDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")
