#!/usr/bin/env python
from DisplacedSUSY.MuMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "HIPStudyRegions_cfg.py"

# choose luminosity used for MC normalization
intLumi = 35863.308 #redefine intLumi here for HIP study


# create list of datasets to process
datasets = [

    # DY
#    'DYJetsToLL',

    # TTbar
#    'TTJets_DiLept',

    # tW
#    'SingleTop',

    # Diboson
#    'Diboson',

    # QCD
#    'QCD_MuEnriched',

    # Signal
    #'DisplacedSUSYSignal',
    
    # Data
#    'DoubleMu_2016',
    'DoubleMu_2016B',
    'DoubleMu_2016C',
    'DoubleMu_2016D',
    'DoubleMu_2016E',
    'DoubleMu_2016F',
    'DoubleMu_2016G',
    'DoubleMu_2016H',
]


InputCondorArguments = {}
