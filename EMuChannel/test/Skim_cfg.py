from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EMuChannel.EMuSkim import *

eventSelections = []
eventSelections.append(EMuSkim)
#eventSelections.append(EMuSkimWithoutTrigger)
#eventSelections.append(EmptySkim)

################################################################################

# REDEFINE variableProducers, weights, scalingfactorproducers, histograms
# to all to be empty for the skim

variableProducers = []

weights = cms.VPSet ()

scalingfactorproducers = []

histograms = cms.VPSet()

################################################################################
##### Attach the channels to the process #######################################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

# customize the process:
# usage: customize(process, analysisChannel = "emu", applyPUReweighting = True, applyTriggerReweighting = True, sampleType = "bgMC")
customize (process, "emu", False, False, "data")
