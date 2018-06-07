import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.Preselection import *

##########################################################################
### Set up the prompt control region, N-1 cuts for the displaced SUSY analysis #####
##########################################################################

PromptControlRegionNoElectronID = copy.deepcopy(PromptControlRegion)
PromptControlRegionNoElectronID.name = cms.string("PromptControlRegionNoElectronID")
removeCuts(PromptControlRegionNoElectronID.cuts,[electron_id_cut])

PromptControlRegionNoMuonIso = copy.deepcopy(PromptControlRegion)
PromptControlRegionNoMuonIso.name = cms.string("PromptControlRegionNoMuonIso")
removeCuts(PromptControlRegionNoMuonIso.cuts,[muon_iso_cut])

PromptControlRegionNoMuonID = copy.deepcopy(PromptControlRegion)
PromptControlRegionNoMuonID.name = cms.string("PromptControlRegionNoMuonID")
removeCuts(PromptControlRegionNoMuonID.cuts,[muon_id_cut])
