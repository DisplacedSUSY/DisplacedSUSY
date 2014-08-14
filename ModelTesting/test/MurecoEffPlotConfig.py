#!/usr/bin/env python
#sdataset='allSample'
sdataset='ToBeSet'
scondor_dir='ModelTestingMoreCTau'

input_histograms = [
    { 'condor_dir' : scondor_dir,
      'dataset' : sdataset,
      'channel_denominator' : 'SecondaryMcPartInitial',
      'channel_numerator' : 'SecondaryMcPartInitial_OneRecoMu',
      'name' : 'secondaryMcparticleAbsD0Beamspot',
      'legend_entry' : 'Muon_cuts',
      'color': 1,
    },
]
