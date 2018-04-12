#!/usr/bin/env python

# input info
input_file = "/data/users/bcardwell/condor/EE_Preselection_18_04_10/Background.root"
hist_x     = "PreselectionPlotter/Electron Plots/electronAbsD0[0]_vs_electronAbsD0[1]_10cm"
hist_y     = "PreselectionPlotter/Electron Plots/electronAbsD0[0]_vs_electronAbsD0[1]_10cm"

# output info
out_file = "BackgroundEstimate.root"
out_hist = "electronLeadingAbsD0_vs_electronSubleadingAbsD0_10cm"
x_axis_title = "subleading electron |d0| [cm]"
y_axis_title = "leading electron |d0| [cm]"

# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data
bin_edges_x = [0.000, 0.002, 0.008, 0.020, 0.072, 10.000]
bin_edges_y = [0.000, 0.002, 0.008, 0.020, 0.072, 10.000]
