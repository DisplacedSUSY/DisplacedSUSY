#!/usr/bin/env python

# input info - be careful if running over preselection data while still blinded
input_file = "/data/users/bcardwell/condor/EMu_Preselection_18_04_10/Background.root"
input_hist = "PreselectionPlotter/Electron-muon Plots/electronLeadingAbsD0_vs_muonLeadingAbsD0_10cm"

# Was the histogram constructed with the variable bin constructor? i.e. TH2(name,title,nbinsx,xbins,nbinsy,ybins)   
variable_bins = True

# output info
output_file  = "Background.root"
x_axis_title = "Leading muon |d_{0}| [cm]"
y_axis_title = "Leading electron |d_{0}| [cm]"

# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data
#bins_x = [0.000, 0.02, 0.05, 0.1, 10.000] #Binning used in 2015 analysis
#bins_y = [0.000, 0.02, 0.05, 0.1, 10.000]

#bins_x = [0.000, 0.002, 0.004, 0.006, 0.014, 0.118, 10.000] #S/sqrt(S+B) |d0| optimization
#bins_y = [0.000, 0.002, 0.008, 0.020, 0.072, 10.000]

#bins_x = [0.000, 0.006, 0.010, 0.076, 0.186, 10.000] #Bartsch and Quast |d0| optimization
#bins_y = [0.000, 0.006, 0.022, 0.048, 0.160, 10.000]

bins_x = [0.005, 0.006, 0.010, 0.076, 0.186, 10.000] #Bartsch and Quast |d0| optimization, starting at 50 microns
bins_y = [0.005, 0.006, 0.022, 0.048, 0.160, 10.000]
