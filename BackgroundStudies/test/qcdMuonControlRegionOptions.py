#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

config_file = "qcdMuonControlRegionAnalyzer_cfg.py"

#intLumi = 19040.  # DoubleMu
#intLumi = 18380.  # DoublePhoton
#intLumi = 18260.  # MuEG
intLumi = 20000.  # MuEG - DISPLACED_LEPTON-v3

datasets = [

####################
### data samples ###
####################

    'DoubleMu_22Jan2013',
    
##########################
### background samples ###
##########################

    'QCD_MuEnriched',

    'Wjets',

    'Diboson',
#    'WW',
#    'WZ',
#    'ZZ',

    'DY',
#    'DYToEE_20',
#    'DYToMuMu_20',
#    'DYToTauTau_20',

    'TTbar',
#    'TTbar_Had',
#    'TTbar_SemiLep',
##    'TTbar_Lep',

#    'Background',



]

colors['stop400_1.0mm_br50'] = 632
colors['stop400_10.0mm_br50'] = 600
colors['stop400_100.0mm_br50'] = 1

labels['stop400_1.0mm_br50'] = "#tilde{t}#tilde{t} M(400) c#tau(1mm)"
labels['stop400_10.0mm_br50'] = "#tilde{t}#tilde{t} M(400) c#tau(10mm)"
labels['stop400_100.0mm_br50'] = "#tilde{t}#tilde{t} M(400) c#tau(100mm)"



options = {}
options['datasets'] = datasets
options['composite_dataset_definitions'] = composite_dataset_definitions
options['dataset_names'] = dataset_names
options['nJobs'] = nJobs
options['maxEvents'] = maxEvents
options['types'] = types
options['labels'] = labels
#add_stops (options, [200,300,400,500,600,700], [1.0,10.0,100.0])
#add_stops (options, [400], [1.0,10.0,100.0])
#add_stops (options, [200,300,400,500,600,700,800], [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0])
