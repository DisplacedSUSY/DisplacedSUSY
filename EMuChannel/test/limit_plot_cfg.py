#!/usr/bin/env python

# enter lumi valus as a list to display a range
intLumi = 112800 # full RunII
#intLumi = [112800, 117600] # full RunII for channel combination
energy = '13'
channel = 'e#mu'
#channel = None # set to None for multi-channel plots

process = 'stopToLB'
masses = [str(m) for m in range(100, 1801, 100)]
lifetimes = [str(10**e) for e in range(-2, 5)]
#lifetimes = [str(b*10**e) for e in range(-2, 4) for b in range(1, 10)] + [str(10000)]

# description of all the plots to be made
plotDefinitions = [
    {
        # this will be the name of the canvas in the output root file
        'title' : 'emu_standard',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{t}} [GeV]',
        'yAxisLabel' : 'c#tau [cm]',

        #define all the curves to include on this canvas
        'th2fs' : [
            {
                'source' : ['EMu_run2_21Sep2020'],
                'th2fsToInclude' : ['exp'],
            },
        ],
        'graphs' : [
            {
                'source' : ['EMu_run2_21Sep2020'],
                'graphsToInclude' : ['twoSigma', 'oneSigma', 'exp'],
                'colorScheme' : 'brazilian',
            },
        ],
    },
    # summary plot of all three channels
    {
        # this will be the name of the canvas in the output root file
        'title' : 'all_standard',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{t}} [GeV]',
        'yAxisLabel' : 'c#tau [cm]',

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : ['2015_AN_bg_estimate_12Sep2019'],
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '2015, e#mu channel'
            },
            {
                'source' : ['EMu_run2_21Sep2020'],
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '2016-18, e#mu channel'
            },
            {
                'source' : ['EE_run2_21Sep2020'],
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '2016-18, ee channel'
            },
            {
                'source' : ['MuMu_run2_21Sep2020'],
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '2016-18, #mu#mu channel'
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_mass',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{t}} [GeV]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : ['EMu_run2_21Sep2020'],
                'lifetime' : '0.1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '0.01 cm',
            },
            {
                'source' : ['EMu_run2_21Sep2020'],
                'lifetime' : '1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '0.1 cm',
            },
            {
                'source' : ['EMu_run2_21Sep2020'],
                'lifetime' : '10',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '1 cm',
            },
            {
                'source' : ['EMu_run2_21Sep2020'],
                'lifetime' : '100',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '10 cm',
            },
            {
                'source' : ['EMu_run2_21Sep2020'],
                'lifetime' : '1000',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '100 cm',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_lifetime',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'c#tau [cm]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : ['EMu_run2_21Sep2020'],
                'mass' : '200',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '200 GeV',
            },
            {
                'source' : ['EMu_run2_21Sep2020'],
                'mass' : '600',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '600 GeV',
            },
            {
                'source' : ['EMu_run2_21Sep2020'],
                'mass' : '1000',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '1000 GeV',
            },
            {
                'source' : ['EMu_run2_21Sep2020'],
                'mass' : '1400',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '1400 GeV',
            },
            {
                'source' : ['EMu_run2_21Sep2020'],
                'mass' : '1800',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '1800 GeV',
            },
        ],
    },
]
