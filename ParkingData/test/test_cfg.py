from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.ParkingData.ParkingDataHistograms import *

#######################################
#### Import the channels to be run ####
#######################################

from DisplacedSUSY.ParkingData.ParkingDataTest import *

eventSelections = [
    ParkingDataTest,
    promptMuons,
    displacedMuons,
    ]

#######################################

# REDIFINE variableProducers, weights, scalingfactorproducers,
# histograms to all to be empty for the skim

variableProducers = []

weights = cms.VPSet()

scalingfactorproducers = []

############################################
#### Attach the channels to the process ####
############################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)

# customize the process:
customize (process, "mumu", False, False, "data")
