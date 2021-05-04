#!/usr/bin/env python

# enter lumi valus as a list to display a range
#intLumi = 112800 # full RunII
intLumi = [112800, 117600] # full RunII for channel combination
energy = '13'
#channel = 'e#mu'
channel = None # set to None for multi-channel plots

process = 'HToSSTo4L'
masses = {
  "125"  : ["30"],
  "300"  : ["20", "50", "150"],
  "400"  : ["50", "150"],
  "600"  : ["50", "150"],
  "800"  : ["50", "150", "250"],
  "1000" : ["30", "150", "350"]
}
bareMasses = {
  125  : [30],
  300  : [20, 50, 150],
  400  : [50, 150],
  600  : [50, 150],
  800  : [50, 150, 250],
  1000 : [30, 150, 350]
}
lifetimes = [str(b*10**e) for e in range(0, 4) for b in range(1, 10)] + [str(10000)] #all lifetimes

# description of all the plots to be made
plotDefinitions = [
    #{
    #    # this will be the name of the canvas in the output root file
    #    'title' : 'emu_standard',

    #    # current options are 'mass' and 'lifetime'
    #    'xAxisType' : 'mass',
    #    'yAxisType' : 'lifetime',

    #    # xmin, xmax, label
    #    'xAxisLabel' : 'm_{H} [GeV]',
    #    'yAxisLabel' : 'c#tau [cm]',

    #    #define all the curves to include on this canvas
    #    'th2fs' : [
    #        {
    #            'source' : 'combined_HToSS_2016_unblinded_29Apr2021',
    #            'th2fsToInclude' : ['exp', 'oneSigma', 'obs'],
    #        },
    #    ],
    #    'graphs' : [
    #        {
    #            'source' : 'combined_HToSS_2016_unblinded_29Apr2021',
    #            'graphsToInclude' : ['exp', 'oneSigma', 'obs'],
    #            'colorScheme' : 'brazilian',
    #        },
    #    ],
    #},
    # summary plot of all three channels
    #{
        # this will be the name of the canvas in the output root file
    #    'title' : 'all_standard',

        # current options are 'mass' and 'lifetime'
    #    'xAxisType' : 'mass',
    #    'yAxisType' : 'lifetime',

        # xmin, xmax, label
    #    'xAxisLabel' : 'm_{H} [GeV]',
    #    'yAxisLabel' : 'c#tau [cm]',

        #define all the curves to include on this canvas
    #    'graphs' : [
            #{
            #    'source' : '2015_AN_bg_estimate_12Sep2019',
            #    'graphsToInclude' : ['exp'],
            #    'colorScheme' : 'red',
            #    'legendEntry' : '2015, e#mu channel'
            #},
    #        {
    #            'source' : 'combined_HToSS_2016_unblinded_29Apr2021',
    #            'graphsToInclude' : ['exp'],
    #            'colorScheme' : 'yellow',
                #'legendEntry' : '2016-18, e#mu channel'
    #            'legendEntry' : '2016-18'
    #        },
           # {
           #     'source' : 'EE_run2_21Sep2020',
           #     'graphsToInclude' : ['exp'],
           #     'colorScheme' : 'blue',
           #     'legendEntry' : '2016-18, ee channel'
           # },
           # {
           #     'source' : 'MuMu_run2_21Sep2020',
           #     'graphsToInclude' : ['exp'],
           #     'colorScheme' : 'green',
           #     'legendEntry' : '2016-18, #mu#mu channel'
           # },
     #   ],
    #},
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_mass',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        # xmin, xmax, label
        'xAxisLabel' : 'm_{H} [GeV]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'combined_HToSS_2016_unblinded_29Apr2021',
                'lifetime' : '0.1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '0.01 cm',
            },
            {
                'source' : 'combined_HToSS_2016_unblinded_29Apr2021',
                'lifetime' : '1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '0.1 cm',
            },
            {
                'source' : 'combined_HToSS_2016_unblinded_29Apr2021',
                'lifetime' : '10',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '1 cm',
            },
            {
                'source' : 'combined_HToSS_2016_unblinded_29Apr2021',
                'lifetime' : '100',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '10 cm',
            },
            {
                'source' : 'combined_HToSS_2016_unblinded_29Apr2021',
                'lifetime' : '1000',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '100 cm',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_lifetime_H125',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'c#tau [cm]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'combined_HToSS_2016_unblinded_29Apr2021',
                'mass' : '125_30',
                'm' : '125',
                #'graphsToInclude' : ['exp', 'obs'],
                'graphsToInclude' : ['exp'],
                #'graphsToInclude' : ['obs'],
                'colorScheme' : 'black',
                'legendEntry' : 'm_{H}, m_{S} = 125, 30 GeV',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_lifetime_H1000',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'c#tau [cm]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'combined_HToSS_2016_unblinded_29Apr2021',
                'mass' : '1000_30',
                'm' : '1000',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'black',
                'legendEntry' : 'm_{H}, m_{S} = 1000, 30 GeV',
            },
            {
                'source' : 'combined_HToSS_2016_unblinded_29Apr2021',
                'mass' : '1000_150',
                'm' : '1000',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'red',
                'legendEntry' : 'm_{H}, m_{S} = 1000, 150 GeV',
            },
            {
                'source' : 'combined_HToSS_2016_unblinded_29Apr2021',
                'mass' : '1000_350',
                'm' : '1000',
                'graphsToInclude' : ['obs'],
                'colorScheme' : 'blue',
                'legendEntry' : 'm_{H}, m_{S} = 1000, 350 GeV',
            },
        ],
    },
]
