from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.EMuChannel.EMuHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EMuChannel.NewPreselection import *

eventSelections = [
    Preselection,
    #PromptControlRegion,
    #DisplacedControlRegion,
    #InclusiveSignalRegion,
    #PreselectionPromptElectron,
    #PreselectionPromptMuon,
    #PreselectionVeryPromptElectron,
    #PreselectionVeryPromptMuon,
    #PreselectionIntermediateElectron,
    #PreselectionIntermediateMuon,

    #NewPromptControlRegion,
    #NewDisplacedControlRegion,
    #NewInclusiveSignalRegion,
    #NewPreselectionPromptElectron,
    #NewPreselectionPromptMuon,
    #NewPreselectionVeryPromptElectron,
    #NewPreselectionVeryPromptMuon,
    #NewPreselectionIntermediateElectron,
    #NewPreselectionIntermediateMuon,
]

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers, True)

#FIXME: fluctuate PU weights properly
#add_channels (process, eventSelections, histograms, weightsFluctuatePileup, scalingfactorproducers, collectionMap, variableProducers, True)

# customize the process:
# usage: customize(process, applyPUReweighting = True, applyTriggerReweighting = True, sampleType = "bgMC") 
customize (process, True, True, "data")
