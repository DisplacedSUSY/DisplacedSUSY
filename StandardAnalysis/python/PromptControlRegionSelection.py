import FWCore.ParameterSet.Config as cms
import copy
import string
from CutDefinitions import *
##########################################################################
######## Set up the prompt control region for the displaced SUSY analysis #########
##########################################################################
##########################################################################
#Displaced control region specific cuts
prompt_control_region_cuts = cms.VPSet(
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
    # OPPOSITE SIGN E-MU PAIR
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("electron.charge * muon.charge < 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("oppositely charged e-mu pair")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("electrons", "muons"),
        cutString = cms.string("deltaR(electron, muon) > 0.5"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
    ),
    #Extra Lepton Veto
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
    ),
    #ELECTRON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)

prompt_control_region_no_os_cuts = cms.VPSet(
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
    #Extra Lepton Veto
    cms.PSet (
        inputCollection = cms.vstring("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
    ),
    #ELECTRON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)

##########################################################################
#Selections without triggers
PromptControlRegion = cms.PSet(
    name = cms.string("PromptControlRegion"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
PromptControlRegion.cuts.extend(electron_basic_selection_cuts)
PromptControlRegion.cuts.append(electron_iso_cut)
PromptControlRegion.cuts.extend(muon_basic_selection_cuts)
PromptControlRegion.cuts.append(muon_iso_cut)
PromptControlRegion.cuts.extend(prompt_control_region_cuts)

AntiIsoMuAntiIsoElePromptControlRegion = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoElePromptControlRegion"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
AntiIsoMuAntiIsoElePromptControlRegion.cuts.extend(electron_basic_selection_cuts)
AntiIsoMuAntiIsoElePromptControlRegion.cuts.append(electron_inverted_iso_cut)
AntiIsoMuAntiIsoElePromptControlRegion.cuts.extend(muon_basic_selection_cuts)
AntiIsoMuAntiIsoElePromptControlRegion.cuts.append(muon_inverted_iso_cut)
AntiIsoMuAntiIsoElePromptControlRegion.cuts.extend(prompt_control_region_cuts)

IsoMuAntiIsoElePromptControlRegion = cms.PSet(
    name = cms.string("IsoMuAntiIsoElePromptControlRegion"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
IsoMuAntiIsoElePromptControlRegion.cuts.extend(electron_basic_selection_cuts)
IsoMuAntiIsoElePromptControlRegion.cuts.append(electron_inverted_iso_cut)
IsoMuAntiIsoElePromptControlRegion.cuts.extend(muon_basic_selection_cuts)
IsoMuAntiIsoElePromptControlRegion.cuts.append(muon_iso_cut)
IsoMuAntiIsoElePromptControlRegion.cuts.extend(prompt_control_region_cuts)

AntiIsoMuIsoElePromptControlRegion = cms.PSet(
    name = cms.string("AntiIsoMuIsoElePromptControlRegion"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
AntiIsoMuIsoElePromptControlRegion.cuts.extend(electron_basic_selection_cuts)
AntiIsoMuIsoElePromptControlRegion.cuts.append(electron_iso_cut)
AntiIsoMuIsoElePromptControlRegion.cuts.extend(muon_basic_selection_cuts)
AntiIsoMuIsoElePromptControlRegion.cuts.append(muon_inverted_iso_cut)
AntiIsoMuIsoElePromptControlRegion.cuts.extend(prompt_control_region_cuts)
##########################################################################
#Selections with different triggers
PromptControlRegionPromptTrigger = cms.PSet(
    name = cms.string("PromptControlRegionPromptTrigger"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
PromptControlRegionPromptTrigger.cuts = cms.VPSet (copy.deepcopy(PromptControlRegion.cuts))

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

PromptControlRegionDisplacedTrigger = cms.PSet(
    name = cms.string("AntiIsoPromptControlRegionDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
PromptControlRegionDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(PromptControlRegion.cuts))

for cut in PromptControlRegionDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")


IsoMuAntiIsoElePromptControlRegionPromptTrigger = cms.PSet(
    name = cms.string("IsoMuAntiIsoElePromptControlRegionPromptTrigger"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
IsoMuAntiIsoElePromptControlRegionPromptTrigger.cuts = cms.VPSet (copy.deepcopy(IsoMuAntiIsoElePromptControlRegion.cuts))

IsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("IsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
IsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(IsoMuAntiIsoElePromptControlRegion.cuts))

for cut in IsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

IsoMuAntiIsoElePromptControlRegionDisplacedTrigger = cms.PSet(
    name = cms.string("AntiIsoPromptControlRegionDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
IsoMuAntiIsoElePromptControlRegionDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(IsoMuAntiIsoElePromptControlRegion.cuts))

for cut in IsoMuAntiIsoElePromptControlRegionDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")

AntiIsoMuIsoElePromptControlRegionPromptTrigger = cms.PSet(
    name = cms.string("AntiIsoMuIsoElePromptControlRegionPromptTrigger"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuIsoElePromptControlRegionPromptTrigger.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuIsoElePromptControlRegion.cuts))

AntiIsoMuIsoElePromptControlRegionInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("AntiIsoMuIsoElePromptControlRegionInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuIsoElePromptControlRegionInclusiveDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuIsoElePromptControlRegion.cuts))

for cut in AntiIsoMuIsoElePromptControlRegionInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuIsoElePromptControlRegionDisplacedTrigger = cms.PSet(
    name = cms.string("AntiIsoPromptControlRegionDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuIsoElePromptControlRegionDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuIsoElePromptControlRegion.cuts))

for cut in AntiIsoMuIsoElePromptControlRegionDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")


AntiIsoMuAntiIsoElePromptControlRegionPromptTrigger = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoElePromptControlRegionPromptTrigger"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuAntiIsoElePromptControlRegionPromptTrigger.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuAntiIsoElePromptControlRegion.cuts))

AntiIsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuAntiIsoElePromptControlRegion.cuts))

for cut in AntiIsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuAntiIsoElePromptControlRegionDisplacedTrigger = cms.PSet(
    name = cms.string("AntiIsoPromptControlRegionDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuAntiIsoElePromptControlRegionDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuAntiIsoElePromptControlRegion.cuts))

for cut in AntiIsoMuAntiIsoElePromptControlRegionDisplacedTrigger.cuts:
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
PromptControlRegionNoIsoInclusiveDisplacedTrigger.cuts.extend(electron_basic_selection_cuts)
PromptControlRegionNoIsoInclusiveDisplacedTrigger.cuts.append(electron_loose_iso_cut)
PromptControlRegionNoIsoInclusiveDisplacedTrigger.cuts.extend(muon_basic_selection_cuts)
PromptControlRegionNoIsoInclusiveDisplacedTrigger.cuts.append(muon_loose_iso_cut)
PromptControlRegionNoIsoInclusiveDisplacedTrigger.cuts.extend(prompt_control_region_cuts)

MuEleNoIsoPromptControlRegionNoOSInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("MuEleNoIsoPromptControlRegionNoOSInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet (
    )
)
PromptControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.extend(electron_basic_selection_cuts)
PromptControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.append(electron_loose_iso_cut)
PromptControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.extend(muon_basic_selection_cuts)
PromptControlRegionNoIsoNoOSInclusiveDisplacedTrigger.cuts.append(muon_loose_iso_cut)
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
PromptControlRegionNoOSInclusiveDisplacedTrigger.cuts.append(electron_iso_cut)
PromptControlRegionNoOSInclusiveDisplacedTrigger.cuts.extend(muon_basic_selection_cuts)
PromptControlRegionNoOSInclusiveDisplacedTrigger.cuts.append(muon_iso_cut)
PromptControlRegionNoOSInclusiveDisplacedTrigger.cuts.extend(prompt_control_region_no_os_cuts)
for cut in PromptControlRegionNoOSInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")
