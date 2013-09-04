import FWCore.ParameterSet.Config as cms
import copy
import string

##############################################################
##### EVENT SELECTIONS FOR OUR QCD B-BBAR CONTROL REGIONS ####
##############################################################

QCD_Muon_Skim = cms.PSet(
    name = cms.string("QCD_Muon_Skim"),
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
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("tightIDdisplaced > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
      ),
      cms.PSet (
        inputCollection = cms.string("jets"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.string("jets"),
        cutString = cms.string("btagCombinedSecVertex > 0.244"),
        numberRequired = cms.string(">= 1"),
      ),
   )
)

##############################################################

QCD_Electron_Skim = cms.PSet(
    name = cms.string("QCD_Electron_Skim"),
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
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("mvaNonTrigV0 > 0.9"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
      ),
      cms.PSet (
        inputCollection = cms.string("jets"),
        cutString = cms.string("abs(eta) < 2.4"),
        numberRequired = cms.string(">= 1"),
      ),
      cms.PSet (
        inputCollection = cms.string("jets"),
        cutString = cms.string("btagCombinedSecVertex > 0.244"),
        numberRequired = cms.string(">= 1"),
      ),
    )
)


##############################################################
# extra cuts for the control region

jet_cut = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("abs(eta) < 2.4 & pt > 50 & btagCombinedSecVertex > 0.679"),
    numberRequired = cms.string(">= 1"),
)
secondary_jet_cut = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("abs(eta) < 2.4 & pt > 50"),
    numberRequired = cms.string(">= 1"),
)
dijet_cut = cms.PSet (
    inputCollection = cms.string("jet-secondary jet pairs"),
    cutString = cms.string("deltaPhi > 2.5"),
    numberRequired = cms.string(">= 1"),
)

muonjet_cut = cms.PSet (
    inputCollection = cms.string("muon-secondary jet pairs"),
    cutString = cms.string("deltaR < 0.2"),
    numberRequired = cms.string(">= 1"),
)
electronjet_cut = cms.PSet (
    inputCollection = cms.string("electron-secondary jet pairs"),
    cutString = cms.string("deltaR < 0.2"),
    numberRequired = cms.string(">= 1"),
)



##############################################################

QCD_Muon_ControlRegion = cms.PSet(
    name = cms.string("QCD_Muon_ControlRegion"),
    triggers = cms.vstring("HLT_Mu17_v"),
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
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("tightIDdisplaced > 0"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
      ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string("== 1")
      ),
   )
)

QCD_Muon_ControlRegion.cuts.append(jet_cut)
QCD_Muon_ControlRegion.cuts.append(secondary_jet_cut)
QCD_Muon_ControlRegion.cuts.append(dijet_cut)
QCD_Muon_ControlRegion.cuts.append(muonjet_cut)

##############################################################

QCD_Electron_ControlRegion = cms.PSet(
    name = cms.string("QCD_Electron_ControlRegion"),
    triggers = cms.vstring("HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v"),
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
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("mvaNonTrigV0 > 0.9"),
        numberRequired = cms.string(">= 1")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
      ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string("== 1")
      ),
    )
)

QCD_Electron_ControlRegion.cuts.append(jet_cut)
QCD_Electron_ControlRegion.cuts.append(secondary_jet_cut)
QCD_Electron_ControlRegion.cuts.append(dijet_cut)
QCD_Electron_ControlRegion.cuts.append(electronjet_cut)


##############################################################
###### BEGIN TRIGGER TESTING FOR MUON QCD CONTROL REGION #####
##############################################################

HLT_BTagMu_DiJet40_Mu5_v = cms.PSet(
        name = cms.string("HLT_BTagMu_DiJet40_Mu5_v"),
            triggers = cms.vstring("HLT_BTagMu_DiJet40_Mu5_v"),
            cuts = cms.VPSet ()
        )
HLT_BTagMu_DiJet40_Mu5_v.cuts.extend(copy.deepcopy(QCD_Muon_ControlRegion.cuts))

HLT_BTagMu_DiJet70_Mu5_v = cms.PSet(
        name = cms.string("HLT_BTagMu_DiJet70_Mu5_v"),
            triggers = cms.vstring("HLT_BTagMu_DiJet70_Mu5_v"),
            cuts = cms.VPSet ()
        )
HLT_BTagMu_DiJet70_Mu5_v.cuts.extend(copy.deepcopy(QCD_Muon_ControlRegion.cuts))

HLT_BTagMu_DiJet20_Mu5_v = cms.PSet(
        name = cms.string("HLT_BTagMu_DiJet20_Mu5_v"),
            triggers = cms.vstring("HLT_BTagMu_DiJet20_Mu5_v"),
            cuts = cms.VPSet ()
        )
HLT_BTagMu_DiJet20_Mu5_v.cuts.extend(copy.deepcopy(QCD_Muon_ControlRegion.cuts))

HLT_Mu17_v = cms.PSet(
        name = cms.string("HLT_Mu17_v"),
            triggers = cms.vstring("HLT_Mu17_v"),
            cuts = cms.VPSet ()
        )
HLT_Mu17_v.cuts.extend(copy.deepcopy(QCD_Muon_ControlRegion.cuts))

HLT_Mu8_v = cms.PSet(
        name = cms.string("HLT_Mu8_v"),
            triggers = cms.vstring("HLT_Mu8_v"),
            cuts = cms.VPSet ()
        )
HLT_Mu8_v.cuts.extend(copy.deepcopy(QCD_Muon_ControlRegion.cuts))

HLT_IsoMu12_DoubleCentralJet65_v = cms.PSet(
        name = cms.string("HLT_IsoMu12_DoubleCentralJet65_v"),
            triggers = cms.vstring("HLT_IsoMu12_DoubleCentralJet65_v"),
            cuts = cms.VPSet ()
        )
HLT_IsoMu12_DoubleCentralJet65_v.cuts.extend(copy.deepcopy(QCD_Muon_ControlRegion.cuts))

HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v = cms.PSet(
        name = cms.string("HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v"),
            triggers = cms.vstring("HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v"),
            cuts = cms.VPSet ()
        )
HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v.cuts.extend(copy.deepcopy(QCD_Muon_ControlRegion.cuts))

HLT_Mu8_DiJet30_v = cms.PSet(
        name = cms.string("HLT_Mu8_DiJet30_v"),
            triggers = cms.vstring("HLT_Mu8_DiJet30_v"),
            cuts = cms.VPSet ()
        )
HLT_Mu8_DiJet30_v.cuts.extend(copy.deepcopy(QCD_Muon_ControlRegion.cuts))

HLT_Mu8_TriJet30_v = cms.PSet(
        name = cms.string("HLT_Mu8_TriJet30_v"),
            triggers = cms.vstring("HLT_Mu8_TriJet30_v"),
            cuts = cms.VPSet ()
        )
HLT_Mu8_TriJet30_v.cuts.extend(copy.deepcopy(QCD_Muon_ControlRegion.cuts))

HLT_Mu8_QuadJet30_v = cms.PSet(
        name = cms.string("HLT_Mu8_QuadJet30_v"),
            triggers = cms.vstring("HLT_Mu8_QuadJet30_v"),
            cuts = cms.VPSet ()
        )
HLT_Mu8_QuadJet30_v.cuts.extend(copy.deepcopy(QCD_Muon_ControlRegion.cuts))

##############################################################
#### BEGIN TRIGGER TESTING FOR ELECTRON QCD CONTROL REGION ###
##############################################################


HLT_Ele17_CaloIdL_CaloIsoVL_v = cms.PSet(
        name = cms.string("HLT_Ele17_CaloIdL_CaloIsoVL_v"),
            triggers = cms.vstring("HLT_Ele17_CaloIdL_CaloIsoVL_v"),
            cuts = cms.VPSet ()
        )
HLT_Ele17_CaloIdL_CaloIsoVL_v.cuts.extend(copy.deepcopy(QCD_Electron_ControlRegion.cuts))

HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v = cms.PSet(
        name = cms.string("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v"),
            triggers = cms.vstring("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v"),
            cuts = cms.VPSet ()
        )
HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v.cuts.extend(copy.deepcopy(QCD_Electron_ControlRegion.cuts))

HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v = cms.PSet(
        name = cms.string("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v"),
            triggers = cms.vstring("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v"),
            cuts = cms.VPSet ()
        )
HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v.cuts.extend(copy.deepcopy(QCD_Electron_ControlRegion.cuts))

HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v = cms.PSet(
        name = cms.string("HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v"),
            triggers = cms.vstring("HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v"),
            cuts = cms.VPSet ()
        )
HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v.cuts.extend(copy.deepcopy(QCD_Electron_ControlRegion.cuts))

HLT_Ele8_CaloIdT_TrkIdVL_v = cms.PSet(
        name = cms.string("HLT_Ele8_CaloIdT_TrkIdVL_v"),
            triggers = cms.vstring("HLT_Ele8_CaloIdT_TrkIdVL_v"),
            cuts = cms.VPSet ()
        )
HLT_Ele8_CaloIdT_TrkIdVL_v.cuts.extend(copy.deepcopy(QCD_Electron_ControlRegion.cuts))

HLT_Ele8_CaloIdL_CaloIsoVL_v = cms.PSet(
        name = cms.string("HLT_Ele8_CaloIdL_CaloIsoVL_v"),
            triggers = cms.vstring("HLT_Ele8_CaloIdL_CaloIsoVL_v"),
            cuts = cms.VPSet ()
        )
HLT_Ele8_CaloIdL_CaloIsoVL_v.cuts.extend(copy.deepcopy(QCD_Electron_ControlRegion.cuts))

HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v = cms.PSet(
        name = cms.string("HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v"),
            triggers = cms.vstring("HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v"),
            cuts = cms.VPSet ()
        )
HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v.cuts.extend(copy.deepcopy(QCD_Electron_ControlRegion.cuts))

HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v = cms.PSet(
        name = cms.string("HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v"),
            triggers = cms.vstring("HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v"),
            cuts = cms.VPSet ()
        )
HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v.cuts.extend(copy.deepcopy(QCD_Electron_ControlRegion.cuts))

HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v = cms.PSet(
        name = cms.string("HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v"),
            triggers = cms.vstring("HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v"),
            cuts = cms.VPSet ()
        )
HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v.cuts.extend(copy.deepcopy(QCD_Electron_ControlRegion.cuts))

HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v = cms.PSet(
        name = cms.string("HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v"),
            triggers = cms.vstring("HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v"),
            cuts = cms.VPSet ()
        )
HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v.cuts.extend(copy.deepcopy(QCD_Electron_ControlRegion.cuts))

HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v = cms.PSet(
        name = cms.string("HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v"),
            triggers = cms.vstring("HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v"),
            cuts = cms.VPSet ()
        )
HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v.cuts.extend(copy.deepcopy(QCD_Electron_ControlRegion.cuts))

