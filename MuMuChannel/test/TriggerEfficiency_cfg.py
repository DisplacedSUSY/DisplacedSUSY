from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.MuMuChannel.MuMuHistograms import *


################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.MuMuChannel.TTbarForTrigEff import *

eventSelections = [
                   TTbarForTrigEffNoTrig,
                   TTbarForTrigEff43,
                   TTbarForTrigEff48,
                   TTbarForTrigEffTagMuonNoTrig,
                   TTbarForTrigEffTagMuon43,
                   TTbarForTrigEffTagMuon48,
                   #TTbarForTrigEffVeto43,
                  ]


################################################################################

# REDEFINE variableProducers, weights, scalingfactorproducers
# to all to be empty for the trigger efficiency calculation
# keep default mumu histograms though

variableProducers = []
variableProducers.append('DisplacedSUSYEventVariableProducer')

weights = cms.VPSet ()

scalingfactorproducers = []


################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collectionMap, variableProducers, True)

# customize the process:
# usage: customize(process, applyPUReweighting = True, applyTriggerReweighting = True) 
customize (process, False, False, "data")
