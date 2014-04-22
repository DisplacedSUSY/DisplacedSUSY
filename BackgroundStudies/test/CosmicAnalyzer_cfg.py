from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from OSUT3Analysis.Configuration.processingUtilities import *

###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################


#dir = "/store/user/ahart/DYToTauTau_M-20_CT10_TuneZ2star_v2_8TeV-powheg-tauola-pythia6/BEAN2012-v4/4a12a6f1b79fbeb9915fe6064a3d6fce/"
#dir = "/mnt/hadoop/se/store/user/ahart/eMuMinimal_new/stop200toBl_10mm/EMu_Minimal"

dir = "/mnt/hadoop/se/store/user/qpython/CosmicSkimer/DYToMuMu_20/LooseCosmic_No_TightId"

for file in os.listdir(dir):
    process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + '/' + file))

#process.source.fileNames.extend(cms.untracked.vstring('file:/home/lantonel/CMSSW_6_1_2/src/DisplacedSUSY/StandardAnalysis/test/signalRegionEvents.root'))

######################################################################
##### Overwrite specific variables defined in osuAnalysis_cfi.py #####
######################################################################

process.OSUAnalysis.electronSFFile  =  cms.string (os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Configuration/data/MVANonTrig_HtoZZto4l_IdIsoSip.root')
process.OSUAnalysis.electronSFID    =  cms.string ('')
process.OSUAnalysis.electronSF      =  cms.string ('h_electronScaleFactor_IdIsoSip')
process.OSUAnalysis.applyTriggerSF  =  True
process.OSUAnalysis.applyTrackingSF =  True
process.OSUAnalysis.applyLeptonSF   =  True

#process.maxEvents = cms.untracked.PSet (
#    input = cms.untracked.int32 (10)
#    )

########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################

#import the desired sets of histograms from the standard python file which defines them
from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.cosmicHistogramDefinitions  import *

process.OSUAnalysis.histogramSets.append(CosmicDiMuonHistograms)
process.OSUAnalysis.histogramSets.append(CosmicMuonHistograms)

process.OSUAnalysis.histogramSets.append(MuonHistograms)
process.OSUAnalysis.histogramSets.append(MuonD0Histograms)

process.OSUAnalysis.histogramSets.append(DiMuonHistograms)

process.OSUAnalysis.histogramSets.append(EventHistograms)

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

#from DisplacedSUSY.StandardAnalysis.Preselection import *
from DisplacedSUSY.BackgroundStudies.CosmicEventSelection import *



process.OSUAnalysis.channels.append(LooseCosmic_No_TightId)
process.OSUAnalysis.channels.append(OnZPeak)
process.OSUAnalysis.channels.append(CosmicTight)
process.OSUAnalysis.channels.append(OffZPeak)





# to add a tree with cut -> skim
#add_channels(process, [LooseCosmic_No_TightId]) 
