import FWCore.ParameterSet.Config as cms
import copy



#   ######################################
# e #         #                          #
# l #         #                          #
# e #         #                          #
# t #         #                          #
# r #         #                          #
# o #    1    #            2             #
# n #         #                          #
#   #         #                          #
# d #         #                          #
# 0 #         #                          #
#   #         #                          #
#   ######################################
#   #         #                          #
#   #         #                          #
#   #    3    #            4             #
#   #         #                          #
#   ######################################
#
#         muon d0 


# Preselection_Prompt_Muon_Displaced_Electron = 1
# Signal_Selection_200um = 2
# Blinded_Preselection = 3
# Preselection_Prompt_Electron_Displaced_Muon = 4

# Preselection_Prompt_Muon = 1+3
# Preselection_Prompt_Electron = 3+4

# Preselection = 1+2+3+4

#################################################################

prompt_electron_d0_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string("== 1")
)

prompt_muon_d0_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string("== 1")
)

displaced_electron_d0_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("abs(correctedD0) > 0.02"),
    numberRequired = cms.string("== 1")
)

displaced_muon_d0_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) > 0.02"),
    numberRequired = cms.string("== 1")
)

#################################################################

from DisplacedSUSY.StandardAnalysis.Preselection import *

#################################################################

Preselection_Prompt_Electron = cms.PSet(
    name = cms.string("Preselection_Prompt_Electron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_Prompt_Electron.cuts.extend(copy.deepcopy(Preselection.cuts))
Preselection_Prompt_Electron.cuts.append(prompt_electron_d0_cut)

#################################################################

Preselection_Prompt_Muon = cms.PSet(
    name = cms.string("Preselection_Prompt_Muon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_Prompt_Muon.cuts.extend(copy.deepcopy(Preselection.cuts))
Preselection_Prompt_Muon.cuts.append(prompt_muon_d0_cut)

#################################################################


#################################################################

Preselection_Prompt_Electron_Displaced_Muon = cms.PSet(
    name = cms.string("Preselection_Prompt_Electron_Displaced_Muon"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_Prompt_Electron_Displaced_Muon.cuts.extend(copy.deepcopy(Preselection.cuts))
Preselection_Prompt_Electron_Displaced_Muon.cuts.append(prompt_electron_d0_cut)
Preselection_Prompt_Electron_Displaced_Muon.cuts.append(displaced_muon_d0_cut)

#################################################################

Preselection_Prompt_Muon_Displaced_Electron = cms.PSet(
    name = cms.string("Preselection_Prompt_Muon_Displaced_Electron"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_Prompt_Muon_Displaced_Electron.cuts.extend(copy.deepcopy(Preselection.cuts))
Preselection_Prompt_Muon_Displaced_Electron.cuts.append(prompt_muon_d0_cut)
Preselection_Prompt_Muon_Displaced_Electron.cuts.append(displaced_electron_d0_cut)

#################################################################
