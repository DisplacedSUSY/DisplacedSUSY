#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_76X_Samples import *

# specify which config file to pass to cmsRun
config_file = "SignalRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2613 # from 8 TeV MuEG dataset

# create list of datasets to process
datasets = [
    #'QCD_MuEnriched',
    #'Diboson',
    #'WJetsToLNu',
    #'DYJetsToLL_50',
    #'SingleTop',
    #'TTJets_Lept',
    'MuonEG_2015D',
   #'stop200_1mm',
   #'stop200_10mm',
   #'stop200_100mm',
   #'stop200_1000mm',
   #'stop300_1mm',
   #'stop300_10mm',
   #'stop300_100mm',
   #'stop300_1000mm',
   #'stop400_1mm',
   #'stop400_10mm',
   #'stop400_100mm',
   #'stop400_1000mm',
   #'stop500_1mm',
   #'stop500_10mm',
   #'stop500_100mm',
   #'stop500_1000mm',
   #'stop600_1mm',
   #'stop600_10mm',
   #'stop600_100mm',
   #'stop600_1000mm',
   #'stop700_1mm',
   #'stop700_10mm',
   #'stop700_100mm',
   #'stop700_1000mm',
   #'stop800_1mm',
   #'stop800_10mm',
   #'stop800_100mm',
   #'stop800_1000mm',
   #'stop900_1mm',
   #'stop900_10mm',
   #'stop900_100mm',
   #'stop900_1000mm',
   #'stop1000_1mm',
   #'stop1000_10mm',
   #'stop1000_100mm',
   #'stop1000_1000mm',
   #'stop1100_1mm',
   #'stop1100_10mm',
   #'stop1100_100mm',
   #'stop1100_1000mm',
   #'stop1200_1mm',
   #'stop1200_10mm',
   #'stop1200_100mm',
   #'stop1200_1000mm',
    #'DisplacedSUSYSignal',
]
InputCondorArguments = {'hold': 'true'}
