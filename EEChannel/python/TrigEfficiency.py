import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *


##########################################################################
### Set up the displaced control region for the displaced SUSY analysis #####
##########################################################################

#main signal triggers for the EE channel

triggerDoublePhoton42and25 = cms.PSet(
    name = cms.string("triggerDoublePhoton42and25"),
    triggers = cms.vstring("HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15"),
    cuts = cms.VPSet()
)



triggerDoublePhoton30 = cms.PSet(
    name = cms.string("triggerDoublePhoton30"),
    triggers = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90"),
    cuts = cms.VPSet()
)




triggerDoublePhoton60 = cms.PSet(
    name = cms.string("triggerDoublePhoton60"),
    triggers = cms.vstring("HLT_DoublePhoton60"),
    cuts = cms.VPSet()
)


triggerDoublePhoton30orDoublePhoton60 = cms.PSet(
    name = cms.string("triggerDoublePhoton30orDoublePhoton60"),
    triggers = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90","HLT_DoublePhoton60"),
    cuts = cms.VPSet()
)



trigMETandEEtrig = cms.PSet(
    name = cms.string("trigMETandEEtrig"),
    triggers = cms.vstring("HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90","HLT_DoublePhoton60"),
    cuts = cms.VPSet()
)
trigMETandEEtrig.cuts.append(cutDummy)
trigMETandEEtrig.cuts.append(pass_trigger)


trigMET = cms.PSet(
    name = cms.string("trigMET"),
    triggers = cms.vstring(""),
    cuts = cms.VPSet()
)
trigMET.cuts.append(cutDummy)
trigMET.cuts.append(pass_trigger)

