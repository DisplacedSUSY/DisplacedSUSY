import FWCore.ParameterSet.Config as cms
import copy

###########################################################
##### Set up the event selections (channels) #####
###########################################################


Preselection_AntiIsoExtraReduced_SS = cms.PSet(
    name = cms.string("Preselection_AntiIsoExtraReduced_SS"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"),
    cuts = cms.VPSet (
      cms.PSet (
        inputCollection = cms.string("events"),
        cutString = cms.string("FilterOutScraping > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("primaryvertexs"),
        cutString = cms.string("isGood > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),    
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("mvaNonTrigV0 > 0.9"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("passConvVeto > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("relPFrhoIso > 0.2 & relPFrhoIso < 1"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),    
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("tightIDdisplaced > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("relPFdBetaIso > 0.24 & relPFdBetaIso < 1.5"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
      ),
      cms.PSet (
        inputCollection = cms.string("electron-muon pairs"),
        cutString = cms.string("chargeProduct > 0"),
        numberRequired = cms.string("== 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electron-muon pairs"),
        cutString = cms.string("deltaR > 0.5"),
        numberRequired = cms.string("== 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string("== 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string("== 1")
      ),
   )   
)


Preselection_AntiIsoExtraReduced_Prompt_SS = cms.PSet(
    name = cms.string("Preselection_AntiIsoExtraReduced_Prompt_SS"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"),
    cuts = cms.VPSet (
      cms.PSet (
        inputCollection = cms.string("events"),
        cutString = cms.string("FilterOutScraping > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("primaryvertexs"),
        cutString = cms.string("isGood > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),    
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("mvaNonTrigV0 > 0.9"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("passConvVeto > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("relPFrhoIso > 0.2 & relPFrhoIso < 1"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),    
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("tightIDdisplaced > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("relPFdBetaIso > 0.24 & relPFdBetaIso < 1.5"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
      ),
      cms.PSet (
        inputCollection = cms.string("electron-muon pairs"),
        cutString = cms.string("chargeProduct > 0"),
        numberRequired = cms.string("== 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electron-muon pairs"),
        cutString = cms.string("deltaR > 0.5"),
        numberRequired = cms.string("== 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string("== 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string("== 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(correctedD0) < 0.02"),
        numberRequired = cms.string("== 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(correctedD0) < 0.02"),
        numberRequired = cms.string("== 1")
      ),
   )   
)




