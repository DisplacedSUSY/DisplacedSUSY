import FWCore.ParameterSet.Config as cms
import copy

##################################################
##### Set up the event selections (channels) #####
##################################################

from DisplacedSUSY.StandardAnalysis.Preselection import *
from DisplacedSUSY.StandardAnalysis.SignalSelections import *


electron_iso_cutString = cms.string("relPFrhoIso > 0.2 & relPFrhoIso < 1")
muon_iso_cutString = cms.string("relPFdBetaIso > 0.24 & relPFdBetaIso < 1.5")

Preselection_AntiIso = cms.PSet(
    name = cms.string("Preselection_AntiIso"),
    triggers = cms.vstring(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_AntiIso.cuts.extend(copy.deepcopy(Preselection.cuts))
for cut in Preselection_AntiIso.cuts:
    if "relPFrhoIso" in str(cut.cutString):
        cut.cutString = electron_iso_cutString
    if "relPFdBetaIso" in str(cut.cutString):    
        cut.cutString = muon_iso_cutString

#################################################################

Preselection_AntiIso_Prompt = cms.PSet(
    name = cms.string("Preselection_AntiIso_Prompt"),
    triggers = cms.vstring(Blinded_Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_AntiIso_Prompt.cuts.extend(copy.deepcopy(Blinded_Preselection.cuts))
for cut in Preselection_AntiIso_Prompt.cuts:
    if "relPFrhoIso" in str(cut.cutString):
        cut.cutString = electron_iso_cutString
    if "relPFdBetaIso" in str(cut.cutString):    
        cut.cutString = muon_iso_cutString


#################################################################
#################################################################

Signal_Selection_AntiIso_200um = cms.PSet(
    name = cms.string("Signal_Selection_AntiIso_200um"),
    triggers = cms.vstring(Preselection.triggers),
    cuts = cms.VPSet ()
)
Signal_Selection_AntiIso_200um.cuts.extend(copy.deepcopy(Signal_Selection_200um.cuts))
for cut in Signal_Selection_AntiIso_200um.cuts:
    if "relPFrhoIso" in str(cut.cutString):
        cut.cutString = electron_iso_cutString
    if "relPFdBetaIso" in str(cut.cutString):    
        cut.cutString = muon_iso_cutString

#################################################################
#################################################################

Preselection_AntiIso_SS = cms.PSet(
    name = cms.string("Preselection_AntiIso_SS"),
    triggers = cms.vstring(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_AntiIso_SS.cuts.extend(copy.deepcopy(Preselection_SS.cuts))
for cut in Preselection_AntiIso_SS.cuts:
    if "relPFrhoIso" in str(cut.cutString):
        cut.cutString = electron_iso_cutString
    if "relPFdBetaIso" in str(cut.cutString):    
        cut.cutString = muon_iso_cutString

#################################################################

Preselection_AntiIso_Prompt_SS = cms.PSet(
    name = cms.string("Preselection_AntiIso_Prompt_SS"),
    triggers = cms.vstring(Blinded_Preselection_SS.triggers),
    cuts = cms.VPSet ()
)
Preselection_AntiIso_Prompt_SS.cuts.extend(copy.deepcopy(Blinded_Preselection_SS.cuts))
for cut in Preselection_AntiIso_Prompt_SS.cuts:
    if "relPFrhoIso" in str(cut.cutString):
        cut.cutString = electron_iso_cutString
    if "relPFdBetaIso" in str(cut.cutString):    
        cut.cutString = muon_iso_cutString





                


