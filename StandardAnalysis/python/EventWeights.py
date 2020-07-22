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
