import os
from OSUT3Analysis.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.genSim_102X_Samples import *

# specify which config file to pass to cmsRun
config_file = "stopRHadronSimAnalyzer_cfg.py"

# create list of datasets to process
datasets = [
    "stopToLB200_1000mm",
    "stopToLB1000_1000mm",
    "stopToLB1800_1000mm",
]
