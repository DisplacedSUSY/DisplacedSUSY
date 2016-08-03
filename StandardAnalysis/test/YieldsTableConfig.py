#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_76X_Samples import *
from array import array
# specify which config file to pass to cmsRun

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [
    #'Diboson',
    #'WJetsToLNu',
    #'DYJetsToLL_50',
    #'SingleTop',
    #'TTJets_Lept',
    #'QCD_MuEnriched',
    #'MuonEG_2015D',
    #'stop200_0p1mm',
    #'stop200_0p3mm',
    #'stop200_0p4mm',
    'stop900_1mm',
    'stop900_10mm',
    'stop900_100mm',
    'stop900_1000mm',
    #'stop200_1mm',
    #'stop200_10mm',
    #'stop800_1000mm',
]

d0cuts_array = array('d',[0.02,0.05,0.1])
#d0cuts_array = array('d',[0.006,0.008])
#d0cuts_array = array('d',[0.01])
d0UpperCut = 10
d0histogramName    = "Electron-muon-beamspot Plots/electronIpMuonIpMedium"
#mud0histogramName  = "Muon-beamspot Plots/muonAbsD0BeamspotM"
mud0histogramName  = "muonAbsD0BeamspotM"
#eled0histogramName = "Electron-beamspot Plots/electronAbsD0BeamspotM"
eled0histogramName = "electronAbsD0BeamspotM"
channel = "EMuPreselectionInclusiveTrigger"
#channel = "DisplacedControlRegionNoIsoInclusiveDisplacedTrigger"

