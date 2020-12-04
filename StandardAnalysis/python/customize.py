import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *

import math
import os

def customize (process, analysisChannel = "emu", applyPUReweighting = True, sampleType = "bgMC"):

    process.LifetimeWeightProducer.requireLastAndFirstCopy = cms.bool(True)
    process.LifetimeWeightProducer.specialRHadronsForDispLeptons = cms.bool(True)

################################################################################
##### remove isolation cut from electron VID  ##################################
################################################################################

    e_id_name = str(collectionProducer.electrons.vidTightIdMap).split(",")[1][1:-2]
    cut_to_remove = 'GsfEleRelPFIsoScaledCut'
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
        cut_to_remove = 'GsfEleEffAreaPFIsoCut'
    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
        cut_to_remove = 'GsfEleRelPFIsoScaledCut'
    else:
        print "unrecognized CMSSW release; electron VID cut removal might not work"

    removeVIDCut(process, e_id_name, cut_to_remove)

################################################################################
##### Set variables needed for DisplacedSUSYEventVariableProducer ##############
################################################################################

    if hasattr(process, "DisplacedSUSYEventVariableProducer"):
        process.DisplacedSUSYEventVariableProducer.type = cms.string(sampleType)
        if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
            process.DisplacedSUSYEventVariableProducer.triggerPaths = cms.vstring("HLT_MET200", "HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight","HLT_PFMET120_PFMHT120_IDTight","HLT_PFMET170_HBHECleaned", "HLT_PFMET300", "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight")
        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
            process.DisplacedSUSYEventVariableProducer.triggerPaths = cms.vstring("HLT_CaloMET350_HBHECleaned","HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight","HLT_PFMET120_PFMHT120_IDTight","HLT_PFMET250_HBHECleaned","HLT_PFMETNoMu120_PFMHTNoMu120_IDTight")
        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
            process.DisplacedSUSYEventVariableProducer.triggerPaths = cms.vstring("HLT_CaloMET350_HBHECleaned","HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight","HLT_PFMET120_PFMHT120_IDTight","HLT_PFMET200_HBHE_BeamHaloCleaned","HLT_PFMET250_HBHECleaned","HLT_PFMETNoMu120_PFMHTNoMu120_IDTight")

        process.DisplacedSUSYEventVariableProducer.AlgInputTag = cms.InputTag("gtStage2Digis")
        process.DisplacedSUSYEventVariableProducer.l1tAlgBlkInputTag = cms.InputTag("gtStage2Digis")
        process.DisplacedSUSYEventVariableProducer.l1tExtBlkInputTag = cms.InputTag("gtStage2Digis")
        if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
            process.DisplacedSUSYEventVariableProducer.l1Seeds = cms.vstring("L1_Mu5_EG20","L1_Mu20_EG15",
                                                                             "L1_DoubleMu_11_4", "L1_DoubleMu_12_5", "L1_DoubleMu_13_6",
                                                                             "L1_SingleEG30", "L1_SingleEG40", "L1_SingleIsoEG22er", "L1_SingleIsoEG28",
                                                                             "L1_DoubleEG_15_10", "L1_DoubleEG_25_12", "L1_SingleJet200", "L1_SingleTau100er")
        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
            process.DisplacedSUSYEventVariableProducer.l1Seeds = cms.vstring("L1_Mu5_EG23","L1_Mu7_EG23","L1_Mu20_EG17","L1_Mu23_EG10",
                                                                             "L1_DoubleMu_12_5", "L1_DoubleMu_13_6", "L1_DoubleMu_15_5", "L1_DoubleMu_15_7",
                                                                             "L1_SingleEG30", "L1_SingleEG50", "L1_SingleIsoEG24", "L1_SingleIsoEG38",
                                                                             "L1_DoubleEG_18_17", "L1_DoubleEG_25_12", "L1_SingleJet200", "L1_SingleTau100er2p1")

        process.DisplacedSUSYEventVariableProducer.ReadPrescalesFromFile = cms.bool(False)

        #all tracker material values in cm
        #beam pipe
        if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
            process.DisplacedSUSYEventVariableProducer.beamPipe_x_center = cms.double(0.124)
            process.DisplacedSUSYEventVariableProducer.beamPipe_y_center = cms.double(0.07)
        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
            process.DisplacedSUSYEventVariableProducer.beamPipe_x_center = cms.double(0.113)
            process.DisplacedSUSYEventVariableProducer.beamPipe_y_center = cms.double(-0.180)
        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
            process.DisplacedSUSYEventVariableProducer.beamPipe_x_center = cms.double(0.171)
            process.DisplacedSUSYEventVariableProducer.beamPipe_y_center = cms.double(-0.176)
        process.DisplacedSUSYEventVariableProducer.beamPipe_outerR = cms.double(2.25)
        process.DisplacedSUSYEventVariableProducer.beamPipe_innerR = cms.double(2.17)

        #BPIX inner shield
        process.DisplacedSUSYEventVariableProducer.nearInnerShield_x_center = cms.double(-0.093)
        process.DisplacedSUSYEventVariableProducer.nearInnerShield_y_center = cms.double(-0.091)
        process.DisplacedSUSYEventVariableProducer.farInnerShield_x_center = cms.double(0.044)
        process.DisplacedSUSYEventVariableProducer.farInnerShield_y_center = cms.double(-0.098)
        if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
            #assume inner shield has the same thickness as the beam pipe
            process.DisplacedSUSYEventVariableProducer.innerShield_outerR = cms.double(3.814)
            process.DisplacedSUSYEventVariableProducer.innerShield_innerR = cms.double(3.734)
        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
            process.DisplacedSUSYEventVariableProducer.innerShield_outerR = cms.double(2.44)
            process.DisplacedSUSYEventVariableProducer.innerShield_innerR = cms.double(2.36)

        #BPIX layers
        #assume module thickness of 0.15 cm
        #L1 at 4.2 and 4.8 cm (2.8 and 3.1 cm) in phase 0 (phase 1)
        #L2 at 6.6 and 7.0 cm in phase 1
        #https://indico.cern.ch/event/750050/contributions/3229824/attachments/1761100/2857630/2018.11.28_PixelFit_kropiv.pdf
        if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
            process.DisplacedSUSYEventVariableProducer.bpix_x_center = cms.double(-0.027)
            process.DisplacedSUSYEventVariableProducer.bpix_y_center = cms.double(-0.078)
            process.DisplacedSUSYEventVariableProducer.bpix_z_center = cms.double(-0.051)
            process.DisplacedSUSYEventVariableProducer.bpix_z_halfLength = cms.double(26.5)
            process.DisplacedSUSYEventVariableProducer.bpixL1_outerR = cms.double(4.875)
            process.DisplacedSUSYEventVariableProducer.bpixL1_innerR = cms.double(4.125)
            process.DisplacedSUSYEventVariableProducer.bpixL2_outerR = cms.double(7.375)
            process.DisplacedSUSYEventVariableProducer.bpixL2_innerR = cms.double(7.225)
            process.DisplacedSUSYEventVariableProducer.bpixL3_outerR = cms.double(10.275)
            process.DisplacedSUSYEventVariableProducer.bpixL3_innerR = cms.double(10.125)
        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
            process.DisplacedSUSYEventVariableProducer.bpix_z_halfLength = cms.double(27.45)
            process.DisplacedSUSYEventVariableProducer.bpixL1_outerR = cms.double(3.175)
            process.DisplacedSUSYEventVariableProducer.bpixL1_innerR = cms.double(2.725)
            process.DisplacedSUSYEventVariableProducer.bpixL2_outerR = cms.double(7.075)
            process.DisplacedSUSYEventVariableProducer.bpixL2_innerR = cms.double(6.525)
            process.DisplacedSUSYEventVariableProducer.bpixL3_outerR = cms.double(10.975)
            process.DisplacedSUSYEventVariableProducer.bpixL3_innerR = cms.double(10.825)
            process.DisplacedSUSYEventVariableProducer.bpixL4_outerR = cms.double(16.075)
            process.DisplacedSUSYEventVariableProducer.bpixL4_innerR = cms.double(15.925)
            if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
                process.DisplacedSUSYEventVariableProducer.bpix_x_center = cms.double(0.109725)
                process.DisplacedSUSYEventVariableProducer.bpix_y_center = cms.double(-0.108993)
                process.DisplacedSUSYEventVariableProducer.bpix_z_center = cms.double(-0.32054)
            elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
                process.DisplacedSUSYEventVariableProducer.bpix_x_center = cms.double(0.0856367)
                process.DisplacedSUSYEventVariableProducer.bpix_y_center = cms.double(-0.101882)
                process.DisplacedSUSYEventVariableProducer.bpix_z_center = cms.double(-0.326049)

        #FPIX disks
        if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
            process.DisplacedSUSYEventVariableProducer.fpix_x_center = cms.double(-0.027)
            process.DisplacedSUSYEventVariableProducer.fpix_y_center = cms.double(-0.078)
            process.DisplacedSUSYEventVariableProducer.fpix_z_center = cms.double(-0.051)
            process.DisplacedSUSYEventVariableProducer.fpix_outerR = cms.double(14.46)
            process.DisplacedSUSYEventVariableProducer.fpix_innerR = cms.double(5.97)
            process.DisplacedSUSYEventVariableProducer.fpixD1_z_center = cms.double(34.5)
            process.DisplacedSUSYEventVariableProducer.fpixD2_z_center = cms.double(46.5)
        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
            process.DisplacedSUSYEventVariableProducer.fpix_outerR = cms.double(16.1)
            process.DisplacedSUSYEventVariableProducer.fpix_innerR = cms.double(4.5)
            process.DisplacedSUSYEventVariableProducer.fpixD1_z_center = cms.double(29.1)
            process.DisplacedSUSYEventVariableProducer.fpixD2_z_center = cms.double(39.6)
            process.DisplacedSUSYEventVariableProducer.fpixD3_z_center = cms.double(51.6)
            if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
                process.DisplacedSUSYEventVariableProducer.fpix_x_center = cms.double(0.0492231)
                process.DisplacedSUSYEventVariableProducer.fpix_y_center = cms.double(-0.11025)
                process.DisplacedSUSYEventVariableProducer.fpix_z_center = cms.double(-0.333341)
            elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
                process.DisplacedSUSYEventVariableProducer.fpix_x_center = cms.double(0.0311191)
                process.DisplacedSUSYEventVariableProducer.fpix_y_center = cms.double(-0.106233)
                process.DisplacedSUSYEventVariableProducer.fpix_z_center = cms.double(-0.338382)
        #assume thickness of 0.15 cm
        process.DisplacedSUSYEventVariableProducer.fpix_z_halfThickness = cms.double(0.075)

        #pixel support tube
        process.DisplacedSUSYEventVariableProducer.supportTube_x_center = cms.double(-0.08)
        process.DisplacedSUSYEventVariableProducer.supportTube_y_center = cms.double(-0.32)
        #assume thickness of 0.15 cm
        process.DisplacedSUSYEventVariableProducer.supportTube_outerRX = cms.double(21.775)
        process.DisplacedSUSYEventVariableProducer.supportTube_outerRY = cms.double(21.875)
        process.DisplacedSUSYEventVariableProducer.supportTube_innerRX = cms.double(21.625)
        process.DisplacedSUSYEventVariableProducer.supportTube_innerRY = cms.double(21.725)

################################################################################
##### Set variables needed for OSUElectron and Muon Producer ###################
################################################################################

    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
        for a in dir(process):
            x = getattr(process, a)
            if not hasattr(x, "type_"):
                continue
            if x.type_() == "OSUElectronProducer":
                setattr(x, "d0SmearingWidth", 0.001475) #in cm; ave of values from e-e and e-mu pcr (elog 1281)
            elif x.type_() == "OSUMuonProducer":
                setattr(x, "d0SmearingWidth", 0.000757) #in cm; ave of values from from e-mu and mu-mu pcr (elog 1281)
    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
        for a in dir(process):
            x = getattr(process, a)
            if not hasattr(x, "type_"):
                continue
            if x.type_() == "OSUElectronProducer":
                setattr(x, "d0SmearingWidth", 0.000918) #in cm; ave of values from e-e and e-mu pcr (elog 1359)
            elif x.type_() == "OSUMuonProducer":
                setattr(x, "d0SmearingWidth", 0.000811) #in cm; ave of values from from e-mu and mu-mu pcr (elog 1359)

################################################################################
##### Apply PU reweighting #####################################################
################################################################################

    if applyPUReweighting:
        process.PUScalingFactorProducer.dataset = cms.string("SingleTop_tW") # default value, only used when running interactively
        process.PUScalingFactorProducer.type = cms.string(sampleType)

        if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
            process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu2016.root')
            process.PUScalingFactorProducer.target = cms.string ("data2016_GH")
            process.PUScalingFactorProducer.targetUp = cms.string ("data2016_GHUp")
            process.PUScalingFactorProducer.targetDown = cms.string ("data2016_GHDown")

        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
            process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu2017.root')
            if analysisChannel=="emu" or analysisChannel=="mumu":
                process.PUScalingFactorProducer.target = cms.string ("data2017_CDEF")
                process.PUScalingFactorProducer.targetUp = cms.string ("data2017_CDEFUp")
                process.PUScalingFactorProducer.targetDown = cms.string ("data2017_CDEFDown")
            elif analysisChannel=="ee":
                process.PUScalingFactorProducer.target = cms.string ("data2017")
                process.PUScalingFactorProducer.targetUp = cms.string ("data2017Up")
                process.PUScalingFactorProducer.targetDown = cms.string ("data2017Down")

        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
            process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu2018.root')
            process.PUScalingFactorProducer.target = cms.string ("data2018")
            process.PUScalingFactorProducer.targetUp = cms.string ("data2018Up")
            process.PUScalingFactorProducer.targetDown = cms.string ("data2018Down")
