#!/usr/bin/env python

intLumi = 36460
energy = '13'

masses = ['200','300','400','500','600','700','800','900','1000','1100','1200']
lifetimes = ['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90','100','200','300','400','500','600','700','800','900','1000']

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
                'source' : ['run2MCTest'],
                'th2fsToInclude' : ['exp'],
            },
        ],        
        'graphs' : [
            {
                'source' : ['run2MCTest'],
#                'graphsToInclude' : ['twoSigma','oneSigma','exp'],
                'graphsToInclude' : ['exp'],
                'legendEntry' : 'MC-based limits',
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
                'source' : ['run2MCTest'],
                'lifetime' : '0.1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '0.1 mm',
            },
            {
                'source' : ['run2MCTest'],
                'lifetime' : '1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '1 mm',
            },
            {
                'source' : ['run2MCTest'],
                'lifetime' : '10',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '1 cm',
            },
            {
                'source' : ['run2MCTest'],
                'lifetime' : '100',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '10 cm',
            },
            {
                'source' : ['run2MCTest'],
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
                'source' : ['run2MCTest'],
                'mass' : '200',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '200 GeV',
            },
            {
                'source' : ['run2MCTest'],
                'mass' : '500',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '500 GeV',
            },
            {
                'source' : ['run2MCTest'],
                'mass' : '800',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '800 GeV',
            },
            {
                'source' : ['run2MCTest'],
                'mass' : '1100',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '1.1 TeV',
            },
            {
                'source' : ['run2MCTest'],
                'mass' : '1200',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '1.2 TeV',
            },
        ],
    },



]


