#!/usr/bin/env python
import os
from DisplacedSUSY.StandardAnalysis.Options import *

config_file = "QCDControlRegions_cfg.py"

# choose luminosity used for MC normalization and set default samples to run over
# lumi and samples vary from channel to channel, so define locally
# units: 1/pb
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):

    intLumi = 16146.2 # 2016G,H only

    default_datasets = [
    'WJetsToLNu',
    'Diboson',
    'DYJetsToLL',
    'SingleTop',
    'TTJets_DiLept',
    'QCD_MuEnriched',
    'SingleMu_2016_postHIP'
        ]

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):

    intLumi = 36733.6 #Nov17 rereco 2017 golden json AND e-mu trigger

    default_datasets = [
    'WJetsToLNu',
    'Diboson',
    'DYJetsToLL',
    'SingleTop',
    'TTJets_DiLept',
    'QCD_MuEnriched',
    'SingleMu_2017'
        ]

# Redefine composite datasets that differ from those in OSUT3Analysis/Configuration/ConfigurationOptions.py
composite_dataset_definitions['Diboson'] = [
    'WWToLNuLNu',
    'WWToLNuQQ',
    'WZToLNu2QorQQ2L',
    'WZToLLLNu',
    'ZZToLLNuNu',
    'ZZToLLLL',
    ]

composite_dataset_definitions['QCD_EMEnriched'] = [
    'QCD_EMEnriched_120to170',
    'QCD_EMEnriched_170to300',
    'QCD_EMEnriched_300toInf',
    ]

composite_dataset_definitions['QCD_MuEnriched'] = [
        'QCD_MuEnriched_80to120',
        'QCD_MuEnriched_120to170',
        'QCD_MuEnriched_170to300',
        'QCD_MuEnriched_300to470',
        'QCD_MuEnriched_470to600',
        'QCD_MuEnriched_600to800',
        'QCD_MuEnriched_800to1000',
        'QCD_MuEnriched_1000toInf',
    ]

# Define background MC composite dataset for plotting
composite_dataset_definitions['Background'] = [x for x in default_datasets if not (x.startswith('MuonEG') or x.startswith('DisplacedSUSYSignal'))]

print "normalizing MC to " + str(intLumi) + " 1/pb"

InputCondorArguments = {}
