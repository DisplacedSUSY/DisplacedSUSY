#!/usr/bin/env python
from DisplacedSUSY.Configuration.limitOptions import *

channel = "mumu"

lumi = {
    '2016' : 16.1,
    '2017' : 36.7,
    '2018' : 59.7,
}

# make the following substitutions for datacard brevity and legibility
predefined_region_names = {
    '_0to100um'     : '',
    '100to500um'    : 'i',
    '500to100000um' : 'ii',
    '0to100GeV'     : 'loPt',
    '100toInfGeV'   : 'hiPt',
    '_0toInfGeV'    : '',
}
predefined_sr_names = {
    'i_i'   : 'I',
    'i_ii'  : 'II',
    'ii_i'  : 'III',
    'ii_ii' : 'IV',
}

# choose how inclusive signal region will be divided; current options are 'L', 'L_inv', and 'grid'
sr_shapes = 'grid'
# signal region binning; enter -1 to include overflow
d0_0_bin_edges = [100, 500, 100000] # um
d0_1_bin_edges = [100, 500, 100000] # um
pt_bin_edges = {
    '2016'    : [0, 100, -1], # GeV
    '2017_18' : [0, 100, -1], # GeV
    '2017' : [0, 100, -1], # GeV
    '2018' : [0, 100, -1], # GeV
}
# |d0| range of prompt lepton in prompt/prompt and prompt/displaced control regions
cr_d0_range = (0, 100) # um

# multiplicative corrections to account for correlation; enter as (value, err_lo, err_hi)
# only list regions in which you want to apply a correction
# see predefined_sr_names for naming convention
abcd_correlation_factors = { # from elog 1852
    '2016' : {
        'SR_I_loPt' : (2.51, 0.87),
        'SR_I_hiPt' : (2.51, 0.87),
    },
    '2017_18' : {
        'SR_I_loPt' : (4.20, 1.51),
        'SR_I_hiPt' : (4.20, 1.51),
    },
    '2017' : {
        'SR_I_loPt' : (4.20, 1.51),
        'SR_I_hiPt' : (4.20, 1.51),
    },
    '2018' : {
        'SR_I_loPt' : (4.20, 1.51),
        'SR_I_hiPt' : (4.20, 1.51),
    },
}

# systematic uncertainty to account for uncertainty in extrapolation point used in determining
# correlation factor; enter as single number (e.g. 0.5 = 50% uncertainty)
abcd_extrapolation_systematics = { # from elog 1872
    '2016' : {
        'SR_I_loPt' : 0.20,
        'SR_I_hiPt' : 0.20,
    },
    '2017_18' : {
        'SR_I_loPt' : 0.24,
        'SR_I_hiPt' : 0.24,
    },
    '2017' : {
        'SR_I_loPt' : 0.24,
        'SR_I_hiPt' : 0.24,
    },
    '2018' : {
        'SR_I_loPt' : 0.24,
        'SR_I_hiPt' : 0.24,
    },
}

# systematic uncertainty on abcd estimate in each signal region (e.g. 0.5 = 50% uncertainty)
# only list regions in which you want to apply a systematic (as opposed to a correction)
abcd_systematics = { # from elog 1860
    '2016' : {
        'SR_II'  : 0.64,
        'SR_III' : 0.64,
        'SR_IV'  : 0.64,
    },
    '2017_18' : {
        'SR_II'  : 1.40,
        'SR_III' : 1.40,
        'SR_IV'  : 1.40,
    },
    '2017' : {
        'SR_II'  : 1.40,
        'SR_III' : 1.40,
        'SR_IV'  : 1.40,
    },
    '2018' : {
        'SR_II'  : 1.40,
        'SR_III' : 1.40,
        'SR_IV'  : 1.40,
    },
}

# one will generally want to use the same histogram for signal and data
# this can be overridden in individual dictionaries if desired
hist = 'PreselectionPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_100000um_vs_muonPt[0]'

# swap x and y axes to match regions defined in AN and paper
# currently only necessary in the emu channel
swap_axes = False

# list separate dictionaries for each year; they will be combined by makeAbcdDatacards if necessary
data_samples = {
    '2016' : {
        'name' : 'DoubleMu_2016_postHIP',
        'dir'  : 'MuMuPreselection_withFixedDispVtxInMaterial_2016Analysis_27Nov2020',
        'file' : 'DoubleMu_2016_postHIP.root',
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2017' : {
        'name' : 'DoubleMu_2017_withoutB',
        'dir'  : 'MuMuPreselection_withFixedDispVtxInMaterial_2017Analysis_28Nov2020',
        'file' : 'DoubleMu_2017_withoutB.root',
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2018' : {
        'name' : 'DoubleMu_2018',
        'dir'  : 'MuMuPreselection_withFixedDispVtxInMaterial_2018Analysis_26Nov2020',
        'file' : 'DoubleMu_2018.root',
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
}

# specify when to substitute a given year's signal sample for another's, usually when signal
# samples are not available in all years. yields will be scaled by luminosity and systematic values
# will be taken from the 'from' year
standin_signal_years = {
    #'to'  : 'from',

    # stops, sleptons, staus, and Higgs
    '2016' : '2016',
    '2017' : '2017',
    '2018' : '2018',

}

# a separate datacard will be produced for each signal point
# list separate dictionaries for each year; they will be combined by makeAbcdDatacards if necessary
signal_samples = {
    '2016' : {
        'name' : '', # will be automatically generated for each signal point
        #'dir'  : 'MuMuPreselection_2016Analysis_Signal_30Jan2021/mergeOut',
        'dir'  : 'MuMuPreselection_2016Analysis_sleptons_29Jun2021/mergeOut',
        #'dir'  : 'MuMuPreselection_2016Analysis_staus_29June2021/mergeOut',
        #'dir'  : 'MuMuPreselection_2016Analysis_HToSS_19Apr2021/mergeOut',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2017' : {
        'name' : '', # will be automatically generated for each signal point
        #'dir'  : 'MuMuPreselection_2017Analysis_Signal_29Jan2021/mergeOut',
        'dir'  : 'MuMuPreselection_2017Analysis_sleptons_12Jul2021/mergeOut',
        #'dir'  : 'MuMuPreselection_2017Analysis_staus_29June2021/mergeOut',
        #'dir'  : 'MuMuPreselection_2017Analysis_HToSS_21May2021/mergeOut',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2018' : {
        'name' : '', # will be automatically generated for each signal point
        #'dir'  : 'MuMuPreselection_2018Analysis_Signal_28Jan2021/mergeOut',
        'dir'  : 'MuMuPreselection_2018Analysis_sleptons_29Jun2021/mergeOut',
        #'dir'  : 'MuMuPreselection_2018Analysis_staus_29June2021/mergeOut',
        #'dir'  : 'MuMuPreselection_2018Analysis_HToSS_30June2021/mergeOut',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
}
