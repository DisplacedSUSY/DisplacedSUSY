#!/usr/bin/env python

intLumi = 16146 # 2016 G an H
energy = '13'

#masses = ['200','300','400','500','600','700','800','900','1000','1100','1200']
masses = ['200','300','400','500','600','700','800','900','1000','1100','1200']
#lifetimes = ['1','10','100','1000']
lifetimes = ['9','10','20','30']

# description of all the plots to be made
plotDefinitions = [

    {
        # this will be the name of the canvas in the output root file
        'title' : 'emu_standard',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'stop mass [GeV]',
        'yAxisLabel' : 'stop #LTc#tau#GT [cm]',

        #define all the curves to include on this canvas
        'th2fs' : [
            {
                'source' : ['preliminary_expected_17_11_27'],
                'th2fsToInclude' : ['exp'],
            },
        ],
        'graphs' : [
            {
                'source' : ['preliminary_expected_17_11_27'],
                'graphsToInclude' : ['exp'],
                'legendEntry' : 'Fit-based limits',
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
                'source' : ['preliminary_expected_17_11_27'],
                'lifetime' : '1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '1 mm',
            },
            {
                'source' : ['preliminary_expected_17_11_27'],
                'lifetime' : '10',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '1 cm',
            },
            {
                'source' : ['preliminary_expected_17_11_27'],
                'lifetime' : '100',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '10 cm',
            },
            {
                'source' : ['preliminary_expected_17_11_27'],
                'lifetime' : '1000',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '1 m',
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
                'source' : ['preliminary_expected_17_11_27'],
                'mass' : '200',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '200 GeV',
            },
            {
                'source' : ['preliminary_expected_17_11_27'],
                'mass' : '500',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '500 GeV',
            },
            {
                'source' : ['preliminary_expected_17_11_27'],
                'mass' : '800',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '800 GeV',
            },
            {
                'source' : ['preliminary_expected_17_11_27'],
                'mass' : '1100',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '1.1 TeV',
            },
            {
                'source' : ['preliminary_expected_17_11_27'],
                'mass' : '1200',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '1.2 TeV',
            },
        ],
    },
]


