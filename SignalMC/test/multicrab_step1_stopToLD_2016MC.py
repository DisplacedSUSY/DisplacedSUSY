from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'

config.Data.outputDatasetTag = 'GenSim'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC'

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    config.General.requestName = 'stopToLD_M_100_1mm_13TeV_2016MC_GenSim'
    config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_100_1mm_TuneCUETP8M1_13TeV_pythia8_cff_py_GEN_SIM.py'
    config.Data.outputPrimaryDataset = 'StopToLD_M_100_1mm_13TeV_2016MC'
    submit(config)

    #config.General.requestName = 'stopToLD_M_100_10mm_13TeV_2016MC_GenSim'
    #config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_100_10mm_TuneCUETP8M1_13TeV_pythia8_cff_py_GEN_SIM.py'
    #config.Data.outputPrimaryDataset = 'StopToLD_M_100_10mm_13TeV_2016MC'
    #submit(config)

    #config.General.requestName = 'stopToLD_M_100_100mm_13TeV_2016MC_GenSim'
    #config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_100_100mm_TuneCUETP8M1_13TeV_pythia8_cff_py_GEN_SIM.py'
    #config.Data.outputPrimaryDataset = 'StopToLD_M_100_100mm_13TeV_2016MC'
    #submit(config)

    #config.General.requestName = 'stopToLD_M_100_1000mm_13TeV_2016MC_GenSim'
    #config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_100_1000mm_TuneCUETP8M1_13TeV_pythia8_cff_py_GEN_SIM.py'
    #config.Data.outputPrimaryDataset = 'StopToLD_M_100_1000mm_13TeV_2016MC'
    #submit(config)

