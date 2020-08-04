 #!/usr/bin/env python
import os
from DisplacedSUSY.Configuration.limitOptions import *

#################################################################################
#################################################################################
### this file contains all information pertaining to systematic uncertainties ###
#################################################################################
#################################################################################


#####################################################
### signal cross sections and their uncertainties ###
#####################################################

#taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom (NLO+NLL)
signal_cross_sections_13TeV = {

    '20' : { #H cross section
      'value' : '43.92',
      'error' : '1.10',
    },
    '50' : { #H cross section
      'value' : '43.92',
      'error' : '1.10',
    },


    '100' : {
      'value' : '1521.11',
      'error' : '1.154038',
    },
    '150' : {
      'value' : '249.409',
      'error' : '1.147477',
    },
    '175' : {
      'value' : '121.416',
      'error' : '1.146341',
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
    '1300' : {
      'value' : '0.000850345',
      'error' : '1.201604',
    },
    '1400' : {
      'value' : '0.000461944',
      'error' : '1.222704',
    },
    '1500' : {
      'value' : '0.000256248',
      'error' : '1.24372',
    },
    '1600' : {
      'value' : '0.000141382',
      'error' : '1.265291',
    },
    '1700' : {
      'value' : '8.07774e-05',
      'error' : '1.287497',
    },
    '1800' : {
      'value' : '4.67492e-05',
      'error' : '1.312291',
    },
    '1900' : {
      'value' : '2.73974e-05',
      'error' : '1.338247',
    },
    '2000' : {
      'value' : '1.62355e-05',
      'error' : '1.365277',
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


######################################################
### Experimental Systematic Uncertainty Parameters ###
######################################################

# list of backgrounds for which we take the yield from MC in some way
mc_normalized_processes = [
    'signal'
]


# uncertainties for which the same value applies to all datasets
if arguments.era == "2016":
    global_systematic_uncertainties = {
        # taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/TWikiLUM#LumiComb
        'lumi_uncorrelated_2016' :  {
            'value' : '1.022',
            'applyList' : mc_normalized_processes,
            },
        'lumi_xyFactorization' :  {
            'value' : '1.009',
            'applyList' : mc_normalized_processes,
            },
        'lumi_beamBeamDeflection' :  {
            'value' : '1.004',
            'applyList' : mc_normalized_processes,
            },
        'lumi_dynamicBeta' :  {
            'value' : '1.005',
            'applyList' : mc_normalized_processes,
            },
        'lumi_ghostsAndSatellites' :  {
            'value' : '1.004',
            'applyList' : mc_normalized_processes,
            },

        # taken from the error on the trigger effieciency scale factor
        'trigger_emu_electron' :  {
            'value' : '1.', #needs to be updated
            'applyList' : mc_normalized_processes,
            },
        'trigger_emu_muon' :  {
            'value' : '1.', #needs to be updated
            'applyList' : mc_normalized_processes,
            },
        'trigger_ee' :  {
            'value' : '1.', #needs to be updated
            'applyList' : mc_normalized_processes,
            },
        'trigger_mumu' :  {
            'value' : '1.', #needs to be updated
            'applyList' : mc_normalized_processes,
            },

        #taken from Ian's study
        'track_reco2016' :  { #2016 uncorrelated with 2017 and 2018 due to different pixel detector in 2016
            'value' : '1.135',
            'applyList' : ['signal'],
            }
        }


elif arguments.era == "2017":
    global_systematic_uncertainties = {
        # taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/TWikiLUM#LumiComb
        'lumi_uncorrelated_2017' :  {
            'value' : '1.020',
            'applyList' : mc_normalized_processes,
            },
        'lumi_xyFactorization' :  {
            'value' : '1.008',
            'applyList' : mc_normalized_processes,
            },
        'lumi_lengthScale' :  {
            'value' : '1.003',
            'applyList' : mc_normalized_processes,
            },
        'lumi_beamBeamDeflection' :  {
            'value' : '1.004',
            'applyList' : mc_normalized_processes,
            },
        'lumi_dynamicBeta' :  {
            'value' : '1.005',
            'applyList' : mc_normalized_processes,
            },
        'lumi_beamCurrentCalibration' :  {
            'value' : '1.003',
            'applyList' : mc_normalized_processes,
            },
        'lumi_ghostsAndSatellites' :  {
            'value' : '1.001',
            'applyList' : mc_normalized_processes,
            },

        # taken from the error on the trigger effieciency scale factor
        'trigger_emu_electron' :  {
            'value' : '1.', #needs to be updated
            'applyList' : mc_normalized_processes,
            },
        'trigger_emu_muon' :  {
            'value' : '1.', #needs to be updated
            'applyList' : mc_normalized_processes,
            },
        'trigger_ee' :  {
            'value' : '1.', #needs to be updated
            'applyList' : mc_normalized_processes,
            },
        'trigger_mumu' :  {
            'value' : '1.', #needs to be updated
            'applyList' : mc_normalized_processes,
            },

        #taken from Ian's study
        'track_reco' :  {
            'value' : '1.047',
            'applyList' : ['signal'],
            }
        }

elif arguments.era == "2018":
    global_systematic_uncertainties = {
        # taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/TWikiLUM#LumiComb
        'lumi_uncorrelated_2018' :  {
            'value' : '1.015',
            'applyList' : mc_normalized_processes,
            },
        'lumi_xyFactorization' :  {
            'value' : '1.020',
            'applyList' : mc_normalized_processes,
            },
        'lumi_lengthScale' :  {
            'value' : '1.002',
            'applyList' : mc_normalized_processes,
            },
        'lumi_beamCurrentCalibration' :  {
            'value' : '1.002',
            'applyList' : mc_normalized_processes,
            },

        # taken from the error on the trigger effieciency scale factor
        'trigger_emu_electron' :  {
            'value' : '1.006',
            'applyList' : mc_normalized_processes,
            },
        'trigger_emu_muon' :  {
            'value' : '1.007',
            'applyList' : mc_normalized_processes,
            },
        'trigger_ee' :  {
            'value' : '1.106',
            'applyList' : mc_normalized_processes,
            },
        'trigger_mumu' :  {
            'value' : '1.008',
            'applyList' : mc_normalized_processes,
            },

        #taken from Ian's study
        'track_reco' :  {
            'value' : '1.', #needs to be updated for 2018
            'applyList' : ['signal'],
            }
        }



# uncertainties that have different values for each dataset
unique_systematic_uncertainties = {
}


# defined in external text files (located in DisplacedSUSY/Configuration/data)
external_systematic_uncertainties = [
    #    'pileup_emu',
    #    'pileup_ee',
    #    'pileup_mumu',
    #    'electronSF_emu',
    #    'muonSF_emu',
    #    'electronSF_ee',
    #    'muonSF_mumu',
    #    'electronD0Smearing_emu',
    #    'muonD0Smearing_emu',
    #    'electronD0Smearing_ee',
    #    'muonD0Smearing_mumu',
]
