#!/usr/bin/env python

intLumi = 117600 # full RunII
energy = '13'
channel = 'ee'

process = 'stopToLB'
masses = [str(m) for m in range(100, 1801, 100)]
#lifetimes = [str(10**e) for e in range(-2, 5)]
lifetimes = [str(b*10**e) for e in range(-1, 4) for b in range(1, 10)] + [str(10000)]

# description of all the plots to be made
plotDefinitions = [
    {
        # this will be the name of the canvas in the output root file
        'title' : 'ee_standard_lb',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{t}} [GeV]',
        'yAxisLabel' : 'c#tau [cm]',

        #define all the curves to include on this canvas
        'th2fs' : [
            {
                'source' : 'ee_lb_runII_03Feb2021',
                'th2fsToInclude' : ['exp'],
            },
        ],
        'graphs' : [
            {
                'source' : 'ee_lb_runII_03Feb2021',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_mass_lb',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{t}} [GeV]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'ee_lb_runII_03Feb2021',
                'lifetime' : '0.1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '0.01 cm',
            },
            {
                'source' : 'ee_lb_runII_03Feb2021',
                'lifetime' : '1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '0.1 cm',
            },
            {
                'source' : 'ee_lb_runII_03Feb2021',
                'lifetime' : '10',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '1 cm',
            },
            {
                'source' : 'ee_lb_runII_03Feb2021',
                'lifetime' : '100',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '10 cm',
            },
            {
                'source' : 'ee_lb_runII_03Feb2021',
                'lifetime' : '1000',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '100 cm',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_lifetime_lb',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'c#tau [cm]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'ee_lb_runII_03Feb2021',
                'mass' : '100',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '100 GeV',
            },
            {
                'source' : 'ee_lb_runII_03Feb2021',
                'mass' : '400',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '400 GeV',
            },
            {
                'source' : 'ee_lb_runII_03Feb2021',
                'mass' : '1000',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '1000 GeV',
            },
            {
                'source' : 'ee_lb_runII_03Feb2021',
                'mass' : '1400',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '1400 GeV',
            },
            {
                'source' : 'ee_lb_runII_03Feb2021',
                'mass' : '1800',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '1800 GeV',
            },
        ],
    },
]
