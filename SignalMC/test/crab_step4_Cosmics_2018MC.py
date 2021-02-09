from CRABClient.UserUtilities import config
config = config()


config.General.requestName = 'Cosmics_13TeV_2018MC_MiniAod'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4_PAT_2018MC.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/Cosmic_MC/tomalin-CMSSW_10_2_5_AOD_v1c-2ae99c03a9905a8bc2708c290ce57cb6/USER'
config.Data.outputDatasetTag = 'MiniAod'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC'
