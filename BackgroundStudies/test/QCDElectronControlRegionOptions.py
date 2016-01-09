#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2Samples import *

# specify which config file to pass to cmsRun
config_file = "QCDElectronControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2556.37 # for 13 TeV Silver Json, 2015D 

# create list of datasets to process
datasets = [
    'SingleEle_2015D',
    'QCD_EMEnriched',
    'QCD_bcToE',
    'TTJets_Lept',
    'SingleTop',
    'DYJetsToLL_50',
    'WJetsToLNu',
    'Diboson',
]
InputCondorArguments = {'hold': 'true'}
