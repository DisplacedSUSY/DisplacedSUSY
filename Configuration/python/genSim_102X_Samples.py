#!/usr/bin/env python

############################################################################################################
############  LIST OF GEN-SIM DATASETS  ####################################################################
############################################################################################################

bg_mc_samples = {
}

signal_mc_samples = {

    'stopToLB1000_0p1mm' : "/StopToLB_M_1000_0p1mm_13TeV_2018MC_withCloudModel/jalimena-GenSim-2d3633c9b37070a7a773d8d5a58080dd/USER",
    'stopToLB1000_1mm'   : "/StopToLB_M_1000_1mm_13TeV_2018MC_withCloudModel/jalimena-GenSim-0f895349610d76a6ea7b0e656c656ff6/USER",
    'stopToLB1000_10mm'  : "/StopToLB_M_1000_10mm_13TeV_2018MC_withCloudModel/jalimena-GenSim-2f4dd0a24c7321dbf8a610eeade31a6c/USER",
    'stopToLB1000_100mm' : "/StopToLB_M_1000_100mm_13TeV_2018MC_withCloudModel/jalimena-GenSim-e39772ad3ad93e329739e185352a7758/USER",
    'stopToLB1000_1000mm': "/StopToLB_M_1000_1000mm_13TeV_2018MC_withCloudModel/jalimena-GenSim-b5612ec4a84bf7b31ddb6ab6fc557441/USER",
    'stopToLB1000_10000mm':"/StopToLB_M_1000_10000mm_13TeV_2018MC_withCloudModel/jalimena-GenSim-3902e700902794915777ca09bb7726b8/USER",

}

# create composite dictionary of all samples
dataset_names = {}
dataset_names.update(bg_mc_samples)
dataset_names.update(signal_mc_samples)
