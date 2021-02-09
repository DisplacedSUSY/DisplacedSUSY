#!/usr/bin/env python
from DisplacedSUSY.EMuChannel.localOptions import *

cutName = '>0 pixel hits'
input_sources = [
    { 'condor_dir' : 'MuMuNum1PixelHitSelWithCosmics_2016Analysis_NoBPTXData_8Feb2021',
      'condor_dir_den' : 'MuMuDen1PixelHitSelWithCosmics_2016Analysis_NoBPTXData_8Feb2021',
      'dataset' :   'NoBPTX_2016_postHIP',
      'den_channel' : 'Den1PixelHitSelWithCosmics',
      'num_channel' : 'Num1PixelHitSelWithCosmics',
      'legend_entry' : 'NoBPTX data',
      'color' : 'black',
      'fill' : 'hollow',
      'marker' : 'circle',
      },
    { 'condor_dir' : 'MuMuNum1PixelHitSelWithCosmics_2016Analysis_CosmicMC_8Feb2021',
      'condor_dir_den' : 'MuMuDen1PixelHitSelWithCosmics_2016Analysis_CosmicMC_8Feb2021',
      'dataset' :   'Cosmics',
      'den_channel' : 'Den1PixelHitSelWithCosmics',
      'num_channel' : 'Num1PixelHitSelWithCosmics',
      'legend_entry' : 'Cosmic MC',
      'color' : 'red',
      'fill' : 'solid',
      'marker' : 'square',
      },
]
