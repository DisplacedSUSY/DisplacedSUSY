import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *

import math
import os

def customize (process, analysisChannel = "emu", applyPUReweighting = True, applyTriggerReweighting = True, sampleType = "bgMC"):

################################################################################
##### remove isolation cut from electron VID  ##################################
################################################################################

    removeVIDCut(process, str(collectionProducer.electrons.vidTightIdMap), 'GsfEleEffAreaPFIsoCut')

################################################################################
##### Set variables needed for DisplacedSUSYEventVariableProducer ##############
################################################################################

    if hasattr(process, "DisplacedSUSYEventVariableProducer"):
        process.DisplacedSUSYEventVariableProducer.type = cms.string(sampleType)
        if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
            process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_MET200_v")
        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
            process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_PFMET200_HBHECleaned")
        process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(1.0)

################################################################################
##### Set variables needed for OSUElectron and Muon Producer ###################
################################################################################

    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
        for a in dir(process):
            x = getattr(process, a)
            if not hasattr(x, "type_"):
                continue
            if x.type_() == "OSUElectronProducer":
                setattr(x, "d0SmearingWidth", 0.00142) # from e-e pcr
            elif x.type_() == "OSUMuonProducer":
                setattr(x, "d0SmearingWidth", 0.00073) # from e-mu pcr

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


################################################################################
##### Apply trigger scale factor ###############################################
################################################################################

#FIXME: need to derive trigger scale factors for 2017 as well

        if applyTriggerReweighting:

            if analysisChannel=="emu":
                if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.965)
#FIXME: need to update for 2017
                elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.965)

            if analysisChannel=="ee":
                if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.962)
#FIXME: need to update for 2017
                elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.962)

            if analysisChannel=="mumu":
                if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.961)
#FIXME: need to update for 2017
                elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(0.961)

