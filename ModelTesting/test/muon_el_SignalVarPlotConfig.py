#!/usr/bin/env python

sdataset='ToBeSet'
scondor_dir='ModelTesting_FactoriszedAcceptanceCut'

input_histograms = [
    { 'condor_dir' : scondor_dir,
      'dataset' : sdataset,
      'channel_numerator' : 'SignalGenMatching_Electron_cuts',
      'channel_denominator' : 'SignalGenMatching',
      'name' : 'mcparticlePt',
      'legend_entry' : 'electrons',
      'color' : 2,
    },
    { 'condor_dir' : scondor_dir,
      'dataset' : sdataset,
      'channel_numerator' : 'SignalGenMatching_Muon_cuts',
      'channel_denominator' : 'SignalGenMatching',
      'name' : 'secondaryMcparticlePt',
      'legend_entry' : 'muons',
      'color' : 3,
    },
]
