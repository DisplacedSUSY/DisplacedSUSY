import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.StandardAnalysis.Preselection import *

#Z->tautau->emu

##########################################################################







ZTauTauControlRegion = cms.PSet(
    name = cms.string("ZTauTautoEMu"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"),
    cuts = cms.VPSet ()
)
ZTauTauControlRegion.cuts.extend(copy.deepcopy(Preselection.cuts))

ZTauTauControlRegion_Prompt = cms.PSet(
    name = cms.string("ZTauTautoEMu_Prompt"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"),
    cuts = cms.VPSet ()
)
ZTauTauControlRegion_Prompt.cuts.extend(copy.deepcopy(Blinded_Preselection.cuts))

e_metMT_cut =  cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("metMT < 50"),
    numberRequired = cms.string("== 1")
)
ZTauTauControlRegion.cuts.insert(12,e_metMT_cut)
ZTauTauControlRegion_Prompt.cuts.append(e_metMT_cut)

mu_metMT_cut =  cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("metMT < 50"),
    numberRequired = cms.string("== 1")
)
ZTauTauControlRegion.cuts.insert(12,mu_metMT_cut)
ZTauTauControlRegion_Prompt.cuts.append(mu_metMT_cut)

deltaPhi_cut =  cms.PSet (
    inputCollection = cms.string("electron-muon pairs"),
    cutString = cms.string("deltaPhi > 2.5"),
    numberRequired = cms.string("== 1")
)
ZTauTauControlRegion.cuts.append(deltaPhi_cut)
ZTauTauControlRegion_Prompt.cuts.append(deltaPhi_cut)

ht_cut =  cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("unfilteredHt < 100"),
    numberRequired = cms.string("== 1")
)
ZTauTauControlRegion.cuts.append(ht_cut)
ZTauTauControlRegion_Prompt.cuts.append(ht_cut)


##########################################################################
ZTauTauControlRegion_ElectronPrompt = cms.PSet(
    name = cms.string("ZTauTautoEMu_ElectronPrompt"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"),
    cuts = cms.VPSet ()
)
ZTauTauControlRegion_ElectronPrompt.cuts.extend(copy.deepcopy(ZTauTauControlRegion_Prompt.cuts))
for cut in ZTauTauControlRegion_ElectronPrompt.cuts:
	if "(correctedD0) < 0.02" in str(cut.cutString) and cut.inputCollection == cms.string("muons"):
		ZTauTauControlRegion_ElectronPrompt.cuts.remove(cut) 


ZTauTauControlRegion_MuonPrompt = cms.PSet(
    name = cms.string("ZTauTautoEMu_MuonPrompt"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"),
    cuts = cms.VPSet ()
)
ZTauTauControlRegion_MuonPrompt.cuts.extend(copy.deepcopy(ZTauTauControlRegion_Prompt.cuts))
for cut in ZTauTauControlRegion_MuonPrompt.cuts:
	if "(correctedD0) < 0.02" in str(cut.cutString) and cut.inputCollection == cms.string("electrons"):
		ZTauTauControlRegion_MuonPrompt.cuts.remove(cut) 
##########################################################################
QCDinZTauTauControlRegion_ElectronPrompt = cms.PSet(
    name = cms.string("QCDinZTauTautoEMu_ElectronPrompt"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"),
    cuts = cms.VPSet ()
)
QCDinZTauTauControlRegion_ElectronPrompt.cuts.extend(copy.deepcopy(ZTauTauControlRegion_ElectronPrompt.cuts))
for cut in QCDinZTauTauControlRegion_ElectronPrompt.cuts:
	if "Beta" in str(cut.cutString):
		cut.cutString = cms.string("relPFdBetaIso > 0.12 & relPFdBetaIso < 1.5")
        if "rho"  in str(cut.cutString):
		cut.cutString = cms.string("relPFrhoIso > 0.1 & relPFrhoIso < 1")

QCDinZTauTauControlRegion_MuonPrompt = cms.PSet(
    name = cms.string("QCDinZTauTautoEMu_MuonPrompt"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"),
    cuts = cms.VPSet ()
)
QCDinZTauTauControlRegion_MuonPrompt.cuts.extend(copy.deepcopy(ZTauTauControlRegion_MuonPrompt.cuts))
for cut in QCDinZTauTauControlRegion_MuonPrompt.cuts:
	 if "Beta" in str(cut.cutString):
                cut.cutString = cms.string("relPFdBetaIso > 0.12 & relPFdBetaIso < 1.5")
         if "rho"  in str(cut.cutString):
                cut.cutString = cms.string("relPFrhoIso > 0.1 & relPFrhoIso < 1")
