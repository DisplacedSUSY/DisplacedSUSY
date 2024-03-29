#!/usr/bin/env python

intLumi = 112800 # full RunII
#intLumi =   59700 # 2018
energy = '13'
channel = '#mu#mu'

process = 'gmsb'
masses = [str(50)] + [str(m) for m in range(100, 1001, 100)]
lifetimes = [str(b*10**e) for e in range(-1, 3) for b in range(1, 10)] + [str(1000)]

# description of all the plots to be made
plotDefinitions = [
    {
        # this will be the name of the canvas in the output root file
        'title' : 'mumu_standard_sleptons_scaled',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{l}} [GeV]',
        'yAxisLabel' : 'c#tau [cm]',

        #define all the curves to include on this canvas
        'th2fs' : [
            {
                'source' : 'sleptons_mumu_runII_from2018Samples_25May2021',
                'th2fsToInclude' : ['obs'],
            },
        ],
        'graphs' : [
            {
                'source' : 'sleptons_mumu_runII_from2018Samples_25May2021',
                'graphsToInclude' : ['exp', 'oneSigma', 'obs'],
                'colorScheme' : 'susy_pag',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'mumu_limits_vs_mass_sleptons_scaled',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{l}} [GeV]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'sleptons_mumu_runII_from2018Samples_25May2021',
                'lifetime' : '0.1',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'yellow',
                'legendEntry' : '0.01 cm',
            },
            {
                'source' : 'sleptons_mumu_runII_from2018Samples_25May2021',
                'lifetime' : '1',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'purple',
                'legendEntry' : '0.1 cm',
            },
            {
                'source' : 'sleptons_mumu_runII_from2018Samples_25May2021',
                'lifetime' : '10',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'blue',
                'legendEntry' : '1 cm',
            },
            {
                'source' : 'sleptons_mumu_runII_from2018Samples_25May2021',
                'lifetime' : '100',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'red',
                'legendEntry' : '10 cm',
            },
            {
                'source' : 'sleptons_mumu_runII_from2018Samples_25May2021',
                'lifetime' : '1000',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'green',
                'legendEntry' : '100 cm',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'mumu_limits_vs_lifetime_sleptons_scaled',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'c#tau [cm]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'sleptons_mumu_runII_from2018Samples_25May2021',
                'mass' : '100',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'yellow',
                'legendEntry' : '100 GeV',
            },
            {
                'source' : 'sleptons_mumu_runII_from2018Samples_25May2021',
                'mass' : '300',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'blue',
                'legendEntry' : '300 GeV',
            },
            {
                'source' : 'sleptons_mumu_runII_from2018Samples_25May2021',
                'mass' : '600',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'red',
                'legendEntry' : '600 GeV',
            },
            {
                'source' : 'sleptons_mumu_runII_from2018Samples_25May2021',
                'mass' : '1000',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'green',
                'legendEntry' : '1000 GeV',
            },
        ],
    },
]
