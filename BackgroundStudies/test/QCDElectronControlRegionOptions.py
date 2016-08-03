#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_76X_Samples import *

# specify which config file to pass to cmsRun
config_file = "QCDElectronControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2613 # for 13 TeV Silver Json, 2015D 

# create list of datasets to process
datasets = [
    #'DoubleEG_2015D',
    'SingleEle_2015D',
    #'Data',
    #'SinglePhoton_2015D',
    'DYJetsToLL_50',
    'WJetsToLNu',
    'Diboson',
    'SingleTop',
    'TTJets_Lept',
    #'QCD',
    'QCD_EMEnriched',
    'QCD_bcToE',
    #'QCD_bcToE_15to20',
    #'QCD_bcToE_20to30',
    #'QCD_bcToE_30to80',
    #'QCD_bcToE_80to170',
    #'QCD_bcToE_170to250',
    #'QCD_bcToE_250toInf',
    #'QCD_EMEnriched_15to20',
    #'QCD_EMEnriched_20to30',
    #'QCD_EMEnriched_30to50',
    #'QCD_EMEnriched_50to80',
    #'QCD_EMEnriched_80to120',
    #'QCD_EMEnriched_120to170',
    #'QCD_EMEnriched_170to300',
    #'QCD_EMEnriched_300toInf', 
    #'stop200_0p1mm',
    #'stop200_0p5mm',
    #'stop200_1mm',
    #'stop200_10mm',
    #'stop200_100mm',
    #'stop200_1000mm',
]
InputCondorArguments = {'hold': 'true','request_memory':'2048MB'}
secondaryCollections ={'bjets':'pat::Jet'}
