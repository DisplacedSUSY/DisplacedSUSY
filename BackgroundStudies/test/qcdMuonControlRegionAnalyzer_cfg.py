from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *

###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

dir = "/store/user/jbrinson/TTJets_FullLeptMGDecays_8TeV-madgraph/BEAN2012-v4/0ff8045eb3a4a7ce9562dd332df0072c/"

for file in os.listdir(dir):
        process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))
        
process.OSUAnalysis.applyBtagSF = True

########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################

#import the desired sets of histograms from the standard python file which defines them
from OSUT3Analysis.Configuration.histogramDefinitions import *

process.OSUAnalysis.histogramSets.append(MuonHistograms)
process.OSUAnalysis.histogramSets.append(JetHistograms)
process.OSUAnalysis.histogramSets.append(MuonJetHistograms)
process.OSUAnalysis.histogramSets.append(EventHistograms)
process.OSUAnalysis.histogramSets.append(MetHistograms)

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisplacedSUSY.BackgroundStudies.QCDControlRegions import *
process.OSUAnalysis.channels.append(QCD_Muon_ControlRegion)










