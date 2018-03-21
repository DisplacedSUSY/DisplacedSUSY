import FWCore.ParameterSet.Config as cms
import os
import copy

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# Using 2016 triggers"
    #http://fwyzard.web.cern.ch/fwyzard/hlt/2016/summary

    #main signal triggers for the MuMu channel
    triggersDoubleMuon = cms.vstring(
        "HLT_DoubleMu33NoFiltersNoVtx",
        "HLT_DoubleMu23NoFiltersNoVtxDisplaced"
        )

    #backup triggers for the MuMu channel
    triggersDoubleMuonBackup = cms.vstring(
        "HLT_DoubleMu38NoFiltersNoVtx",
        "HLT_DoubleMu28NoFiltersNoVtxDisplaced"
        )

    #main signal triggers for the EE channel
    triggersDoublePhoton = cms.vstring(
        "HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15" #Photon36_Photon22_Mass15 was prescaled sometime during 2016
        )

    #backup triggers for the EE channel
    triggersDoublePhotonBackup = cms.vstring()

    #main signal triggers for the EMu channel
    triggersMuonPhoton = cms.vstring(
        "HLT_Mu38NoFiltersNoVtx_Photon38_CaloIdL_v",
        "HLT_Mu28NoFiltersNoVtxDisplaced_Photon28_CaloIdL_v" 
        )

    #backup triggers for the EMu channel
    triggersMuonPhotonBackup = cms.vstring(
        "HLT_Mu42NoFiltersNoVtx_Photon42_CaloIdL",
        "HLT_Mu33NoFiltersNoVtxDisplaced_Photon33_CaloIdL_v" 
        )

    triggersSingleElectron = cms.vstring(
        "HLT_Ele27_WPTight_Gsf_v"
        )

    triggersSingleMuon = cms.vstring(
        "HLT_Mu50_v", 
        "HLT_TkMu50_v"
        )

    triggersIsoSingleMuon = cms.vstring(
        "HLT_IsoMu24_v"
        )

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "# Using 2017 triggers"
    #http://fwyzard.web.cern.ch/fwyzard/hlt/2017/summary

    #main signal triggers for the MuMu channel
    triggersDoubleMuon = cms.vstring(
        "HLT_DoubleMu43NoFiltersNoVtx"
        )

    #backup triggers for the MuMu channel
    triggersDoubleMuonBackup = cms.vstring(
        "HLT_DoubleMu48NoFiltersNoVtx",
        )

    #main signal triggers for the EE channel
    triggersDoublePhoton = cms.vstring(
        "HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90"
        )

    #backup triggers for the EE channel
    triggersDoublePhotonBackup = cms.vstring(
        "HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95"
        )

    #main signal triggers for the EMu channel
    triggersMuonPhoton = cms.vstring(
        "HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v"
        )

    #backup triggers for the EMu channel
    triggersMuonPhotonBackup = cms.vstring(
        "HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v",
        )

    triggersSingleElectron = cms.vstring(
        "HLT_Ele27_WPTight_Gsf_v"
        )

    triggersSingleMuon = cms.vstring(
        "HLT_Mu50_v", 
        )

    triggersIsoSingleMuon = cms.vstring(
        "HLT_IsoMu27_v"
        )

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_0_"):
    print "# Using 2018 triggers"
    #http://fwyzard.web.cern.ch/fwyzard/hlt/2018/summary

    #main signal triggers for the MuMu channel
    triggersDoubleMuon = cms.vstring(
        "HLT_DoubleMu43NoFiltersNoVtx"
        )

    #backup triggers for the MuMu channel
    triggersDoubleMuonBackup = cms.vstring(
        "HLT_DoubleMu48NoFiltersNoVtx",
        )

    #main signal triggers for the EE channel
    triggersDoublePhoton = cms.vstring(
        "HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90"
        )

    #backup triggers for the EE channel
    triggersDoublePhotonBackup = cms.vstring(
        "HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95"
        )

    #main signal triggers for the EMu channel
    triggersMuonPhoton = cms.vstring(
        "HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v"
        )

    #backup triggers for the EMu channel
    triggersMuonPhotonBackup = cms.vstring(
        "HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v",
        )

    triggersSingleElectron = cms.vstring(
        "HLT_Ele27_WPTight_Gsf_v"
        )

    triggersSingleMuon = cms.vstring(
        "HLT_Mu50_v", 
        )

    triggersIsoSingleMuon = cms.vstring(
        "HLT_IsoMu27_v"
        )

else:
    print "# You're using a CMSSW version we don't expect, so the triggers are not defined"
