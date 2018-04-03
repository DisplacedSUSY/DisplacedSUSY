#!/usr/bin/env python

# input info
input_file    = "/data/users/bcardwell/condor/EMu_Sidebands_18_01_15/MuonEG_2016_postHIP.root"
electron_hist = "PreselectionPromptMuonPlotter/Electron-muon Plots/electronAbsD0_vs_muonAbsD0_10cm"
muon_hist     = "PreselectionPromptElectronPlotter/Electron-muon Plots/electronAbsD0_vs_muonAbsD0_10cm"

# output info
out_file = "BackgroundEstimate.root"
out_hist = "electronAbsD0_vs_muonAbsD0_10cm"

# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data
bin_edges_e   = [0.00, 0.02, 0.05, 0.10, 10.00]
bin_edges_mu  = [0.00, 0.02, 0.05, 0.10, 10.00]
