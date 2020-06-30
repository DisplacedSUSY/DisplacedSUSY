#!/usr/bin/env python

# input info - be careful if running over preselection data while still blinded
#input_file = "/uscms_data/d3/cardwell/condor/EEPreselection_2016Analysis_24July2018/Background.root"
#input_file = "/uscms_data/d3/cardwell/condor/EEPreselection_2017Analysis_26July2018/Background.root"
input_file = "/uscms_data/d3/alimena/condor/EEAdditionalPreselection_2018Analysis_2June2020/EGamma_2018.root"
#input_file = "/uscms_data/d3/alimena/condor/EEAdditionalPreselection_2018Analysis_2June2020/DYJetsToLL.root"
#input_file = "/uscms_data/d3/alimena/condor/EEAdditionalPreselection_2018Analysis_2June2020/Background.root"
input_hist = "AdditionalPreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_100000um"

# Was the histogram constructed with the variable bin constructor? i.e. TH2(name,title,nbinsx,xbins,nbinsy,ybins)
variable_bins = True

# output info
#output_file  = "BackgroundABCDEstimate_Data.root"
output_file  = "BackgroundABCDClosureTest_Data_startAt0mum_PromptRegion.root"
#output_file  = "BackgroundABCDClosureTest_Data_startAt0mum_DisplacedSubleadingEleRegion.root"
#output_file  = "BackgroundABCDClosureTest_Data_startAt0mum_DisplacedLeadingEleRegion.root"

x_axis_title = "Subleading electron |d_{0}| [#mum]"
y_axis_title = "Leading electron |d_{0}| [#mum]"

# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data
#bins_x = [50, 60, 220, 480, 1600, 100000] #Bartsch and Quast |d0| optimization, starting at 50 microns
#bins_y = [50, 60, 220, 480, 1600, 100000]

#bins_x = [0, 100, 500, 1000, 100000]
#bins_y = [0, 100, 500, 1000, 100000]



# prompt-e/prompt-e region
bins_x = [ 0, 40, 100]
bins_y = [ 0, 40, 100]

# prompt-leading-e/displaced-subleading-e region
#bins_x = [0, 20,  100,  100000]
#bins_y = [0, 20,  40,   100]

# displaced-leading-e/prompt-subleading-e region
#bins_x = [0, 20,  40,   100]
#bins_y = [0, 20, 100,  100000]
