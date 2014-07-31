#!/usr/bin/env python
#sdataset='allSample'
sdataset='ToBeSet'
scondor_dir='modelTesting_check'

input_histograms = [
    { 'condor_dir' : scondor_dir,
      'dataset' : sdataset,
      'channel_numerator' : 'SignalGenMatching_KynCuts_CrossCuts_oneRecoEl_Electron_cuts',
      'channel_denominator' : 'SignalGenMatching_KynCuts_CrossCuts_oneRecoEl',
      'name' : 'mcparticlePt',
      'legend_entry' : 'Electron_cuts',
      'color': 1,
    },

]
