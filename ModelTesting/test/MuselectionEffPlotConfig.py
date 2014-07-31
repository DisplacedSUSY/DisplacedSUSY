#!/usr/bin/env python
#sdataset='allSample'
sdataset='ToBeSet'
scondor_dir='modelTesting_check'

input_histograms = [
    { 'condor_dir' : scondor_dir,
      'dataset' : sdataset,
      'channel_numerator' : 'SignalGenMatching_KynCuts_CrossCuts_oneRecoMu_Muon_cuts',
      'channel_denominator' : 'SignalGenMatching_KynCuts_CrossCuts_oneRecoMu',
      'name' : 'secondaryMcparticlePt',
      'legend_entry' : 'Muon_cuts',
      'color': 1,
    },
]
