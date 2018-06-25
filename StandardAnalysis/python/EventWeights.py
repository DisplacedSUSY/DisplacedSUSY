import FWCore.ParameterSet.Config as cms
import copy
import os

#################################################################
##### 2016/2017 PAYLOADS ##################################
#################################################################

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# EventWeights applied: 2016"
    electronRecoPayload = "electronReco2016"
    electronIdPayload = "electronID2016Tight"
    muonRecoPayload = "muonReco2016"
    muonIdPayload = "muonID2016Tight"
    muonIsoPayload = "muonIso2016Tight"
    triggerScaleFactorEEChannelPayload  = "triggerScaleFactorEEChannel2016"
    triggerScaleFactorMuMuChannelPayload  = "triggerScaleFactorMuMuChannel2016"
    triggerScaleFactorEMuChannelPayload  = "triggerScaleFactorEMuChannel2016"

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "# EventWeights applied: 2017"
    electronIdPayload = "electronID2017Tight"
    muonIsoPayload = "muonIso2017TightTightID"
    triggerScaleFactorEEChannelPayload = "triggerScaleFactorEEChannel2017"
    triggerScaleFactorMuMuChannelPayload = "triggerScaleFactorMuMuChannel2017"
    triggerScaleFactorEMuChannelPayload = "triggerScaleFactorEMuChannel2017"

else:
    print "what release are you in? We expect to be in 80X or 94X for the event weights"



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
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    electronWeights = cms.VPSet(
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(electronIdPayload)
            ),
        )

#################################################################

#OFFLINE MUON WEIGHTS
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    muonWeights = cms.VPSet(
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(muonRecoPayload)
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
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    muonWeights = cms.VPSet(
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(muonIsoPayload)
            ),
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
