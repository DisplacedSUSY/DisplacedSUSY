#!/usr/bin/env python
from DisplacedSUSY.EEChannel.localOptions import *

cutName = 'trigger'
input_sources = [
  #  { 'condor_dir_den' : 'EETrigEff_Den_2018Analysis_10Jan2021',
  #    'condor_dir' : 'EETrigEff_Num_2018Analysis_10Jan2021',
  #      'dataset' :   'MET_2018',
  #  { 'condor_dir_den' : 'EETrigEff_Den_2017Analysis_13Jan2021',
  #    'condor_dir' : 'EETrigEff_Num_2017Analysis_13Jan2021',
  #    'dataset' :   'MET_2017',
  #  { 'condor_dir_den' : 'EETrigEff_Den_2016Analysis_16Jan2021',
  #    'condor_dir' : 'EETrigEff_Num_2016Analysis_16Jan2021',
  #    'dataset' :   'MET_2016_postHIP',
  #    'den_channel' : 'TrigEffDen',
  #    'num_channel' : 'TrigEffNum',
  #    'legend_entry' : 'Data',
  #    'color' : 'black',
  #    'fill' : 'hollow',
  #    'marker' : 'circle',
    #},
  #  { 'condor_dir_den' : 'EETrigEff_Den_2018Analysis_10Jan2021',
  #    'condor_dir' : 'EETrigEff_Num_2018Analysis_10Jan2021',
  #  { 'condor_dir_den' : 'EETrigEff_Den_2017Analysis_13Jan2021',
  #    'condor_dir' : 'EETrigEff_Num_2017Analysis_13Jan2021',
  #  { 'condor_dir_den' : 'EETrigEff_Den_2016Analysis_16Jan2021',
  #    'condor_dir' : 'EETrigEff_Num_2016Analysis_16Jan2021',
  #    'dataset' : 'DYJetsToLL',
  #    'den_channel' : 'TrigEffDen',
  #    'num_channel' : 'TrigEffNum',
  #    'legend_entry' : 'DY',
  #    'color' : 'red',
  #    'fill' : 'solid',
  #    'marker' : 'square',
    #},


  #  {   'condor_dir_den' : 'EETrigEff_DenInPtPlateau_2018Analysis_30July2020',
  #      'condor_dir' : 'EETrigEff_NumInPtPlateau_2018Analysis_30July2020',
  #      'dataset' :   'MET_2018',
   #     'den_channel' : 'TrigEffDenInPtPlateau',
   #     'num_channel' : 'TrigEffNumInPtPlateau',
   #     'legend_entry' : 'Data',
   #     'color' : 'black',
   #     'fill' : 'hollow',
   #     'marker' : 'circle',
   # },


 #  {   'condor_dir_den' : 'EETrigEff_DenInPtPlateau_2018Analysis_30July2020',
 #      'condor_dir' : 'EETrigEff_NumInPtPlateau_2018Analysis_30July2020',
 #      'dataset' :   'stopToLB200_1000mm',
 #      'den_channel' : 'TrigEffDenInPtPlateau',
 #      'num_channel' : 'TrigEffNumInPtPlateau',
 #      'legend_entry' : '#tilde{t}#tilde{t}#rightarrow lb lb, M=200 GeV, c#tau=1000 mm',
 #      'color' : 'black',
 #      'fill' : 'solid',
 #      'marker' : 'circle',
 #  },

 #  {   'condor_dir_den' : 'EETrigEff_DenInPtPlateau_2018Analysis_30July2020',
 #      'condor_dir' : 'EETrigEff_NumInPtPlateau_2018Analysis_30July2020',
 #      'dataset' :   'stopToLB1000_1000mm',
 #      'den_channel' : 'TrigEffDenInPtPlateau',
 #      'num_channel' : 'TrigEffNumInPtPlateau',
 #      'legend_entry' : '#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=1000 mm',
 #      'color' : 'red',
 #      'fill' : 'hollow',
 #      'marker' : 'square',
 #  },

 #   {   'condor_dir_den' : 'EETrigEff_DenInPtPlateau_2018Analysis_30July2020',
 #       'condor_dir' : 'EETrigEff_NumInPtPlateau_2018Analysis_30July2020',
 #       'dataset' :   'stopToLB1800_1000mm',
 #       'den_channel' : 'TrigEffDenInPtPlateau',
 #       'num_channel' : 'TrigEffNumInPtPlateau',
 #       'legend_entry' : '#tilde{t}#tilde{t}#rightarrow lb lb, M=1800 GeV, c#tau=1000 mm',
 #       'color' : 'blue',
    #      'fill' : 'solid',
 #       'marker' : 'triangle',
 #   },





    { 'condor_dir_den' : 'EETrigEff_DenD0GreaterThan10_2018Analysis_31Mar2021',
      'condor_dir' : 'EETrigEff_NumD0GreaterThan10_2018Analysis_31Mar2021',
        'dataset' :   'MET_2018',
  #  { 'condor_dir_den' : '',
  #    'condor_dir' : '',
  #    'dataset' :   'MET_2017',
  #  { 'condor_dir_den' : '',
  #    'condor_dir' : '',
  #    'dataset' :   'MET_2016_postHIP',
      'den_channel' : 'TrigEffDenD0GreaterThan10',
      'num_channel' : 'TrigEffNumD0GreaterThan10',
      'legend_entry' : 'Data',
      'color' : 'black',
      'fill' : 'hollow',
      'marker' : 'circle',
    },
    { 'condor_dir_den' : 'EETrigEff_DenD0GreaterThan10_2018Analysis_31Mar2021',
      'condor_dir' : 'EETrigEff_NumD0GreaterThan10_2018Analysis_31Mar2021',
  #  { 'condor_dir_den' : '',
  #    'condor_dir' : '',
  #  { 'condor_dir_den' : '',
  #    'condor_dir' : '',
      'dataset' : 'DYJetsToLL',
      'den_channel' : 'TrigEffDenD0GreaterThan10',
      'num_channel' : 'TrigEffNumD0GreaterThan10',
      'legend_entry' : 'DY',
      'color' : 'red',
      'fill' : 'solid',
      'marker' : 'square',
    },

]
