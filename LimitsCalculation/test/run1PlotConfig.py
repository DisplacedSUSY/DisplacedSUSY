#!/usr/bin/env python

from DisplacedSUSY.Configuration.systematicsDefinitions import signal_cross_sections

intLumi = 19680 # MuEG 22Jan Rereco

masses = ['200','300','400','500','600','700','800','900']
lifetimes = ['0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90','100','200','300','400','500','600','700','800','900','1000']

# description of all the plots to be made
plotDefinitions = [

    {
        # this will be the name of the canvas in the output root file
        'title' : '8_TeV_Asym_limits',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'stop mass [GeV]',
        'yAxisLabel' : 'stop c#tau [cm]',
        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : ['Run1_FinalResults_Asymptotic'],
                'energy' : '8TeV'
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
                'legendEntry' : 'Asym. CL_{s}',
            },
        ],
        'th2fs' : [
            {
                'source' : ['Run1_FinalResults_Asymptotic'],
                'energy' : '8TeV'
                'th2fsToInclude' : ['exp','obs'],
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : '8_TeV_MCMC_limits',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'stop mass [GeV]',
        'yAxisLabel' : 'stop c#tau [cm]',
        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : ['Run1_FinalResults_MCMC'],
                'energy' : '8TeV'
                'graphsToInclude' : ['twoSigma','oneSigma','exp','obs'],
                'legendEntry' : 'MCMC',
            },
        ],
        'th2fs' : [
            {
                'source' : ['Run1_FinalResults_MCMC'],
                'energy' : '8TeV'
                'th2fsToInclude' : ['exp','obs'],
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : '8_TeV_limit_comparison',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'stop mass [GeV]',
        'yAxisLabel' : 'stop c#tau [cm]',
        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : ['Run1_FinalResults_Asymptotic'],
                'energy' : '8TeV'
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'red',
                'legendEntry' : 'Asym. CL_{s}',
            },
            {
                'source' : ['Run1_FinalResults_MCMC'],
                'energy' : '8TeV'
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'blue',
                'legendEntry' : 'MCMC',
            },

        ],
    },
]


