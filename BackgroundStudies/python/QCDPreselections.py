import FWCore.ParameterSet.Config as cms
import copy

##################################################
##### Set up the event selections (channels) #####
##################################################

from DisplacedSUSY.StandardAnalysis.Preselection import *
from DisplacedSUSY.StandardAnalysis.SignalSelections import *

electron_iso_cutString = cms.string("relPFrhoIso > 0.2 & relPFrhoIso < 1")
muon_iso_cutString = cms.string("relPFdBetaIso > 0.24 & relPFdBetaIso < 1.5")

vetoes = {
    "extra electron veto" : cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("relPFrhoIso < 0.1"),
        numberRequired = cms.string("== 0"),
        alias = cms.string("extra electron veto"),
        isVeto = cms.bool(True)
    ),
    "extra muon veto" : cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("relPFdBetaIso < 0.12"),
        numberRequired = cms.string("== 0"),
        alias = cms.string("extra muon veto"),
        isVeto = cms.bool(True)
    ),
}

def invert_isolation (template_cuts):
    cuts = cms.VPSet (copy.deepcopy(template_cuts))
    for i in range (0, len (cuts)):
        alias = cuts[i].alias.pythonValue ()[1:-1] if hasattr (cuts[i], "alias") else ""
        if "relPFrhoIso" in str(cuts[i].cutString):
            cuts[i].cutString = electron_iso_cutString
        if "relPFdBetaIso" in str(cuts[i].cutString):
            cuts[i].cutString = muon_iso_cutString
        if alias == "extra electron veto" or alias == "extra muon veto":
            cuts[i] = vetoes[alias]
    return cuts

#################################################################

Preselection_AntiIso = cms.PSet(
    name = cms.string("Preselection_AntiIso"),
    triggers = cms.vstring(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_AntiIso.cuts = invert_isolation (Preselection.cuts)

#################################################################

Preselection_AntiIso_Prompt = cms.PSet(
    name = cms.string("Preselection_AntiIso_Prompt"),
    triggers = cms.vstring(Blinded_Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_AntiIso_Prompt.cuts = invert_isolation (Blinded_Preselection.cuts)

#################################################################
#################################################################

Signal_Selection_AntiIso_200um = cms.PSet(
    name = cms.string("Signal_Selection_AntiIso_200um"),
    triggers = cms.vstring(Preselection.triggers),
    cuts = cms.VPSet ()
)
Signal_Selection_AntiIso_200um.cuts = invert_isolation (Signal_Selection_200um.cuts)

#################################################################
#################################################################

Preselection_AntiIso_SS = cms.PSet(
    name = cms.string("Preselection_AntiIso_SS"),
    triggers = cms.vstring(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_AntiIso_SS.cuts = invert_isolation (Preselection_SS.cuts)

#################################################################

Preselection_AntiIso_Prompt_SS = cms.PSet(
    name = cms.string("Preselection_AntiIso_Prompt_SS"),
    triggers = cms.vstring(Blinded_Preselection_SS.triggers),
    cuts = cms.VPSet ()
)
Preselection_AntiIso_Prompt_SS.cuts = invert_isolation (Blinded_Preselection_SS.cuts)
