#!/usr/bin/env python

intLumi = 1263.88 
energy = '13'

masses = ['200','300','400','500','600','700','800','900','1000','1100','1200']
lifetimes = ['0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90','100','200','300','400','500','600','700','800','900','1000']

# description of all the plots to be made
plotDefinitions = [

    {
        # this will be the name of the canvas in the output root file
        'title' : 'testaroo',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'stop mass [GeV]',
        'yAxisLabel' : 'stop #LTc#tau#GT [cm]',

        #define all the curves to include on this canvas
        'graphs' : [
           {
               'source' : ['Run1_FinalResults_MCMC'],
               'add_MiniAOD' : True,
               'energy' : '8',
               'graphsToInclude' : ['exp','obs'],
               'colorScheme' : 'blue',
               'legendEntry' : 'Run 1 results',
           },
           {
               'source' : ['limit_july19th_MarkovChain'],
               'energy' : '13',
               'graphsToInclude' : ['exp','obs'],
               'colorScheme' : 'red',
               'legendEntry' : 'Run 2 (2015) results',
           },
           {
               'source' : ['run2MCTest'],
               'energy' : '13',
               'graphsToInclude' : ['exp'],
               'colorScheme' : 'green',
               'legendEntry' : 'expected Run 2 (2016) results',
           },

        ],
    },




]


