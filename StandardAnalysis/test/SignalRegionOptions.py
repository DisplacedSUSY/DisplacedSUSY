#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions_13TeV import *

# specify which config file to pass to cmsRun
config_file = "SignalRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2445.23  # from 8 TeV MuEG dataset

# create list of datasets to process
datasets = [
    'QCD_MuEnriched_MiniAOD',
    'Diboson_MiniAOD',
    'WJetsToLNu_MiniAOD',
    'DYJetsToLL_50_MiniAOD',
    'SingleTop_MiniAOD',
    'TTJets_Lept_MiniAOD',
    'MuonEG_2015D',
#   'stop200_1mm_MiniAOD',
#   'stop200_10mm_MiniAOD',
#   'stop200_100mm_MiniAOD',
#   'stop200_1000mm_MiniAOD',
#   'stop300_1mm_MiniAOD',
#   'stop300_10mm_MiniAOD',
#   'stop300_100mm_MiniAOD',
#   'stop300_1000mm_MiniAOD',
#   'stop400_1mm_MiniAOD',
#   'stop400_10mm_MiniAOD',
#   'stop400_100mm_MiniAOD',
#   'stop400_1000mm_MiniAOD',
#   'stop500_1mm_MiniAOD',
#   'stop500_10mm_MiniAOD',
#   'stop500_100mm_MiniAOD',
#   'stop500_1000mm_MiniAOD',
#   'stop600_1mm_MiniAOD',
#   'stop600_10mm_MiniAOD',
#   'stop600_100mm_MiniAOD',
#   'stop600_1000mm_MiniAOD',
#   'stop700_1mm_MiniAOD',
#   'stop700_10mm_MiniAOD',
#   'stop700_100mm_MiniAOD',
#   'stop700_1000mm_MiniAOD',
#   'stop800_1mm_MiniAOD',
#   'stop800_10mm_MiniAOD',
#   'stop800_100mm_MiniAOD',
#   'stop800_1000mm_MiniAOD',
#   'stop900_1mm_MiniAOD',
#   'stop900_10mm_MiniAOD',
#   'stop900_100mm_MiniAOD',
#   'stop900_1000mm_MiniAOD',
#   'stop1000_1mm_MiniAOD',
#   'stop1000_10mm_MiniAOD',
#   'stop1000_100mm_MiniAOD',
#   'stop1000_1000mm_MiniAOD',
#   'stop1100_1mm_MiniAOD',
#   'stop1100_10mm_MiniAOD',
#   'stop1100_100mm_MiniAOD',
#   'stop1100_1000mm_MiniAOD',
#   'stop1200_1mm_MiniAOD',
#   'stop1200_10mm_MiniAOD',
#   'stop1200_100mm_MiniAOD',
#   'stop1200_1000mm_MiniAOD',
    'DisplacedSUSY',
]
InputCondorArguments = {'hold': 'true'}
