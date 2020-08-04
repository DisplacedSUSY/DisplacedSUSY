from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.MuMuChannel.MuMuHistograms import *


from DisplacedSUSY.MuMuChannel.TrigEfficiency import *

eventSelections = [
    TrigEffNum,
    #TrigEffDen,

    #TrigEffNumInPtPlateau,
    #TrigEffDenInPtPlateau,
]

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

# Redefine scalingfactorproducers to not include electron scale factors
scalingfactorproducers = []
scalingfactorproducers.append(MuonScaleFactorProducer)

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)
#add_channels (process, eventSelections, histograms, weightsMuMuChannel, scalingfactorproducers, collectionMap, variableProducers) #can apply trigger SFs when measuring trig eff in pt plateau

# customize the process:
# usage: customize(process, analysisChannel = "emu", applyPUReweighting = True, sampleType = "bgMC")
customize (process, "mumu", True, "data")
