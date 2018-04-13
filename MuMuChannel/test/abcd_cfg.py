#!/usr/bin/env python

# input info
input_file = "/data/users/bcardwell/condor/MuMu_Preselection_18_04_10/Background.root"
hist_x     = "PreselectionPlotter/Muon Plots/muonAbsD0[0]_vs_muonAbsD0[1]_10cm"
hist_y     = "PreselectionPlotter/Muon Plots/muonAbsD0[0]_vs_muonAbsD0[1]_10cm"
# Were the histograms constructed with the variable bin constructor? i.e. TH1(name,title,nbins,xbins)   
x_variable_bins = True
y_variable_bins = True

# output info
out_file = "BackgroundEstimate.root"
out_hist = "muonLeadingAbsD0_vs_muonSubleadingAbsD0_10cm"
x_axis_title = "Subleading muon |d_{0}| [cm]"
y_axis_title = "Leading muon |d_{0}| [cm]"

# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data
bin_edges_x = [0.000, 0.002, 0.004, 0.006, 0.014, 0.118, 10.000]
bin_edges_y = [0.000, 0.002, 0.004, 0.006, 0.014, 0.118, 10.000]
