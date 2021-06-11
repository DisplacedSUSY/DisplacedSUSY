#!/usr/bin/env python

# enter lumi valus as a list to display a range
#intLumi = 112800 # full RunII
intLumi = [112800, 117600] # full RunII for channel combination
#intLumi = [52800, 57600] # 2016_2017 for channel combination
#intLumi = 16100 # 2016 only
energy = '13'
#channel = 'e#mu'
channel = None # set to None for multi-channel plots

process = 'HToSSTo4L'
masses = {
    "125"  : ["30", "50"],
    "300"  : ["20", "50", "150"],
    "400"  : ["50", "150"],
    "600"  : ["50", "150"],
    "800"  : ["50", "150", "250"],
    #"1000" : ["30", "150", "350"]
    "1000" : ["150", "350"]
}
bareMasses = {
    125  : [30, 50],
    300  : [20, 50, 150],
    400  : [50, 150],
    600  : [50, 150],
    800  : [50, 150, 250],
    #1000 : [30, 150, 350]
    1000 : [150, 350]
}
#20: green
#30: blue
#50: red
#150: purple
#250: magenta
#350: orange

lifetimes = [str(b*10**e) for e in range(0, 4) for b in range(1, 10)] + [str(10000)] #all lifetimes

# description of all the plots to be made
plotDefinitions = [
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
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '125_30',
                'm' : '125',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'blue',
                'legendEntry' : 'm_{H} = 125 GeV, m_{S} = 30 GeV',
            },
            {
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '125_50',
                'm' : '125',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'red',
                'legendEntry' : 'm_{H} = 125 GeV, m_{S} = 50 GeV',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_lifetime_H300',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'c#tau [cm]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '300_20',
                'm' : '300',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'green',
                'legendEntry' : 'm_{H} = 300 GeV, m_{S} = 20 GeV',
            },
            {
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '300_50',
                'm' : '300',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'red',
                'legendEntry' : 'm_{H} = 300 GeV, m_{S} = 50 GeV',
            },
            {
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '300_150',
                'm' : '300',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'purple',
                'legendEntry' : 'm_{H} = 300 GeV, m_{S} = 150 GeV',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_lifetime_H400',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'c#tau [cm]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '400_50',
                'm' : '400',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'red',
                'legendEntry' : 'm_{H} = 400 GeV, m_{S} = 50 GeV',
            },
            {
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '400_150',
                'm' : '400',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'purple',
                'legendEntry' : 'm_{H} = 400 GeV, m_{S} = 150 GeV',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_lifetime_H600',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'c#tau [cm]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '600_50',
                'm' : '600',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'red',
                'legendEntry' : 'm_{H} = 600 GeV, m_{S} = 50 GeV',
            },
            {
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '600_150',
                'm' : '600',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'purple',
                'legendEntry' : 'm_{H} = 600 GeV, m_{S} = 150 GeV',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_lifetime_H800',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'c#tau [cm]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '800_50',
                'm' : '800',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'red',
                'legendEntry' : 'm_{H} = 800 GeV, m_{S} = 50 GeV',
            },
            {
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '800_150',
                'm' : '800',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'purple',
                'legendEntry' : 'm_{H} = 800 GeV, m_{S} = 150 GeV',
            },
            {
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '800_250',
                'm' : '800',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'magenta',
                'legendEntry' : 'm_{H} = 800 GeV, m_{S} = 250 GeV',
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
            #{
            #    'source' : 'combined_HToSS_201617_unblinded_24May2021',
            #    'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
            #    'mass' : '1000_30',
            #    'm' : '1000',
            #    'graphsToInclude' : ['exp', 'obs'],
            #    'colorScheme' : 'blue',
            #    'legendEntry' : 'm_{H} = 1000 GeV, m_{S} = 30 GeV',
            #},
            {
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '1000_150',
                'm' : '1000',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'purple',
                'legendEntry' : 'm_{H} = 1000 GeV, m_{S} = 150 GeV',
            },
            {
                #'source' : 'combined_HToSS_201617_unblinded_24May2021',
                'source' : 'combined_HToSS_scaledRunII_unblinded_10June2021',
                'mass' : '1000_350',
                'm' : '1000',
                'graphsToInclude' : ['exp', 'obs'],
                'colorScheme' : 'orange',
                'legendEntry' : 'm_{H} = 1000 GeV, m_{S} = 350 GeV',
            },
        ],
    },
]
