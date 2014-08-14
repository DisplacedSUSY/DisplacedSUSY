#!/usr/bin/env python

scondor_dir1='PreselectionMoreCTau'
scondor_dir2='ClosureTest_M_Allctau_All'
sdataset='ToBeSet'

input_histograms = [
    { 'condor_dir' : scondor_dir1,
      'dataset' : sdataset,
      'channel' : 'Preselection',
      'name' : 'muonPt_smartBin',
      'legend_entry' : 'reco muons',
      'color' : 2,
    },
    { 'condor_dir' : scondor_dir2,
      'dataset' : sdataset,
      'channel' : 'Preselection_GenLevel',
      'name' : 'secondaryMcparticlePt_smartBin',
      'legend_entry' : 'gen level muons',
      'color' : 3,
    },
]
