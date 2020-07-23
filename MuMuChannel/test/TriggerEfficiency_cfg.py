from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.Configuration.helperFunctions import *
from DisplacedSUSY.MuMuChannel.MuMuHistograms import *


from DisplacedSUSY.MuMuChannel.TrigEfficiency import *

eventSelections = [
    TrigEffNum,
    TrigEffDen,
]

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

# Redefine scalingfactorproducers to not include electron scale factors
scalingfactorproducers = []
scalingfactorproducers.append(MuonScaleFactorProducer)

check_definitions(eventSelections)
check_definitions(histograms)

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)

# customize the process:
# usage: customize(process, analysisChannel = "emu", applyPUReweighting = True, sampleType = "bgMC")
customize (process, "mumu", True, "data")
