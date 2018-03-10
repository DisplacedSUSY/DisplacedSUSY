# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "TrigEfficiency_cfg.py"

# choose luminosity used for MC normalization
intLumi = 36460 
systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [

    'stop200_1mm',
    'stop200_10mm',
    'stop200_100mm',
    'stop200_1000mm',


    'stop800_1mm',
    'stop800_10mm',
    'stop800_100mm',
    'stop800_1000mm',

    'stop1200_1mm',
    'stop1200_10mm',
    'stop1200_100mm',
    'stop1200_1000mm',
 
]


InputCondorArguments = {}

