#!/usr/bin/env python

# input info
input_file = "/data/users/bcardwell/condor/EMu_Preselection_18_04_10/Background.root"
hist_x     = "PreselectionPlotter/Electron-muon Plots/electronLeadingAbsD0_vs_muonLeadingAbsD0_10cm"
hist_y     = "PreselectionPlotter/Electron-muon Plots/electronLeadingAbsD0_vs_muonLeadingAbsD0_10cm"

# output info
out_file = "BackgroundEstimate.root"
out_hist = "electronLeadingAbsD0_vs_muonLeadingAbsD0_10cm"
x_axis_title = "Leading muon |d_{0}| [cm]"
y_axis_title = "Leading electron |d_{0}| [cm]"

# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data
bin_edges_x = [0.000, 0.002, 0.004, 0.006, 0.014, 0.118, 10.000]
bin_edges_y = [0.000, 0.002, 0.008, 0.020, 0.072, 10.000]
