from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'stopToLBottom_M_175_1000mm_13TeV_2018MC_MiniAod'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4_PAT_2018MC.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8

config.Data.inputDataset = '/StopToLBottom_M_175_1000mm_13TeV_2018MC/manunezo-Reco-2fd59cbde119ecab78af65e08efe8aae/USER'
config.Data.outputDatasetTag = 'MiniAod'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC'
