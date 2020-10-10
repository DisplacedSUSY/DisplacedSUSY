from CRABClient.UserUtilities import config
config = config()


config.General.requestName = 'stopToLBottom_M_1100_0p1mm_13TeV_2018MC_Reco'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RAW2DIGI_L1Reco_RECO_RECOSIM_EI_2018MC.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/StopToLBottom_M_1100_0p1mm_13TeV_2018MC/jalimena-DigiRawHlt-98b2ebbf2a73ad4baba14fc5516a6604/USER'
config.Data.outputDatasetTag = 'Reco'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
