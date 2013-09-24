from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from OSUT3Analysis.Configuration.processingUtilities import *

###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

dir = "/mnt/hadoop/mc/stop200ToBottom_100mm_8TeV-pythia6_Summer12-START52_V9-v2_ahart-stop200ToBottom_100mm_TuneZ2star_8TeV-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v2-3c2c2ea126eaa14f77b77129f5e671ee_USER_STOP2012-v1/"
#dir = "/store/user/ahart/DYToTauTau_M-20_CT10_TuneZ2star_v2_8TeV-powheg-tauola-pythia6/BEAN2012-v4/4a12a6f1b79fbeb9915fe6064a3d6fce/"
#dir = "/store/user/jbrinson/TTJets_FullLeptMGDecays_8TeV-madgraph/BEAN2012-v4/0ff8045eb3a4a7ce9562dd332df0072c/"

for file in os.listdir(dir):
        process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))


process.OSUAnalysis.doTopPtReweighting = True


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

process.OSUAnalysis.histogramSets.append(MetHistograms)
process.OSUAnalysis.histogramSets.append(EventHistograms)

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisplacedSUSY.StandardAnalysis.Preselection import *
#process.OSUAnalysis.channels.append(Preselection)
process.OSUAnalysis.channels.append(Blinded_Preselection)

