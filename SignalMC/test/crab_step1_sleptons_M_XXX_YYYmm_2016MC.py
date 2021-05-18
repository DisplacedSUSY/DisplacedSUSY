from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'sleptons_M_XXX_YYYmm_13TeV_2016MC_GenSim'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'Sleptons_M_XXX_YYYmm_TuneCUETP8M1_13TeV_pythia8_cff_py_LHE_GEN_SIM.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.inputFiles = ['/uscms/home/alimena/public_html/GMSBgridpacks/sleptons_XXX_slc6_amd64_gcc700_CMSSW_10_2_24_patch1_tarball.tar.xz']

config.Data.outputPrimaryDataset = 'Sleptons_M_XXX_YYYmm_13TeV_2016MC'
config.Data.outputDatasetTag = 'GenSim'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outLFNDirBase = '/store/group/lpclonglived/DisplacedLeptons/'

config.Site.whitelist = ["T1_US_FNAL","T2_US_Nebraska","T2_US_Vanderbilt"]
config.Site.storageSite = 'T3_US_FNALLPC'
