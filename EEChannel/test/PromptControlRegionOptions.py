#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "PromptControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 35863.308

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
    #'QCD_EMEnriched',
    #'QCD_bcToE',
    
    # Signal
    #'DisplacedSUSYSignal',
    
    # Data
    #'DoubleEG_2016',
    'DoubleEG_2016B',
    'DoubleEG_2016C',
    'DoubleEG_2016D',
    'DoubleEG_2016E',
    'DoubleEG_2016F',
    'DoubleEG_2016G',
    'DoubleEG_2016H',

]

InputCondorArguments = {}
