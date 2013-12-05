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
##     'Diboson' : {
##        'value' : '1.16',
##        'type' : 'lnN',
##     },
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
       'value' : '1.15',
       'type' : 'lnN',
    },

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
    'muonSF',
    'electronSF',
    'pdf'
]
