#!/usr/bin/env python
import os
from DisplacedSUSY.StandardAnalysis.Options import *

# choose luminosity used for MC normalization and set default samples to run over
# lumi and samples vary from channel to channel, so define locally
# units: 1/pb
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):

    intLumi = 16146.2 # 2016G,H only

    default_datasets = [
        'DoubleEG_2016_postHIP',
        'DYJetsToLL',
        'TTJets_Lept',
        'SingleTop',
        'Diboson',
        'QCD_EMEnriched',
        'QCD_DoubleEMEnriched',
        'DisplacedSUSYSignal',
        ]

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):

    intLumi = 41527.5 #Nov17 rereco 2017 golden json AND e-e triggers

    default_datasets = [
        'DoubleEG_2017',
        'DYJetsToLL',
        'TTJets_Lept',
        'SingleTop',
        'Diboson',
        'QCD_EMEnriched',
        'QCD_DoubleEMEnriched',
        'DisplacedSUSYSignal',
        ]

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):

    intLumi = 59740 #17Sept early rereco 2018 golden json, with approved PHYSICS normtag

    default_datasets = [
        'EGamma_2018',
        'DYJetsToLL',
        'TTJets_Lept',
        'SingleTop',
        'Diboson',
        'QCD_EMEnriched',
        'QCD_DoubleEMEnriched',
        'DisplacedSUSYSignal',
        ]

# Define background MC composite dataset for plotting
composite_dataset_definitions['Background'] = [x for x in default_datasets if not (x.startswith('DoubleEG') or x.startswith('EGamma') or x.startswith('DisplacedSUSYSignal'))]
composite_dataset_definitions['NonQcdBackground'] = [x for x in composite_dataset_definitions['Background'] if not x.startswith('QCD')]

composite_dataset_definitions['Background_noDYTauTau'] = ["DYJetsToLL_noDYTauTau" if x == "DYJetsToLL" else x for x in composite_dataset_definitions['Background']]

# Define combined-across-years data datasets
composite_dataset_definitions['DoubleEG_2017_2018'] = [
    'DoubleEG_2017',
    'EGamma_2018'
]
composite_dataset_definitions['DoubleEG_2016_2017_2018'] = [
    'DoubleEG_2016_postHIP',
    'DoubleEG_2017',
    'EGamma_2018'
]

composite_dataset_definitions['DYJetsToLL_2017_2018'] = [
    'DYJetsToLL_2017',
    'DYJetsToLL_2018'
]

composite_dataset_definitions['Background_noDYTauTau_2017_2018'] = [
    'Background_noDYTauTau_2017',
    'Background_noDYTauTau_2018'
]

analysisChannel = "ee"

print "normalizing MC to " + str(intLumi) + " 1/pb"

InputCondorArguments = {}
