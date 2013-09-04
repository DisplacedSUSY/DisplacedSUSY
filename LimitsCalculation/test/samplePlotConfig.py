#!/usr/bin/env python


# there are 3 parameters that define a signal model:
#   mass
#   lifetime
#   br

# first we define the values to be used when the limit plot axis is the given variable

#stop masses
#masses = ['200','300','400','500','600','700','800']
masses = ['300','400','500','600','700','800']

#stop ctau values
lifetimes = ['0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0','2.0','3.0','4.0','5.0','6.0','7.0','8.0','9.0','10.0','20.0','30.0','40.0','50.0','60.0','70.0','80.0','90.0','100.0']
#lifetimes = ['0.5','1.0','5.0','10.0','50.0','100.0']

#stop->Bl branching ratios in percent
branching_ratios = ['50']

#taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections8TeVstopsbottom
signal_cross_sections = {

    '200' : {
        'value' : '18.5245',
        'error' : '1.149147',
    },
    '300' : {
        'value' : '1.99608',
        'error' : '1.146905',
    },
    '400' : {
        'value' : '0.35683',
        'error' : '1.142848',
    },
    '500' : {
        'value' : '0.0855847',
        'error' : '1.149611',
    },
    '600' : {
        'value' : '0.0248009',
        'error' : '1.166406',
    },
    '700' : {
        'value' : '0.0081141',
        'error' : '1.184146',
     },
    '800' : {
        'value' : '0.00289588',
        'error' : '1.20516',
     },
}


# description of all the plots to be made
plotDefinitions = [

    #each entry corresponds to a canvas in the output file   

    ######################## EXAMPLE LIMIT PLOT VS LIFETIME
##     {
##         # this will be the name of the canvas in the output root file
##         'title' : 'limits_vs_ctau',

##         # current options are 'mass' and 'lifetime'
##         'xAxisType' : 'lifetime',

##         # xmin, xmax, label
##         'xAxisLabel' : 'Stop c#tau [mm]',

##         # optional (scaled automatically if not included)
##         #'yAxis' : [0.0001,100],

##         # optional (False if not included)
##         # currently only works if the x-axis is mass
##         'showTheory' : False,

##         #define all the curves to include on this canvas
##         'graphs' : [
##             {
##                 'source' : 'AUG29_200um',
##                 'br'   : 50,
##                 'mass' : 400,
##                 'graphsToInclude' : ['exp'],
##                 'colorScheme' : 'purple',
##                 'legendEntry' : 'mass_{#tilde{t}} = 400 GeV',
##             },
##             {
##                 'source' : 'AUG29_200um',
##                 'br'   : 50,
##                 'mass' : 600,
##                 'graphsToInclude' : ['exp'],
##                 'colorScheme' : 'yellow',
##                 'legendEntry' : 'mass_{#tilde{t}} = 600 GeV',
##             },
##             {
##                 'source' : 'AUG29_200um',
##                 'br'   : 50,
##                 'mass' : 800,
##                 'graphsToInclude' : ['exp'],
##                 'colorScheme' : 'red',
##                 'legendEntry' : 'mass_{#tilde{t}} = 800 GeV',
##             },
##         ],
##     },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_ctau_optimized',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'Stop c#tau [mm]',

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'AUG29_piecewise',
                'br'   : 50,
                'mass' : 500,
                'graphsToInclude' : ['exp','oneSigma','twoSigma'],
                'colorScheme' : 'brazilian',
                'legendEntry' : 'optimized',
            },
        ],
    },


    ##################### EXAMPLE LIMIT PLOT VS. MASS
    {
        'showTheory' : True,
        'title' : 'limits_vs_mass',
        'xAxisType' : 'mass',
        'xAxisLabel' : 'Stop Mass [GeV]',
        'graphs' : [
            {
                'source' : 'AUG29_200um',
                'br'   : 50,
                'lifetime' : 0.5,
                'colorScheme' : 'green',
                'graphsToInclude' : ['exp'],
                'legendEntry' : 'c#tau_{#tilde{t}} = 0.5 mm',
            },
            {
                'source' : 'AUG29_1000um',
                'br'   : 50,
                'lifetime' : 5.0,
                'colorScheme' : 'red',
                'graphsToInclude' : ['exp'],
                'legendEntry' : 'c#tau_{#tilde{t}} = 5 mm',
            },
            {
                'source' : 'AUG29_1000um',
                'br'   : 50,
                'lifetime' : 50.0,
                'colorScheme' : 'brazilian',
                'graphsToInclude' : ['exp'],
                'legendEntry' : 'c#tau_{#tilde{t}} = 50 mm',
            },
        ],
    },



    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_ctau',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'Stop c#tau [mm]',

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'AUG29_piecewise',
                'br'   : 50,
                'mass' : 500,
                'graphsToInclude' : ['oneSigma','twoSigma'],
                'colorScheme' : 'brazilian',
                'legendEntry' : 'optimized',
            },
##             {
##                 'source' : 'AUG29_0um',
##                 'br'   : 50,
##                 'mass' : 500,
##                 'graphsToInclude' : ['exp'],
##                 'colorScheme' : 'brazilian',
##                 'legendEntry' : 'no |d_{0}| cut',
##             },
            {
                'source' : 'AUG29_200um',
                'br'   : 50,
                'mass' : 500,
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '|d_{0}| > 200 #mum',
            },
            {
                'source' : 'AUG29_500um',
                'br'   : 50,
                'mass' : 500,
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '|d_{0}| > 500 #mum',
            },
            {
                'source' : 'AUG29_1000um',
                'br'   : 50,
                'mass' : 500,
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '|d_{0}| > 1000 #mum',
            },
        ],
    },




]


