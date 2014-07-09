#!/usr/bin/env python
intLumi = 19680

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

#cutName = 'electron cuts'


if 0 > 1 :
    print "crazy!!!"
    
sdataset='ToBeSet'
scondor_dir='ModelTesting_FactoriszedAcceptanceCut' 

input_histograms = [
    ### Muon d0
    { 'condor_dir' : scondor_dir,
      'dataset' : sdataset,
      'channel_denominator' : 'Preselection_SignalGenMatching',
      'channel_numerator' : 'Preselection_SignalGenMatching_200umMuon',
      'legend_entry' : '200umMuon_cuts',
      'name' : 'secondaryMcparticleAbsD0Beamspot',
      'color' : 3,
      },
    { 'condor_dir' : scondor_dir,
      'dataset' : sdataset,
      'channel_denominator' : 'Preselection_SignalGenMatching',
      'channel_numerator' : 'Preselection_SignalGenMatching_500umMuon',
      'legend_entry' : '500umMuon_cuts',
      'name' : 'secondaryMcparticleAbsD0Beamspot',
      'color' : 2,
    },
    { 'condor_dir' : scondor_dir,
      'dataset' : sdataset,
      'channel_denominator' : 'Preselection_SignalGenMatching',
      'channel_numerator' : 'Preselection_SignalGenMatching_1000umMuon',
      'legend_entry' : '1000umMuon_cuts',
      'name' : 'secondaryMcparticleAbsD0Beamspot',
      'color' : 1,
    },



 ]
