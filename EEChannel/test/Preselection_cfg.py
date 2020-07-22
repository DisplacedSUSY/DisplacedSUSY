from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.EEChannel.EEHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EEChannel.Preselection import *

eventSelections = [
    Preselection,
    #ElectronD00to40ElectronD0Above100Region,
    #ElectronD00to40ElectronD00to100Region,
    #ElectronD00to40ElectronD0100to500Region,
    #ElectronD00to40ElectronD0500to1000Region,
    #AdditionalPreselection,
    #PreselectionLooseIsoCutBTagVeto,
    #PromptControlRegion,
    #DisplacedControlRegion,
    #PromptLowPtControlRegion,
    #PromptHighPtControlRegion,
    #DisplacedLowPtControlRegion,
    #DisplacedHighPtControlRegion,
    #DisplacedGreaterThan100,
    #ZControlRegion,
    #InclusiveSignalRegion,
    #PreselectionLeptonsFromW,
    #PreselectionLeptonsFromWorZ,
    #PreselectionLeptonsFromTau,
    #Preselection2TausFromZ,
    #PreselectionEleFromLightMeson,
    #PreselectionEleFromHeavyMeson,
    #DisplacedHighPtL1PrefiringCheck,
    #GenEEFromStopsSelection,
    #GenEEFromStopsAndHLTTrigSelection,
    #GenEEFromStopsAndL1TrigSelection,
    ]

# Redefine scalingfactorproducers to not include muon scale factors
scalingfactorproducers = []
scalingfactorproducers.append(ElectronScaleFactorProducer)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weightsEEChannel, scalingfactorproducers, collectionMap, variableProducers)

# customize the process:
# usage: customize(process, analysisChannel = "ee", applyPUReweighting = True, sampleType = "bgMC")
customize (process, "ee", True, "data")
