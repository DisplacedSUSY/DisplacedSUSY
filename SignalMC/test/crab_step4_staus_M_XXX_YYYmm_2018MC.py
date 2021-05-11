from CRABClient.UserUtilities import config
config = config()


config.General.requestName = 'staus_leptonFilter_M_XXX_YYYmm_13TeV_2018MC_MiniAod'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4_PAT_2018MC.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/Staus_LeptonFilter_M_XXX_YYYmm_13TeV_2018MC/jalimena-Reco-2f1667a4ab974bdf4cb2916f291c3603/USER'
config.Data.outputDatasetTag = 'MiniAod'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True
config.Data.outLFNDirBase = '/store/group/lpclonglived/DisplacedLeptons/'

config.Site.whitelist = ["T1_US_FNAL","T2_US_Nebraska","T2_US_Vanderbilt"]
config.Site.storageSite = 'T3_US_FNALLPC'
