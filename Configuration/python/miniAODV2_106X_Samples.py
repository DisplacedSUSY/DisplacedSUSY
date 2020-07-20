#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD V2 DATASETS  ####################################################################
############################################################################################################

signal_mc_samples = {
    #DisplacedSUSY Signal (stop --> l+b) MC MiniAOD - 100k events/sample
    'stopToLB800_500mm_2024' : "/DisplacedSUSY_stopToBottom_M_800_500mm_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-106X_mcRun3_2024_realistic_v4-v2/MINIAODSIM",
    'stopToLB800_500mm_2023' : "/DisplacedSUSY_stopToBottom_M_800_500mm_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM",
    'stopToLB800_500mm_2021' : "/DisplacedSUSY_stopToBottom_M_800_500mm_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-106X_mcRun3_2021_realistic_v3-v2/MINIAODSIM",

    'stopToLB300_1000mm_preVFP'  : "/RelValDispSUSY_M300_1000mm_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_preVFP_v8_hltul16_preVFP-v1/MINIAODSIM",
    'stopToLB300_1000mm_postVFP' : "/RelValDispSUSY_M300_1000mm_13UP16/CMSSW_10_6_12-PU25ns_106X_mcRun2_asymptotic_v13_hltul16_postVFP-v1/MINIAODSIM",

}

# create composite dictionary of all samples
dataset_names = {}
dataset_names.update(signal_mc_samples)

# Propagate displaced SUSY sample names to the lifetime-reweighted samples
#from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import renameReweightedSamples
#renameReweightedSamples(dataset_names)
