from DisplacedSUSY.StandardAnalysis.protoConfig_cfg import *
from DisplacedSUSY.StandardAnalysis.customize import *
from DisplacedSUSY.EMuChannel.EMuHistograms import *

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisplacedSUSY.EMuChannel.Preselection import *
from DisplacedSUSY.EMuChannel.PreselectionWithExplicitEleId import *

eventSelections = [
    Preselection,
    #PromptControlRegion,
    #DisplacedControlRegion,
    #MuonD00to40ElectronD00to100Region,
    #MuonD00to40ElectronD0100to500Region,
    #MuonD00to40ElectronD0500to1000Region,
    #ElectronD00to40MuonD00to100Region,
    #ElectronD00to40MuonD0100to500Region,
    #ElectronD00to40MuonD00to40Region,
    #ElectronD00to40MuonD040to500Region,
    #ElectronD00to40MuonD0500to1000Region,
    #PromptLowPtControlRegion,
    #PromptHighPtControlRegion,
    #DisplacedLowPtControlRegion,
    #DisplacedHighPtControlRegion,
    #InclusiveSignalRegion,
    #pfBetaIsoCorrPreselection,
    #AntiIsoPreselection,
    #AntiIsoPromptElectronDisplacedMuonRegion,
    #AntiIsoPromptMuonDisplacedElectronRegion,
    #PreselectionElectronBarrel,
    #PreselectionElectronEndcap,

    #PreselectionWithExplicitEleIdBarrel,
    #PreselectionWithExplicitEleIdEndcap,

    #PreselectionCorrelatedD0,
    #PreselectionUncorrelatedD0,
    #PreselectionCorrelatedGenD0,
    #PreselectionUncorrelatedGenD0,

    #PreselectionLeptonsFromW,
    #PreselectionLeptonsFromWorZ,
    #PreselectionLeptonsNotFromTau,
    #PreselectionMuFromTau,
    #PreselectionEFromTau,
    #PreselectionMuFromWorZ,
    #PreselectionEFromWorZ,
    #Preselection2TausFromZ,
    #PreselectionMuFromLightMeson,
    #PreselectionMuFromHeavyMeson,
    #PreselectionEFromLightMeson,
    #PreselectionEFromHeavyMeson,
    #PreselectionEOrMuFromHeavyMeson,

    #GenEMuFromStopsSelection,
    #GenEMuFromStopsEleSelection,
    #GenEMuFromStopsMuSelection,
    #GenEMuFromStopsEleAndHLTTrigSelection,
    #GenEMuFromStopsMuAndHLTTrigSelection,
    #GenEMuFromStopsEleAndL1TrigSelection,
    #GenEMuFromStopsMuAndL1TrigSelection,
]

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, eventSelections, histograms, weightsEMuChannel, scalingfactorproducers, collectionMap, variableProducers, branchSets=emuBranchSets)
#add_channels (process, eventSelections, histograms, weightsFluctuatePileup, scalingfactorproducers, collectionMap, variableProducers, branchSets=emuBranchSets)
#add_channels (process, eventSelections, histograms, weightsEMuChannelFluctuateEleAndMuSFs, scalingfactorproducers, collectionMap, variableProducers, branchSets=emuBranchSets)

# customize the process:
# usage: customize(process, analysisChannel = "emu", applyPUReweighting = True, sampleType = "bgMC")
customize (process, "emu", True, "bgMC")
