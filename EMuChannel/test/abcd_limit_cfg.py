#!/usr/bin/env python
from DisplacedSUSY.Configuration.limitOptions import *

# choose how inclusive signal region will be divided; current options are 'L', 'L_inv', and 'grid'
sr_shapes = 'grid'
# signal region binning; enter -1 to include overflow
d0_0_bin_edges = [100, 500, 100000] # um
d0_1_bin_edges = [100, 500, 100000] # um
pt_bin_edges = [0, 200, -1] # GeV
# |d0| range of prompt lepton in prompt/displaced control regions
cr_d0_range = (20, 100) # um

# multiplicative corrections to account for correlation; enter as (value, one-sigma uncertainty)
# only list regions in which you want to apply a correction
abcd_correlation_factors = {}

# fixme: abcd systematics specified here temporarily
# systematic uncertainty on abcd estimate in each signal region (e.g. 0.5 = 50% uncertainty)
# only list regions in which you want to apply a systematic (as opposed to a correction)
abcd_systematics = {
    'SR_100to500um_100to500um_0to200GeV'         : 0.03,
    'SR_100to500um_500to100000um_0to200GeV'      : 0.03,
    'SR_500to100000um_100to500um_0to200GeV'      : 0.03,
    'SR_500to100000um_500to100000um_0to200GeV'   : 0.03,
    'SR_100to500um_100to500um_200toInfGeV'       : 0.03,
    'SR_100to500um_500to100000um_200toInfGeV'    : 0.03,
    'SR_500to100000um_100to500um_200toInfGeV'    : 0.03,
    'SR_500to100000um_500to100000um_200toInfGeV' : 0.03,
}

# one will generally want to use the same histogram for signal and data
# this can be overridden in individual dictionaries if desired
hist = 'AdditionalPreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_100000um_vs_muonPt[0]'
#hist = 'AdditionalPreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_100000um_vs_electronPt[0]'

data = {
    'name' : 'MuonEG_2016_2017_2018',
    'dir'  : 'emu_runII_ptBinned_estimates_15July2020',
    'file' : 'MuonEG_2016_2017_2018.root',
    'hist' : hist,
    'var_bins' : True,
    'blinded'  : True,
}

# a separate datacard will be produced for each signal point
# list separate dictionaries for each year; they will be combined by makeAbcdDatacards if necessary
signal_samples = {
    '2016' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : '',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2017' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : '',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    },
    '2018' : {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EMuAdditionalPreselection_2018Analysis_signal_coarse3DHists_10July2020',
        'file' : '', # will be automatically generated for each signal point
        'hist' : hist,
        'var_bins' : True,
        'blinded'  : False,
    }
}
