import FWCore.ParameterSet.Config as cms
import copy
import string
from CutDefinitions import *
##########################################################################
######## Set up the prompt control region for the displaced SUSY analysis #########
##########################################################################
##########################################################################
#Displaced control region specific cuts
displaced_control_region_cuts = cms.VPSet(
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
    # ELECTRON DXY BLINDING
    cms.PSet (
        inputCollection = cms.vstring("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)

##########################################################################
#Selections without triggers
DisplacedControlRegion = cms.PSet(
    name = cms.string("DisplacedControlRegion"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
DisplacedControlRegion.cuts.extend(electron_basic_selection_cuts)
DisplacedControlRegion.cuts.append(electron_iso_cut)
DisplacedControlRegion.cuts.extend(muon_basic_selection_cuts)
DisplacedControlRegion.cuts.append(muon_iso_cut)
DisplacedControlRegion.cuts.extend(displaced_control_region_cuts)

AntiIsoMuAntiIsoEleDisplacedControlRegion = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoEleDisplacedControlRegion"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
AntiIsoMuAntiIsoEleDisplacedControlRegion.cuts.extend(electron_basic_selection_cuts)
AntiIsoMuAntiIsoEleDisplacedControlRegion.cuts.append(electron_inverted_iso_cut)
AntiIsoMuAntiIsoEleDisplacedControlRegion.cuts.extend(muon_basic_selection_cuts)
AntiIsoMuAntiIsoEleDisplacedControlRegion.cuts.append(muon_inverted_iso_cut)
AntiIsoMuAntiIsoEleDisplacedControlRegion.cuts.extend(displaced_control_region_cuts)

IsoMuAntiIsoEleDisplacedControlRegion = cms.PSet(
    name = cms.string("IsoMuAntiIsoEleDisplacedControlRegion"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
IsoMuAntiIsoEleDisplacedControlRegion.cuts.extend(electron_basic_selection_cuts)
IsoMuAntiIsoEleDisplacedControlRegion.cuts.append(electron_inverted_iso_cut)
IsoMuAntiIsoEleDisplacedControlRegion.cuts.extend(muon_basic_selection_cuts)
IsoMuAntiIsoEleDisplacedControlRegion.cuts.append(muon_iso_cut)
IsoMuAntiIsoEleDisplacedControlRegion.cuts.extend(displaced_control_region_cuts)

AntiIsoMuIsoEleDisplacedControlRegion = cms.PSet(
    name = cms.string("AntiIsoMuIsoEleDisplacedControlRegion"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
AntiIsoMuIsoEleDisplacedControlRegion.cuts.extend(electron_basic_selection_cuts)
AntiIsoMuIsoEleDisplacedControlRegion.cuts.append(electron_iso_cut)
AntiIsoMuIsoEleDisplacedControlRegion.cuts.extend(muon_basic_selection_cuts)
AntiIsoMuIsoEleDisplacedControlRegion.cuts.append(muon_inverted_iso_cut)
AntiIsoMuIsoEleDisplacedControlRegion.cuts.extend(displaced_control_region_cuts)
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


IsoMuAntiIsoEleDisplacedControlRegionPromptTrigger = cms.PSet(
    name = cms.string("IsoMuAntiIsoEleDisplacedControlRegionPromptTrigger"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
IsoMuAntiIsoEleDisplacedControlRegionPromptTrigger.cuts = cms.VPSet (copy.deepcopy(IsoMuAntiIsoEleDisplacedControlRegion.cuts))

IsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("IsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
IsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(IsoMuAntiIsoEleDisplacedControlRegion.cuts))

for cut in IsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

IsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger = cms.PSet(
    name = cms.string("IsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
IsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(IsoMuAntiIsoEleDisplacedControlRegion.cuts))

for cut in IsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")

AntiIsoMuIsoEleDisplacedControlRegionPromptTrigger = cms.PSet(
    name = cms.string("AntiIsoMuIsoEleDisplacedControlRegionPromptTrigger"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuIsoEleDisplacedControlRegionPromptTrigger.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuIsoEleDisplacedControlRegion.cuts))

AntiIsoMuIsoEleDisplacedControlRegionInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("AntiIsoMuIsoEleDisplacedControlRegionInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuIsoEleDisplacedControlRegionInclusiveDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuIsoEleDisplacedControlRegion.cuts))

for cut in AntiIsoMuIsoEleDisplacedControlRegionInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuIsoEleDisplacedControlRegionDisplacedTrigger = cms.PSet(
    name = cms.string("AntiIsoMuIsoEleDisplacedControlRegionDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuIsoEleDisplacedControlRegionDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuIsoEleDisplacedControlRegion.cuts))

for cut in AntiIsoMuIsoEleDisplacedControlRegionDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")


AntiIsoMuAntiIsoEleDisplacedControlRegionPromptTrigger = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoEleDisplacedControlRegionPromptTrigger"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuAntiIsoEleDisplacedControlRegionPromptTrigger.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuAntiIsoEleDisplacedControlRegion.cuts))

AntiIsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuAntiIsoEleDisplacedControlRegion.cuts))

for cut in AntiIsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuAntiIsoEleDisplacedControlRegion.cuts))

for cut in AntiIsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger.cuts:
    if "pt > 25" in str(cut.cutString) and "electrons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")


