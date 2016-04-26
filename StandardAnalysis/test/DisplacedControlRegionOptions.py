#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_76X_Samples import *

# specify which config file to pass to cmsRun
config_file = "DisplacedControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2613 # from 13 TeV MuEG 2015D dataset, Silver Json
systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [
    'Diboson',
    'WJetsToLNu',
    'DYJetsToLL_50',
    'SingleTop',
    'TTJets_Lept',
    #'QCD_MuEnriched',
    'MuonEG_2015D',
    #'DisplacedSUSYSignal'
    #'stop200_10mm',
    #'stop500_10mm',
    #'stop800_10mm',
    #'stop1100_10mm',
]

InputCondorArguments = {'hold': 'true'}
