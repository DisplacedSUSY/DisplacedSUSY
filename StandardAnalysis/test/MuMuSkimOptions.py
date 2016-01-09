#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2Samples import *

#from OSUT3Analysis.Configuration.configurationOptions_13TeV_miniAODv2 import *
# specify which config file to pass to cmsRun
config_file = "MuMuPreselection_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2538.43 # for 13 TeV 2015D Silver Json                                                                                                                                                       
# create list of datasets to process
datasets = [
    'DoubleMu_2015',
    'QCD_MuEnriched',
    'WJetsToLNu',
    'SingleTop',
    'TTJets_Lept',
    'DYJetsToLL_50',
    'Diboson',
    'DisplacedSUSYSignal'
]
#InputCondorArguments = {'hold': 'true'}
