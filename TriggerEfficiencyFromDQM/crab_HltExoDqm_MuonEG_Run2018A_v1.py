from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'HltExoDqm_MuonEG_Run2018A_PromptReco_v1_22May2018_v1'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'hltExodqm2018.py'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.lumiMask = '/uscms_data/d3/alimena/2018TriggerDisplacedSUSY_take2/CMSSW_10_1_5/src/json_DCSONLY_22May2018.txt'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.inputDataset = '/MuonEG/Run2018A-PromptReco-v1/AOD'
config.Data.outputDatasetTag = 'HltExoDqm_MuonEG_Run2018A_PromptReco_v1_22May2018_v1'

config.Site.storageSite = 'T3_US_FNALLPC'