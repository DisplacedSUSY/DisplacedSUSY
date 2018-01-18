#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from DisplacedSUSY.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# choose luminosity used for MC normalization
intLumi = 36460 # from 2016BCDEFGH re-reco golden json

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [

#    'DisplacedSUSYSignal'


    'stop200_0p1mm',
    'stop200_0p2mm',
    'stop200_0p3mm',
    'stop200_0p4mm',
    'stop200_0p5mm',
    'stop200_0p6mm',
    'stop200_0p7mm',
    'stop200_0p8mm',
    'stop200_0p9mm',
    'stop200_1mm',
    # 'stop200_2mm',
    # 'stop200_3mm',
    # 'stop200_4mm',
    # 'stop200_5mm',
    # 'stop200_6mm',
    # 'stop200_7mm',
    # 'stop200_8mm',
    # 'stop200_9mm',
    # 'stop200_10mm',
    # 'stop200_20mm',
    # 'stop200_30mm',
    # 'stop200_40mm',
    # 'stop200_50mm',
    # 'stop200_60mm',
    # 'stop200_70mm',
    # 'stop200_80mm',
    # 'stop200_90mm',
    # 'stop200_100mm',
    # 'stop200_200mm',
    # 'stop200_300mm',
    # 'stop200_400mm',
    # 'stop200_500mm',
    # 'stop200_600mm',
    # 'stop200_700mm',
    # 'stop200_800mm',
    # 'stop200_900mm',
    # 'stop200_1000mm',

]

InputCondorArguments = {}

