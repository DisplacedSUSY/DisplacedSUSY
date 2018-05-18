import FWCore.ParameterSet.Config as cms

import math
import os

def customize (process, analysisChannel = "emu", applyPUReweighting = True, applyTriggerReweighting = True, sampleType = "bgMC"):

################################################################################
##### Set variables needed for DisplacedSUSYEventVariableProducer ##############
################################################################################

    if hasattr(process, "DisplacedSUSYEventVariableProducer"):
        process.DisplacedSUSYEventVariableProducer.type = cms.string(sampleType)
        process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("HLT_MET200_v")
        process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(1.0)

################################################################################
##### Apply PU reweighting #####################################################
################################################################################

    if applyPUReweighting:
        process.PUScalingFactorProducer.dataset = cms.string("TTJets_DiLept") # default value, only used when running interactively
        process.PUScalingFactorProducer.type = cms.string(sampleType)

        if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
            process.PUScalingFactorProducer.target = cms.string ("data2016_GH")
            process.PUScalingFactorProducer.targetUp = cms.string ("data2016_GHUp")
            process.PUScalingFactorProducer.targetDown = cms.string ("data2016_GHDown")
            process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu2016.root')

#FIXME: need to update for 2017
        elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
            process.PUScalingFactorProducer.target = cms.string ("data2016_GH")
            process.PUScalingFactorProducer.targetUp = cms.string ("data2016_GHUp")
            process.PUScalingFactorProducer.targetDown = cms.string ("data2016_GHDown")
            process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisplacedSUSY/StandardAnalysis/data/pu2016.root')

################################################################################
##### Apply trigger scale factor ###############################################
################################################################################

#FIXME: need to derive trigger scale factors for ee and mumu channels as well

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

#FIXME: need to update for mumu channel, for 2016 and 2017
            if analysisChannel=="mumu":
                if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(1.0)
                elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
                    process.DisplacedSUSYEventVariableProducer.triggerScaleFactor = cms.double(1.0)

