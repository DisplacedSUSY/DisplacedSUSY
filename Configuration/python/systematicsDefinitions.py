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
      'error' : '1.3',
    },
    '300' : {
      'value' : '1.99608',
      'error' : '1.3',
    },
    '400' : {
      'value' : '0.35683',
      'error' : '1.3',
    },
    '500' : {
      'value' : '0.0855847',
      'error' : '1.3',
    },
    '600' : {
      'value' : '0.0248009',
      'error' : '1.3',
    },
    '700' : {
      'value' : '0.0081141',
      'error' : '1.3',
    },
    '800' : {
      'value' : '0.00289588',
      'error' : '1.3',
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

    'DY' : {
       'value' : '1.2',
       'type' : 'lnN',
    },
    'Diboson' : {
       'value' : '1.2',
       'type' : 'lnN',
    },
    'TTbar' : {
       'value' : '1.3',
       'type' : 'lnN',
    },
    'SingleTop' : {
       'value' : '1.3',
       'type' : 'lnN',
    },
    'Wjets' : {
       'value' : '1.2',
       'type' : 'lnN',
    },
    'QCDFromData' : {
       'value' : '1.3',
       'type' : 'lnN',
    },

}

######################################################
### Experimental Systematic Uncertainty Parameters ###
######################################################

#list of backgrounds for which we take the yield from MC in some way
mc_normalized_processes = [
   'TTbar',
   'Diboson',
   'DY',
   'Wjets',
#   'QCDFromData',
   'signal'
]

#uncertainties for which the same value applies to all datasets
global_systematic_uncertainties = {
   'lumi' :  {
   	'value' : '1.026',
   	'applyList' : mc_normalized_processes,
    },
}

#defined in external text files (located in DisplacedSUSY/Configuration/data)
external_systematic_uncertainties = [
    'trigger',
    'pileup',
    'muonSF'
]
