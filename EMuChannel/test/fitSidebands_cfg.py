#!/usr/bin/env python

# output info
th2_name = "electronAbsD0_vs_muonAbsD0_10cm"

# input info
sidebands = {
  "x" : {
    "name"  : "muon |d0| [cm]",
    "unit"  : "cm",
    "depth" : 0.02, # sideband depth in same units as input hist
    "bins"  : [0.00, 0.02, 0.05, 0.10, 10.00],
    "prompt" : {
      "file" : "/data/users/bcardwell/condor/MuMu_ZCR_18_02_07/DoubleMu_2016_postHIP.root",
      "hist" : "ZControlRegionPlotter/Muon Plots/muonAbsD0_10cm",
      "name" : "Prompt Muon Background",
    },
    "displaced" : {
      "file" : "/data/users/bcardwell/condor/QCDMuonCR_Mu50_noSkim_18_03_02/SingleMu_2016_postHIP.root",
      "hist" : "QCDMuonControlRegionPlotter/Muon Plots/muonAbsD0_10cm",
      "name" : "Displaced Muon Background",
    },
    "sideband" : {
      "file" : "/data/users/bcardwell/condor/EMu_Sidebands_18_01_15/MuonEG_2016_postHIP.root",
      "hist" : "PreselectionPromptElectronPlotter/Electron-muon Plots/electronAbsD0_vs_muonAbsD0_10cm",
      "name" : "Muon Sideband",
    },
  },
  "y" : {
    "name"  : "electron |d0| [cm]",
    "unit"  : "cm",
    "depth" : 0.02, # sideband depth in same units as input hist
    "bins"  : [0.00, 0.02, 0.05, 0.10, 10.00],
    "prompt" : {
      "file" : "/data/users/bcardwell/condor/EE_ZCR_18_02_07/DoubleEG_2016_postHIP.root",
      "hist" : "ZControlRegionPlotter/Electron Plots/electronAbsD0_10cm",
      "name" : "Prompt Electron Background",
    },
    "displaced" : {
      "file" : "/data/users/bcardwell/condor/QCDElectronCR_El27_18_03_12/SingleEle_2016_postHIP.root",
      "hist" : "QCDElectronControlRegionPlotter/Electron Plots/electronAbsD0_10cm",
      "name" : "Displaced Electron Background",
    },
    "sideband" : {
      "file" : "/data/users/bcardwell/condor/EMu_Sidebands_18_01_15/MuonEG_2016_postHIP.root",
      "hist" : "PreselectionPromptMuonPlotter/Electron-muon Plots/electronAbsD0_vs_muonAbsD0_10cm",
      "name" : "Muon Sideband",
    },
  }
}
