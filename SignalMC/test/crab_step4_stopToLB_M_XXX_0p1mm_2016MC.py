from CRABClient.UserUtilities import config
config = config()


config.General.requestName = 'stopToLB_M_XXX_0p1mm_13TeV_2016MC_MiniAod'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4_PAT_2016MC_miniAODv3.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/StopToLBottom_M_XXX_0p1mm_13TeV_2016MC/jalimena-Reco-f61d9997d6423ef82b24bdc986ce3431/USER'
config.Data.outputDatasetTag = 'MiniAod'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC'
