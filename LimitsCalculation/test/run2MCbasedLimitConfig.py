#!/usr/bin/env python

energy = '13'

##################################
### Event Selection Parameters ###
##################################

#name of histogram to integrate to get yields
d0histogramName = "Electron-muon-beamspot Plots/electronAbsD0_vs_muonAbsD0_10cm"


#########################
### Signal Parameters ###
#########################

# a separate datacard will be produced with each value of MASS,CTAU
# named "datacard_stopMASS_CTAUmm.root"

#stop masses
#masses = ['200','300','400','500','600','700','800','900','1000','1100','1200']
#masses = ['300','700']
masses = ['500']
#masses = ['200','500','800']

#stop ctau values (in mm!)
#lifetimes = ['0p1','2']
#lifetimes = ['0.5','5.0','50.0']
#lifetimes = ['0.5','1.0','5.0','10.0','50.0','100.0']
#lifetimes = ['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90','100','200','300','400','500','700','800','900','1000']
#lifetimes = ['0.2','0.3','0.4']
#lifetimes = ['0.5','0.6','0.7','0.8','0.9','1.0']
#lifetimes = ['2.0','3.0','4.0','5.0','6.0','7.0']
#lifetimes = ['8.0','9.0','10.0','20.0','30.0','40.0','50.0','60.0','70.0','80.0','90.0','100.0']
#lifetimes = ['1','10','100','1000']
lifetimes = ['1']


#condor directory in which to find signal root files
signal_condor_dir = 'EMuPreselection_MC_Dec9'

#name of event selection from which to take signal yields
signal_channel = 'PreselectionPlotter'


#######################
### Data Parameters ###
#######################

#this just sets the observed number of events equal to the total background expectation
run_blind_limits = True

data_dataset = "MuonEG_2016"

#condor directory in which to find data root file
data_condor_dir = 'EMuPreselection_MC_Dec9'

#name of event selection from which to take observed events
data_channel = 'PreselectionPlotter'

#############################
### Background Parameters ###
#############################

#list of backgrounds that will be added into the datacards
backgrounds = [
    'Diboson',
#    'DYJetsToLL_50',
    'SingleTop',
    'TTJets_Lept',
#    'QCD_MuEnriched'
]


#information about where to get the yields for each background
background_sources = {
   'Diboson' : {
      'condor_dir' : 'EMuPreselection_MC_Dec9',
      'channel'    : 'PreselectionPlotter',
   },
   'DYJetsToLL_50' : {
      'condor_dir' : 'EMuPreselection_MC_Dec9',
      'channel'    : 'PreselectionPlotter',
   },
   'SingleTop' : {
      'condor_dir' : 'EMuPreselection_MC_Dec9',
      'channel'    : 'PreselectionPlotter',
   },
   'TTJets_Lept' : {
      'condor_dir' : 'EMuPreselection_MC_Dec9',
      'channel'    : 'PreselectionPlotter',
   },
    'QCD_MuEnriched' : {
      'condor_dir' : 'EMuPreselection_MC_Dec9',
      'channel'    : 'PreselectionPlotter',
   },
}

