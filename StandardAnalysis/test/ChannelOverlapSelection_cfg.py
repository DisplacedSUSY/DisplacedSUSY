from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.Configuration.helperFunctions import *
from DisplacedSUSY.EMuChannel.EMuHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.StandardAnalysis.ChannelOverlapSelection import *

eventSelections = []
eventSelections.append(EMuEEPreselectionOverlap)
#eventSelections.append(EMuMuMuPreselectionOverlap)
#eventSelections.append(MuMuEEPreselectionOverlap)

################################################################################
##### Attach the channels to the process #######################################
################################################################################

check_definitions(eventSelections)
check_definitions(histograms)

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

# customize the process:
# usage: customize(process, analysisChannel = "emu", applyPUReweighting = True, applyTriggerReweighting = True, sampleType = "bgMC")
customize (process, "emu", True, True, "signalMC")
