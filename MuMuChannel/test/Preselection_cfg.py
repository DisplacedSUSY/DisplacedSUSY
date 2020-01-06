from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.MuMuChannel.MuMuHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.MuMuChannel.Preselection import *

eventSelections = [
    Preselection,
    #AdditionalPreselection,
    #PreselectionNoIsoCut,
    #PreselectionVeryLooseIsoCut,
    #PreselectionBTagVeto,
    #PreselectionVeryLooseIsoCutBTagVeto,
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
    #puScalingFactorNegative,
    #lifetimeWeightNegative,
    #GenMuMuFromStopsSelection,
    #GenMuMuFromZSelection,
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

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)

# customize the process:
# usage: customize(process, analysisChannel = "mumu", applyPUReweighting = True, applyTriggerReweighting = True)
customize (process, "mumu", True, True, "data")
