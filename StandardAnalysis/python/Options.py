#!/usr/bin/env python
import os

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *
    print "using 80X samples"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    from DisplacedSUSY.Configuration.miniAODV2_94X_Samples import *
    print "using 94X samples"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    from DisplacedSUSY.Configuration.miniAODV2_102X_Samples import *
    print "using 102X samples"
else:
    print "What CMSSW release are you in? We expect the samples to be imported from the 80X or 94X or 102X list"

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

InputCondorArguments = {}

# Define composite datasets of all samples
composite_dataset_definitions['all_bg_mc'] = bg_mc_samples.keys()
composite_dataset_definitions['non_interpolated_signal_mc'] = signal_mc_samples.keys()

# Redefine composite datasets that differ from those in OSUT3Analysis/Configuration/ConfigurationOptions.py
composite_dataset_definitions['QCD_MuEnriched'] = [
    'QCD_MuEnriched_20to30',
    'QCD_MuEnriched_30to50',
    'QCD_MuEnriched_50to80',
    'QCD_MuEnriched_80to120',
    'QCD_MuEnriched_120to170',
    'QCD_MuEnriched_170to300',
    'QCD_MuEnriched_300to470',
    'QCD_MuEnriched_470to600',
    'QCD_MuEnriched_600to800',
    'QCD_MuEnriched_800to1000',
    'QCD_MuEnriched_1000toInf',
]
