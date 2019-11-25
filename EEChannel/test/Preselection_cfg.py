from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.EEChannel.EEHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EEChannel.Preselection import *

eventSelections = [
    Preselection,
    #PreselectionLooseIsoCutBTagVeto,
    #PromptControlRegion,
    #DisplacedControlRegion,
    #PromptLowPtControlRegion,
    #PromptHighPtControlRegion,
    #DisplacedLowPtControlRegion,
    #DisplacedHighPtControlRegion,
    #ZControlRegion,
    #InclusiveSignalRegion,
    #PreselectionLeptonsFromW,
    #DisplacedHighPtL1PrefiringCheck,
    #GenEEFromStopsSelection,
    ]

# Redefine scalingfactorproducers to not include muon scale factors
scalingfactorproducers = []
scalingfactorproducers.append(ElectronScaleFactorProducer)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)

# customize the process:
# usage: customize(process, analysisChannel = "ee", applyPUReweighting = True, applyTriggerReweighting = True)
customize (process, "ee", True, True, "data")
