 #!/usr/bin/env python

#################################################################################
#################################################################################
### this file contains all information pertaining to systematic uncertainties ###
#################################################################################
#################################################################################


#####################################################
### signal cross sections and their uncertainties ###
#####################################################

#taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom
signal_cross_sections_13TeV = {

    '100' : {
      'value' : '1521.11',
      'error' : '1.154038',
    },
    '200' : {
      'value' : ' 64.5085',
      'error' : '1.144098',
    },
    '300' : {
      'value' : '8.51615',
      'error' : '1.139223',
    },
    '400' : {
      'value' : '1.83537',
      'error' : '1.136985',
    },
    '500' : {
      'value' : '0.51848',
      'error' : '1.133797',
    },
    '600' : {
      'value' : '0.174599',
      'error' : '1.132074',
    },
    '700' : {
      'value' : '0.0670476',
      'error' : '1.133429',
    },
    '800' : {
      'value' : '0.0283338',
      'error' : '1.14171',
    },
    '900' : {
      'value' : '0.0128895',
      'error' : '1.152026',
    },
    '1000' : {
      'value' : '0.00615134',
      'error' : '1.162953',
    },
    '1100' : {
      'value' : '0.00307413',
      'error' : '1.173377',
    },
    '1200' : {
      'value' : '0.00159844',
      'error' : '1.185209',
    },
}


signal_cross_sections_8TeV = {

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
    '900' : {
      'value' : '0.00109501',
      'error' : '1.239439',
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
#   The measured cross-sections have similar errors to the theory ones, 
#   and are often in different mass windows than our signals
#   so we'll use the theory uncertainties from this twiki:
#   https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV
#       -Jamie 4-19-16
#
# For things take from data, this should be the uncertainty on the data-driven method


background_normalization_uncertainties = {
    #'DYJetsToLL_50' : {
    #   'value' : '1.0379',
    #  'value' : '1.2',
    #  'type' : 'lnN',
    #},
    ## use WW values
    #'Diboson' : {
    #   'value' : '1.025',
    #  'value' : '1.2',
    #  'type' : 'lnN',
    #},
    #'SingleTop' : {
    #   'value' : '1.0423',
    #  'value' : '1.2',
    #  'type' : 'lnN',
    #},
    #'TTJets_Lept' : {
    #   'value' : '1.0614',
    #  'value' : '1.2',
    #  'type' : 'lnN',
    #},
    # 'QCD_MuEnriched' : {
    #    'value' : '1.5',
    #    'type' : 'lnN',
    # },
    # 'QCDFromData' : {
    #    'type': 'lnN',
    #    '0.02':{'value' : '1.324'},
    #    '0.05':{'value' : '1.800'},
    #    '0.1':{'value' : '1.923'},
    # },

}

######################################################
### Experimental Systematic Uncertainty Parameters ###
######################################################

# list of backgrounds for which we take the yield from MC in some way
mc_normalized_processes = [
    'signal'
]


# uncertainties for which the same value applies to all datasets
global_systematic_uncertainties = {
    'lumi' :  {
        'value' : '1.025',
    'applyList' : mc_normalized_processes,
    },
    # taken from the error on the trigger effieciency scale factor
    'trigger' :  {
        'value' : '1.011',
        'applyList' : mc_normalized_processes,
     },
    #taken from Ian's study
    'track_reco' :  {
        'value' : '1.024',
    'applyList' : ['signal'],
}
}

# uncertainties that have different values for each dataset
unique_systematic_uncertainties = {
}


# defined in external text files (located in DisplacedSUSY/Configuration/data)
external_systematic_uncertainties = [
#    'electronSF',
#    'muonSF',
    'pileup',
]
