#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions_13TeV import *

# specify which config file to pass to cmsRun
config_file = "CosmicMuon_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2538.43 #from 13 TeV MuEG dataset 2015D Silver JSON

# create list of datasets to process
datasets = [
    'NoBPTX_2015D',
]

InputCondorArguments = {}
