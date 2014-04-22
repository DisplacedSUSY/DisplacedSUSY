#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

#config_file = "Cosmic_Skimer_cfg.py"
config_file = "CosmicAnalyzer_cfg.py"

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"

external_systematics_directory = 'DisplacedSUSY/Configuration/data/'

intLumi = 19300.  # SingleMu

channel = 'Preselection'

d0histogramName = 'electronAbsD0BeamspotVsMuonAbsD0BeamspotForLimits'

d0cuts_array = {
#    0 :    'Preselection',
    0.02 : 'Signal_Selection_200um',
    0.05 : 'Signal_Selection_500um',
    0.1 :  'Signal_Selection_1000um',
}

datasets = [
    #MC
    'DYToMuMu_20',
    
    #data
    
    'SingleMu',
    
]

