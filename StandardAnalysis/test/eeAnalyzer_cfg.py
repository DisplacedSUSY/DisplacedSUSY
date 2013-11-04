from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from OSUT3Analysis.Configuration.processingUtilities import *

###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

#dir = "/mnt/hadoop/mc/stop200ToBottom_100mm_8TeV-pythia6_Summer12-START52_V9-v2_ahart-stop200ToBottom_100mm_TuneZ2star_8TeV-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v2-3c2c2ea126eaa14f77b77129f5e671ee_USER_STOP2012-v1/"
#dir = "/store/user/ahart/eMuMinimal/TTbar_Lep/EMu_Minimal"
dir = "/store/user/ahart/BN_DYToEE_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_0/"
#dir = "/store/user/ahart/BN_DYToTauTau_M-20_CT10_TuneZ2star_v2_8TeV-powheg-tauola-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_0/"
for file in os.listdir(dir):
    process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + '/' + file))

######################################################################
##### Overwrite specific variables defined in osuAnalysis_cfi.py #####
######################################################################

process.OSUAnalysis.electronSFFile  =  cms.string (os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Configuration/data/MVANonTrig_HtoZZto4l_IdIsoSip.root')
process.OSUAnalysis.electronSFID    =  cms.string ('')
process.OSUAnalysis.electronSF      =  cms.string ('h_electronScaleFactor_IdIsoSip')
process.OSUAnalysis.applyTriggerSF  =  False

########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################

#import the desired sets of histograms from the standard python file which defines them
from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisplacedSUSY.Configuration.histogramDefinitions import *

process.OSUAnalysis.histogramSets.append(ElectronHistograms)
process.OSUAnalysis.histogramSets.append(ElectronD0Histograms)

process.OSUAnalysis.histogramSets.append(SecondaryElectronHistograms)
process.OSUAnalysis.histogramSets.append(SecondaryElectronD0Histograms)

process.OSUAnalysis.histogramSets.append(ElectronSecondaryElectronHistograms)
process.OSUAnalysis.histogramSets.append(ElectronSecondaryElectronD0Histograms)


#process.OSUAnalysis.histogramSets.append(JetHistograms)
#process.OSUAnalysis.histogramSets.append(ElectronJetHistograms)
#process.OSUAnalysis.histogramSets.append(ElectronJetHistograms)


process.OSUAnalysis.histogramSets.append(MetHistograms)
process.OSUAnalysis.histogramSets.append(EventHistograms)

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisplacedSUSY.StandardAnalysis.Preselection_EE import *
from DisplacedSUSY.StandardAnalysis.SignalSelections import *
from DisplacedSUSY.BackgroundStudies.QCDPreselections import *


process.OSUAnalysis.channels.append(Preselection_EE) # B
process.OSUAnalysis.channels.append(Preselection_EE_SS) # A
process.OSUAnalysis.channels.append(Preselection_EE_AntiIso) # D
process.OSUAnalysis.channels.append(Preselection_EE_AntiIso_SS) # C

process.OSUAnalysis.channels.append(Signal_Selection_EE_200um)
process.OSUAnalysis.channels.append(Signal_Selection_EE_AntiIso_200um)

