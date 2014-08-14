#!/usr/bin/env python
#sdataset='allSample'
sdataset='ToBeSet'
scondor_dir='ModelTestingMoreCTau'

input_histograms = [
    { 'condor_dir' : scondor_dir,
      'dataset' : sdataset,
      'channel_denominator' : 'McPartInitial_OneRecoEl',
      'channel_numerator' : 'McPartInitial_OneRecoEl_Electron_cuts',
      'name' : 'mcparticlePt_smartBin',
      'legend_entry' : 'Electron_cuts',
      'color': 1,
    },

]
