#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# choose luminosity used for MC normalization
#intLumi = 35863.308 # from  Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
intLumi = 16146.2 # 2016G,H only

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"


# create list of datasets to process
datasets = [
    #'stopToLB200_1mm',
    #'stopToLB200_10mm',
    #'stopToLB200_100mm',
    #'stopToLB200_1000mm',
    #'stopToLB300_100mm',
    #'stopToLB400_1mm',
    #'stopToLB400_10mm',
    #'stopToLB400_100mm',
    #'stopToLB400_1000mm',
    #'stopToLB500_1mm',
    #'stopToLB500_10mm',
    #'stopToLB500_100mm',
    #'stopToLB600_1000mm',
    #'stopToLB900_10mm',
    #'Background'
    'Diboson',
    #'DYJetsToLL',
    'TTJets_Lept',
]

#from ROOT import kRed
#colors['DisplacedSUSYSignal'] = kRed +1
#labels['DisplacedSUSYSignal'] = "Signal"
#types['DisplacedSUSYSignal'] = "bgMC"

InputCondorArguments = {}
