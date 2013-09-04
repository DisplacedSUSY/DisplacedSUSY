from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *

###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

dir = "/store/user/jbrinson/TTJets_FullLeptMGDecays_8TeV-madgraph/BEAN2012-v4/0ff8045eb3a4a7ce9562dd332df0072c/"

for file in os.listdir(dir):
        process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))
        
########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################

#import the desired sets of histograms from the standard python file which defines them
from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.histogramDefinitions import *

process.OSUAnalysis.histogramSets.append(ElectronHistograms)
process.OSUAnalysis.histogramSets.append(ElectronD0Histograms)

process.OSUAnalysis.histogramSets.append(MuonHistograms)
process.OSUAnalysis.histogramSets.append(MuonD0Histograms)

process.OSUAnalysis.histogramSets.append(ElectronMuonHistograms)
process.OSUAnalysis.histogramSets.append(ElectronMuonD0Histograms)

#process.OSUAnalysis.histogramSets.append(JetHistograms)
#process.OSUAnalysis.histogramSets.append(ElectronJetHistograms)
#process.OSUAnalysis.histogramSets.append(MuonJetHistograms)

process.OSUAnalysis.histogramSets.append(EventHistograms)
process.OSUAnalysis.histogramSets.append(MetHistograms)

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisplacedSUSY.BackgroundStudies.QCDPreselections import *

#process.OSUAnalysis.channels.append(Preselection_NoIso)
#process.OSUAnalysis.channels.append(Preselection_NoIso_Prompt)

#process.OSUAnalysis.channels.append(Preselection_AntiIso)
#process.OSUAnalysis.channels.append(Preselection_AntiIso_Prompt)

process.OSUAnalysis.channels.append(Preselection_AntiIsoExtraReduced)
process.OSUAnalysis.channels.append(Preselection_AntiIsoExtraReduced_Prompt)
