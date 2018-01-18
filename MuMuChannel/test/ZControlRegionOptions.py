#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from DisplacedSUSY.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "ZControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 16146.2 # 2016G,H only

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [

    # DY
    #'DYJetsToLL',

    # TTbar
    #'TTJets_DiLept',

    # tW
    #'SingleTop',

    # Diboson
    #'Diboson',

    # QCD
    #'QCD_MuEnriched',

    # Signal
    #'DisplacedSUSYSignal',

    # Data
    #'DoubleMu_2016',
    #'DoubleMu_2016_postHIP',
    #'DoubleMu_2016G',
    'DoubleMu_2016H',

]

InputCondorArguments = {}
