from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EEChannel.EESkim import *

eventSelections = []
eventSelections.append(EESkim)

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

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers, True)
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

# customize the process:
# usage: customize(process, applyPUReweighting = True, applyTriggerReweighting = True)
customize (process, False, False)
