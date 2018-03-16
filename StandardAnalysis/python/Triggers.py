import FWCore.ParameterSet.Config as cms
import os
import copy

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# Using 2016 triggers"

    triggersDoubleMuon = cms.vstring(
        "HLT_DoubleMu33NoFiltersNoVtx",
        "HLT_DoubleMu23NoFiltersNoVtxDisplaced"
        )

    triggersDoublePhoton = cms.vstring(
        "HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_Eta2_Mass15",
        "HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15"
        )

    triggersMuonPhoton = cms.vstring(
        "HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v"
        )

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "# Using 2017 triggers"

    triggersDoubleMuon = cms.vstring(
        "HLT_DoubleMu43NoFiltersNoVtx"
        )

    triggersDoublePhoton = cms.vstring(
        "HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90"
        )

    triggersMuonPhoton = cms.vstring(
        "HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v"
        )

else:
    print "# You're using a CMSSW version we don't expect, so the triggers are not defined"
