from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.MuMuChannel.TrigEfficiency import *

eventSelections = [TriggerDoubleMu33, TriggerDoubleMu23Displaced, TriggerDoubleMu33ORDoubleMu23Displaced]

################################################################################

# REDEFINE variableProducers, weights, scalingfactorproducers, histograms 
# to all to be empty for the trigger efficiency calculation on signal

histograms = cms.VPSet()
weights = cms.VPSet()
scalingfactorproducers = []
variableProducers = []

################################################################################
##### Attach the channels to the process #######################################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers, True)
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

# customize the process:
# usage: customize(process, analysisChannel = "mumu", applyPUReweighting = True, applyTriggerReweighting = True)
customize (process, "mumu", False, False, "data")
