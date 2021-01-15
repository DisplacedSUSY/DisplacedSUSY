#!/usr/bin/env python
from DisplacedSUSY.EMuChannel.localOptions import *

cutName = 'trigger'
input_sources = [
    #{ 'condor_dir' : 'MuMuTrigEff_NoHighPtMuon_2018Analysis_8July2020',
      #'dataset' :   'MET_2018',
    #{ 'condor_dir' : 'MuMuTrigEff_Num_2017Analysis_13Aug2020',
    #  'condor_dir_den' : 'MuMuTrigEff_Den_2017Analysis_15Aug2020',
    #  'dataset' :   'MET_2017_withoutB',
    { 'condor_dir' : 'MuMuTrigEff_Num_2016Analysis_20Aug2020',
      'condor_dir_den' : 'MuMuTrigEff_Den_2016Analysis_20Aug2020',
      'dataset' :   'MET_2016_postHIP',
      'den_channel' : 'TrigEffDen',
      'num_channel' : 'TrigEffNum',
      'legend_entry' : 'Data',
      'color' : 'black',
      'fill' : 'hollow',
      'marker' : 'circle',
      },
    #{ 'condor_dir' : 'MuMuTrigEff_NoHighPtMuon_2018Analysis_8July2020',
    #{ 'condor_dir' : 'MuMuTrigEff_Num_2017Analysis_13Aug2020',
    #  'condor_dir_den' : 'MuMuTrigEff_Den_2017Analysis_15Aug2020',
    { 'condor_dir' : 'MuMuTrigEff_Num_2016Analysis_20Aug2020',
      'condor_dir_den' : 'MuMuTrigEff_Den_2016Analysis_20Aug2020',
      'dataset' :   'DYJetsToLL',
      'den_channel' : 'TrigEffDen',
      'num_channel' : 'TrigEffNum',
      'legend_entry' : 'DY',
      'color' : 'red',
      'fill' : 'solid',
      'marker' : 'square',
      },
]
