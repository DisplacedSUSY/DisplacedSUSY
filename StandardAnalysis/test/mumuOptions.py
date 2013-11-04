#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

config_file = "mumuAnalyzer_cfg.py"

intLumi = 19423.  # DoubleMuParked 22Jan Re-Reco

datasets = [

##########################
### background samples ###
##########################

## #    'QCD_MuEnriched',
## #    'Background',

     'Wjets',

    'QCDFromData',

      'Diboson',
##     'WW',                                                                                                                                                                                                
##     'WZ',                                                                                                                                                                                                
##     'ZZ',                                                                                                                                                                                                
##     'ZG',
##     'WG',

      'SingleTop',
##      'SingleT_s',                                                                                                                                                                                       
##      'SingleTbar_s',                                                                                                                                                                                    
##      'SingleT_t',                                                                                                                                                                                       
##      'SingleTbar_t',                                                                                                                                                                                    
##      'SingleT_tW',                                                                                                                                                                                      
##      'SingleTbar_tW',                                                                                                                                                                                   

      'TTbar',
##     'TTbar_Had',                                                                                                                                                                                         
##     'TTbar_SemiLep',                                                                                                                                                                                     
##     'TTbar_Lep',                                                                                                                                                                                         

      'DY',
##     'DYToEE_20',                                                                                                                                                                                         
##     'DYToMuMu_20',                                                                                                                                                                                       
##     'DYToTauTau_20',  





####################
### data samples ###
####################

    'DoubleMu_22Jan2013',

]

