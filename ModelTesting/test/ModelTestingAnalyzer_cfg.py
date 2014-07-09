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

###!!!!
#on the following dir the job is running decently fast but it is not the default dir chosen when lauhcing condor jobs
###!!!!
dir="/store/user/ahart/BN_stop200ToBottom_1.00mm_8TeV-pythia6_Summer12-START52_V9-v2_ahart-stop200ToBottom_1.00mm_TuneZ2star_8TeV-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v3-e542883f7d1b22c1f30ae55768bc52e5_USER_0/"
###
#dir="/mnt/hadoop/se/store/user/ahart/BN_stopToBottom_M_200_1mm_Tune4C_8TeV_pythia8_biliu-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_1/"

for file in os.listdir(dir):
            process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + '/' + file))

#process.source.fileNames.extend(cms.untracked.vstring('file:/store/user/ahart/eMuMinimal/stop300toTnu_50.0mm/EMu_Minimal/bean_0.root'))

#######################################################################
##### Import the information about all the histograms to be filled #####
########################################################################

#import the desired sets of histograms from the standard python file which defines them
from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.histogramDefinitions import *

#process.OSUAnalysis.histogramSets.append(ElectronHistograms)
#process.OSUAnalysis.histogramSets.append(ElectronD0Histograms)
## process.OSUAnalysis.histogramSets.append(ConversionHistograms)

process.OSUAnalysis.histogramSets.append(MCParticleHistograms)
process.OSUAnalysis.histogramSets.append(SecondaryMCParticleHistograms)



#process.OSUAnalysis.histogramSets.append(MuonHistograms)
#process.OSUAnalysis.histogramSets.append(MuonD0Histograms)

#process.OSUAnalysis.histogramSets.append(ElectronMuonHistograms)
#process.OSUAnalysis.histogramSets.append(ElectronMuonD0Histograms)

#process.OSUAnalysis.histogramSets.append(JetHistograms)
#process.OSUAnalysis.histogramSets.append(ElectronJetHistograms)
#process.OSUAnalysis.histogramSets.append(MuonJetHistograms)



## #process.OSUAnalysis.histogramSets.append(PhotonHistograms)
## #process.OSUAnalysis.histogramSets.append(ElectronPhotonHistograms)
## #process.OSUAnalysis.histogramSets.append(MuonPhotonHistograms)

#process.OSUAnalysis.histogramSets.append(MetHistograms)
#process.OSUAnalysis.histogramSets.append(EventHistograms)

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

#from DisplacedSUSY.StandardAnalysis.ModelTestingSelections import *
from DisplacedSUSY.ModelTesting.ModelTestingSelections import *

#from DisplacedSUSY.BackgroundStudies.QCDPreselections import *

#from DisplacedSUSY.StandardAnalysis.SignalSelections import *


### MC particles selection for eta range Technical proposal study
#process.OSUAnalysis.channels.append(Mc_muon)
#process.OSUAnalysis.channels.append(Mc_electron)

#process.OSUAnalysis.channels.append(Preselection_SignalGenMatching_500umMuon)
### Empty selection
process.OSUAnalysis.channels.append(SignalGenMatching_KynCuts_CrossCuts)#1
#"""
process.OSUAnalysis.channels.append(SignalGenMatching_KynCuts_CrossCuts_oneRecoEl)#2a
process.OSUAnalysis.channels.append(SignalGenMatching_KynCuts_CrossCuts_oneRecoMu)#2b
process.OSUAnalysis.channels.append(SignalGenMatching_KynCuts_CrossCuts_oneRecoEl_Electron_cuts)#3a
process.OSUAnalysis.channels.append(SignalGenMatching_KynCuts_CrossCuts_oneRecoMu_Muon_cuts)#3b
#"""
"""
process.OSUAnalysis.channels.append(Preselection_SignalGenMatching_NoTrigger)
process.OSUAnalysis.channels.append(Preselection_SignalGenMatching)
process.OSUAnalysis.channels.append(Preselection_SignalGenMatching_200umElectron)
process.OSUAnalysis.channels.append(Preselection_SignalGenMatching_200umMuon)
process.OSUAnalysis.channels.append(Preselection_SignalGenMatching_500umElectron)
process.OSUAnalysis.channels.append(Preselection_SignalGenMatching_500umMuon)
process.OSUAnalysis.channels.append(Preselection_SignalGenMatching_1000umElectron)
process.OSUAnalysis.channels.append(Preselection_SignalGenMatching_1000umMuon)
"""
### skim example
#add_channels(process, [SignalGenMatching_KynCuts_CrossCuts])
