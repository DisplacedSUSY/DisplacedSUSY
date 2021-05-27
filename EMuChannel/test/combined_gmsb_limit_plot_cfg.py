#!/usr/bin/env python

intLumi = [112800, 117600] # full RunII for channel combination
#intLumi = 59700 # 2018
energy = '13'
channel = None

process = 'gmsb'
masses = [str(50)] + [str(m) for m in range(100, 1001, 100)]
lifetimes = [str(b*10**e) for e in range(-1, 3) for b in range(1, 10)] + [str(1000)]

# description of all the plots to be made
plotDefinitions = [
    {
        # this will be the name of the canvas in the output root file
        'title' : 'combined_standard_gmsb_runII_from2018Samples',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{l}} [GeV]',
        'yAxisLabel' : 'c#tau [cm]',
        #'yAxisLabel' : '#tau [ns]',

        #define all the curves to include on this canvas
        'th2fs' : [
            {
                'source' : 'gmsb_coNLSP_runII_from2018Samples_25May2021',
                'th2fsToInclude' : ['obs'],
            },
        ],
        'graphs' : [
            {
                'source' : 'gmsb_coNLSP_runII_from2018Samples_25May2021',
                'graphsToInclude' : ['oneSigma', 'exp', 'obs'],
                'colorScheme' : 'susy_pag',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'comparison_standard_gmsb_runII_from2018Samples',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{l}} [GeV]',
        'yAxisLabel' : 'c#tau [cm]',
        #'yAxisLabel' : '#tau [ns]',

        'graphs' : [
            {
                'source' : 'gmsb_coNLSP_runII_from2018Samples_25May2021',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'orange',
                'legendEntry' : 'co-NLSP'
            },
            {
                'source' : 'sleptons_ee_runII_from2018Samples_25May2021',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'blue',
                'legendEntry' : '#tilde{e} NLSP'
            },
            {
                'source' : 'sleptons_mumu_runII_from2018Samples_25May2021',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'green',
                'legendEntry' : '#tilde{#mu} NLSP'
            },
            {
                'source' : 'staus_combined_runII_from2018Samples_25May2021',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'red',
                'legendEntry' : '#tilde{#tau} NLSP'
            },
        ],
    },
]
