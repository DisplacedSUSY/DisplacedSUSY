#! /usr/bn/env python
#run with makeEfficiencyPlots.py -l triggerEfficiencyPlot_UL2016_cfg.py
intLumi = 16146.2 # 2016G,H only

###################
# 'color' options #
###################
## 'black'
## 'red'
## 'green'
## 'purple'
## 'blue'
## 'yellow'
## default: cycle through list


####################
# 'marker' options #
####################
## 'circle'
## 'square'
## 'triangle'
## default: 'circle'

####################
#  'fill' options  #
####################
## 'solid'
## 'hollow'
## default: 'solid'

#cutName = 'trigger'
cutName = 'L1 trigger'

input_sources = [
    #HLT efficiency with basic e-mu reco selection
    #{
     #   'condor_dir'   : 'EMuSkimTrigTurnOn_UL2016_6May2020',
     #   'dataset'      : 'stopToLB300_1000mm',
     #   'den_channel'  : 'EMuSkimWithoutTrigger',
     #   'num_channel'  : 'EMuSkim',
     #   'legend_entry' : 'RunIIAutum16MiniAODv2',
     #   'marker'       : 'circle',
     #   'color'        : 'black',
    #},
    #{
     #   'condor_dir'   : 'EMuSkimTrigTurnOn_UL2016_6May2020',
     #   'dataset'      : 'stopToLB300_1000mm_preVFP',
     #   'den_channel'  : 'EMuSkimWithoutTrigger',
     #   'num_channel'  : 'EMuSkim',
     #   'legend_entry' : 'UL2016, preVFP',
     #   'marker'       : 'square',
     #   'color'        : 'red',
    #},
    #{
     #   'condor_dir'   : 'EMuSkimTrigTurnOn_UL2016_6May2020',
     #   'dataset'      : 'stopToLB300_1000mm_postVFP',
     #   'den_channel'  : 'EMuSkimWithoutTrigger',
     #   'num_channel'  : 'EMuSkim',
     #   'legend_entry' : 'UL2016, postVFP',
     #   'marker'       : 'triangle',
     #   'color'        : 'blue',
    #},

    #HLT efficiency with basic e-mu gen selection
   # {
   #     'condor_dir_den'   : 'GenEMuFromStopsEle_UL2016_10June2020',
   #     'condor_dir'       : 'GenEMuFromStopsEleAndHLTTrig_UL2016_10June2020',
   #     'den_channel'      : 'GenEMuFromStopsEleSelection',
   #     'num_channel'      : 'GenEMuFromStopsEleAndHLTTrigSelection',
   #     'dataset'          : 'stopToLB300_1000mm',
   #     'legend_entry'     : 'RunIIAutum16MiniAODv2',
   #     'marker'           : 'circle',
   #     'color'            : 'black',
   # },
   # {
   #     'condor_dir_den'   : 'GenEMuFromStopsEle_UL2016_10June2020',
   #     'condor_dir'       : 'GenEMuFromStopsEleAndHLTTrig_UL2016_10June2020',
   #     'den_channel'      : 'GenEMuFromStopsEleSelection',
   #     'num_channel'      : 'GenEMuFromStopsEleAndHLTTrigSelection',
   #     'dataset'          : 'stopToLB300_1000mm_preVFP',
   #     'legend_entry'     : 'UL2016, preVFP',
   #     'marker'           : 'square',
   #     'color'            : 'red',
   # },
   # {
   #     'condor_dir_den'   : 'GenEMuFromStopsEle_UL2016_10June2020',
   #     'condor_dir'       : 'GenEMuFromStopsEleAndHLTTrig_UL2016_10June2020',
   #     'den_channel'      : 'GenEMuFromStopsEleSelection',
   #     'num_channel'      : 'GenEMuFromStopsEleAndHLTTrigSelection',
   #     'dataset'          : 'stopToLB300_1000mm_postVFP',
   #     'legend_entry'     : 'UL2016, postVFP',
   #     'marker'           : 'triangle',
   #     'color'            : 'blue',
   # },


     #L1 efficiency with basic e-mu gen selection
     {
        'condor_dir_den'   : 'GenEMuFromStopsEle_UL2016_10June2020',
        'condor_dir'       : 'GenEMuFromStopsEleAndL1Trig_UL2016_10June2020',
        'den_channel'      : 'GenEMuFromStopsEleSelection',
        'num_channel'      : 'GenEMuFromStopsEleAndL1TrigSelection',
        'dataset'          : 'stopToLB300_1000mm',
        'legend_entry'     : 'RunIIAutum16MiniAODv2',
        'marker'           : 'circle',
        'color'            : 'black',
     },
     {
        'condor_dir_den'   : 'GenEMuFromStopsEle_UL2016_10June2020',
        'condor_dir'       : 'GenEMuFromStopsEleAndL1Trig_UL2016_10June2020',
        'den_channel'      : 'GenEMuFromStopsEleSelection',
        'num_channel'      : 'GenEMuFromStopsEleAndL1TrigSelection',
        'dataset'          : 'stopToLB300_1000mm_preVFP',
        'legend_entry'     : 'UL2016, preVFP',
        'marker'           : 'square',
        'color'            : 'red',
     },
     {
         'condor_dir_den'   : 'GenEMuFromStopsEle_UL2016_10June2020',
         'condor_dir'       : 'GenEMuFromStopsEleAndL1Trig_UL2016_10June2020',
         'den_channel'      : 'GenEMuFromStopsEleSelection',
         'num_channel'      : 'GenEMuFromStopsEleAndL1TrigSelection',
         'dataset'          : 'stopToLB300_1000mm_postVFP',
         'legend_entry'     : 'UL2016, postVFP',
         'marker'           : 'triangle',
         'color'            : 'blue',
     },


]
