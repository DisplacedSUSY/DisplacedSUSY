from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from OSUT3Analysis.Configuration.processingUtilities import *

###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################


#dir = "/store/user/ahart/DYToTauTau_M-20_CT10_TuneZ2star_v2_8TeV-powheg-tauola-pythia6/BEAN2012-v4/4a12a6f1b79fbeb9915fe6064a3d6fce/"
dir = "/mnt/hadoop/se/store/user/ahart/eMuMinimal_new/stop200toBl_10mm/EMu_Minimal"

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
#process.OSUAnalysis.doPileupReweighting = True

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

process.OSUAnalysis.histogramSets.append(JetHistograms)
process.OSUAnalysis.histogramSets.append(ElectronJetHistograms)
process.OSUAnalysis.histogramSets.append(MuonJetHistograms)

#process.OSUAnalysis.histogramSets.append(PhotonHistograms)
#process.OSUAnalysis.histogramSets.append(ElectronPhotonHistograms)
#process.OSUAnalysis.histogramSets.append(MuonPhotonHistograms)

process.OSUAnalysis.histogramSets.append(MetHistograms)
process.OSUAnalysis.histogramSets.append(EventHistograms)

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisplacedSUSY.StandardAnalysis.Preselection import *
from DisplacedSUSY.BackgroundStudies.QCDPreselections import *

process.OSUAnalysis.channels.append(Preselection_100um) # B
process.OSUAnalysis.channels.append(Preselection_SS_100um) # A
process.OSUAnalysis.channels.append(Preselection_AntiIso) # D
process.OSUAnalysis.channels.append(Preselection_AntiIso_SS_100um) # C
