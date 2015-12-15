#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2Samples import *

# specify which config file to pass to cmsRun
config_file = "QCDElectronSkim_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2556.37 # for 13 TeV Silver Json, 2015D 

# create list of datasets to process
datasets = [
    'Diboson',
    'WJetsToLNu',
    'DYJetsToLL_50',
    'SingleTop',
    'TTJets_Lept',
    'QCD_EMEnriched',
    'QCD_bcToE',
    'SingleEle_2015D',
]
InputCondorArguments = {'hold': 'true'}
