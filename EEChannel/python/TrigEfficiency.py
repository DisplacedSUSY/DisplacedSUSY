import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EEChannel.CutDefinitions import *

##########################################################################
### Set up the DY regions for trigger efficiency plots
##########################################################################

# No Trigger
TrigEffDen = cms.PSet(
    name = cms.string("TrigEffDen"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### passes MET trigger (use eventvariable so that triggers can be ANDed)
TrigEffDen.cuts.append(pass_trigger)
TrigEffDen.cuts.append(electron_eta_cut)
TrigEffDen.cuts.append(electron_gap_veto)
TrigEffDen.cuts.append(electron_pt_25_cut)
TrigEffDen.cuts.append(electron_id_cut)
TrigEffDen.cuts.append(diElectron_invMass_Z_cut)
### extra electron veto
TrigEffDen.cuts.append(electron_2electron_cut)

TrigEffNum = cms.PSet(
    name = cms.string("TrigEffNum"),
    triggers = triggersDoublePhoton,
    cuts = cms.VPSet(copy.deepcopy(TrigEffDen.cuts))
)



### use electron tag variable
trigMETandEEtrigTagElectron = cms.PSet(
    name = cms.string("trigMETandEEtrigTagElectron"),
    triggers = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90","HLT_DoublePhoton60"),
    cuts = cms.VPSet(copy.deepcopy(TrigEffDen.cuts))
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
