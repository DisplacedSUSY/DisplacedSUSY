from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.EEChannel.EEHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EEChannel.TrigEfficiency import *

eventSelections = [
    TrigEffNum,
    #TrigEffDen,

    #TrigEffNumInPtPlateau,
    #TrigEffDenInPtPlateau,
]

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

# Redefine scalingfactorproducers to not include muon scale factors
scalingfactorproducers = []
scalingfactorproducers.append(ElectronScaleFactorProducer)

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)
#add_channels (process, eventSelections, histograms, weightsEEChannel, scalingfactorproducers, collectionMap, variableProducers) #can apply trigger SFs when measuring trig eff in pt plateau

# customize the process:
# usage: customize(process, analysisChannel = "ee", applyPUReweighting = True)
customize (process, "ee", True, "data")
