#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# choose luminosity used for MC normalization
#intLumi = 35863.308 # from  Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
intLumi = 16146.2 # 2016G,H only

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"


# create list of datasets to process
datasets = [
    'stop200_1mm',
    'stop200_10mm',
    'stop200_100mm',
    'stop200_1000mm',
    #'stop300_100mm',
    #'stop400_1mm',
    #'stop400_10mm',
    #'stop400_100mm',
    #'stop400_1000mm',
    #'stop500_1mm',
    #'stop500_10mm',
    #'stop500_100mm',
    #'stop600_1000mm',
    #'stop900_10mm',
    'Background'
]

#from ROOT import kRed
#colors['DisplacedSUSYSignal'] = kRed +1
#labels['DisplacedSUSYSignal'] = "Signal"
#types['DisplacedSUSYSignal'] = "bgMC"

InputCondorArguments = {}
