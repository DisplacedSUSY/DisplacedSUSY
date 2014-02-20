 #!/usr/bin/env python

#################################################################################
#################################################################################
### this file contains all information pertaining to systematic uncertainties ###
#################################################################################
#################################################################################


#####################################################
### signal cross sections and their uncertainties ###
#####################################################

#taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections8TeVstopsbottom
signal_cross_sections = {

    '200' : {
      'value' : '18.5245',
      'error' : '1.149',
    },
    '300' : {
      'value' : '1.99608',
      'error' : '1.147',
    },
    '400' : {
      'value' : '0.35683',
      'error' : '1.143',
    },
    '500' : {
      'value' : '0.0855847',
      'error' : '1.15',
    },
    '600' : {
      'value' : '0.0248009',
      'error' : '1.166',
    },
    '700' : {
      'value' : '0.0081141',
      'error' : '1.184',
    },
    '800' : {
      'value' : '0.00289588',
      'error' : '1.205',
    },

}



##############################################
### background normalization uncertainties ###
##############################################

# These are the systematics on the methods to determine the contribution of each process
#
# For things taken from MC, this should be the uncertainty on the calculated cross-section
# or the uncertainty on the measured CMS cross-section
#
# For things take from data, this should be the uncertainty on the data-driven method

background_normalization_uncertainties = {
    # this is basically all Z->tautau, so we take the uncertainty from the last H->tautau result, HIG-13-004
    # 3% number found on page 92 of supporting note AN-2013/011
    'DY' : { 
       'value' : '1.03',
       'type' : 'lnN',
    },
    # this is basically all WW, so we'll take the uncertainty from CMS PAS SMP-12-013
    # central value should be 69.9 pb (need to change that, it's 30% higher than theory value)  
    # well... the WW control region supports using the theory cross section... effing physics
    # 'Diboson' : {
    #    'value' : '1.16',
    #    'type' : 'lnN',
    # },
    # on second thought, let's just use the NLO prediction that they compare to in SMP-12-013
    # that central value is 57.25, and we currently use 54.83, so ~5% higher
    'Diboson' : {
       'value' : '0.972/1.041',
       'type' : 'lnN',
    },
    # taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat8TeV#List_of_processes
    'TTbar' : {
       'value' : '0.966/1.025',
       'type' : 'lnN',
    },
    # taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat8TeV#List_of_processes
    'SingleTop' : {
       'value' : '1.03',
       'type' : 'lnN',
    },
    # use number from PAS SMP-12-011
    # central value should be 356400 pb (need to change that, it's 5% lower than theory value) 
    'WNjets' : {
       'value' : '1.065',
       'type' : 'lnN',
    },


    # taken from error on fitting for QCD yield in ABCD method
    'QCDFromData' : {
       'value' : '1.3',
       'type' : 'lnN',
    },

    # with new merged datasets, just take the uncertainty from the dataset which dominates the sample

##     # dominated by TTbar
##     'Top' : {
##        'value' : '0.966/1.025',
##        'type' : 'lnN',
##     },
##     # dominated by Z->tautau
##     'EWK_WNjets' : {
##        'value' : '1.03',
##        'type' : 'lnN',
##     },


}

######################################################
### Experimental Systematic Uncertainty Parameters ###
######################################################

#list of backgrounds for which we take the yield from MC in some way
mc_normalized_processes = [
   'TTbar',
   'SingleTop',
   'Diboson',
   'DY',
   'WNjets',
   'signal'
]

## mc_normalized_processes = [
##    'Top',
##    'EWK_WNjets',
##    'signal'
## ]



#uncertainties for which the same value applies to all datasets
global_systematic_uncertainties = {
   'lumi' :  {
        'value' : '1.026',
   	'applyList' : mc_normalized_processes,
    },
   'trigger' :  {
        'value' : '1.004',
   	'applyList' : mc_normalized_processes,
    },
   'track_reco' :  {
        'value' : '1.017',
   	'applyList' : mc_normalized_processes,
    },

}

#uncertainties which have different values for each dataset
unique_systematic_uncertainties = {
##     'Top_matching' : {
##         'value' : '1.05',
##         'dataset' : 'Top'
##     },
##     'Top_scale' : {
##         'value' : '1.64',
##         'dataset' : 'Top'
##     },
##     'EWK_WNjets_matching' : {
##         'value' : '1.19',
##         'dataset' : 'EWK_WNjets'
##     },
##     'EWK_WNjets_scale' : {
##         'value' : '1.22',
##         'dataset' : 'EWK_WNjets'
##     },    

    'TTbar_matching' : {
        'value' : '1.004',
        'dataset' : 'TTbar'
    },
    'TTbar_scale' : {
        'value' : '1.02',
        'dataset' : 'TTbar'
    },
##     'SingleTop_matching' : {
##         'value' : '1.05',
##         'dataset' : 'SingleTop'
##     },
##     'SingleTop_scale' : {
##         'value' : '1.64',
##         'dataset' : 'SingleTop'
##     },
    'WNjets_matching' : {
        'value' : '1.08',
        'dataset' : 'WNjets'
    },
    'WNjets_scale' : {
        'value' : '1.026',
        'dataset' : 'WNjets'
    },    
##     'Diboson_matching' : {
##         'value' : '1.19',
##         'dataset' : 'Diboson'
##     },
##     'Diboson_scale' : {
##         'value' : '1.22',
##         'dataset' : 'Diboson'
##     },    
##     'DY_matching' : {
##         'value' : '1.19',
##         'dataset' : 'DY'
##     },
##     'DY_scale' : {
##         'value' : '1.22',
##         'dataset' : 'DY'
##     },    

}


#defined in external text files (located in DisplacedSUSY/Configuration/data)
external_systematic_uncertainties = [
    'electronSF',
    'muonSF',
    'pdf',
    'pileup',
]
