from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.MuMuChannel.MuMuHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.MuMuChannel.Preselection import *

eventSelections = [
    Preselection,
    #PromptControlRegion,
    #AntiIsoPromptControlRegion,
    #DisplacedControlRegion,
    #AntiIsoDisplacedControlRegion,
    #ZControlRegion,
    ]

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers, True)

# customize the process:
# usage: customize(process, applyPUReweighting = True, applyTriggerReweighting = True) 
customize (process, True, True, "data")
