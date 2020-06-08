import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *

import math
import os

def customize (process, analysisChannel = "emu", applyPUReweighting = True, applyTriggerReweighting = True, sampleType = "bgMC"):

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
            process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_MET200_v")
        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
            process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_PFMET200_HBHECleaned")
        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
            process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_PFMET200_HBHECleaned")
        process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(1.0)

        process.DisplacedSUSYEventVariableProducer.AlgInputTag = cms.InputTag("gtStage2Digis")
        process.DisplacedSUSYEventVariableProducer.l1tAlgBlkInputTag = cms.InputTag("gtStage2Digis")
        process.DisplacedSUSYEventVariableProducer.l1tExtBlkInputTag = cms.InputTag("gtStage2Digis")
        process.DisplacedSUSYEventVariableProducer.l1Seeds = cms.vstring("L1_Mu5_EG20","L1_Mu20_EG15","L1_DoubleMu_11_4", "L1_DoubleMu_12_5", "L1_DoubleMu_13_6", "L1_SingleEG30", "L1_SingleEG40", "L1_SingleIsoEG22er", "L1_SingleIsoEG28", "L1_DoubleEG_15_10", "L1_DoubleEG_25_12", "L1_SingleJet200", "L1_SingleTau100er") #just for 2016 seeds for now
        process.DisplacedSUSYEventVariableProducer.ReadPrescalesFromFile = cms.bool(False)
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



################################################################################
##### Apply trigger scale factor ###############################################
################################################################################

#FIXME: need to derive trigger scale factors for 2017 and 2018 as well

        if applyTriggerReweighting:

            if analysisChannel=="emu":
                if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.965)
#FIXME: need to update for 2017
                elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.965)
#FIXME: need to update for 2018
                elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(1.0)

            if analysisChannel=="ee":
                if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.962)
#FIXME: need to update for 2017
                elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.962)
#FIXME: need to update for 2018
                elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(1.0)


            if analysisChannel=="mumu":
                if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.961)
#FIXME: need to update for 2017
                elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.961)
#FIXME: need to update for 2018
                elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(1.0)
