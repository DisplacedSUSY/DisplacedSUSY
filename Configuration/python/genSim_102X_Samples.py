#!/usr/bin/env python

############################################################################################################
############  LIST OF GEN-SIM DATASETS  ####################################################################
############################################################################################################

bg_mc_samples = {
}

signal_mc_samples = {
    'stopToLB200_1000mm' : "/StopToLB_M_200_1000mm_13TeV_2018MC_withCloudModel/jalimena-GenSim-c69c98045b4066c4b21b3b374c9684cc/USER",
    'stopToLB1000_1000mm': "/StopToLB_M_1000_1000mm_13TeV_2018MC_withCloudModel/jalimena-GenSim-5fcce4e8b93b0e2895d6c1ae16c2514c/USER",
    'stopToLB1800_1000mm': "/StopToLB_M_1800_1000mm_13TeV_2018MC_withCloudModel/jalimena-GenSim-341f225603b71ea433029af453b2e534/USER",
}

# create composite dictionary of all samples
dataset_names = {}
dataset_names.update(bg_mc_samples)
dataset_names.update(signal_mc_samples)
