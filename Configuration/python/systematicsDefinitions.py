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
# For things take from data, this should be the uncertainty on the data-driven method

background_normalization_uncertainties = {
    'DY' : { 
       'value' : '1.045',
       'type' : 'lnN',
    },
    'Diboson' : {
       'value' : '1.062',
       'type' : 'lnN',
    },
    'TTbar' : {
       'value' : '1.043',
       'type' : 'lnN',
    },
    'SingleTop' : {
       'value' : '1.069',
       'type' : 'lnN',
    },
    'WNjets' : {
       'value' : '1.035',
       'type' : 'lnN',
    },

    # with new merged datasets, just take the uncertainty from the dataset which dominates the sample

    'DYToTauTau_20' : { 
       'value' : '1.045',
       'type' : 'lnN',
    },
    # dominated by TTbar
    'Top' : {
       'value' : '1.045',
       'type' : 'lnN',
    },
    # lots of contributions, call it 10% to be safe
    'EWK_WNjets_Other' : {
       'value' : '1.10',
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
## mc_normalized_processes = [
##    'EWK_WNjets_Other',
##    'Top',
##    'DYToTauTau_20',
##    'TTbar',
##    'SingleTop',
##    'Diboson',
##    'DY',
##    'WNjets',
##    'signal'
## ]

mc_normalized_processes = [
    'Diboson_MiniAOD',
#    'WJetsToLNu_MiniAOD',                                                                                                                                                                                  
#    'DYJetsToLL_50_MiniAOD',                                                                                                                                                                               
    'SingleTop_MiniAOD',
    'TTJets_Lept_MiniAOD',

   'EWK_WNjets_Other',
   'Top',
   'DYToTauTau_20',
   'signal',

   'TTbar',
   'SingleTop',
   'Diboson',
   'DY',
   'WNjets',

]


#uncertainties for which the same value applies to all datasets
global_systematic_uncertainties = {
   'lumi' :  {
        'value' : '1.026',
   	'applyList' : mc_normalized_processes,
    },
   'trigger' :  {
        'value' : '1.02',
   	'applyList' : mc_normalized_processes,
    },
   'track_reco' :  {
        'value' : '1.056',
   	'applyList' : mc_normalized_processes,
    },
   'dummy' :  {
        'value' : '1.5',
   	'applyList' : mc_normalized_processes,
    },

}

#uncertainties which have different values for each dataset
unique_systematic_uncertainties = {
    'TTbar_matching' : {
        'value' : '1.004',
        'dataset' : 'TTbar'
    },
    'TTbar_scale' : {
        'value' : '1.02',
        'dataset' : 'TTbar'
    },
    'WNjets_matching' : {
        'value' : '1.08',
        'dataset' : 'WNjets'
    },
    'WNjets_scale' : {
        'value' : '1.026',
        'dataset' : 'WNjets'
    },    
}


#defined in external text files (located in DisplacedSUSY/Configuration/data)
external_systematic_uncertainties = [
#    'electronSF',
#    'muonSF',
#    'pdf',
#    'pileup',
]
