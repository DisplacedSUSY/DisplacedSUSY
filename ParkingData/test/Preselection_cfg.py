from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.ParkingData.ParkingDataHistograms import *

#######################################
#### Import the channels to be run ####
#######################################

from DisplacedSUSY.ParkingData.Preselection import *

eventSelections = [
    #triggerSelection,
    #pTselection,
    #etaSelection,
    #globalCutSelection,
    #idSelection,
    #isoSelection,
    #MuMuPreselection,
    ParkingPreselection,
    ]

#######################################

# REDIFINE variableProducers, weights, scalingfactorproducers,
# histograms to all to be empty for the skim

#variableProducers = []

weights = cms.VPSet()

scalingfactorproducers = []

############################################
#### Attach the channels to the process ####
############################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)

# customize the process:
customize (process, "mumu", True, False, "signal")
