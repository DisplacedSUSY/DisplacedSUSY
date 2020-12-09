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
    muonTrackingPayload = "muonTracking2016"
    muonIdPayload = "muonID2016Tight"
    muonIsoPayload = "muonIso2016TightTightID"
    electronTriggerEEPayload  = "electronTrigger2016ee"
    muonTriggerMuMuPayload  = "muonTrigger2016mumu"
    electronTriggerEMuPayload  = "electronTrigger2016emu"
    muonTriggerEMuPayload  = "muonTrigger2016emu"

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "# EventWeights applied: 2017"
    electronIdPayload = "electronID2017Tight"
    muonIdPayload = "muonID2017Tight"
    muonIsoPayload = "muonIso2017TightTightID"
    electronTriggerEEPayload = "electronTrigger2017ee"
    muonTriggerMuMuPayload = "muonTrigger2017mumu"
    electronTriggerEMuPayload = "electronTrigger2017emu"
    muonTriggerEMuPayload  = "muonTrigger2017emu"

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    print "# EventWeights applied: 2018"
    electronIdPayload = "electronID2018Tight"
    muonIdPayload = "muonID2018Tight"
    muonIsoPayload = "muonIso2018TightTightID"
    electronTriggerEEPayload = "electronTrigger2018ee"
    muonTriggerMuMuPayload = "muonTrigger2018mumu"
    electronTriggerEMuPayload = "electronTrigger2018emu"
    muonTriggerEMuPayload  = "muonTrigger2018emu"

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
electronWeights = cms.VPSet(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(electronIdPayload)
    ),
)
electronWeightsFluctuate = cms.VPSet(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(electronIdPayload),
        fluctuations = cms.vstring(electronIdPayload+"Up", electronIdPayload+"Down")
    ),
)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    electronWeights.append(
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(electronRecoPayload)
        ),
    )
    electronWeightsFluctuate.append(
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(electronRecoPayload),
            fluctuations = cms.vstring(electronRecoPayload+"Up", electronRecoPayload+"Down")
        ),
    )
#################################################################

#OFFLINE MUON WEIGHTS
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
muonWeightsFluctuate = cms.VPSet(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(muonIdPayload),
        fluctuations = cms.vstring(muonIdPayload+"Up", muonIdPayload+"Down")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(muonIsoPayload),
        fluctuations = cms.vstring(muonIsoPayload+"Up", muonIsoPayload+"Down")
    ),
)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    muonWeights.append(
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(muonTrackingPayload)
            ),
        )
    muonWeightsFluctuate.append(
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(muonTrackingPayload),
            fluctuations = cms.vstring(muonTrackingPayload+"Up", muonTrackingPayload+"Down")
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
        inputVariable = cms.string(electronTriggerEEPayload)
        ),
    )

weightsEEChannelFluctuateEleSFs = copy.deepcopy(weights)
weightsEEChannelFluctuateEleSFs.extend(electronWeightsFluctuate)
weightsEEChannelFluctuateEleSFs.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(electronTriggerEEPayload)
        ),
    )

#################################################################

# MU-MU CHANNEL
weightsMuMuChannel = copy.deepcopy(weights)
weightsMuMuChannel.extend(muonWeights)
weightsMuMuChannel.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(muonTriggerMuMuPayload)
        ),
    )

weightsMuMuChannelFluctuateMuSFs = copy.deepcopy(weights)
weightsMuMuChannelFluctuateMuSFs.extend(muonWeightsFluctuate)
weightsMuMuChannelFluctuateMuSFs.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(muonTriggerMuMuPayload)
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
        inputVariable = cms.string(electronTriggerEMuPayload)
    )
)
weightsEMuChannel.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(muonTriggerEMuPayload)
    )
)

weightsEMuChannelFluctuateEleAndMuSFs = copy.deepcopy(weights)
weightsEMuChannelFluctuateEleAndMuSFs.extend(electronWeightsFluctuate)
weightsEMuChannelFluctuateEleAndMuSFs.extend(muonWeightsFluctuate)
weightsEMuChannelFluctuateEleAndMuSFs.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(electronTriggerEMuPayload)
    )
)
weightsEMuChannelFluctuateEleAndMuSFs.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(muonTriggerEMuPayload)
    )
)
