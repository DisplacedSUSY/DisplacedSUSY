from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'stopToLpi_M_XXX_YYYmm_13TeV_2018MC_withCloudModel_GenSim'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'DisplacedSUSY_stopToLB_M_XXX_YYYmm_TuneCP5_13TeV_pythia8_withCloudModel_cff_py_GEN_SIM.py'
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True

config.Data.outputPrimaryDataset = 'StopToLpi_M_XXX_YYYmm_13TeV_2018MC_withCloudModel'
config.Data.outputDatasetTag = 'GenSim'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 100  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC'
