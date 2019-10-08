from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'stopToLBottom_M_150_1000mm_13TeV_2018MC_GenSim'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_150_1000mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM.py'
config.JobType.numCores = 8

config.Data.outputPrimaryDataset = 'StopToLBottom_M_150_1000mm_13TeV_2018MC'
config.Data.outputDatasetTag = 'GenSim'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/manunezo'
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC'
