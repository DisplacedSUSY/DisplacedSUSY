#!/usr/bin/env python

# input info - be careful if running over preselection data while still blinded
input_file = "/data/users/bcardwell/condor/MuMu_Preselection_18_04_10/Background.root"
input_hist = "PreselectionPlotter/Muon Plots/muonAbsD0[0]_vs_muonAbsD0[1]_10cm"

# Was the histogram constructed with the variable bin constructor? i.e. TH2(name,title,nbinsx,xbins,nbinsy,ybins)   
variable_bins = True

# output info
output_file  = "BackgroundEstimate.root"
x_axis_title = "Subleading muon |d_{0}| [cm]"
y_axis_title = "Leading muon |d_{0}| [cm]"

# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data
#bins_x = [0.000, 0.02, 0.05, 0.1, 10.000] #Binning used in 2015 analysis
#bins_y = [0.000, 0.02, 0.05, 0.1, 10.000]

#bins_x = [0.000, 0.002, 0.004, 0.006, 0.014, 0.118, 10.000] #S/sqrt(S+B) |d0| optimization
#bins_y = [0.000, 0.002, 0.004, 0.006, 0.014, 0.118, 10.000]

#bins_x = [0.000, 0.006, 0.010, 0.076, 0.186, 10.000] #Bartsch and Quast |d0| optimization
#bins_y = [0.000, 0.006, 0.010, 0.076, 0.186, 10.000]

bins_x = [0.005, 0.006, 0.010, 0.076, 0.186, 10.000] #Bartsch and Quast |d0| optimization, starting at 50 microns
bins_y = [0.005, 0.006, 0.010, 0.076, 0.186, 10.000]
