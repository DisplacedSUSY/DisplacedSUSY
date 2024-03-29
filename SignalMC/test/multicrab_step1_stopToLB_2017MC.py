from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.numCores = 8

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

    config.General.requestName = 'stopToLB_M_100_1mm_13TeV_2017MC_GenSim'
    config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_100_1mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM_2017.py'
    config.Data.outputPrimaryDataset = 'StopToLB_M_100_1mm_13TeV_2017MC'
    submit(config)

    config.General.requestName = 'stopToLB_M_100_10mm_13TeV_2017MC_GenSim'
    config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_100_10mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM_2017.py'
    config.Data.outputPrimaryDataset = 'StopToLB_M_100_10mm_13TeV_2017MC'
    submit(config)

    config.General.requestName = 'stopToLB_M_100_100mm_13TeV_2017MC_GenSim'
    config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_100_100mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM_2017.py'
    config.Data.outputPrimaryDataset = 'StopToLB_M_100_100mm_13TeV_2017MC'
    submit(config)

    config.General.requestName = 'stopToLB_M_100_1000mm_13TeV_2017MC_GenSim'
    config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_100_1000mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM_2017.py'
    config.Data.outputPrimaryDataset = 'StopToLB_M_100_1000mm_13TeV_2017MC'
    submit(config)

    #config.General.requestName = 'stopToLB_M_200_1mm_13TeV_2017MC_GenSim'
    #config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_200_1mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM.py'
    #config.Data.outputPrimaryDataset = 'StopToLB_M_200_1mm_13TeV_2017MC'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_200_10mm_13TeV_2017MC_GenSim'
    #config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_200_10mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM.py'
    #config.Data.outputPrimaryDataset = 'StopToLB_M_200_10mm_13TeV_2017MC'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_200_100mm_13TeV_2017MC_GenSim'
    #config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_200_100mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM.py'
    #config.Data.outputPrimaryDataset = 'StopToLB_M_200_100mm_13TeV_2017MC'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_200_1000mm_13TeV_2017MC_GenSim'
    #config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_200_1000mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM.py'
    #config.Data.outputPrimaryDataset = 'StopToLB_M_200_1000mm_13TeV_2017MC'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_300_1mm_13TeV_2017MC_GenSim'
    #config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_300_1mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM.py'
    #config.Data.outputPrimaryDataset = 'StopToLB_M_300_1mm_13TeV_2017MC'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_300_10mm_13TeV_2017MC_GenSim'
    #config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_300_10mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM.py'
    #config.Data.outputPrimaryDataset = 'StopToLB_M_300_10mm_13TeV_2017MC'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_300_100mm_13TeV_2017MC_GenSim'
    #config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_300_100mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM.py'
    #config.Data.outputPrimaryDataset = 'StopToLB_M_300_100mm_13TeV_2017MC'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_300_1000mm_13TeV_2017MC_GenSim'
    #config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_300_1000mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM.py'
    #config.Data.outputPrimaryDataset = 'StopToLB_M_300_1000mm_13TeV_2017MC'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_400_1mm_13TeV_2017MC_GenSim'
    #config.JobType.psetName = 'DisplacedSUSY_stopToBottom_M_400_1mm_TuneCP5_13TeV_pythia8_cff_py_GEN_SIM.py'
    #config.Data.outputPrimaryDataset = 'StopToLB_M_400_1mm_13TeV_2017MC'
    #submit(config)
