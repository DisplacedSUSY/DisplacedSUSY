#!/usr/bin/env python


##################################
### Event Selection Parameters ###
##################################

#name of histogram to integrate to get yields
d0histogramName = "electronAbsD0BeamspotVsMuonAbsD0BeamspotForLimits"

#########################
### Signal Parameters ###
#########################

# a separate datacard will be produced with each value of MASS,CTAU,BR
# named "datacard_stopMASS_CTAUmm_brBR.root"

#stop masses
#masses = ['200','300','400','500','600','700','800']
#masses = ['300','700']
masses = ['500']

#stop ctau values
#lifetimes = ['1.0']
#lifetimes = ['0.5','5.0','50.0']
#lifetimes = ['0.5','1.0','5.0','10.0','50.0','100.0']
lifetimes = ['0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0','2.0','3.0','4.0','5.0','6.0','7.0','8.0','9.0','10.0','20.0','30.0','40.0','50.0','60.0','70.0','80.0','90.0','100.0']
#lifetimes = ['0.2','0.3','0.4']
#lifetimes = ['0.5','0.6','0.7','0.8','0.9','1.0']
#lifetimes = ['2.0','3.0','4.0','5.0','6.0','7.0']
#lifetimes = ['8.0','9.0','10.0','20.0','30.0','40.0','50.0','60.0','70.0','80.0','90.0','100.0']

#stop->Bl branching ratios in percent
#branching_ratios = ['0','50','100']
branching_ratios = ['50']

#condor directory in which to find signal root files
signal_condor_dir = 'AUG28__PRESELECTION_AND_BLINDED_PRESELECTION'

#name of event selection from which to take signal yields
signal_channel = 'Preselection'

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

#######################
### Data Parameters ###
#######################

#this just sets the observed number of events equal to the total background expectation
run_blind_limits = True

dataset = "MuEG_22Jan2013"

#condor directory in which to find data root file
data_condir_dir = 'Don\'t even think about looking at the data yet'

#name of event selection from which to take observed events
data_channel = 'Preselection'

#############################
### Background Parameters ###
#############################

#list of backgrounds that will be added into the datacards
backgrounds = [
   'TTbar',
   'Diboson',
   'DY',
   'Wjets',
   'QCDFromData',
]

#information about where to get the yields for each background
#can be taken from a histogram or set manually
background_sources = {
   'TTbar' : {
      'condor_dir' : 'AUG28__PRESELECTION_AND_BLINDED_PRESELECTION',
      'channel'    : 'Preselection',
   },
   'Diboson' : {
      'condor_dir' : 'AUG28__PRESELECTION_AND_BLINDED_PRESELECTION',
      'channel'    : 'Preselection',
   },
   'DY' : {
      'condor_dir' : 'AUG28__PRESELECTION_AND_BLINDED_PRESELECTION',
      'channel'    : 'Preselection',
   },
   'Wjets' : {
      'condor_dir' : 'AUG28__PRESELECTION_AND_BLINDED_PRESELECTION',
      'channel'    : 'Preselection',
   },
   'QCDFromData' : {
      'condor_dir' : 'AUG28__PRESELECTION_AND_BLINDED_PRESELECTION',
      'channel'    : 'Preselection',
   },

}

#'FromHistogram' will calculate the yield by integrating the 'd0histogramName' histogram above the 'd0Cut' value
background_normalization_values = {
   'TTbar'          : 'FromHistogram',
   'Diboson'        : 'FromHistogram',    
   'DY'             : 'FromHistogram',    
   'Wjets'          : 'FromHistogram',    
   'QCDFromData'    : 'FromHistogram',
}

#'FromHistogram' will compute the statistical error on the MC sample used
background_normalization_uncertainties = {

    'DY' : {
       'value' : 'FromHistogram',
       'type' : 'lnN',
    },
    'Diboson' : {
       'value' : 'FromHistogram',
       'type' : 'lnN',
    },
    'TTbar' : {
       'value' : 'FromHistogram',
       'type' : 'lnN',
    },
    'Wjets' : {
       'value' : 'FromHistogram',
       'type' : 'lnN',
    }, 
    'QCDFromData' : {
       'value' : 'FromHistogram',
#       'value' : '1.50', #from MC efficiency estimation scaling
       'type' : 'lnN',
    }, 
}

background_cross_section_uncertainties = {

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
    'Wjets' : {
       'value' : '1.2',
       'type' : 'lnN',
    },
    'QCDFromData' : {
       'value' : '3',
       'type' : 'lnN',
    },

}


######################################################
### Experimental Systematic Uncertainty Parameters ###
######################################################

#list of backgrounds for which we take the yield from MC
mc_normalized_processes = [
   'TTbar',
   'Diboson',
   'DY',
   'Wjets',
   'QCDFromData',
   'signal'
]

systematic_uncertainties = {
   'Lumi' :  {
        'type' : 'lnN',
   	'value' : '1.044',
   	'applyList' : mc_normalized_processes,
    },
}


