from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *

###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

dir = "/store/user/ahart/eMuMinimal/TTbar_Lep/EMu_Minimal"

for file in os.listdir(dir):
    process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + '/' + file))

process.OSUAnalysis.applyBtagSF = True
process.OSUAnalysis.electronSFFile  =  cms.string (os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Configuration/data/MVANonTrig_HtoZZto4l_IdIsoSip.root')
process.OSUAnalysis.electronSFID    =  cms.string ('')
process.OSUAnalysis.electronSF      =  cms.string ('h_electronScaleFactor_IdIsoSip')
#process.OSUAnalysis.applyTriggerSF  =  True
process.OSUAnalysis.applyLeptonSF  =  True
#process.OSUAnalysis.applyTrackingSF = True

########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################

#import the desired sets of histograms from the standard python file which defines them
from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.histogramDefinitions import *

process.OSUAnalysis.histogramSets.append(MuonD0Histograms)
#process.OSUAnalysis.histogramSets.append(JetHistograms)
#process.OSUAnalysis.histogramSets.append(ElectronJetHistograms)
process.OSUAnalysis.histogramSets.append(EventHistograms)
#process.OSUAnalysis.histogramSets.append(MetHistograms)

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisplacedSUSY.BackgroundStudies.BbBarControlRegions import *
process.OSUAnalysis.channels.append(BbBar_Muon_Selection_NoIso)


