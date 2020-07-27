#!/usr/bin/env python
from DisplacedSUSY.EEChannel.localOptions import *

cutName = 'trigger'
input_sources = [
    {   'condor_dir' : 'EETrigEff_NoHighPtEle_2018Analysis_14July2020',
        'dataset' :   'MET_2018',
        'den_channel' : 'TrigEffDen',
        'num_channel' : 'TrigEffNum',
        'legend_entry' : 'Data',
        'color' : 'black',
        'fill' : 'hollow',
        'marker' : 'circle',
    },
    {   'condor_dir' : 'EETrigEff_NoHighPtEle_2018Analysis_14July2020',
        'dataset' : 'DYJetsToLL',
        'den_channel' : 'TrigEffDen',
        'num_channel' : 'TrigEffNum',
        'legend_entry' : 'DY',
        'color' : 'red',
        'fill' : 'solid',
        'marker' : 'square',
    },
]
