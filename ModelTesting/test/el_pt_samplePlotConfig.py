#!/usr/bin/env python

scondor_dir1='PreselectionMoreCTau'
scondor_dir2='ClosureTest_M_Allctau_All'
sdataset='ToBeSet'

input_histograms = [
    { 'condor_dir' : scondor_dir1,
      'dataset' : sdataset,
      'channel' : 'Preselection',
      'name' : 'electronPt_smartBin',
      'legend_entry' : 'reco electrons',
      'color' : 2,
    },
    { 'condor_dir' : scondor_dir2,
      'dataset' : sdataset,
      'channel' : 'Preselection_GenLevel',
      'name' : 'mcparticlePt_smartBin',
      'legend_entry' : 'gen level electrons',
      'color' : 3,
    },
]
