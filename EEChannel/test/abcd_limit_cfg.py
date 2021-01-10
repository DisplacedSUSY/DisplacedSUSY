#!/usr/bin/env python
from DisplacedSUSY.Configuration.limitOptions import *

channel = "ee"

# make the following substitutions for datacard legibility
predefined_sr_names = {
    '100to500um_100to500um'       : 'I',
    '100to500um_500to100000um'    : 'II',
    '500to100000um_100to500um'    : 'III',
    '500to100000um_500to100000um' : 'IV',
}

# choose how inclusive signal region will be divided; current options are 'L', 'L_inv', and 'grid'
sr_shapes = 'grid'
# signal region binning; enter -1 to include overflow
d0_0_bin_edges = [100, 500, 100000] # um
d0_1_bin_edges = [100, 500, 100000] # um
pt_bin_edges = [0, 300, -1] # GeV; only the most-prompt region will be binned in pT
#pt_bin_edges = [0, 400, -1] # GeV; only the most-prompt region will be binned in pT
# |d0| range of prompt lepton in prompt/displaced control regions
cr_d0_range = (0, 100) # um

# multiplicative corrections to account for correlation; enter as (value, err_lo, err_hi)
# only list regions in which you want to apply a correction
# see predefined_sr_names for naming convention
abcd_correlation_factors = { # from elog 1852
    '2016' : {
        'SR_I_0to300GeV'   : (1.00, 0.97, 0.23),
        'SR_I_300toInfGeV' : (1.00, 0.97, 0.23),
    },
    '2017_18' : {
        'SR_I_0to400GeV'   : (1.51, 0.39, 0.39),
        'SR_I_400toInfGeV' : (1.51, 0.39, 0.39),
    }
}

# systematic uncertainty to account for uncertainty in extrapolation point used in determining
# correlation factor; enter as single number (e.g. 0.5 = 50% uncertainty)
abcd_extrapolation_systematics = { # from elog 1872
    '2016' : {
        'SR_I_0to300GeV'   : 0.00,
        'SR_I_300toInfGeV' : 0.00,
    },
    '2017_18' : {
        'SR_I_0to400GeV'   : 0.12,
        'SR_I_400toInfGeV' : 0.12,
    }
}

# systematic uncertainty on abcd estimate in each signal region (e.g. 0.5 = 50% uncertainty)
# only list regions in which you want to apply a systematic (as opposed to a correction)
abcd_systematics = { # from elog 1860
    '2016' : {
        'SR_II_0toInfGeV'  : 1.99,
        'SR_III_0toInfGeV' : 1.99,
        'SR_IV_0toInfGeV'  : 1.99,
    },
    '2017_18' : {
        'SR_II_0toInfGeV'  : 0.37,
        'SR_III_0toInfGeV' : 0.37,
        'SR_IV_0toInfGeV'  : 0.37,
    },
}

# one will generally want to use the same histogram for signal and data
# this can be overridden in individual dictionaries if desired
hist = 'PreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_100000um_vs_electronPt[0]'

# list separate dictionaries for each year; they will be combined by makeAbcdDatacards if necessary
data_samples = {
    '2016' : {
        'name' : 'DoubleEG_2016_postHIP',
        'dir'  : 'EEPreselection_withFixedDispVtxInMaterial_2016Analysis_27Nov2020',
        'file' : 'DoubleEG_2016_postHIP.root',
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : True,
    },
    '2017' : {
        'name' : 'DoubleEG_2017',
        'dir'  : 'EEPreselection_withFixedDispVtxInMaterial_2017Analysis_28Nov2020',
        'file' : 'DoubleEG_2017.root',
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : True,
    },
    '2018' : {
        'name' : 'EGamma_2018',
        'dir'  : 'EEPreselection_withFixedDispVtxInMaterial_2018Analysis_26Nov2020',
        'file' : 'EGamma_2018.root',
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : True,
    },
}

# a separate datacard will be produced for each signal point
# list separate dictionaries for each year; they will be combined by makeAbcdDatacards if necessary
signal_samples = {
    '2016' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EEPreselection_2016Analysis_Signal_5Dec2020/mergeOut',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2017' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EEPreselection_2017Analysis_Signal_5Dec2020/mergeOut',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2018' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EEPreselection_2018Analysis_Signal_5Dec2020/mergeOut',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    }
}
