#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "EESkim_cfg.py"

# choose luminosity used for MC normalization
intLumi = 36460

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [

    # DY
    'DYJetsToLL',
    #'DYJetsToLL_50',
    #'DYJetsToLL_10to50',

    # TTbar
    'TTJets_DiLept',

    # tW
    #'SingleTop_tbarW',
    'SingleTop',

    # Diboson
    'Diboson',
    #'WWToLNuLNu',
    #'ZZToLLNuNu',
    #'ZG',

    # QCD
    'QCD_MuEnriched',
    
    # Signal
    'DisplacedSUSYSignal',
    
    # Data
    'DoubleEG_2016_23Sep',
    #'DoubleEG_2016H',

]

InputCondorArguments = {}
