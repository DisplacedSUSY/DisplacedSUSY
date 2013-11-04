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



#################################################################
#################################################################
#################################################################
#################################################################
        
from DisplacedSUSY.StandardAnalysis.Preselection_EE import *

Preselection_EE_AntiIso = cms.PSet(
    name = cms.string("Preselection_EE_AntiIso"),
    triggers = cms.vstring(Preselection_EE.triggers),
    cuts = cms.VPSet ()
)
Preselection_EE_AntiIso.cuts.extend(copy.deepcopy(Preselection_EE.cuts))
for cut in Preselection_EE_AntiIso.cuts:
    if "relPFrhoIso" in str(cut.cutString):
        cut.cutString = electron_iso_cutString

#################################################################

Signal_Selection_EE_AntiIso_200um = cms.PSet(
    name = cms.string("Signal_Selection_EE_AntiIso_200um"),
    triggers = cms.vstring(Preselection_EE.triggers),
    cuts = cms.VPSet ()
)
Signal_Selection_EE_AntiIso_200um.cuts.extend(copy.deepcopy(Signal_Selection_EE_200um.cuts))
for cut in Signal_Selection_EE_AntiIso_200um.cuts:
    if "relPFrhoIso" in str(cut.cutString):
        cut.cutString = electron_iso_cutString

#################################################################

Preselection_EE_AntiIso_SS = cms.PSet(
    name = cms.string("Preselection_EE_AntiIso_SS"),
    triggers = cms.vstring(Preselection_EE.triggers),
    cuts = cms.VPSet ()
)
Preselection_EE_AntiIso_SS.cuts.extend(copy.deepcopy(Preselection_EE_SS.cuts))
for cut in Preselection_EE_AntiIso_SS.cuts:
    if "relPFrhoIso" in str(cut.cutString):
        cut.cutString = electron_iso_cutString



#################################################################
#################################################################


        
from DisplacedSUSY.StandardAnalysis.Preselection_MuMu import *

Preselection_MuMu_AntiIso = cms.PSet(
    name = cms.string("Preselection_MuMu_AntiIso"),
    triggers = cms.vstring(Preselection_MuMu.triggers),
    cuts = cms.VPSet ()
)
Preselection_MuMu_AntiIso.cuts.extend(copy.deepcopy(Preselection_MuMu.cuts))
for cut in Preselection_MuMu_AntiIso.cuts:
    if "relPFdBetaIso" in str(cut.cutString):
        cut.cutString = muon_iso_cutString

#################################################################

Signal_Selection_MuMu_AntiIso_200um = cms.PSet(
    name = cms.string("Signal_Selection_MuMu_AntiIso_200um"),
    triggers = cms.vstring(Preselection_MuMu.triggers),
    cuts = cms.VPSet ()
)
Signal_Selection_MuMu_AntiIso_200um.cuts.extend(copy.deepcopy(Signal_Selection_MuMu_200um.cuts))
for cut in Signal_Selection_MuMu_AntiIso_200um.cuts:
    if "relPFdBetaIso" in str(cut.cutString):
        cut.cutString = muon_iso_cutString

#################################################################

Preselection_MuMu_AntiIso_SS = cms.PSet(
    name = cms.string("Preselection_MuMu_AntiIso_SS"),
    triggers = cms.vstring(Preselection_MuMu.triggers),
    cuts = cms.VPSet ()
)
Preselection_MuMu_AntiIso_SS.cuts.extend(copy.deepcopy(Preselection_MuMu_SS.cuts))
for cut in Preselection_MuMu_AntiIso_SS.cuts:
    if "relPFdBetaIso" in str(cut.cutString):
        cut.cutString = muon_iso_cutString


