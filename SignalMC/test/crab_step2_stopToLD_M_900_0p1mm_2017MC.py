from CRABClient.UserUtilities import config
config = config()


config.General.requestName = 'stopToLD_M_900_0p1mm_13TeV_2017MC_DigiRawHlt'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGIPREMIX_S2_DATAMIX_L1_DIGI2RAW_HLT_2017MC.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/StopToLD_M_900_0p1mm_13TeV_2017MC/bcardwel-GenSim-b6469fbbd76e293b69fdb4ccc498bc3e/USER'
config.Data.outputDatasetTag = 'DigiRawHlt'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
