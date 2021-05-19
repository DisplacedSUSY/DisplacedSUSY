#!/usr/bin/env python
from DisplacedSUSY.Configuration.limitOptions import *

channel = "emu"

# make the following substitutions for datacard brevity and legibility
predefined_region_names = {
    '_0to100um'     : '',
    '100to500um'    : 'i',
    '500to100000um' : 'ii',
    '0to90GeV'      : 'loPt',
    '0to140GeV'     : 'loPt',
    '90toInfGeV'    : 'hiPt',
    '140toInfGeV'   : 'hiPt',
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
    '2016'    : [0, 90, -1], # GeV
    '2017_18' : [0, 140, -1], # GeV
    '2018' : [0, 140, -1], # GeV
}
# |d0| range of prompt lepton in prompt/displaced control regions
cr_d0_range = (0, 100) # um

# multiplicative corrections to account for correlation; enter as (value, err_lo, err_hi)
# only list regions in which you want to apply a correction
# see predefined_sr_names for naming convention
abcd_correlation_factors = { # from elog 1852 and 1919
    '2016' : {
        'SR_I_loPt' : (1.00, 1.27),
        'SR_I_hiPt' : (1.00, 1.27),
    },
    '2017_18' : {
        'SR_I_loPt' : (3.07, 0.77),
        'SR_I_hiPt' : (3.07, 0.77),
    },
    '2018' : {
        'SR_I_loPt' : (3.07, 0.77),
        'SR_I_hiPt' : (3.07, 0.77),
    },
}

# systematic uncertainty to account for uncertainty in extrapolation point used in determining
#correlation factor; enter as single number (e.g. 0.5 = 50% uncertainty)
abcd_extrapolation_systematics = { # from elog 1872
    '2016' : {
        'SR_I_loPt' : 0.00,
        'SR_I_hiPt' : 0.00,
    },
    '2017_18' : {
        'SR_I_loPt' : 0.22,
        'SR_I_hiPt' : 0.22,
    },
    '2018' : {
        'SR_I_loPt' : 0.22,
        'SR_I_hiPt' : 0.22,
    },
}

# systematic uncertainty on abcd estimate in each signal region (e.g. 0.5 = 50% uncertainty)
# only list regions in which you want to apply a systematic (as opposed to a correction)
abcd_systematics = { # from elog 1860
    '2016' : {
        'SR_II'  : 0.98,
        'SR_III' : 0.98,
        'SR_IV'  : 0.98,
    },
    '2017_18' : {
        'SR_II'  : 1.06,
        'SR_III' : 1.06,
        'SR_IV'  : 1.06,
    },
    '2018' : {
        'SR_II'  : 1.06,
        'SR_III' : 1.06,
        'SR_IV'  : 1.06,
    },
}

# one will generally want to use the same histogram for signal and data
# this can be overridden in individual dictionaries if desired
hist = 'PreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_100000um_vs_muonPt[0]'
#hist = 'PreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_100000um_vs_electronPt[0]'

# swap x and y axes to match regions defined in AN and paper
# currently only necessary in the emu channel
swap_axes = True

# list separate dictionaries for each year; they will be combined by makeAbcdDatacards if necessary
data_samples = {
    '2016' : {
        'name' : 'MuonEG_2016_postHIP',
        'dir'  : 'EMuPreselection_withFixedDispVtxInMaterial_2016Analysis_27Nov2020',
        'file' : 'MuonEG_2016_postHIP.root',
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2017' : {
        'name' : 'MuonEG_2017_withoutB',
        'dir'  : 'EMuPreselection_withFixedDispVtxInMaterial_2017Analysis_28Nov2020',
        'file' : 'MuonEG_2017_withoutB.root',
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2018' : {
        'name' : 'MuonEG_2018',
        'dir'  : 'EMuPreselection_withFixedDispVtxInMaterial_2018Analysis_26Nov2020',
        'file' : 'MuonEG_2018.root',
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
}

# a separate datacard will be produced for each signal point
# list separate dictionaries for each year; they will be combined by makeAbcdDatacards if necessary
signal_samples = {
    '2016' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EMuPreselection_2016Analysis_Signal_30Jan2021/mergeOut',
        #'dir'  : 'EMuPreselection_2016Analysis_HToSS_19Apr2021/mergeOut',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2017' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EMuPreselection_2017Analysis_Signal_29Jan2021/mergeOut',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2018' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EMuPreselection_2018Analysis_Signal_28Jan2021/mergeOut',
        #'dir'  : 'EMuPreselection_2018Analysis_sleptons_17May2021/mergeOut',
        #'dir'  : 'EMuPreselection_2018Analysis_staus_19May2021/mergeOut',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    }
}
