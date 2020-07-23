from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.Configuration.helperFunctions import *
from DisplacedSUSY.EMuChannel.EMuHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EMuChannel.EMuSkim import *

eventSelections = []
eventSelections.append(EMuSkim)
#eventSelections.append(EMuSkimWithoutTrigger)
#eventSelections.append(EMuSkimWithOnlyL1Trigger)
#eventSelections.append(EmptySkim)

################################################################################

# REDEFINE weights, scalingfactorproducers, histograms
# to all to be empty for the skim

weights = cms.VPSet ()

scalingfactorproducers = []

histograms = cms.VPSet() #but need to make histograms for trigger study

################################################################################
##### Attach the channels to the process #######################################
################################################################################

check_definitions(eventSelections)
check_definitions(histograms)

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

# customize the process:
# usage: customize(process, analysisChannel = "emu", applyPUReweighting = True, sampleType = "bgMC")
customize (process, "emu", False, "data")
