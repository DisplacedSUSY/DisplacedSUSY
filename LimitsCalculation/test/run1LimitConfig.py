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
masses = ['200','300','400','500','600','700','800','900']
#masses = ['300','700']
#masses = ['200']

#stop ctau values
#lifetimes = ['1']
#lifetimes = ['0.5','5','50']
#lifetimes = ['0.5','1','5','10','50','100']
lifetimes = ['0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90','100','200','300','400','500','600','700','800','900','1000']
#lifetimes = ['0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1']
#lifetimes = ['0.2','0.3','0.4']
#lifetimes = ['0.5','0.6','0.7','0.8','0.9','1']
#lifetimes = ['2','3','4','5','6','7']
#lifetimes = ['8','9','10','20','30','40','50','60','70','80','90','100']

#stop->Bl branching ratios in percent
#branching_ratios = ['0','50','100']
branching_ratio = '100'

#condor directory in which to find signal root files
#signal_condor_dir = 'NOV26__QCD_ESTIMATE_DELTAR_SIGNAL'
signal_condor_dir = 'JAN28__Signal'

#name of event selection from which to take signal yields
signal_channel = 'Preselection_100um'


#######################
### Data Parameters ###
#######################

#this just sets the observed number of events equal to the total background expectation
run_blind_limits = False

data_dataset = "MuEG_22Jan2013"

#condor directory in which to find data root file
#data_condor_dir = 'NOV26__QCD_ESTIMATE_DELTAR'
data_condor_dir = 'JAN28__MC_Backgrounds'

#name of event selection from which to take observed events
data_channel = 'Preselection_100um'

#############################
### Background Parameters ###
#############################

#list of backgrounds that will be added into the datacards
backgrounds = [
##    'TTbar',
##    'SingleTop',
##    'Diboson',
##    'DY',
##    'WNjets',
    'Top',
    'EWK_WNjets',
    'QCDFromData',
]

#information about where to get the yields for each background
background_sources = {
##    'TTbar' : {
##       'condor_dir' : 'JAN28__MC_Backgrounds',
##       'channel'    : 'Preselection_100um',
##    },
##    'SingleTop' : {
##       'condor_dir' : 'JAN28__MC_Backgrounds',
##       'channel'    : 'Preselection_100um',
##    },
##    'Diboson' : {
##       'condor_dir' : 'JAN28__MC_Backgrounds',
##       'channel'    : 'Preselection_100um',
##    },
##    'DY' : {
##       'condor_dir' : 'JAN28__MC_Backgrounds',
##       'channel'    : 'Preselection_100um',
##    },
##    'WNjets' : {
##       'condor_dir' : 'JAN28__MC_Backgrounds',
##       'channel'    : 'Preselection_100um',
##    },
   'Top' : {
      'condor_dir' : 'JAN28__MC_Backgrounds',
      'channel'    : 'Preselection_100um',
   },
   'EWK_WNjets' : {
      'condor_dir' : 'JAN28__MC_Backgrounds',
      'channel'    : 'Preselection_100um',
   },
   'QCDFromData' : {
      'condor_dir' : 'JAN28__MC_Backgrounds',
      'channel'    : 'Preselection_100um',
   },

}

