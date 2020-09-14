from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.MuMuChannel.MuMuHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.MuMuChannel.MuMuSkim import *

eventSelections = []
eventSelections.append(MuMuSkim)
#eventSelections.append(MuMuSkimWithoutTrigger)
#eventSelections.append(MuMuSkimWithOnlyL1Trigger)
#eventSelections.append(EmptySkim)
#eventSelections.append(CosmicsSelection)
################################################################################

# REDEFINE weights, scalingfactorproducers, histograms
# to all to be empty for the skim

weights = cms.VPSet ()

scalingfactorproducers = []

histograms = cms.VPSet() #but need to make histograms for trigger study

################################################################################
##### Attach the channels to the process #######################################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)
#add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMapAOD, variableProducers)
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

# customize the process:
# usage: customize(process, analyisChannel = "mumu", applyPUReweighting = True, sampleType = "bgMC")
customize (process, "mumu", False, "data")
