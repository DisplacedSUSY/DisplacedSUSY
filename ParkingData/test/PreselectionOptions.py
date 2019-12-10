from DisplacedSUSY.MuMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# create list of datasets to process

#datasets = []
#datasets = default_datasets
#datasets.remove('DisplacedSUSYSignal')
#datasets.append('Background')

datasets = [
    'stopToLB100_1000mm',
    'stopToLB100_1mm',
    'stopToLB150_1000mm',
    'stopToLB150_1mm',
    'stopToLB175_1000mm',
    'stopToLB175_1mm',
    'stopToLB200_1000mm',
    'stopToLB200_1mm',
    'stopToLB300_1000mm',
    'stopToLB300_1mm',
    'stopToLB400_1000mm',
    'stopToLB400_1mm',
    ]
