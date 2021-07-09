#!/usr/bin/env python

intLumi = 117600 # full RunII
energy = '13'
channel = 'ee'

#masses = ['200','300','400','500','600','700','800','900','1000','1100','1200']
#masses = ['200','300','400','500','600','700','800','900','1000','1100','1200']
process = 'stopToLB'
masses = [str(m) for m in range(100, 1801, 100)]
#lifetimes = [str(10**e) for e in range(-2, 5)]
lifetimes = [str(b*10**e) for e in range(-1, 4) for b in range(1, 10)] + [str(10000)]

# description of all the plots to be made
plotDefinitions = [
    {
        # this will be the name of the canvas in the output root file
        'title' : 'ee_standard',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{t}} [GeV]',
        'yAxisLabel' : 'c#tau_{0} [cm]',

        #define all the curves to include on this canvas
        'th2fs' : [
            {
                'source' : 'ee_lb_runII_unblinded_07Mar2021_significance',
                'th2fsToInclude' : ['obs'],
            },
        ],
        'graphs' : [
            #{
            #    'source' : 'ee_lb_runII_unblinded_07Mar2021_significance',
            #    'graphsToInclude' : ['twoSigma', 'oneSigma', 'obs'],
            #    'colorScheme' : 'brazilian',
            #},
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
                'source' : 'ee_lb_runII_unblinded_07Mar2021_significance',
                'lifetime' : '0.1',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'yellow',
                'legendEntry' : '0.01 cm',
            },
            {
                'source' : 'ee_lb_runII_unblinded_07Mar2021_significance',
                'lifetime' : '1',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'purple',
                'legendEntry' : '0.1 cm',
            },
            {
                'source' : 'ee_lb_runII_unblinded_07Mar2021_significance',
                'lifetime' : '10',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'blue',
                'legendEntry' : '1 cm',
            },
            {
                'source' : 'ee_lb_runII_unblinded_07Mar2021_significance',
                'lifetime' : '100',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'red',
                'legendEntry' : '10 cm',
            },
            {
                'source' : 'ee_lb_runII_unblinded_07Mar2021_significance',
                'lifetime' : '1000',
                'graphsToInclude' : ['obs'],
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
        'xAxisLabel' : 'c#tau_{0} [cm]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'ee_lb_runII_unblinded_07Mar2021_significance',
                'mass' : '200',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'yellow',
                'legendEntry' : '200 GeV',
            },
            {
                'source' : 'ee_lb_runII_unblinded_07Mar2021_significance',
                'mass' : '600',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'blue',
                'legendEntry' : '600 GeV',
            },
            {
                'source' : 'ee_lb_runII_unblinded_07Mar2021_significance',
                'mass' : '1000',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'red',
                'legendEntry' : '1000 GeV',
            },
            {
                'source' : 'ee_lb_runII_unblinded_07Mar2021_significance',
                'mass' : '1400',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'green',
                'legendEntry' : '1400 GeV',
            },
            {
                'source' : 'ee_lb_runII_unblinded_07Mar2021_significance',
                'mass' : '1800',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'purple',
                'legendEntry' : '1800 GeV',
            },
        ],
    },
]
