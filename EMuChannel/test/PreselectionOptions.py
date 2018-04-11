#!/usr/bin/env python
import os
from DisplacedSUSY.StandardAnalysis.Options import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

composite_dataset_definitions['Background'] = ['DYJetsToLL','TTJets_Lept','SingleTop','Diboson','QCD_MuEnriched']

# create list of datasets to process
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    datasets = [

        ### DY
        'DYJetsToLL',

        ### TTbar
        'TTJets_Lept',
        #'TTJets_SingleLeptFromT',
        #'TTJets_SingleLeptFromTbar',
        #'TTJets_DiLept',

        ### single top
        'SingleTop',
        #'SingleTop_s_channel',
        #'SingleTop_tW',
        #'SingleTop_tbarW',
        #'SingleTop_t_channel_antitop',
        #'SingleTop_t_channel_top',

        ### Diboson
        'Diboson',
        #'WWToLNuLNu',
        #'WWToLNuQQ',
        #'WZToLLLNu',
        #'WZToLNuNuNu',
        #'ZZToLLLL',
        #'ZZToLLNuNu',
        #'ZZToLLQQ',
        #'ZZToNuNuQQ',

        ### QCD (mu-enriched is bigger)
        'QCD_MuEnriched',

        ### Sum of background
        #'Background',

        ### Data
        'MuonEG_2016_postHIP',

        ### Signal MC
        #'DisplacedSUSYSignal',
        #'stop200_1mm',
        #'stop200_10mm',
        #'stop200_100mm',
        #'stop200_1000mm',
        #'stop300_1mm',
        #'stop300_10mm',
        #'stop300_100mm',
        #'stop300_1000mm',
        #'stop400_1mm',
        #'stop400_10mm',
        #'stop400_100mm',
        #'stop400_1000mm',
        #'stop500_1mm',
        #'stop500_10mm',
        #'stop500_100mm',
        #'stop500_1000mm',
        #'stop600_1mm',
        #'stop600_10mm',
        #'stop600_100mm',
        #'stop600_1000mm',
        #'stop700_1mm',
        #'stop700_10mm',
        #'stop700_100mm',
        #'stop700_1000mm',
        #'stop800_1mm',
        #'stop800_10mm',
        #'stop800_100mm',
        #'stop800_1000mm',
        #'stop900_1mm',
        #'stop900_10mm',
        #'stop900_100mm',
        #'stop900_1000mm',
        #'stop1000_1mm',
        #'stop1000_10mm',
        #'stop1000_100mm',
        #'stop1000_1000mm',
        #'stop1100_1mm',
        #'stop1100_10mm',
        #'stop1100_100mm',
        #'stop1100_1000mm',
        #'stop1200_1mm',
        #'stop1200_10mm',
        #'stop1200_100mm',
        #'stop1200_1000mm',
        ]
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasets = [
        'MuonEG_2017'
        ]
