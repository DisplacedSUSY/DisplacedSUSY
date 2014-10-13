#!/usr/bin/env python

sHistogram='histo'
scondor_dir='ModelTesting_v0_vz_ptCut'
sMcInitialChannel='McPartInitial'
sSecondMcInitialChannel='SecondaryMcPartInitial'


### Depending on what kind of efficiencies we want to do, pick the corresponding numerator and denominator

sefficiencyType='mu_sel'
checktype=sefficiencyType

if (checktype=="el_reco"):
    sDenChannel=sMcInitialChannel
    sNumChannel=sMcInitialChannel+'_OneRecoEl'
    sHistogram='mcparticleAbsD0Beamspot'
    print sNumChannel

if (checktype=="el_sel"):
    sDenChannel=sMcInitialChannel+'_OneRecoEl'
    sNumChannel=sMcInitialChannel+'_OneRecoEl_Electron_cuts'
    sHistogram='mcparticlePt_smartBin'
    print sNumChannel

if (checktype=="mu_reco"):
    sDenChannel=sSecondMcInitialChannel
    sNumChannel=sSecondMcInitialChannel+'_OneRecoMu'
    sHistogram='secondaryMcparticleAbsD0Beamspot'
    print sNumChannel

if (checktype=="mu_sel"):
    sDenChannel=sSecondMcInitialChannel+'_OneRecoMu'
    sNumChannel=sSecondMcInitialChannel+'_OneRecoMu_Muon_cuts'
    sHistogram='secondaryMcparticlePt_smartBin'
    print sNumChannel
    
sCtau='1000'


input_histograms = [
  { 'condor_dir' : scondor_dir,
    'dataset' : 'stopHadron200toBl_'+sCtau+'.0mm',
    'channel_denominator' : sDenChannel,
    'channel_numerator' : sNumChannel,
    'name' : sHistogram,
    'legend_entry' : 'M=200, CTau='+sCtau+'mm',
    'color' : 2,
    #      'fills' : 'solid',
    },
    { 'condor_dir' : scondor_dir,
    'dataset' : 'stopHadron600toBl_'+sCtau+'.0mm',
    'channel_denominator' : sDenChannel,
    'channel_numerator' : sNumChannel,
    'name' : sHistogram,
    'legend_entry' : 'M=600, CTau='+sCtau+'mm',
    'color' : 2,
    #      'fills' : 'solid',
    },
    { 'condor_dir' : scondor_dir,
    'dataset' : 'stopHadron1000toBl_'+sCtau+'.0mm',
    'channel_denominator' : sDenChannel,
    'channel_numerator' : sNumChannel,
    'name' : sHistogram,
    'legend_entry' : 'M=1000, CTau='+sCtau+'mm',
    'color' : 2,
    #      'fills' : 'solid',
    },
  
]
