from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *

variableProducers = []

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EEChannel.EESkim import *

eventSelections = []
eventSelections.append(EESkim)

weights = cms.VPSet ()

scalingfactorproducers = []
################################################################################
##### Import the histograms to be plotted ######################################
################################################################################
histograms = cms.VPSet()


################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers, True)
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

# usage: customize(process, applyPUReweighting = True, applyTriggerReweighting = True)
customize (process, False, False)
