from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.EEChannel.EEHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EEChannel.TrigEfficiency import *

eventSelections = [
		   # triggerDoublePhoton30orDoublePhoton60, # EE trigger
                   trigMETandEEtrig, 
                   trigMET,
		   TTbarForTrigEffNoTrig,
                   trigMETandEEtrigTagElectron,
                   trigMETTagElectron,
	           TTbarForHLTDiphoton30,
	           TTbarForHLTDoublePhoton60,
	           TTbarForHLTDiphoton30eTag,
	           TTbarForHLTDoublePhoton60eTag,
                  ]

################################################################################

# REDEFINE variableProducers, weights, scalingfactorproducers, histograms 
# to all to be empty for the trigger efficiency calculation in signal

# histograms = cms.VPSet()
weights = cms.VPSet()
scalingfactorproducers = []
variableProducers = []
variableProducers.append('DisplacedSUSYEventVariableProducer')

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers)

# customize the process:
# usage: customize(process, analysisChannel = "ee", applyPUReweighting = True, applyTriggerReweighting = True)
customize (process, "ee", False, False, "data")
