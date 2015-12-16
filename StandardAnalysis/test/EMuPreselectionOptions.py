#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2Samples import *

# specify which config file to pass to cmsRun
config_file = "EMuPreselection_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2538.43 # for 13 TeV 2015D Silver Json 

# create list of datasets to process
datasets = [
    #'Diboson',
    #'WJetsToLNu',
    #'DYJetsToLL_50',
    #'SingleTop',
    #'TTJets_Lept',
    #'QCD_MuEnriched',
    #'MuonEG_2015D',
    'stop200_1000mm',
]
InputCondorArguments = {'hold': 'true'}
