#!/usr/bin/env python
import os
from DisplacedSUSY.MuMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Skim_cfg.py"

# create list of datasets to process
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    datasets = [
        'DoubleMu_2016_postHIP',
        ]
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasets = [
        'DoubleMu_2017',
        'DYJetsToLL',
        'SingleTop',
        'QCD_MuEnriched',
        ]
