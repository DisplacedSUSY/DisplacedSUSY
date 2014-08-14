#!/usr/bin/env python
#sdataset='allSample'
sdataset='ToBeSet'
scondor_dir='ModelTestingMoreCTau'

input_histograms = [
    { 'condor_dir' : scondor_dir,
      'dataset' : sdataset,
      'channel_denominator' : 'McPartInitial',
      'channel_numerator' : 'McPartInitial_OneRecoEl',
      'name' : 'mcparticleAbsD0Beamspot',
      'legend_entry' : 'Electron_cuts',
      'color': 1,
    },
]
