#!/usr/bin/env python

intLumi = 11280 # full RunII
energy = '13'

#masses = ['200','300','400','500','600','700','800','900','1000','1100','1200']
#masses = ['200','300','400','500','600','700','800','900','1000','1100','1200']
process = 'stopToLB'
masses = ['200','600','1000', '1400', '1800']
lifetimes = ['1','10','100', '1000']

# description of all the plots to be made
plotDefinitions = [
    {
        # this will be the name of the canvas in the output root file
        'title' : 'mumu_standard',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'stop mass [GeV]',
        'yAxisLabel' : 'stop #LTc#tau#GT [cm]',

        #define all the curves to include on this canvas
        'th2fs' : [
            {
                'source' : ['FullRun2_test_30Aug2019'],
                'th2fsToInclude' : ['exp'],
            },
        ],
        'graphs' : [
            {
                'source' : ['FullRun2_test_30Aug2019'],
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
        'xAxisLabel' : 'stop mass [GeV]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : ['FullRun2_test_30Aug2019'],
                'lifetime' : '1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '1 mm',
            },
            {
                'source' : ['FullRun2_test_30Aug2019'],
                'lifetime' : '10',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '10 mm',
            },
            {
                'source' : ['FullRun2_test_30Aug2019'],
                'lifetime' : '100',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '100 mm',
            },
            {
                'source' : ['FullRun2_test_30Aug2019'],
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
        'xAxisLabel' : 'stop #LTc#tau#GT [cm]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : ['FullRun2_test_30Aug2019'],
                'mass' : '200',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '200 GeV',
            },
            {
                'source' : ['FullRun2_test_30Aug2019'],
                'mass' : '600',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '600 GeV',
            },
            {
                'source' : ['FullRun2_test_30Aug2019'],
                'mass' : '1000',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '1000 GeV',
            },
            {
                'source' : ['FullRun2_test_30Aug2019'],
                'mass' : '1400',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '1400 GeV',
            },
            {
                'source' : ['FullRun2_test_30Aug2019'],
                'mass' : '1800',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '1800 GeV',
            },
        ],
    },
]
