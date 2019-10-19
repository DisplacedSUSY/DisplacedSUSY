from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'stopToLB_M_400_1000mm_13TeV_2018MC_DigiRawHlt'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI_L1_DIGI2RAW_HLT_PU.py'
config.JobType.maxMemoryMB = 8000

config.Data.inputDataset = '/StopToLB_M_400_1000mm_13TeV_2018MC/jalimena-GenSim-dcbf478d9c2f1a9ccd2edb69b20655cf/USER'
config.Data.outputDatasetTag = 'DigiRawHlt'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
