from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.Configuration.helperFunctions import *
from DisplacedSUSY.BackgroundStudies.QCDHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.BackgroundStudies.QCDMuonControlRegionSelections import *

eventSelections = [
    QCDMuonControlRegion,
    #QCDIsoMuonControlRegion,
    #QCDAntiIsoMuonControlRegion,
]

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

check_definitions(eventSelections)
check_definitions(histograms)

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)

#FIXME: fluctuate PU weights properly
#add_channels (process, eventSelections, histograms, weightsFluctuatePileup, scalingfactorproducers, collectionMap, variableProducers, True)

# customize the process:
# usage: customize(process, analysisChannel = "emu", applyPUReweighting = True, applyTriggerReweighting = True, sampleType = "bgMC")
customize (process, "emu", True, True, "data")
