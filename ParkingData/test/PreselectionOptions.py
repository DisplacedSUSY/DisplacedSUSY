from DisplacedSUSY.MuMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# create list of datasets to process

#datasets = default_datasets
#datasets.remove('DisplacedSUSYSignal')

datasets = [
    'stopToLB200_1000mm',
    ]
