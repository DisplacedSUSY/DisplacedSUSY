#!/usr/bin/env python

#intLumi = 112800 # full RunII
intLumi =   59700 # 2018
energy = '13'
channel = 'ee'

process = 'sleptons'
masses = [str(50)] + [str(m) for m in range(100, 1001, 100)]
#lifetimes = [str(10**e) for e in range(-1, 5)]
lifetimes = [str(b*10**e) for e in range(-1, 4) for b in range(1, 10)] + [str(10000)]

# description of all the plots to be made
plotDefinitions = [
    {
        # this will be the name of the canvas in the output root file
        'title' : 'ee_standard_sleptons',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{l}} [GeV]',
        'yAxisLabel' : 'c#tau [cm]',

        #define all the curves to include on this canvas
        'th2fs' : [
            {
                'source' : 'sleptons_ee_2018_18May2021',
                'th2fsToInclude' : ['obs'],
            },
        ],
        'graphs' : [
            {
                'source' : 'sleptons_ee_2018_18May2021',
                'graphsToInclude' : ['exp', 'oneSigma', 'obs'],
                'colorScheme' : 'susy_pag',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'ee_limits_vs_mass_sleptons',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{l}} [GeV]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'sleptons_ee_2018_18May2021',
                'lifetime' : '0.1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '0.01 cm',
            },
            {
                'source' : 'sleptons_ee_2018_18May2021',
                'lifetime' : '1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '0.1 cm',
            },
            {
                'source' : 'sleptons_ee_2018_18May2021',
                'lifetime' : '10',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '1 cm',
            },
            {
                'source' : 'sleptons_ee_2018_18May2021',
                'lifetime' : '100',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '10 cm',
            },
            {
                'source' : 'sleptons_ee_2018_18May2021',
                'lifetime' : '1000',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '100 cm',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'ee_limits_vs_lifetime_sleptons',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'c#tau [cm]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'sleptons_ee_2018_18May2021',
                'mass' : '50',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '50 GeV',
            },
            {
                'source' : 'sleptons_ee_2018_18May2021',
                'mass' : '100',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '100 GeV',
            },
            {
                'source' : 'sleptons_ee_2018_18May2021',
                'mass' : '300',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '300 GeV',
            },
            {
                'source' : 'sleptons_ee_2018_18May2021',
                'mass' : '600',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '600 GeV',
            },
        ],
    },
]
