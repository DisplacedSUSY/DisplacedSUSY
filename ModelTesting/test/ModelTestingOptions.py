#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

#config_file = "eMuAnalyzer_cfg.py"
config_file = "ModelTestingAnalyzer_cfg.py"


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


]


## colors and labels must defined for signal samples that will be plotted

colors['stopHadron200_1.0mm_br100'] = 632
colors['stopHadron200_100.0mm_br100'] = 600
colors['stopHadron200_10000.0mm_br100'] = 1

colors['stopHadron600_1.0mm_br100'] = 633
colors['stopHadron600_100.0mm_br100'] = 601
colors['stopHadron600_10000.0mm_br100'] = 2

colors['stopHadron1000_1.0mm_br100'] = 634
colors['stopHadron1000_100.0mm_br100'] = 602
colors['stopHadron1000_10000.0mm_br100'] = 3


labels['stopHadron200_1.0mm_br100'] = "#tilde{t}#tilde{t} M(200) c#tau(1mm)"
labels['stopHadron200_100.0mm_br100'] = "#tilde{t}#tilde{t} M(200) c#tau(10mm)"
labels['stopHadron200_10000.0mm_br100'] = "#tilde{t}#tilde{t} M(200) c#tau(100mm)"

labels['stopHadron600_1.0mm_br100'] = "#tilde{t}#tilde{t} M(200) c#tau(1mm)"
labels['stopHadron600_100.0mm_br100'] = "#tilde{t}#tilde{t} M(200) c#tau(10mm)"
labels['stopHadron600_10000.0mm_br100'] = "#tilde{t}#tilde{t} M(200) c#tau(100mm)"

labels['stopHadron1000_1.0mm_br100'] = "#tilde{t}#tilde{t} M(200) c#tau(1mm)"
labels['stopHadron1000_100.0mm_br100'] = "#tilde{t}#tilde{t} M(200) c#tau(10mm)"
labels['stopHadron1000_10000.0mm_br100'] = "#tilde{t}#tilde{t} M(200) c#tau(100mm)"


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

#add_stops (options, [200], [1.0])
add_stops (options, [200,600,1000], [1.0,100.0,10000.0])
#add_stops (options, [600], [1.0,100.0,10000.0])
