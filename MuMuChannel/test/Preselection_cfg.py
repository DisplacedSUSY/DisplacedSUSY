from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.MuMuChannel.MuMuHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.MuMuChannel.Preselection import *

eventSelections = [
    Preselection,
    #CosmicsAdditionalPreselection,
    #MuonD00to40MuonD00to100Region,
    #MuonD00to40MuonD0100to500Region,
    #MuonD00to40MuonD0500to1000Region,
    #AdditionalPreselection,
    #GenPromptRegion,
    #etaLessThan1GenPromptRegion,
    #pT50to60GenPromptRegion,
    #pTGreaterThan150GenPromptRegion,
    #PromptRegion,
    #PreselectionNoIsoCut,
    #pfBetaIsoCorrPreselection,
    #PreselectionBTagVeto,
    #PromptControlRegion,
    #AntiIsoPromptControlRegion,
    #DisplacedControlRegion,
    #AntiIsoDisplacedControlRegion,
    #PromptLowPtControlRegion,
    #PromptHighPtControlRegion,
    #DisplacedLowPtControlRegion,
    #DisplacedHighPtControlRegion,
    #PromptLowPtControlRegionNoIsoCut,
    #PromptHighPtControlRegionNoIsoCut,
    #DisplacedLowPtControlRegionNoIsoCut,
    #DisplacedHighPtControlRegionNoIsoCut,
    #PromptLowPtControlRegionLowEta,
    #PromptHighPtControlRegionLowEta,
    #DisplacedLowPtControlRegionLowEta,
    #DisplacedHighPtControlRegionLowEta,
    #PromptLowPtControlRegionHighEta,
    #PromptHighPtControlRegionHighEta,
    #DisplacedLowPtControlRegionHighEta,
    #DisplacedHighPtControlRegionHighEta,
    #ZControlRegion,
    #InclusiveSignalRegion,
    #PreselectionLeptonsFromW,
    #PreselectionLeptonsFromWorZ,
    #PreselectionLeptonsFromTau,
    #Preselection1LeptonFromTau,
    #Preselection2LeptonsFromTau,
    #Preselection2TausFromZ,
    #PreselectionMuFromLightMeson,
    #PreselectionMuFromHeavyMeson,
    #puScalingFactorNegative,
    #lifetimeWeightNegative,
    #GenMuMuFromStopsSelection,
    #GenMuMuFromZSelection,
    #GenMuMuFromStopsAndHLTTrigSelection,
    #GenMuMuFromStopsAndL1TrigSelection,
    #PreselectionOneLessThan40umOneGreaterThan100um,
    #PreselectionPromptMuonDisplacedTagMuon100um,
    #PreselectionPromptTagMuonDisplacedMuon100um,
    #PreselectionPromptMuonDisplacedTagMuon500um,
    ]

# Redefine scalingfactorproducers to not include electron scale factors
scalingfactorproducers = []
scalingfactorproducers.append(MuonScaleFactorProducer)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weightsMuMuChannel, scalingfactorproducers, collectionMap, variableProducers)

# customize the process:
# usage: customize(process, analysisChannel = "mumu", applyPUReweighting = True, sampleType = "bgMC")
customize (process, "mumu", True, "signalMC")
