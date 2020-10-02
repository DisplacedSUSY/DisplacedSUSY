from CRABClient.UserUtilities import config
config = config()


config.General.requestName = 'stopToLBottom_M_300_0p1mm_13TeV_2018MC_DigiRawHlt'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI_DATAMIX_L1_DIGI2RAW_HLT_2018MC.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/StopToLBottom_M_300_0p1mm_13TeV_2018MC/jalimena-GenSim-0060ea1636d6ca87d130b3509802ba88/USER'
config.Data.outputDatasetTag = 'DigiRawHlt'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True
config.Data.outLFNDirBase = '/store/group/lpclonglived/DisplacedLeptons/'

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
