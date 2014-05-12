from DisplacedSUSY.StandardAnalysis.displacedSUSY_cfi import *
from OSUT3Analysis.Configuration.processingUtilities import *

###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################


#dir = "/store/user/ahart/DYToTauTau_M-20_CT10_TuneZ2star_v2_8TeV-powheg-tauola-pythia6/BEAN2012-v4/4a12a6f1b79fbeb9915fe6064a3d6fce/"
#dir = "/mnt/hadoop/se/store/user/ahart/eMuMinimal_new/WW/EMu_Minimal"
#dir = "./condor/eMuMinimal/DYToTauTau_20/EMu_Minimal"
#for file in os.listdir(dir):
#    process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + '/' + file))

process.source.fileNames.extend(cms.untracked.vstring('file:/store/user/ahart/EMuSkim/DYToTauTau_20/EMu_Skim/bean_0.root'))



#######################################################################
##### Import the information about all the histograms to be filled #####
########################################################################

#import the desired sets of histograms from the standard python file which defines them
from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.histogramDefinitions import *

process.OSUAnalysis.histogramSets.append(ElectronHistograms)
process.OSUAnalysis.histogramSets.append(ElectronD0Histograms)
## process.OSUAnalysis.histogramSets.append(ConversionHistograms)

process.OSUAnalysis.histogramSets.append(MuonHistograms)
process.OSUAnalysis.histogramSets.append(MuonD0Histograms)

process.OSUAnalysis.histogramSets.append(ElectronMuonHistograms)
process.OSUAnalysis.histogramSets.append(ElectronMuonD0Histograms)

process.OSUAnalysis.histogramSets.append(JetHistograms)
process.OSUAnalysis.histogramSets.append(ElectronJetHistograms)
process.OSUAnalysis.histogramSets.append(MuonJetHistograms)

## #process.OSUAnalysis.histogramSets.append(PhotonHistograms)
## #process.OSUAnalysis.histogramSets.append(ElectronPhotonHistograms)
## #process.OSUAnalysis.histogramSets.append(MuonPhotonHistograms)

process.OSUAnalysis.histogramSets.append(MetHistograms)
process.OSUAnalysis.histogramSets.append(EventHistograms)

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisplacedSUSY.StandardAnalysis.Preselection import *
#from DisplacedSUSY.BackgroundStudies.QCDPreselections import *

#from DisplacedSUSY.StandardAnalysis.SignalSelections import *

process.OSUAnalysis.channels.append(Blinded_Preselection)
#process.OSUAnalysis.channels.append(Preselection)
#process.OSUAnalysis.channels.append(Signal_Selection_200um)
#process.OSUAnalysis.channels.append(Signal_Selection_500um)
#process.OSUAnalysis.channels.append(Signal_Selection_1000um)


#process.OSUAnalysis.channels.append(Preselection_100um) # B

#add_channels(process, [Preselection])

#process.OSUAnalysis.channels.append(Blinded_Preselection)
#process.OSUAnalysis.channels.append(Preselection_real_electron)
#process.OSUAnalysis.channels.append(Preselection_fake_electron)
#process.OSUAnalysis.channels.append(Empty_Selection)
#process.OSUAnalysis.channels.append(Preselection_100um_SS) # A
#process.OSUAnalysis.channels.append(Preselection_100um_AntiIso) # D
#process.OSUAnalysis.channels.append(Preselection_100um_AntiIso_SS) # C
#process.OSUAnalysis.channels.append(Preselection_AntiIso) # D
#process.OSUAnalysis.channels.append(Preselection_AntiIso_SS) # C

## add_channels(process, [MuonPromptElectronNonPrompt_Preselection])
## add_channels(process, [MuonPromptElectronNonPrompt_Preselection_SS])
## add_channels(process, [MuonPromptElectronNonPrompt_Preselection_AntiIso])
## add_channels(process, [MuonPromptElectronNonPrompt_Preselection_SS_AntiIso])

## add_channels(process, [ElectronPromptMuonNonPrompt_Preselection])
## add_channels(process, [ElectronPromptMuonNonPrompt_Preselection_SS])
## add_channels(process, [ElectronPromptMuonNonPrompt_Preselection_AntiIso])
## add_channels(process, [ElectronPromptMuonNonPrompt_Preselection_SS_AntiIso])

#process.OSUAnalysis.channels.append(MuonPromptElectronNonPrompt_Preselection_NoID)
#process.OSUAnalysis.channels.append(MuonPromptElectronNonPrompt_Preselection_NoConvVeto)

#process.OSUAnalysis.channels.append(ElectronPromptMuonNonPrompt_Preselection)
#process.OSUAnalysis.channels.append(ElectronPromptMuonNonPrompt_Preselection_NoID)

#add_channels(process, [Preselection])
