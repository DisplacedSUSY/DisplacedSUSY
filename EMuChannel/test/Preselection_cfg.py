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
    #AdditionalPreselection,
    #PromptControlRegion,
    #DisplacedControlRegion,
    #MuonD00to40ElectronD00to100Region,
    #MuonD00to40ElectronD0100to500Region,
    #MuonD00to40ElectronD0500to1000Region,
    #ElectronD00to40MuonD00to100Region,
    #ElectronD00to40MuonD0100to500Region,
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
    #PreselectionMuFromTau,
    #PreselectionEFromTau,
    #PreselectionMuFromWorZ,
    #Preselection2TausFromZ,

    #GenEMuFromStopsSelection,
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
