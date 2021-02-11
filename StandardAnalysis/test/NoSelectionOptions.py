#!/usr/bin/env python
import os
from DisplacedSUSY.EMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "NoSelection_cfg.py"

# create list of datasets to process
#datasets = default_datasets
#datasets.append()
#datasets.remove('DisplacedSUSYSignal')

datasets = [
    'stopToLB200_1mm_withCloudModel',
    'stopToLB200_10mm_withCloudModel',
    'stopToLB200_100mm_withCloudModel',
    'stopToLB200_1000mm_withCloudModel',
    'stopToLB1000_1mm_withCloudModel',
    'stopToLB1000_10mm_withCloudModel',
    'stopToLB1000_100mm_withCloudModel',
    'stopToLB1000_1000mm_withCloudModel',
    'stopToLB1800_1mm_withCloudModel',
    'stopToLB1800_10mm_withCloudModel',
    'stopToLB1800_100mm_withCloudModel',
    'stopToLB1800_1000mm_withCloudModel',

    'stopToLB200_1mm',
    'stopToLB200_10mm',
    'stopToLB200_100mm',
    'stopToLB200_1000mm',
    'stopToLB1000_1mm',
    'stopToLB1000_10mm',
    'stopToLB1000_100mm',
    'stopToLB1000_1000mm',
    'stopToLB1800_1mm',
    'stopToLB1800_10mm',
    'stopToLB1800_100mm',
    'stopToLB1800_1000mm',

]

colors['stop1000_1mm'] = 4
colors['stop1000_100mm'] = 8

#colors['stopToLB200_1000mm'] = 1
#colors['stopToLB1000_1000mm'] = 2
#colors['stopToLB1800_1000mm'] = 4
#colors['stopToLB200_1000mm_withCloudModel'] = 8
#colors['stopToLB1000_1000mm_withCloudModel'] = 6
#colors['stopToLB1800_1000mm_withCloudModel'] = 7

#colors['stopToLB200_100mm'] = 1
#colors['stopToLB1000_100mm'] = 2
#colors['stopToLB1800_100mm'] = 4
#colors['stopToLB200_100mm_withCloudModel'] = 8
#colors['stopToLB1000_100mm_withCloudModel'] = 6
#colors['stopToLB1800_100mm_withCloudModel'] = 7



colors['stopToLB200_1000mm'] = 9
colors['stopToLB1000_1mm'] = 1
colors['stopToLB1000_10mm'] = 2
colors['stopToLB1000_100mm'] = 3
colors['stopToLB1000_1000mm'] = 4
colors['stopToLB1800_1000mm'] = 46

colors['stopToLB200_1000mm_withCloudModel'] = 11
colors['stopToLB1000_1mm_withCloudModel'] = 8
colors['stopToLB1000_10mm_withCloudModel'] = 5
colors['stopToLB1000_100mm_withCloudModel'] = 6
colors['stopToLB1000_1000mm_withCloudModel'] = 7
colors['stopToLB1800_1000mm_withCloudModel'] = 12
