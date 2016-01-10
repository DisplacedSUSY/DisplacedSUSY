#!/usr/bin/env python
intLumi = 19800

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

cutName = 'trigger'

input_sources = [
    { 'condor_dir' : 'triggerEfficiencyTest',
      'condor_dir_den' : '
      'dataset' : 'stop400_100.0mm_br50',
      'den_channel' : 'NoTrigger',
      'num_channel' : 'Mu22Photon22',
      'legend_entry' : '#epsilon of HLT_Mu22_Photon22_CaloIdL_v',
      'color' : 'red',
    },
    { 'condor_dir' : 'triggerEfficiencyTest',
      'dataset' : 'stop400_100.0mm_br50',
      'den_channel' : 'NoTrigger',
      'num_channel' : 'Mu30Ele30',
      'legend_entry' : '#epsilon of HLT_Mu30_Ele30_CaloIdL_v',
      'color' : 'green',
    },
]
