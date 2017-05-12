#! /usr/bin/env python

input_sources = [
    { 'condor_dir' : 'EMuPreselection_MC_Dec9',
      'dataset'    : 'DYJetsToLL_50.root',
      'channel'    : 'Preselection',
      'hist_dir'   : 'Electron-muon-beamspot Plots',
      'hist'       : 'electronAbsD0_vs_muonAbsD0_500um',
    },

    { 'condor_dir' : 'EMuPreselection_MC_Dec9',
      'dataset'    : 'Diboson.root',
      'channel'    : 'Preselection',
      'hist_dir'   : 'Electron-muon-beamspot Plots',
      'hist'       : 'electronAbsD0_vs_muonAbsD0_500um',
    }
]
