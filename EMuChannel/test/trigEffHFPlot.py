#!/usr/bin/env python
from DisplacedSUSY.EMuChannel.localOptions import *

cutName = 'trigger'
input_sources = [

    { 'condor_dir_den' : 'EMuHFTrigEff_MuDen_2018Analysis_9Jan2021',
      'condor_dir' : 'EMuHFTrigEff_MuNum_2018Analysis_26Jan2021',
      'dataset' :   'MET_2018',
      'den_channel' : 'TrigEffHFHighPtEleDen',
      'num_channel' : 'TrigEffHFHighPtEleNum',
      'legend_entry' : 'Data',
      'color' : 'black',
      'fill' : 'hollow',
      'marker' : 'circle',
      },

    { 'condor_dir_den' : 'EMuHFTrigEff_MuDen_2018Analysis_9Jan2021',
      'condor_dir' : 'EMuHFTrigEff_MuNum_2018Analysis_26Jan2021',
      'dataset' :   'QCD_MuEnriched',
      'den_channel' : 'TrigEffHFHighPtEleDen',
      'num_channel' : 'TrigEffHFHighPtEleNum',
      'legend_entry' : '#mu-enriched QCD',
      'color' : 'red',
      'fill' : 'solid',
      'marker' : 'square',
      },

]
