from CRABClient.UserUtilities import config
config = config()


config.General.requestName = 'Cosmics_13TeV_2017MC_MiniAod'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4_PAT_2017MC.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 4
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/Cosmic_MC/tomalin-CMSSW_9_4_10_v1_AOD-d8e16b8877c56c814741f1109ef7da05/USER'
config.Data.outputDatasetTag = 'MiniAod'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC'
