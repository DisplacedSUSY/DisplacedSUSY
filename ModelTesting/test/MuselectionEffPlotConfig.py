#!/usr/bin/env python
#sdataset='allSample'
sdataset='ToBeSet'
scondor_dir='ModelTestingMoreCTau'

input_histograms = [
    { 'condor_dir' : scondor_dir,
      'dataset' : sdataset,
      'channel_denominator' : 'SecondaryMcPartInitial_OneRecoMu',
      'channel_numerator' : 'SecondaryMcPartInitial_OneRecoMu_Muon_cuts',
      'name' : 'secondaryMcparticlePt_smartBin',
      'legend_entry' : 'Muon_cuts',
      'color': 1,
    },
]
