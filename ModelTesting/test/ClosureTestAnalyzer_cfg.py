from DisplacedSUSY.StandardAnalysis.displacedSUSY_cfi import *
from OSUT3Analysis.Configuration.processingUtilities import *

###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################



dir="/store/user/ahart/BN_stop200ToBottom_1.00mm_8TeV-pythia6_Summer12-START52_V9-v2_ahart-stop200ToBottom_1.00mm_TuneZ2star_8TeV-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v3-e542883f7d1b22c1f30ae55768bc52e5_USER_0/"
###
#dir="/mnt/hadoop/se/store/user/ahart/BN_stopToBottom_M_200_1mm_Tune4C_8TeV_pythia8_biliu-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_1/"

for file in os.listdir(dir):
            process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + '/' + file))

#process.source.fileNames.extend(cms.untracked.vstring('file:/store/user/ahart/eMuMinimal/stop300toTnu_50.0mm/EMu_Minimal/bean_0.root'))


process.OSUAnalysis.applyGentoRecoEfficiency = True

#######################################################################
##### Import the information about all the histograms to be filled #####
########################################################################

#import the desired sets of histograms from the standard python file which defines them
from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.histogramDefinitions import *

### block of gen level histograms
#"""
process.OSUAnalysis.histogramSets.append(MCParticleHistograms)
process.OSUAnalysis.histogramSets.append(SecondaryMCParticleHistograms)
process.OSUAnalysis.histogramSets.append(MCParticleDrJetHistogram)
process.OSUAnalysis.histogramSets.append(SecondaryMCParticleDrJetHistogram)
#"""

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisplacedSUSY.ModelTesting.ModelTestingSelections_short import *



process.OSUAnalysis.channels.append(Preselection_GenLevel)


### skim example
#add_channels(process, [SignalGenMatching_KynCuts_CrossCuts])
