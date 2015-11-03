import FWCore.ParameterSet.Config as cms
import copy
import string
from CutDefinitions_13TeV import *
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
        inputCollection = cms.vstring("candeles","beamspots"),
        cutString = cms.string("abs((-(candele.vx - beamspot.x0)*candele.py + (candele.vy - beamspot.y0)*candele.px)/candele.pt) <= 0.01 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron dxy <= 0.01 cm")
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
PromptControlRegion_13TeV = cms.PSet(
    name = cms.string("PromptControlRegion13TeV"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
PromptControlRegion_13TeV.cuts.extend(electron_basic_selection_cuts)
PromptControlRegion_13TeV.cuts.append(electron_iso_cut)
PromptControlRegion_13TeV.cuts.extend(muon_basic_selection_cuts)
PromptControlRegion_13TeV.cuts.append(muon_iso_cut)
PromptControlRegion_13TeV.cuts.extend(prompt_control_region_cuts)

AntiIsoMuAntiIsoElePromptControlRegion_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoElePromptControlRegion13TeV"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
AntiIsoMuAntiIsoElePromptControlRegion_13TeV.cuts.extend(electron_basic_selection_cuts)
AntiIsoMuAntiIsoElePromptControlRegion_13TeV.cuts.append(electron_inversed_iso_cut)
AntiIsoMuAntiIsoElePromptControlRegion_13TeV.cuts.extend(muon_basic_selection_cuts)
AntiIsoMuAntiIsoElePromptControlRegion_13TeV.cuts.append(muon_inversed_iso_cut)
AntiIsoMuAntiIsoElePromptControlRegion_13TeV.cuts.extend(prompt_control_region_cuts)

IsoMuAntiIsoElePromptControlRegion_13TeV = cms.PSet(
    name = cms.string("IsoMuAntiIsoElePromptControlRegion13TeV"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
IsoMuAntiIsoElePromptControlRegion_13TeV.cuts.extend(electron_basic_selection_cuts)
IsoMuAntiIsoElePromptControlRegion_13TeV.cuts.append(electron_inversed_iso_cut)
IsoMuAntiIsoElePromptControlRegion_13TeV.cuts.extend(muon_basic_selection_cuts)
IsoMuAntiIsoElePromptControlRegion_13TeV.cuts.append(muon_iso_cut)
IsoMuAntiIsoElePromptControlRegion_13TeV.cuts.extend(prompt_control_region_cuts)

AntiIsoMuIsoElePromptControlRegion_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuIsoElePromptControlRegion13TeV"),
    triggers = cms.vstring(), # TRIGGER
    cuts = cms.VPSet (
    )
)
AntiIsoMuIsoElePromptControlRegion_13TeV.cuts.extend(electron_basic_selection_cuts)
AntiIsoMuIsoElePromptControlRegion_13TeV.cuts.append(electron_iso_cut)
AntiIsoMuIsoElePromptControlRegion_13TeV.cuts.extend(muon_basic_selection_cuts)
AntiIsoMuIsoElePromptControlRegion_13TeV.cuts.append(muon_inversed_iso_cut)
AntiIsoMuIsoElePromptControlRegion_13TeV.cuts.extend(prompt_control_region_cuts)
##########################################################################
#Selections with different triggers
PromptControlRegionPromptTrigger_13TeV = cms.PSet(
    name = cms.string("PromptControlRegionPromptTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
PromptControlRegionPromptTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(PromptControlRegion_13TeV.cuts))

PromptControlRegionInclusiveDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("PromptControlRegionInclusiveDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
PromptControlRegionInclusiveDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(PromptControlRegion_13TeV.cuts))

for cut in PromptControlRegionInclusiveDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

PromptControlRegionDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoPromptControlRegionDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
PromptControlRegionDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(PromptControlRegion_13TeV.cuts))

for cut in PromptControlRegionDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")


IsoMuAntiIsoElePromptControlRegionPromptTrigger_13TeV = cms.PSet(
    name = cms.string("IsoMuAntiIsoElePromptControlRegionPromptTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
IsoMuAntiIsoElePromptControlRegionPromptTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(IsoMuAntiIsoElePromptControlRegion_13TeV.cuts))

IsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("IsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
IsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(IsoMuAntiIsoElePromptControlRegion_13TeV.cuts))

for cut in IsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

IsoMuAntiIsoElePromptControlRegionDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoPromptControlRegionDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
IsoMuAntiIsoElePromptControlRegionDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(IsoMuAntiIsoElePromptControlRegion_13TeV.cuts))

for cut in IsoMuAntiIsoElePromptControlRegionDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")

AntiIsoMuIsoElePromptControlRegionPromptTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuIsoElePromptControlRegionPromptTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuIsoElePromptControlRegionPromptTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuIsoElePromptControlRegion_13TeV.cuts))

AntiIsoMuIsoElePromptControlRegionInclusiveDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuIsoElePromptControlRegionInclusiveDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuIsoElePromptControlRegionInclusiveDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuIsoElePromptControlRegion_13TeV.cuts))

for cut in AntiIsoMuIsoElePromptControlRegionInclusiveDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuIsoElePromptControlRegionDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoPromptControlRegionDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuIsoElePromptControlRegionDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuIsoElePromptControlRegion_13TeV.cuts))

for cut in AntiIsoMuIsoElePromptControlRegionDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")


AntiIsoMuAntiIsoElePromptControlRegionPromptTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoElePromptControlRegionPromptTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuAntiIsoElePromptControlRegionPromptTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuAntiIsoElePromptControlRegion_13TeV.cuts))

AntiIsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuAntiIsoElePromptControlRegion_13TeV.cuts))

for cut in AntiIsoMuAntiIsoElePromptControlRegionInclusiveDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 42")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 40")

AntiIsoMuAntiIsoElePromptControlRegionDisplacedTrigger_13TeV = cms.PSet(
    name = cms.string("AntiIsoPromptControlRegionDisplacedTrigger13TeV"),
    triggers = cms.vstring("HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
)
AntiIsoMuAntiIsoElePromptControlRegionDisplacedTrigger_13TeV.cuts = cms.VPSet (copy.deepcopy(AntiIsoMuAntiIsoElePromptControlRegion_13TeV.cuts))

for cut in AntiIsoMuAntiIsoElePromptControlRegionDisplacedTrigger_13TeV.cuts:
    if "pt > 25" in str(cut.cutString) and "candeles" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 32")
    if "pt > 25" in str(cut.cutString) and "muons" in str(cut.inputCollection):
        cut.cutString = cms.string("pt > 30")


