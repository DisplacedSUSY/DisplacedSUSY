#!/usr/bin/env python

# input info - be careful if running over preselection data while still blinded
#input_file = "/uscms_data/d3/cardwell/condor/EEPreselection_2016Analysis_24July2018/Background.root"
input_file = "/uscms_data/d3/cardwell/condor/EEPreselection_2017Analysis_26July2018/Background.root"
input_hist = "PreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_100000um"

# Was the histogram constructed with the variable bin constructor? i.e. TH2(name,title,nbinsx,xbins,nbinsy,ybins)
variable_bins = True

# output info
output_file  = "BackgroundABCDEstimate.root"
x_axis_title = "Subleading electron |d_{0}| [#mum]"
y_axis_title = "Leading electron |d_{0}| [#mum]"

# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data
bins_x = [50, 60, 220, 480, 1600, 100000] #Bartsch and Quast |d0| optimization, starting at 50 microns
bins_y = [50, 60, 220, 480, 1600, 100000]
