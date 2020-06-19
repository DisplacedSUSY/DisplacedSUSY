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

#cutName = 'HLT'
cutName = 'L1'

input_sources = [
    #with simple reco selection for hlt eff vs reco objects
   # {
   #     'condor_dir'   : 'EESkimTrigTurnOn_UL2016_6May2020',
   #     'dataset'      : 'stopToLB300_1000mm',
   #     'den_channel'  : 'EESkimWithoutTrigger',
   #     'num_channel'  : 'EESkim',
   #     'legend_entry' : 'RunIIAutum16MiniAODv2',
   #     'marker'       : 'circle',
   #     'color'        : 'black',
   # },
   # {
   #     'condor_dir'   : 'EESkimTrigTurnOn_UL2016_6May2020',
   #     'dataset'      : 'stopToLB300_1000mm_preVFP',
   #     'den_channel'  : 'EESkimWithoutTrigger',
   #     'num_channel'  : 'EESkim',
   #     'legend_entry' : 'UL2016, preVFP',
   #     'marker'       : 'square',
   #     'color'        : 'red',
   # },
   # {
   #     'condor_dir'   : 'EESkimTrigTurnOn_UL2016_6May2020',
   #     'dataset'      : 'stopToLB300_1000mm_postVFP',
   #     'den_channel'  : 'EESkimWithoutTrigger',
   #     'num_channel'  : 'EESkim',
   #     'legend_entry' : 'UL2016, postVFP',
   #     'marker'       : 'triangle',
   #     'color'        : 'blue',
   # },

    #HLT efficiency with basic ee gen selection
   # {
   #     'condor_dir_den'   : 'GenEEFromStops_UL2016_15June2020',
   #     'condor_dir'       : 'GenEEFromStopsAndHLTTrig_UL2016_15June2020',
   #     'den_channel'      : 'GenEEFromStopsSelection',
   #     'num_channel'      : 'GenEEFromStopsAndHLTTrigSelection',
   #     'dataset'          : 'stopToLB300_1000mm',
   #     'legend_entry'     : 'RunIIAutum16MiniAODv2',
   #     'marker'           : 'circle',
   #     'color'            : 'black',
   # },
   # {
   #     'condor_dir_den'   : 'GenEEFromStops_UL2016_15June2020',
   #     'condor_dir'       : 'GenEEFromStopsAndHLTTrig_UL2016_15June2020',
   #     'den_channel'      : 'GenEEFromStopsSelection',
   #     'num_channel'      : 'GenEEFromStopsAndHLTTrigSelection',
   #     'dataset'          : 'stopToLB300_1000mm_preVFP',
   #     'legend_entry'     : 'UL2016, preVFP',
   #     'marker'           : 'square',
   #     'color'            : 'red',
   # },
   # {
   #     'condor_dir_den'   : 'GenEEFromStops_UL2016_15June2020',
   #     'condor_dir'       : 'GenEEFromStopsAndHLTTrig_UL2016_15June2020',
   #     'den_channel'      : 'GenEEFromStopsSelection',
   #     'num_channel'      : 'GenEEFromStopsAndHLTTrigSelection',
   #     'dataset'          : 'stopToLB300_1000mm_postVFP',
   #     'legend_entry'     : 'UL2016, postVFP',
   #     'marker'           : 'triangle',
   #     'color'            : 'blue',
   # },


     #L1 efficiency with basic ee gen selection
      {
        'condor_dir_den'   : 'GenEEFromStops_UL2016_18June2020',
        'condor_dir'       : 'GenEEFromStopsAndL1Trig_UL2016_18June2020',
        'den_channel'      : 'GenEEFromStopsSelection',
        'num_channel'      : 'GenEEFromStopsAndL1TrigSelection',
        'dataset'          : 'stopToLB300_1000mm',
        'legend_entry'     : 'RunIIAutum16MiniAODv2',
        'marker'           : 'circle',
        'color'            : 'black',
     },
     {
        'condor_dir_den'   : 'GenEEFromStops_UL2016_18June2020',
        'condor_dir'       : 'GenEEFromStopsAndL1Trig_UL2016_18June2020',
        'den_channel'      : 'GenEEFromStopsSelection',
        'num_channel'      : 'GenEEFromStopsAndL1TrigSelection',
        'dataset'          : 'stopToLB300_1000mm_preVFP',
        'legend_entry'     : 'UL2016, preVFP',
        'marker'           : 'square',
        'color'            : 'red',
     },
     {
         'condor_dir_den'   : 'GenEEFromStops_UL2016_18June2020',
         'condor_dir'       : 'GenEEFromStopsAndL1Trig_UL2016_18June2020',
         'den_channel'      : 'GenEEFromStopsSelection',
         'num_channel'      : 'GenEEFromStopsAndL1TrigSelection',
         'dataset'          : 'stopToLB300_1000mm_postVFP',
         'legend_entry'     : 'UL2016, postVFP',
         'marker'           : 'triangle',
         'color'            : 'blue',
     },

]
