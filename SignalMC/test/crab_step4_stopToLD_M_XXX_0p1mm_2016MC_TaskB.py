from CRABClient.UserUtilities import config, getLumiListInValidFiles
from WMCore.DataStructs.LumiList import LumiList
config = config()


config.General.requestName = 'stopToLD_M_XXX_0p1mm_13TeV_2016MC_MiniAod_TaskB'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4_PAT_2016MC_miniAODv3.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/StopToLD_M_XXX_0p1mm_13TeV_2016MC/jalimena-Reco-f61d9997d6423ef82b24bdc986ce3431/USER'
config.Data.outputDatasetTag = 'MiniAod'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True

taskALumis = getLumiListInValidFiles(dataset='/StopToLD_M_XXX_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER', dbsurl='phys03')
officialLumiMask = LumiList(filename='totalMCLumis.json')
newLumiMask = officialLumiMask - taskALumis
newLumiMask.writeJSON('my_lumi_mask.json')
config.Data.lumiMask = 'my_lumi_mask.json'

config.Site.storageSite = 'T3_US_FNALLPC'
