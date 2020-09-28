#!/usr/bin/env python
from DisplacedSUSY.Configuration.limitOptions import *

channel = "ee"

# choose how inclusive signal region will be divided; current options are 'L', 'L_inv', and 'grid'
sr_shapes = 'grid'
# signal region binning; enter -1 to include overflow
d0_0_bin_edges = [100, 500, 100000] # um
d0_1_bin_edges = [100, 500, 100000] # um
pt_bin_edges = [0, 300, -1] # GeV
# |d0| range of prompt lepton in prompt/displaced control regions
cr_d0_range = (20, 100) # um

# multiplicative corrections to account for correlation; enter as (value, one-sigma uncertainty)
# only list regions in which you want to apply a correction
abcd_correlation_factors = {}

# fixme: abcd systematics specified here temporarily
# systematic uncertainty on abcd estimate in each signal region (e.g. 0.5 = 50% uncertainty)
# only list regions in which you want to apply a systematic (as opposed to a correction)
abcd_systematics = {
    'SR_100to500um_100to500um_0to300GeV'         : 0.10,
    'SR_100to500um_500to100000um_0to300GeV'      : 0.10,
    'SR_500to100000um_100to500um_0to300GeV'      : 0.10,
    'SR_500to100000um_500to100000um_0to300GeV'   : 0.10,
    'SR_100to500um_100to500um_300toInfGeV'       : 0.10,
    'SR_100to500um_500to100000um_300toInfGeV'    : 0.10,
    'SR_500to100000um_100to500um_300toInfGeV'    : 0.10,
    'SR_500to100000um_500to100000um_300toInfGeV' : 0.10,
}

# one will generally want to use the same histogram for signal and data
# this can be overridden in individual dictionaries if desired
hist = 'PreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_100000um_vs_electronPt[0]'

data = {
    'name' : 'DoubleEG_2016_2017_2018',
    'dir'  : 'EEBackgroundEstimates_RunII_11Sep2020',
    'file' : 'DoubleEG_2016_2017_2018.root',
    'hist' : hist,
    'var_bins' : True,
    'blinded'  : True,
}

# a separate datacard will be produced for each signal point
# list separate dictionaries for each year; they will be combined by makeAbcdDatacards if necessary
signal_samples = {
    '2016' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EEPreselection_2016Analysis_94X_StopToLBMajorPoints_11Sept2020',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2017' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EEPreselection_2017Analysis_StopToLBMajorPoints_9Sept2020',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2018' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EEPreselection_2018Analysis_StopToLBMajorPoints_9Sept2020',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    }
}
