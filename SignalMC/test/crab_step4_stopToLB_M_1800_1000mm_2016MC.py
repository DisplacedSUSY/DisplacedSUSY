from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'stopToLB_M_1800_1000mm_13TeV_2016MC_MiniAod'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4_PAT_2016MC_miniAODv3.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8

config.Data.inputDataset = '/StopToLB_M_1800_1000mm_13TeV_2016MC/jalimena-Reco-b1a4edca9adfa7a2e4059536bf605cd7/USER'
config.Data.outputDatasetTag = 'MiniAod'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC'
