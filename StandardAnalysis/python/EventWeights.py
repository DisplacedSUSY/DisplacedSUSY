import FWCore.ParameterSet.Config as cms
import copy
import os

#################################################################
##### 2016/2017/2018 PAYLOADS ###################################
#################################################################

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# EventWeights applied: 2016"
    electronRecoPayload = "electronReco2016"
    electronIdPayload = "electronID2016Tight"
    muonTrackingPayload = "muonTracking2016GH"
    muonIdPayload = "muonID2016TightGH"
    muonIsoPayload = "muonIso2016TightTightIDGH"
    triggerScaleFactorEEChannelPayload  = "triggerScaleFactorEEChannel2016"
    triggerScaleFactorMuMuChannelPayload  = "triggerScaleFactorMuMuChannel2016"
    triggerScaleFactorEMuChannelPayload  = "triggerScaleFactorEMuChannel2016"

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "# EventWeights applied: 2017"
    electronIdPayload = "electronID2017Tight"
    muonIdPayload = "muonID2017Tight"
    muonIsoPayload = "muonIso2017TightTightID"
    triggerScaleFactorEEChannelPayload = "triggerScaleFactorEEChannel2017"
    triggerScaleFactorMuMuChannelPayload = "triggerScaleFactorMuMuChannel2017"
    triggerScaleFactorEMuChannelPayload = "triggerScaleFactorEMuChannel2017"

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    print "# EventWeights applied: 2018"
    electronIdPayload = "electronID2018Tight"
    muonIdPayload = "muonID2018Tight"
    muonIsoPayload = "muonIso2018TightTightID"
    triggerScaleFactorEEChannelPayload = "triggerScaleFactorEEChannel2018"
    triggerScaleFactorMuMuChannelPayload = "triggerScaleFactorMuMuChannel2018"
    triggerScaleFactorEMuChannelPayload = "triggerScaleFactorEMuChannel2018"

else:
    print "what release are you in? We expect to be in 80X or 94X or 102X for the event weights"



#################################################################
##### DEFINE WEIGHTS IN COMMON ##################################
#################################################################

# DEFAULT EVENT WEIGHTS (for selections without electrons, muons or trigger required)
weights = cms.VPSet(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("lifetimeWeight")
    ),
   cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor")
    ),
)

weightsFluctuatePileup = cms.VPSet(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("lifetimeWeight")
    ),
   cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor"),
        fluctuations = cms.vstring("puScalingFactorUp", "puScalingFactorDown")
    ),
)

#################################################################

#OFFLINE ELECTRON WEIGHTS
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    electronWeights = cms.VPSet(
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(electronRecoPayload)
            ),
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(electronIdPayload)
            ),
        )
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    electronWeights = cms.VPSet(
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(electronIdPayload)
            ),
        )

elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_6_")):
    electronWeights = cms.VPSet(
        )

#################################################################

#OFFLINE MUON WEIGHTS
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    muonWeights = cms.VPSet(
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(muonTrackingPayload)
            ),
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(muonIdPayload)
            ),
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(muonIsoPayload)
            ),
        )
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    muonWeights = cms.VPSet(
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(muonIdPayload)
            ),
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(muonIsoPayload)
            ),
        )
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_6_")):
    muonWeights = cms.VPSet(
        )

#################################################################
####### #START OF WEIGHTS PER CHANNEL ###########################
#################################################################

#FIXME: DEFINE TRIGGER SCALE FACTORS PER CHANNEL AND PER YEAR

# E-E CHANNEL
weightsEEChannel = copy.deepcopy(weights)
weightsEEChannel.extend(electronWeights)
weightsEEChannel.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(triggerScaleFactorEEChannelPayload)
        ),
    )

#################################################################

# MU-MU CHANNEL
weightsMuMuChannel = copy.deepcopy(weights)
weightsMuMuChannel.extend(muonWeights)
weightsMuMuChannel.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(triggerScaleFactorMuMuChannelPayload)
        ),
    )

#################################################################

# E-MU CHANNEL
weightsEMuChannel = copy.deepcopy(weights)
weightsEMuChannel.extend(electronWeights)
weightsEMuChannel.extend(muonWeights)
weightsEMuChannel.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(triggerScaleFactorEMuChannelPayload)
        ),
    )
