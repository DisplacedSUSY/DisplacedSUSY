from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'staus_M_XXX_YYYmm_13TeV_2018MC_GenSim'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'Staus_M_XXX_YYYmm_TuneCP5_13TeV_pythia8_cff_py_LHE_GEN_SIM.py'
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True
config.JobType.inputFiles = ['/uscms/home/alimena/public_html/GMSBgridpacks/staus_XXX_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz']

config.Data.outputPrimaryDataset = 'Staus_M_XXX_YYYmm_13TeV_2018MC'
config.Data.outputDatasetTag = 'GenSim'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outLFNDirBase = '/store/group/lpclonglived/DisplacedLeptons/'

config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.storageSite = 'T2_CH_CERN'
