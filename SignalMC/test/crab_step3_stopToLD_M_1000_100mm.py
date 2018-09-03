from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'stopToLD_M_1000_100mm_13TeV_2017MC_Reco'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RAW2DIGI_RECO_RECOSIM_EI.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8

config.Data.inputDataset = '/StopToLD_M_1000_100mm_13TeV_2017MC/jalimena-DigiRawHlt-424e4485a07f26f554e82f829d793003/USER'
config.Data.outputDatasetTag = 'Reco'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpclonglived/DisplacedLeptons'
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
