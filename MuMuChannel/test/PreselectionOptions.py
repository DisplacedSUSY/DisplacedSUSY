#!/usr/bin/env python
from DisplacedSUSY.MuMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# create list of datasets to process
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    datasets = default_datasets
    #datasets.append()
    datasets.remove('DisplacedSUSYSignal') #all samples ready

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasets = default_datasets
    #datasets.remove('DisplacedSUSYSignal') #all samples ready

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    composite_dataset_definitions['Taus'] = ['DYJetsToTauTauLeptonic', 'TTJets_Lept']
    #datasets = default_datasets
    #datasets.remove('DisplacedSUSYSignal') #all samples ready
    #datasets = ['DoubleMu_2016_2017_2018']

    #processes = ['stopToLB']
    #masses = [m for m in range(100, 1801, 100)]
    #lifetimes = [10**e for e in range(-1, 4)]
    #datasets = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]
    #datasets = [name.replace('.', 'p') for name in datasets]

    #datasets = [
        #'DYJetsToLL',
        #'DoubleMu_2018'
        #'DYJetsToTauTauLeptonic',
        #'TTJets_Lept',
        #'TTJets_inclusive',
        #'Diboson',
        #'DYBBJetsToLL',
        #'SingleTop',
        #'QCD_MuEnriched',
        #'Taus'
        #]
    #datasets = ['stopToLB200_1mm',
                #'stopToLB200_10mm',
                #'stopToLB200_100mm',
                #'stopToLB200_1000mm',
                #'stopToLB300_1000mm',
                #'stopToLB1000_1mm',
                #'stopToLB1000_10mm',
                #'stopToLB1000_100mm',
                #'stopToLB1000_1000mm',
                #'stopToLB1800_1mm',
                #'stopToLB1800_10mm',
                #'stopToLB1800_100mm',
                #'stopToLB1800_1000mm',
                #'stopToLD200_1mm',
                #'stopToLD200_10mm',
                #'stopToLD200_100mm',
                #'stopToLD200_1000mm',
                #'stopToLD1000_1mm',
                #'stopToLD1000_10mm',
                #'stopToLD1000_100mm',
                #'stopToLD1000_1000mm',
                #'stopToLD1800_1mm',
                #'stopToLD1800_10mm',
                #'stopToLD1800_100mm',
                #'stopToLD1800_1000mm',

        #'HTo4Mu125_50_50mm',
        #'HTo4Mu125_50_500mm',
        #'HTo4Mu125_50_5000mm',
        #'HTo4Mu125_20_13mm',
        #'HTo4Mu125_20_130mm',
        #'HTo4Mu125_20_1300mm',

        #'NoBPTX_2018D',
        #'DoubleMu_2018',
        #'stopToLB400_1mm',
        #'stopToLB1000_1mm',
        #'stopToLB1800_1mm',

                #]
    #colors['stopToLB1000_1mm'] = 1
    #colors['stopToLB1000_10mm'] = 2
    #colors['stopToLB1000_100mm'] = 4
    #colors['stopToLB1000_1000mm'] = 8

    colors['stopToLB200_1mm'] = 1
    colors['stopToLB1000_1mm'] = 2
    colors['stopToLB1800_1mm'] = 4
    #colors['stopToLD200_1mm'] = 8
    #colors['stopToLB1000_1000mm'] = 8
    #colors['stopToLD1800_1mm'] = 7

    # add extra lifetimes for original masses
    #processes = ['stopToLB',
                 #'stopToLD'
    #]
    #masses = [m for m in range(200, 1801, 100)]
    #lifetimes = [b*10**e for e in [-2, 3] for b in range(1, 10)] + [10000]
    #lifetimes.remove(1000)
    #datasets = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]

    # add all lifetimes for 100GeV
    #lifetimes = [b*10**e for e in range(-2, 4) for b in range(1, 10)] + [10000]
    #datasets.extend(["{}100_{}mm".format(p, l) for p in processes for l in lifetimes])
    #datasets = [d.replace('.', 'p') for d in datasets]
