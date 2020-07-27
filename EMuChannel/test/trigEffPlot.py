#!/usr/bin/env python
from DisplacedSUSY.EMuChannel.localOptions import *

cutName = 'trigger'
input_sources = [
    { 'condor_dir' : 'EMuTrigEff_HighPtEle_2018Analysis_17July2020',
      'dataset' :   'MET_2018',
      'den_channel' : 'TrigEffHighPtEleDen',
      'num_channel' : 'TrigEffHighPtEleNum',
      'legend_entry' : 'Data',
      'color' : 'black',
      'fill' : 'hollow',
      'marker' : 'circle',
      },
    { 'condor_dir' : 'EMuTrigEff_HighPtEle_2018Analysis_17July2020',
      'dataset' :   'TTJets_Lept',
      'den_channel' : 'TrigEffHighPtEleDen',
      'num_channel' : 'TrigEffHighPtEleNum',
      'legend_entry' : 't#bar{t}',
      'color' : 'red',
      'fill' : 'solid',
      'marker' : 'square',
      },
]
