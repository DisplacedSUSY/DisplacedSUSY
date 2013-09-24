#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

config_file = "zTauTauControlRegionAnalyzer_cfg.py"

intLumi = 19680.  # MuEG 22Jan Re-Reco

datasets = [

##########################
### background samples ###
##########################

#    'QCDFromData',
#     'QCD_ElectronEnriched',
#     'QCD_MuEnriched',
#     'QCD_bEnriched',

    'Wjets',

    'Diboson',
#    'WW',
#    'WZ',
#    'ZZ',

    'SingleTop',
##     'SingleT_s',
##     'SingleTbar_s',
##     'SingleT_t',
##     'SingleTbar_t',
##     'SingleT_tW',
##     'SingleTbar_tW',

    'TTbar',
#    'TTbar_Had',
#    'TTbar_SemiLep',
#    'TTbar_Lep',

    'DY',
#    'DYToEE_20',
#    'DYToMuMu_20',
#    'DYToTauTau_20',


####################
### data samples ###
####################

    'MuEG_22Jan2013',


]



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
