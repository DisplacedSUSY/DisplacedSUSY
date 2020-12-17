#!/usr/bin/env python
import os
from DisplacedSUSY.EEChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Skim_cfg.py"

# create list of datasets to process
datasets = default_datasets
#datasets.append()
datasets.remove('DisplacedSUSYSignal')
