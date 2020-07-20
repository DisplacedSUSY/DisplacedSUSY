#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD V2 DATASETS  ####################################################################
############################################################################################################

signal_mc_samples = {
    #DisplacedSUSY Signal (stop --> l+b) MC MiniAOD - 100k events/sample
    'stopToLB800_500mm_2024' : "/DisplacedSUSY_stopToBottom_M_800_500mm_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-106X_mcRun3_2024_realistic_v4-v2/MINIAODSIM",
    'stopToLB800_500mm_2023' : "/DisplacedSUSY_stopToBottom_M_800_500mm_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM",
    'stopToLB800_500mm_2021' : "/DisplacedSUSY_stopToBottom_M_800_500mm_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-106X_mcRun3_2021_realistic_v3-v2/MINIAODSIM",

}

# create composite dictionary of all samples
dataset_names = {}
dataset_names.update(signal_mc_samples)

# Propagate displaced SUSY sample names to the lifetime-reweighted samples
#from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import renameReweightedSamples
#renameReweightedSamples(dataset_names)
