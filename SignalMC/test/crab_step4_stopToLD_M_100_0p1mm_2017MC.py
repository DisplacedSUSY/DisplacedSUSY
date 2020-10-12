from CRABClient.UserUtilities import config
config = config()


config.General.requestName = 'stopToLD_M_100_0p1mm_13TeV_2017MC_MiniAod'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4_PAT_2017MC.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 4
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/StopToLD_M_100_0p1mm_13TeV_2017MC/bcardwel-Reco-55097c5b89a6879c0c27fa85d653eedf/USER'
config.Data.outputDatasetTag = 'MiniAod'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
