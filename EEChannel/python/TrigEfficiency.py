import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EEChannel.CutDefinitions import *


##########################################################################
### Set up the displaced control region for the displaced SUSY analysis #####
##########################################################################

#main signal triggers for the EE channel

triggerDoublePhoton42and25 = cms.PSet(
    name = cms.string("triggerDoublePhoton42and25"),
    triggers = cms.vstring("HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15"),
    cuts = cms.VPSet()
)
triggerDoublePhoton42and25.cuts.append(cutDummy)

triggerDoublePhoton30 = cms.PSet(
    name = cms.string("triggerDoublePhoton30"),
    triggers = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90"),
    cuts = cms.VPSet()
)
triggerDoublePhoton30.cuts.append(cutDummy)

triggerDoublePhoton60 = cms.PSet(
    name = cms.string("triggerDoublePhoton60"),
    triggers = cms.vstring("HLT_DoublePhoton60"),
    cuts = cms.VPSet()
)

# main EE trigger for analysis
triggerDoublePhoton30orDoublePhoton60 = cms.PSet(
    name = cms.string("triggerDoublePhoton30orDoublePhoton60"),
    triggers = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90","HLT_DoublePhoton60"),
    cuts = cms.VPSet()
)


##########################################################################
### Set up the TTbar regions for trigger efficiency plots
##########################################################################

# No Trigger
TTbarForTrigEffNoTrig = cms.PSet(
    name = cms.string("TTbarForTrigEffNoTrig"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
TTbarForTrigEffNoTrig.cuts.append(electron_eta_cut)
TTbarForTrigEffNoTrig.cuts.append(electron_pt_25_cut)
TTbarForTrigEffNoTrig.cuts.append(electron_id_cut) ##versioned tight ID includes tight isolation
### good electron, electron pair
TTbarForTrigEffNoTrig.cuts.append(diElectron_opposite_charge_cut)
TTbarForTrigEffNoTrig.cuts.append(diElectron_deltaR_cut)
### two good jets, one medium b jet
TTbarForTrigEffNoTrig.cuts.append(atLeastTwo_jet_eta_cut)
TTbarForTrigEffNoTrig.cuts.append(atLeastTwo_jet_pt_30_cut)
TTbarForTrigEffNoTrig.cuts.append(atLeastTwo_jet_id_cut)
TTbarForTrigEffNoTrig.cuts.append(atLeastTwo_jet_lepton_cleaning_cut)
TTbarForTrigEffNoTrig.cuts.append(jet_btag_mwp_cut)
### extra electron veto
TTbarForTrigEffNoTrig.cuts.append(electron_2electron_cut)

TTbarForHLTDiphoton30 = cms.PSet(
    name = cms.string("TTbarForHLTDiphoton30"),
    triggers = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)
TTbarForHLTDiphoton30.cuts.append(pass_trigger)


TTbarForHLTDoublePhoton60 = cms.PSet(
    name = cms.string("TTbarForHLTDoublePhoton60"),
    triggers = cms.vstring("HLT_DoublePhoton60"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)
TTbarForHLTDoublePhoton60.cuts.append(pass_trigger)

# EE trigger and MET trigger
trigMETandEEtrig = cms.PSet(
    name = cms.string("trigMETandEEtrig"),
    triggers = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90","HLT_DoublePhoton60"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)
trigMETandEEtrig.cuts.append(pass_trigger)

# MET trigger 
trigMET = cms.PSet(
    name = cms.string("trigMET"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)
trigMET.cuts.append(pass_trigger)

### use electron tag variable
trigMETandEEtrigTagElectron = cms.PSet(
    name = cms.string("trigMETandEEtrigTagElectron"),
    triggers = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90","HLT_DoublePhoton60"),
    cuts = cms.VPSet(copy.deepcopy(TTbarForTrigEffNoTrig.cuts))
)
for cut in trigMETandEEtrigTagElectron.cuts:
    if "electron.charge * electron.charge < 0" in str(cut.cutString):
        trigMETandEEtrigTagElectron.cuts.remove(cut)
    if "deltaR(electron, electron) > 0.5" in str(cut.cutString):
        trigMETandEEtrigTagElectron.cuts.remove(cut)
trigMETandEEtrigTagElectron.cuts.append(tagElectronExists_cut)
trigMETandEEtrigTagElectron.cuts.append(electron_opposite_charge_from_tag_cut)
trigMETandEEtrigTagElectron.cuts.append(electron_deltaR_from_tag_cut)
trigMETandEEtrigTagElectron.cuts.append(pass_trigger)

trigMETTagElectron = cms.PSet(
    name = cms.string("trigMETTagElectron"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet(copy.deepcopy(trigMETandEEtrigTagElectron.cuts))
)
trigMETTagElectron.cuts.append(pass_trigger)


TTbarForHLTDiphoton30eTag = cms.PSet(
    name = cms.string("TTbarForHLTDiphoton30eTag"),
    triggers = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90"),
    cuts = cms.VPSet(copy.deepcopy(trigMETandEEtrigTagElectron.cuts))
)
TTbarForHLTDiphoton30eTag.cuts.append(pass_trigger)


TTbarForHLTDoublePhoton60eTag = cms.PSet(
    name = cms.string("TTbarForHLTDoublePhoton60eTag"),
    triggers = cms.vstring("HLT_DoublePhoton60"),
    cuts = cms.VPSet(copy.deepcopy(trigMETandEEtrigTagElectron.cuts))
)
TTbarForHLTDoublePhoton60eTag.cuts.append(pass_trigger)
