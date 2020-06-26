from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.EMuChannel.EMuHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EMuChannel.TrigEfficiency import *

eventSelections = [
    TrigEffHighPtEleNum,
    TrigEffHighPtEleDen,

    #TrigEffHighPtMuNum,
    #TrigEffHighPtMuDen,
]

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################


add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)

# customize the process:
# usage: customize(process, analysisChannel = "emu", applyPUReweighting = True, applyTriggerReweighting = True, sampleType = "bgMC")
customize (process, "emu", True, False, "data")
