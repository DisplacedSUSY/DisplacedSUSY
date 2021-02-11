#!/usr/bin/env python
from DisplacedSUSY.MuMuChannel.localOptions import *

cutName = '>0 pixel hits'
input_sources = [
    {
        'condor_dir' : 'MuMuNum1PixelHitSelWithCosmicsWithDz15cmCut_2016Analysis_NoBPTXData_10Feb2021',
        'condor_dir_den' : 'MuMuDen1PixelHitSelWithCosmicsWithDz15cmCut_2016Analysis_NoBPTXData_10Feb2021',
        'dataset' :   'NoBPTX_2016_postHIP',
        #'condor_dir' : 'MuMuNum1PixelHitSelWithCosmics_2017Analysis_NoBPTXData_11Feb2021',
        #'condor_dir_den' : 'MuMuDen1PixelHitSelWithCosmics_2017Analysis_NoBPTXData_11Feb2021',
        #'dataset' :   'NoBPTX_2017',
        #'condor_dir' : 'MuMuNum1PixelHitSelWithCosmics_2018Analysis_NoBPTXData_11Feb2021',
        #'condor_dir_den' : 'MuMuDen1PixelHitSelWithCosmics_2018Analysis_NoBPTXData_11Feb2021',
        #'dataset' :   'NoBPTX_2018',
        'den_channel' : 'Den1PixelHitSelWithCosmics',
        'num_channel' : 'Num1PixelHitSelWithCosmics',
        'legend_entry' : 'NoBPTX data',
        'color' : 'black',
        'fill' : 'hollow',
        'marker' : 'circle',
    },
    {
        'condor_dir' : 'MuMuNum1PixelHitSelWithCosmics_2016Analysis_CosmicMC_11Feb2021',
        'condor_dir_den' : 'MuMuDen1PixelHitSelWithCosmics_2016Analysis_CosmicMC_11Feb2021',
        #'condor_dir' : 'MuMuNum1PixelHitSelWithCosmics_2017Analysis_CosmicMC_11Feb2021',
        #'condor_dir_den' : 'MuMuDen1PixelHitSelWithCosmics_2017Analysis_CosmicMC_11Feb2021',
        #'condor_dir' : 'MuMuNum1PixelHitSelWithCosmics_2018Analysis_CosmicMC_11Feb2021',
        #'condor_dir_den' : 'MuMuDen1PixelHitSelWithCosmics_2018Analysis_CosmicMC_11Feb2021',
        'dataset' :   'Cosmics',
        'den_channel' : 'Den1PixelHitSelWithCosmics',
        'num_channel' : 'Num1PixelHitSelWithCosmics',
        'legend_entry' : 'Cosmic MC',
        'color' : 'red',
        'fill' : 'solid',
        'marker' : 'square',
    },
]
