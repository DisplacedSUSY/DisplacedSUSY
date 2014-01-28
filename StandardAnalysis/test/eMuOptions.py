#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

config_file = "eMuAnalyzer_cfg.py"

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"

external_systematics_directory = 'DisplacedSUSY/Configuration/data/'

intLumi = 19680.  # MuEG 22Jan Re-Reco

channel = 'Preselection'

d0histogramName = 'electronAbsD0BeamspotVsMuonAbsD0BeamspotForLimits'

d0cuts_array = {
#    0 :    'Preselection',
    0.02 : 'Signal_Selection_200um',
    0.05 : 'Signal_Selection_500um',
    0.1 :  'Signal_Selection_1000um',
}

datasets = [

##########################
### background samples ###
##########################


      'WNjets',
#       'Wjets',

      'Diboson',
      'SingleTop',
      'TTbar',
      'QCDFromData',
      'DY',

#      'QCD_MuEnriched',

####################
### data samples ###
####################

     'MuEG_22Jan2013',

]


## colors and labels must defined for signal samples that will be plotted

colors['stop200_1.0mm_br50'] = 632
colors['stop200_10.0mm_br50'] = 600
colors['stop200_100.0mm_br50'] = 1

labels['stop200_1.0mm_br50'] = "#tilde{t}#tilde{t} M(200) c#tau(1mm)"
labels['stop200_10.0mm_br50'] = "#tilde{t}#tilde{t} M(200) c#tau(10mm)"
labels['stop200_100.0mm_br50'] = "#tilde{t}#tilde{t} M(200) c#tau(100mm)"

options = {}
options['datasets'] = datasets
options['composite_dataset_definitions'] = composite_dataset_definitions
options['dataset_names'] = dataset_names
options['nJobs'] = nJobs
options['maxEvents'] = maxEvents
options['types'] = types
options['labels'] = labels

########################################################
### add_stops function is used to add signal samples ###
########################################################

# the syntax is as follows
# add_stops (options, masses, ctaus, bottomBranchingRatios = [])
# the masses and ctaus are required
# the bottom BRs is optional and will default to just 50%

########################################################

#add_stops (options, [200], [1.0,10.0,100.0])
#add_stops (options, [200,300,400,500,600,700,800], [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0])

