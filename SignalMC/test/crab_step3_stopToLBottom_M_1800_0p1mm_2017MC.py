from CRABClient.UserUtilities import config
config = config()


config.General.requestName = 'stopToLBottom_M_1800_0p1mm_13TeV_2017MC_Reco'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RAW2DIGI_RECO_RECOSIM_EI_2017MC.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/StopToLB_M_1800_0p1mm_13TeV_2017MC/bcardwel-DigiRawHlt-159339de0f85bbc0cfe65bb47abccdb3/USER'
config.Data.outputDatasetTag = 'Reco'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
