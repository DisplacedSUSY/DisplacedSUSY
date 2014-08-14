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


### block of gen level histograms
#"""
process.OSUAnalysis.histogramSets.append(MCParticleHistograms)
process.OSUAnalysis.histogramSets.append(SecondaryMCParticleHistograms)
process.OSUAnalysis.histogramSets.append(MCParticleDrJetHistogram)
process.OSUAnalysis.histogramSets.append(SecondaryMCParticleDrJetHistogram)
#"""


### block of reco level histograms
"""
process.OSUAnalysis.histogramSets.append(MuonHistograms)
process.OSUAnalysis.histogramSets.append(ElectronHistograms)
"""

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

#from DisplacedSUSY.StandardAnalysis.ModelTestingSelections import *
#from DisplacedSUSY.ModelTesting.ModelTestingSelections import *
from DisplacedSUSY.ModelTesting.ModelTestingSelections_short import *
from DisplacedSUSY.ModelTesting.CheckRecoEffSelections import *

# for standard Preselection
from DisplacedSUSY.StandardAnalysis.Preselection import *



### ModelTesting block. Create the 6 necessary channel to make the reweighting histograms
#"""
process.OSUAnalysis.channels.append(McPartInitial)
process.OSUAnalysis.channels.append(McPartInitial_OneRecoEl)
process.OSUAnalysis.channels.append(McPartInitial_OneRecoEl_Electron_cuts)
process.OSUAnalysis.channels.append(SecondaryMcPartInitial)
process.OSUAnalysis.channels.append(SecondaryMcPartInitial_OneRecoMu)
process.OSUAnalysis.channels.append(SecondaryMcPartInitial_OneRecoMu_Muon_cuts)
#"""



#process.OSUAnalysis.channels.append(Preselection)
#process.OSUAnalysis.channels.append(Preselection_GenLevel)
#process.OSUAnalysis.channels.append(Preselection_GenLevel_test)

### Different signal region block  
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


### Check reco efficiency block
"""
process.OSUAnalysis.channels.append(McPartMatchedToSignal)
process.OSUAnalysis.channels.append(McPartMatchedToSignal_OneRecoEl)
process.OSUAnalysis.channels.append(SecondaryMcPartMatchedToSignal)
process.OSUAnalysis.channels.append(SecondaryMcPartMatchedToSignalOneRecoMu)

process.OSUAnalysis.channels.append(OneMcPartMatchedToSignal)
process.OSUAnalysis.channels.append(OneMcPartMatchedToSignal_OneRecoEl)
process.OSUAnalysis.channels.append(OneSecondaryMcPartMatchedToSignal)
process.OSUAnalysis.channels.append(OneSecondaryMcPartMatchedToSignalOneRecoMu)


process.OSUAnalysis.channels.append(EmptySelection)
process.OSUAnalysis.channels.append(OneRecoEl)
process.OSUAnalysis.channels.append(OneRecoMu)
"""



### skim example
#add_channels(process, [SignalGenMatching_KynCuts_CrossCuts])
