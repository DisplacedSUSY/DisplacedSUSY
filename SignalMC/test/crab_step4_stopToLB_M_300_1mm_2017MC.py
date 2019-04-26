from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'stopToLB_M_300_1mm_13TeV_2017MC_MiniAod'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4_PAT_2017MC.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 4

config.Data.inputDataset = '/StopToLB_M_300_1mm_13TeV_2017MC/jalimena-Reco-ce5bdde49b39cbb6b29d59a381558487/USER'
config.Data.outputDatasetTag = 'MiniAod'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC'
