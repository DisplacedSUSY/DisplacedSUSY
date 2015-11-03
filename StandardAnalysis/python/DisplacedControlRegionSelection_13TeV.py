import FWCore.ParameterSet.Config as cms
import copy
import string
from CutDefinitions_13TeV import *
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
        inputCollection = cms.vstring("candeles","beamspots"),
        cutString = cms.string("abs((-(candele.vx - beamspot.x0)*candele.py + (candele.vy - beamspot.y0)*candele.px)/candele.pt) > 0.01 "),
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
        inputCollection = cms.vstring("candeles","beamspots"),
        cutString = cms.string("abs((-(candele.vx - beamspot.x0)*candele.py + (candele.vy - beamspot.y0)*candele.px)/candele.pt) <= 0.02 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron dxy <= 0.02 cm")
    ),
    # OPPOSITE SIGN E-MU PAIR
    cms.PSet (
        inputCollection = cms.vstring("candeles", "muons"),
        cutString = cms.string("candele.charge * muon.charge < 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("oppositely charged e-mu pair")
    ),
    # ELECTRON AND MUON ARE NOT OVERLAPPING
    cms.PSet (
        inputCollection = cms.vstring("candeles", "muons"),
        cutString = cms.string("deltaR(candele, muon) > 0.5"),
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
        inputCollection = cms.vstring("candeles"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
    ),
)

##########################################################################
#Selections without triggers
DisplacedControlRegion_13TeV = cms.PSet(
    name = cms.string("DisplacedControlRegion13TeV"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
DisplacedControlRegion_13TeV.cuts.extend(electron_basic_selection_cuts)
DisplacedControlRegion_13TeV.cuts.append(electron_iso_cut)
DisplacedControlRegion_13TeV.cuts.extend(muon_basic_selection_cuts)
DisplacedControlRegion_13TeV.cuts.append(muon_iso_cut)
DisplacedControlRegion_13TeV.cuts.extend(displaced_control_region_cuts)

AntiIsoMuAntiIsoEleDisplacedControlRegion_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoEleDisplacedControlRegion13TeV"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
AntiIsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts.extend(electron_basic_selection_cuts)
AntiIsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts.append(electron_inversed_iso_cut)
AntiIsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts.extend(muon_basic_selection_cuts)
AntiIsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts.append(muon_inversed_iso_cut)
AntiIsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts.extend(displaced_control_region_cuts)

IsoMuAntiIsoEleDisplacedControlRegion_13TeV = cms.PSet(
    name = cms.string("IsoMuAntiIsoEleDisplacedControlRegion13TeV"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
IsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts.extend(electron_basic_selection_cuts)
IsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts.append(electron_inversed_iso_cut)
IsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts.extend(muon_basic_selection_cuts)
IsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts.append(muon_iso_cut)
IsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts.extend(displaced_control_region_cuts)

AntiIsoMuIsoEleDisplacedControlRegion_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuIsoEleDisplacedControlRegion13TeV"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
AntiIsoMuIsoEleDisplacedControlRegion_13TeV.cuts.extend(electron_basic_selection_cuts)
AntiIsoMuIsoEleDisplacedControlRegion_13TeV.cuts.append(electron_iso_cut)
AntiIsoMuIsoEleDisplacedControlRegion_13TeV.cuts.extend(muon_basic_selection_cuts)
AntiIsoMuIsoEleDisplacedControlRegion_13TeV.cuts.append(muon_inversed_iso_cut)
AntiIsoMuIsoEleDisplacedControlRegion_13TeV.cuts.extend(displaced_control_region_cuts)
##########################################################################
#Selections with different triggers
DisplacedControlRegionPromptTrigger_13TeV = cms.PSet(
    name = cms.string("DisplacedControlRegionPromptTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
DisplacedControlRegionPromptTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(DisplacedControlRegion_13TeV.cuts))

DisplacedControlRegionInclusiveDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("DisplacedControlRegionInclusiveDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
DisplacedControlRegionInclusiveDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(DisplacedControlRegion_13TeV.cuts))

for cut in DisplacedControlRegionInclusiveDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

DisplacedControlRegionDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("DisplacedControlRegionDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
DisplacedControlRegionDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(DisplacedControlRegion_13TeV.cuts))

for cut in DisplacedControlRegionDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")


IsoMuAntiIsoEleDisplacedControlRegionPromptTrigger_13TeV = cms.PSet(
    name = cms.string("IsoMuAntiIsoEleDisplacedControlRegionPromptTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
IsoMuAntiIsoEleDisplacedControlRegionPromptTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(IsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts))

IsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("IsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
IsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(IsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts))

for cut in IsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

IsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("IsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
IsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(IsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts))

for cut in IsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")

AntiIsoMuIsoEleDisplacedControlRegionPromptTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuIsoEleDisplacedControlRegionPromptTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuIsoEleDisplacedControlRegionPromptTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuIsoEleDisplacedControlRegion_13TeV.cuts))

AntiIsoMuIsoEleDisplacedControlRegionInclusiveDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuIsoEleDisplacedControlRegionInclusiveDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuIsoEleDisplacedControlRegionInclusiveDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuIsoEleDisplacedControlRegion_13TeV.cuts))

for cut in AntiIsoMuIsoEleDisplacedControlRegionInclusiveDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuIsoEleDisplacedControlRegionDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuIsoEleDisplacedControlRegionDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuIsoEleDisplacedControlRegionDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuIsoEleDisplacedControlRegion_13TeV.cuts))

for cut in AntiIsoMuIsoEleDisplacedControlRegionDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")


AntiIsoMuAntiIsoEleDisplacedControlRegionPromptTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoEleDisplacedControlRegionPromptTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuAntiIsoEleDisplacedControlRegionPromptTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts))

AntiIsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts))

for cut in AntiIsoMuAntiIsoEleDisplacedControlRegionInclusiveDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuAntiIsoEleDisplacedControlRegion_13TeV.cuts))

for cut in AntiIsoMuAntiIsoEleDisplacedControlRegionDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")


