#!/usr/bin/env python
from DisplacedSUSY.EMuChannel.localOptions import *

cutName = 'trigger'
input_sources = [
   # { 'condor_dir_den' : 'EMuTrigEff_HighPtEleDen_2018Analysis_5Jan2021',
   #   'condor_dir' : 'EMuTrigEff_HighPtEleNum_2018Analysis_5Jan2021',
   #   'dataset' :   'MET_2018',
   # { 'condor_dir_den' : 'EMuTrigEff_HighPtEleDen_2017Analysis_13Jan2021',
   #   'condor_dir' : 'EMuTrigEff_HighPtEleNum_2017Analysis_12Jan2021',
   #   'dataset' :   'MET_2017_withoutB',
   # { 'condor_dir_den' : 'EMuTrigEff_HighPtEleDen_2016Analysis_13Jan2021',
   #   'condor_dir' : 'EMuTrigEff_HighPtEleNum_2016Analysis_13Jan2021',
   #   'dataset' :   'MET_2016_postHIP',
   #   'den_channel' : 'TrigEffHighPtEleDen',
   #   'num_channel' : 'TrigEffHighPtEleNum',
   #   'legend_entry' : 'Data',
   #   'color' : 'black',
   #   'fill' : 'hollow',
   #   'marker' : 'circle',
   #   },

   # { 'condor_dir_den' : 'EMuTrigEff_HighPtEleDen_2018Analysis_5Jan2021',
   #   'condor_dir' : 'EMuTrigEff_HighPtEleNum_2018Analysis_5Jan2021',
   # { 'condor_dir_den' : 'EMuTrigEff_HighPtEleDen_2017Analysis_13Jan2021',
   #   'condor_dir' : 'EMuTrigEff_HighPtEleNum_2017Analysis_12Jan2021',
   # { 'condor_dir_den' : 'EMuTrigEff_HighPtEleDen_2016Analysis_13Jan2021',
   #   'condor_dir' : 'EMuTrigEff_HighPtEleNum_2016Analysis_13Jan2021',
   #   'dataset' :   'TTJets_Lept',
   #   'den_channel' : 'TrigEffHighPtEleDen',
   #   'num_channel' : 'TrigEffHighPtEleNum',
   #   'legend_entry' : 't#bar{t}',
   #   'color' : 'red',
   #   'fill' : 'solid',
   #   'marker' : 'square',
   #   },


   # { 'condor_dir_den' : 'EMuTrigEff_HighPtMuDen_2018Analysis_7Jan2021',
   #   'condor_dir' : 'EMuTrigEff_HighPtMuNum_2018Analysis_6Jan2021',
   #   'dataset' :   'MET_2018',
   # { 'condor_dir_den' : 'EMuTrigEff_HighPtMuDen_2017Analysis_13Jan2021',
   #   'condor_dir' : 'EMuTrigEff_HighPtMuNum_2017Analysis_13Jan2021',
   #   'dataset' :   'MET_2017_withoutB',
    { 'condor_dir_den' : 'EMuTrigEff_HighPtMuDen_2016Analysis_15Jan2021',
      'condor_dir' : 'EMuTrigEff_HighPtMuNum_2016Analysis_15Jan2021',
      'dataset' :   'MET_2016_postHIP',
      'den_channel' : 'TrigEffHighPtMuDen',
      'num_channel' : 'TrigEffHighPtMuNum',
      'legend_entry' : 'Data',
      'color' : 'black',
      'fill' : 'hollow',
      'marker' : 'circle',
      },
   # { 'condor_dir_den' : 'EMuTrigEff_HighPtMuDen_2018Analysis_7Jan2021',
   #   'condor_dir' : 'EMuTrigEff_HighPtMuNum_2018Analysis_6Jan2021',
   # { 'condor_dir_den' : 'EMuTrigEff_HighPtMuDen_2017Analysis_13Jan2021',
   #   'condor_dir' : 'EMuTrigEff_HighPtMuNum_2017Analysis_13Jan2021',
    { 'condor_dir_den' : 'EMuTrigEff_HighPtMuDen_2016Analysis_15Jan2021',
      'condor_dir' : 'EMuTrigEff_HighPtMuNum_2016Analysis_15Jan2021',
      'dataset' :   'TTJets_Lept',
      'den_channel' : 'TrigEffHighPtMuDen',
      'num_channel' : 'TrigEffHighPtMuNum',
      'legend_entry' : 't#bar{t}',
      'color' : 'red',
      'fill' : 'solid',
      'marker' : 'square',
      },

  #  { 'condor_dir_den' : 'EMuTrigEff_DenInPtPlateau_2018Analysis_3Aug2020',
  #    'condor_dir' : 'EMuTrigEff_NumInPtPlateau_2018Analysis_31July2020',
  #    'dataset' :   'MET_2018',
  #    'den_channel' : 'TrigEffDenInPtPlateau',
  #    'num_channel' : 'TrigEffNumInPtPlateau',
  #    'legend_entry' : 'Data',
  #    'color' : 'black',
  #    'fill' : 'hollow',
  #    'marker' : 'circle',
  #    },

  #  { 'condor_dir_den' : 'EMuTrigEff_DenInPtPlateau_2018Analysis_3Aug2020',
  #    'condor_dir' : 'EMuTrigEff_NumInPtPlateau_2018Analysis_31July2020',
  #    'dataset' :   'stopToLB200_1000mm',
  #    'den_channel' : 'TrigEffDenInPtPlateau',
  #    'num_channel' : 'TrigEffNumInPtPlateau',
  #    'legend_entry' : '#tilde{t}#tilde{t}#rightarrow lb lb, M=200 GeV, c#tau=1000 mm',
  #    'color' : 'black',
  #    'fill' : 'hollow',
  #    'marker' : 'circle',
  #    },
  #  { 'condor_dir_den' : 'EMuTrigEff_DenInPtPlateau_2018Analysis_3Aug2020',
  #    'condor_dir' : 'EMuTrigEff_NumInPtPlateau_2018Analysis_31July2020',
  #    'dataset' :   'stopToLB1000_1000mm',
  #    'den_channel' : 'TrigEffDenInPtPlateau',
  #    'num_channel' : 'TrigEffNumInPtPlateau',
  #    'legend_entry' : '#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=1000 mm',
  #    'color' : 'red',
  #    'fill' : 'solid',
  #    'marker' : 'square',
  #    },
  #  { 'condor_dir_den' : 'EMuTrigEff_DenInPtPlateau_2018Analysis_3Aug2020',
  #    'condor_dir' : 'EMuTrigEff_NumInPtPlateau_2018Analysis_31July2020',
  #    'dataset' :   'stopToLB1800_1000mm',
  #    'den_channel' : 'TrigEffDenInPtPlateau',
  #    'num_channel' : 'TrigEffNumInPtPlateau',
  #    'legend_entry' : '#tilde{t}#tilde{t}#rightarrow lb lb, M=1800 GeV, c#tau=1000 mm',
  #    'color' : 'blue',
  #    'fill' : 'solid',
  #    'marker' : 'triangle',
  #    },

]
