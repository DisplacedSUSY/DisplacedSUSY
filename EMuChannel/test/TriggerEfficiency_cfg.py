from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EMuChannel.TrigEfficiency import *

eventSelections = [
                   TriggerMuonPhoton38,
                   TriggerDisplacedMuonPhoton28,
                   TriggerMuonPhoton38orDisplacedMuonPhoton28,
                   #TTbarForTrigEff,
                   #TTbarForTrigEffMet,
                   #TTbarForTrigEff38,
                   #TTbarForTrigEff43,
                   #TTbarForTrigEff48,
                   #TTbarForTrigEffHighPtE,
                   #TTbarForTrigEff38HighPtE,
                   #TTbarForTrigEff43HighPtE,
                   #TTbarForTrigEff48HighPtE,
                   #TTbarForTrigEffHighPtMu,
                   #TTbarForTrigEff38HighPtMu,
                   #TTbarForTrigEff43HighPtMu,
                   #TTbarForTrigEff48HighPtMu,
                   #TTbarForTrigEff43EFilter,
                   #TTbarForTrigEff43MuFilter,
                  ]

################################################################################

# REDEFINE variableProducers, weights, scalingfactorproducers, histograms 
# to all to be empty when looking at trigger efficiency in signal

variableProducers = []

weights = cms.VPSet ()

scalingfactorproducers = []

histograms = cms.VPSet()

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################


add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers, False)

# customize the process:
# usage: customize(process, applyPUReweighting = True, applyTriggerReweighting = True, sampleType = "bgMC") 
customize (process, False, False, "data")
