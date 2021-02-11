from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.EMuChannel.EMuHistograms import *
from DisplacedSUSY.EMuChannel.localOptions import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.StandardAnalysis.BasicSelections import *

eventSelections = [
    NoSelection,

    #bothStopRhadronsAre1000612,
    #bothStopRhadronsAre1000622,
    #bothStopRhadronsAre1000632,
    #stopRhadron1000612or1000622,
    #stopRhadron1000612or1000632,
    #stopRhadron1000622or1000632,
    #stopRhadronEverythingElse,
]

################################################################################
##### Attach the channels to the process #######################################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers,branchSets=emuBranchSets)
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

# customize the process:
# usage: customize(process, analysisChannel = "emu", applyPUReweighting = True, applyTriggerReweighting = True, sampleType = "bgMC")
customize (process, analysisChannel, True, "signalMC")
