#!/usr/bin/env python
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

datasets = [
    'Wjets',
    'Diboson',
    'SingleTop',
    'TTbar',
    'DY',
]

options = {}
options['datasets'] = datasets
options['composite_dataset_definitions'] = composite_dataset_definitions
options['dataset_names'] = dataset_names
options['nJobs'] = nJobs
options['maxEvents'] = maxEvents
options['types'] = types
options['labels'] = labels

#add_stops (options, [200], [1.0,10.0,100.0])
#add_stops (options, [200], [0.2])
#add_stops (options, [200,300,400,500,600,700,800], [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0])


systematic_name = "trigger"
channel = "Blinded_Preselection"

minus_condor_dir   = "Blinded_preselection_minusTrigger"
central_condor_dir = "Blinded_preselection_centralTrigger"
plus_condor_dir    = "Blinded_preselection_plusTrigger"

