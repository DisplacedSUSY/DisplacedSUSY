from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.EMuChannel.EMuHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EMuChannel.NewPreselection import *
from DisplacedSUSY.EMuChannel.PreselectionWithExplicitEleId import *

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

    #PreselectionWithExplicitEleIdBarrel,
    #PreselectionWithExplicitEleIdEndcap,

    #PreselectionCorrelatedD0,
    #PreselectionUncorrelatedD0,
    #PreselectionCorrelatedGenD0,
    #PreselectionUncorrelatedGenD0,

    #PreselectionLeptonsFromW,
]

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)

#FIXME: fluctuate PU weights properly
#add_channels (process, eventSelections, histograms, weightsFluctuatePileup, scalingfactorproducers, collectionMap, variableProducers, True)

# customize the process:
# usage: customize(process, analysisChannel = "emu", applyPUReweighting = True, applyTriggerReweighting = True, sampleType = "bgMC")
customize (process, "emu", True, True, "bgMC")
