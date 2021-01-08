#!/usr/bin/env python
from DisplacedSUSY.Configuration.limitOptions import *

channel = "emu"

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
#pt_bin_edges = [0, 90, -1] # GeV; only the most-prompt region will be binned in pT
pt_bin_edges = [0, 140, -1] # GeV; only the most-prompt region will be binned in pT
# |d0| range of prompt lepton in prompt/displaced control regions
cr_d0_range = (0, 100) # um

# multiplicative corrections to account for correlation; enter as (value, err_lo, err_hi)
# only list regions in which you want to apply a correction
# see predefined_sr_names for naming convention
abcd_correlation_factors = { # from elog 1852
    '2016' : {
        'SR_I_0to90GeV'   : (1.00, 1.00, 1.19),
        'SR_I_90toInfGeV' : (1.00, 1.00, 1.19),
    },
    '2017_18' : {
        'SR_I_0to140GeV'   : (3.07, 0.77, 0.77),
        'SR_I_140toInfGeV' : (3.07, 0.77, 0.77),
    }
}

# systematic uncertainty to account for uncertainty in extrapolation point used in determining
#correlation factor; enter as single number (e.g. 0.5 = 50% uncertainty)
abcd_extrapolation_systematics = { # from elog 1872
    '2016' : {
        'SR_I_0to90GeV'    : 0.00,
        'SR_I_90toInfGeV'  : 0.00,
    },
    '2017_18' : {
        'SR_I_0to140GeV'   : 0.22,
        'SR_I_140toInfGeV' : 0.22,
    }
}

# systematic uncertainty on abcd estimate in each signal region (e.g. 0.5 = 50% uncertainty)
# only list regions in which you want to apply a systematic (as opposed to a correction)
abcd_systematics = { # from elog 1860
    '2016' : {
        'SR_II_0toInfGeV'  : 0.98,
        'SR_III_0toInfGeV' : 0.98,
        'SR_IV_0toInfGeV'  : 0.98,
    },
    '2017_18' : {
        'SR_II_0toInfGeV'  : 1.06,
        'SR_III_0toInfGeV' : 1.06,
        'SR_IV_0toInfGeV'  : 1.06,
    },
}

# one will generally want to use the same histogram for signal and data
# this can be overridden in individual dictionaries if desired
hist = 'PreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_100000um_vs_muonPt[0]'
#hist = 'PreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_100000um_vs_electronPt[0]'

# list separate dictionaries for each year; they will be combined by makeAbcdDatacards if necessary
data_samples = {
    '2016' : {
        'name' : 'MuonEG_2016_postHIP',
        'dir'  : 'EMuPreselection_withFixedDispVtxInMaterial_2016Analysis_27Nov2020',
        'file' : 'MuonEG_2016_postHIP.root',
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : True,
    },
    '2017' : {
        'name' : 'MuonEG_2017_withoutB',
        'dir'  : 'EMuPreselection_withFixedDispVtxInMaterial_2017Analysis_28Nov2020',
        'file' : 'MuonEG_2017_withoutB.root',
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : True,
    },
    '2018' : {
        'name' : 'MuonEG_2018',
        'dir'  : 'EMuPreselection_withFixedDispVtxInMaterial_2018Analysis_26Nov2020',
        'file' : 'MuonEG_2018.root',
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
        'dir'  : 'EMuPreselection_2016Analysis_Signal_9Dec2020/mergeOut',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2017' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EMuPreselection_2017Analysis_Signal_5Dec2020/mergeOut',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2018' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EMuPreselection_2018Analysis_Signal_5Dec2020/mergeOut',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    }
}
