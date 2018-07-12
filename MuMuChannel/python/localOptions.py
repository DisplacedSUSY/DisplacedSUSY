#!/usr/bin/env python
import os
from DisplacedSUSY.StandardAnalysis.Options import *

# choose luminosity used for MC normalization
# units: 1/pb
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):

    intLumi = 16146.2 # 2016G,H only

    default_datasets = [
        'DoubleMu_2016_postHIP',
        'DYJetsToLL',
        'TTJets_Lept',
        'SingleTop',
        'Diboson',
        'QCD_MuEnriched',
        'DisplacedSUSYSignal', #ready for stop-->l+b, m=200 to 1300 GeV; NOT ready for stop-->l+b, m=1400 to 1800 GeV and NOT ready for stop-->l+d, m=200 to 1800 GeV
        ]

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):

    intLumi = 36733.6 #Nov17 rereco 2017 golden json AND mu-mu trigger

    default_datasets = [
        'DoubleMu_2017',
        'DYJetsToLL',
        'TTJets_Lept',
        'TTJets_inclusive',
        'SingleTop',
        'Diboson',
        'QCD_MuEnriched',
        'DisplacedSUSYSignal', #NOT ready for stop-->l+b, NOT ready for stop-->l+d
        ]

# Define background MC composite dataset for plotting
composite_dataset_definitions['Background'] = [x for x in default_datasets if not (x.startswith('DoubleMu') or x.startswith('DisplacedSUSYSignal'))]

print "normalizing MC to " + str(intLumi) + " 1/pb"

InputCondorArguments = {}
