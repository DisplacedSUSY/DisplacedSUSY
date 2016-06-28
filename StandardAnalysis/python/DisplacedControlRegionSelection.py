import FWCore.ParameterSet.Config as cms
import copy
import string
from CutDefinitions import *
##########################################################################
######## Set up the prompt control region for the displaced SUSY analysis #########
##########################################################################
##########################################################################
#Displaced control region specific cuts
displaced_control_region_no_os_no_veto_cuts = cms.VPSet(
    # MUON DXY DISPLACED
    cms.PSet (
        inputCollection = cms.vstring("muons","beamspots"),
        cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) > 0.01 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("muon dxy > 0.01 cm")
    ),
    # ELECTRON DISPLACED
    cms.PSet (
        inputCollection = cms.vstring("electrons","beamspots"),
        cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) > 0.01 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron dxy > 0.01 cm")
    ),
    # MUON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("muons","beamspots"),
        cutString = cms.string("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) <= 0.02 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("muon dxy <= 0.02 cm")
    ),
    # ELECTRON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("electrons","beamspots"),
        cutString = cms.string("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) <= 0.02 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron dxy <= 0.02 cm")
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
extra_e_veto = cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
)
extra_mu_veto = cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
)

displaced_control_region_no_os_cuts = cms.VPSet()
displaced_control_region_no_os_cuts.extend(displaced_control_region_no_os_no_veto_cuts)
displaced_control_region_no_os_cuts.append(extra_e_veto)
displaced_control_region_no_os_cuts.append(extra_mu_veto)

displaced_control_region_cuts = cms.VPSet()
displaced_control_region_cuts.extend(displaced_control_region_no_os_no_veto_cuts)
displaced_control_region_cuts.append(e_mu_os_cut)
displaced_control_region_cuts.append(extra_e_veto)
displaced_control_region_cuts.append(extra_mu_veto)


##########################################################################
#Selections without triggers
DisplacedControlRegion = cms.PSet(
    name = cms.string("DisplacedControlRegion"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
DisplacedControlRegion.cuts.extend(electron_basic_selection_cuts)
DisplacedControlRegion.cuts.append(electron_iso_corr_cut)
DisplacedControlRegion.cuts.extend(muon_basic_selection_cuts)
DisplacedControlRegion.cuts.append(muon_iso_corr_cut)
DisplacedControlRegion.cuts.extend(displaced_control_region_cuts)

##########################################################################
#Selections with different triggers
DisplacedControlRegionPromptTrigger = cms.PSet(
    name = cms.string("DisplacedControlRegionPromptTrigger"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
DisplacedControlRegionPromptTrigger.cuts = cms.VPSet (copy.deepcopy(DisplacedControlRegion.cuts))

DisplacedControlRegionInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("DisplacedControlRegionInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
DisplacedControlRegionInclusiveDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(DisplacedControlRegion.cuts))
for cut in DisplacedControlRegionInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

DisplacedControlRegionDisplacedTrigger = cms.PSet(
    name = cms.string("DisplacedControlRegionDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
DisplacedControlRegionDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(DisplacedControlRegion.cuts))
for cut in DisplacedControlRegionDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")

DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
    )
)
DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.extend(electron_basic_selection_cuts)
DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.append(electron_loose_iso_corr_cut)
DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.extend(muon_basic_selection_cuts)
DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.append(muon_loose_iso_corr_cut)
DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.extend(displaced_control_region_no_os_cuts)
for cut in DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

DisplacedControlRegionNoIsoInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("DisplacedControlRegionNoIsoInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
    )
)
DisplacedControlRegionNoIsoInclusiveDisplacedTrigger.cuts.extend(electron_basic_selection_cuts)
DisplacedControlRegionNoIsoInclusiveDisplacedTrigger.cuts.append(electron_loose_iso_corr_cut)
DisplacedControlRegionNoIsoInclusiveDisplacedTrigger.cuts.extend(muon_basic_selection_cuts)
DisplacedControlRegionNoIsoInclusiveDisplacedTrigger.cuts.append(muon_loose_iso_corr_cut)
DisplacedControlRegionNoIsoInclusiveDisplacedTrigger.cuts.extend(displaced_control_region_cuts)
for cut in DisplacedControlRegionNoIsoInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

DisplacedControlRegionNoOSInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("DisplacedControlRegionNoOSInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
    )
)
DisplacedControlRegionNoOSInclusiveDisplacedTrigger.cuts.extend(electron_basic_selection_cuts)
DisplacedControlRegionNoOSInclusiveDisplacedTrigger.cuts.append(electron_iso_corr_cut)
DisplacedControlRegionNoOSInclusiveDisplacedTrigger.cuts.extend(muon_basic_selection_cuts)
DisplacedControlRegionNoOSInclusiveDisplacedTrigger.cuts.append(muon_iso_corr_cut)
DisplacedControlRegionNoOSInclusiveDisplacedTrigger.cuts.extend(displaced_control_region_no_os_cuts)
for cut in DisplacedControlRegionNoOSInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

DisplacedControlRegionNonIsoInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("DisplacedControlRegionNonIsoInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
    )
)
DisplacedControlRegionNonIsoInclusiveDisplacedTrigger.cuts.extend(electron_basic_selection_cuts)
DisplacedControlRegionNonIsoInclusiveDisplacedTrigger.cuts.append(electron_inverted_iso_corr_cut)
DisplacedControlRegionNonIsoInclusiveDisplacedTrigger.cuts.extend(muon_basic_selection_cuts)
DisplacedControlRegionNonIsoInclusiveDisplacedTrigger.cuts.append(muon_inverted_iso_corr_cut)
DisplacedControlRegionNonIsoInclusiveDisplacedTrigger.cuts.extend(displaced_control_region_cuts)
for cut in DisplacedControlRegionNonIsoInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")
