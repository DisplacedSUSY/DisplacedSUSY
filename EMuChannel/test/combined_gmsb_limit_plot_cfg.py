#!/usr/bin/env python

intLumi = [112800, 117600] # full RunII for channel combination
#intLumi = 59700 # 2018
energy = '13'
channel = None

process = 'gmsb'
masses = [str(50)] + [str(m) for m in range(100, 901, 100)]
lifetimes = [str(b*10**e) for e in range(-2, 4) for b in range(1, 10)] + [str(10000)]

# description of all the plots to be made
plotDefinitions = [
    {
        # this will be the name of the canvas in the output root file
        'title' : 'combined_standard_gmsb_runII_from2016and2018Samples',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : '\\text{m}_{\\~{\\ell}}\\text{ [GeV]}',
        'yAxisLabel' : 'c#tau_{0} [cm]',

        #define all the curves to include on this canvas
        'th2fs' : [
            {
                'source' : 'sleptons_combined_runII_from2016and2018_30Jun2021',
                'th2fsToInclude' : ['obs'],
            },
        ],
        'graphs' : [
            {
                'source' : 'sleptons_combined_runII_from2016and2018_30Jun2021',
                'graphsToInclude' : ['oneSigma', 'exp', 'obs'],
                'colorScheme' : 'susy_pag',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'comparison_standard_gmsb_runII_from2016and2018Samples',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : '\\text{m}_{\\~{\\ell}}\\text{ [GeV]}',
        'yAxisLabel' : 'c#tau_{0} [cm]',

        'graphs' : [
            {
                'source' : 'sleptons_combined_runII_from2016and2018_30Jun2021',
                'graphsToInclude' : ['obs', 'exp'],
                'colorScheme' : 'orange',
                'legendEntry' : 'co-NLSP',
                'filled' : 'true',
            },
            {
                'source' : 'sleptons_mumu_runII_from2016and2018_30Jun2021',
                'graphsToInclude' : ['obs', 'exp'],
                'colorScheme' : 'green',
                'legendEntry' : '\\~{\\mu}\\text{ NLSP}',
                'filled' : 'true',
            },
            {
                'source' : 'sleptons_ee_runII_from2016and2018_30Jun2021',
                'graphsToInclude' : ['obs', 'exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '\\~{\\text{e}}\\text{ NLSP}',
                'filled' : 'true',
            },
            {
                'source' : 'combined_staus_runII_unblinded_30June2021',
                'graphsToInclude' : ['obs', 'exp'],
                'colorScheme' : 'red',
                'legendEntry' : '\\~{\\tau}\\text{ NLSP}',
                'filled' : 'true',
            },
        ],
    },
]
