#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "ZControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 36460

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [

    # DY
    'DYJetsToLL',

    # TTbar
    'TTJets_DiLept',

    # tW
    'SingleTop',

    # Diboson
    'Diboson',

    # QCD
    'QCD_MuEnriched',
    
    # Signal
    #'DisplacedSUSYSignal',
    
    # Data
    'DoubleEG_2016_23Sep',

]

InputCondorArguments = {}
