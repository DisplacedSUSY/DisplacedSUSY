#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_76X_Samples import *
# specify which config file to pass to cmsRun
config_file = "QCDMuonSkim_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2613.0 # for 13 TeV Silver Json, 2015D 

# create list of datasets to process
datasets = [
    #'Diboson',
    #'WJetsToLNu',
    #'DYJetsToLL_50',
    #'SingleTop',
    #'TTJets_Lept',
    'QCD_MuEnriched',
    #'QCD_MuEnriched_170to300',
    #'ZZToLLNuNu',
    #'SingleMu_2015D',
]
InputCondorArguments = {'request_memory':'2048MB'}
secondaryCollections ={}
