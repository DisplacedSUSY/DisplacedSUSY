#!/usr/bin/env python

intLumi = 11280 # full RunII
energy = '13'

#masses = ['200','300','400','500','600','700','800','900','1000','1100','1200']
#masses = ['200','300','400','500','600','700','800','900','1000','1100','1200']
process = 'stopToLB'
masses = [str(m) for m in range(200, 1801, 400)]
lifetimes = [str(10**e) for e in range(0, 4)]

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
        'yAxisLabel' : 'c#tau [cm]',

        #define all the curves to include on this canvas
        'th2fs' : [
            {
                'source' : ['EE_FullRun2_200um_10PercentSys_30Aug2019'],
                'th2fsToInclude' : ['exp'],
            },
        ],
        'graphs' : [
            {
                'source' : ['EE_FullRun2_200um_10PercentSys_30Aug2019'],
                'graphsToInclude' : ['exp'],
                'legendEntry' : 'expected limits',
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
                'source' : ['EE_FullRun2_200um_10PercentSys_30Aug2019'],
                'lifetime' : '1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '1 mm',
            },
            {
                'source' : ['EE_FullRun2_200um_10PercentSys_30Aug2019'],
                'lifetime' : '10',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '10 mm',
            },
            {
                'source' : ['EE_FullRun2_200um_10PercentSys_30Aug2019'],
                'lifetime' : '100',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '100 mm',
            },
            {
                'source' : ['EE_FullRun2_200um_10PercentSys_30Aug2019'],
                'lifetime' : '1000',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '1000 mm',
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
                'source' : ['EE_FullRun2_200um_10PercentSys_30Aug2019'],
                'mass' : '200',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '200 GeV',
            },
            {
                'source' : ['EE_FullRun2_200um_10PercentSys_30Aug2019'],
                'mass' : '600',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '600 GeV',
            },
            {
                'source' : ['EE_FullRun2_200um_10PercentSys_30Aug2019'],
                'mass' : '1000',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '1000 GeV',
            },
            {
                'source' : ['EE_FullRun2_200um_10PercentSys_30Aug2019'],
                'mass' : '1400',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '1400 GeV',
            },
            {
                'source' : ['EE_FullRun2_200um_10PercentSys_30Aug2019'],
                'mass' : '1800',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '1800 GeV',
            },
        ],
    },
]
