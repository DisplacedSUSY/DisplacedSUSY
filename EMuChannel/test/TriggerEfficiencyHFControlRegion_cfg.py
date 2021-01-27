from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.EMuChannel.EMuHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EMuChannel.TrigEfficiencyHFControlRegion import *

eventSelections = [

    TrigEffHFNum,
    #TrigEffHFDen,
    #TrigEffHFDenWithIso,

]

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################


add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)
#add_channels (process, eventSelections, histograms, weightsEMuChannel, scalingfactorproducers, collectionMap, variableProducers) #can apply trigger SFs when measuring trig eff in pt plateau

# customize the process:
# usage: customize(process, analysisChannel = "emu", applyPUReweighting = True, sampleType = "bgMC")
customize (process, "emu", True, "data")
