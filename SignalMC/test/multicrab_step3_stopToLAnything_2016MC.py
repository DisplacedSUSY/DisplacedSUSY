from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RAW2DIGI_RECO_EI_2016MC.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 4

config.Data.outputDatasetTag = 'Reco'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
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

    #config.General.requestName = 'stopToLD_M_100_1mm_13TeV_2016MC_Reco'
    #config.Data.inputDataset = '/StopToLD_M_100_1mm_13TeV_2016MC/jalimena-DigiRawHlt-16ca0fac1b892ff3c3d45d801745cbbf/USER'
    #submit(config)

    #config.General.requestName = 'stopToLD_M_100_10mm_13TeV_2016MC_Reco'
    #config.Data.inputDataset = '/StopToLD_M_100_10mm_13TeV_2016MC/jalimena-DigiRawHlt-16ca0fac1b892ff3c3d45d801745cbbf/USER'
    #submit(config)

    #config.General.requestName = 'stopToLD_M_100_100mm_13TeV_2016MC_Reco'
    #config.Data.inputDataset = '/StopToLD_M_100_100mm_13TeV_2016MC/jalimena-DigiRawHlt-16ca0fac1b892ff3c3d45d801745cbbf/USER'
    #submit(config)

    #config.General.requestName = 'stopToLD_M_100_1000mm_13TeV_2016MC_Reco'
    #config.Data.inputDataset = '/StopToLD_M_100_1000mm_13TeV_2016MC/jalimena-DigiRawHlt-16ca0fac1b892ff3c3d45d801745cbbf/USER'
    #submit(config)

    config.General.requestName = 'stopToLB_M_100_1mm_13TeV_2016MC_Reco'
    config.Data.inputDataset = '/StopToLB_M_100_1mm_13TeV_2016MC/jalimena-DigiRawHlt-16ca0fac1b892ff3c3d45d801745cbbf/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_100_10mm_13TeV_2016MC_Reco'
    config.Data.inputDataset = '/StopToLB_M_100_10mm_13TeV_2016MC/jalimena-DigiRawHlt-16ca0fac1b892ff3c3d45d801745cbbf/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_100_100mm_13TeV_2016MC_Reco'
    config.Data.inputDataset = '/StopToLB_M_100_100mm_13TeV_2016MC/jalimena-DigiRawHlt-16ca0fac1b892ff3c3d45d801745cbbf/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_100_1000mm_13TeV_2016MC_Reco'
    config.Data.inputDataset = '/StopToLB_M_100_1000mm_13TeV_2016MC/jalimena-DigiRawHlt-16ca0fac1b892ff3c3d45d801745cbbf/USER'
    submit(config)

    #config.General.requestName = 'stopToLB_M_1300_1mm_13TeV_2016MC_Reco'
    #config.Data.inputDataset = '/StopToLB_M_1300_1mm_13TeV_2016MC/jalimena-DigiRawHlt-16ca0fac1b892ff3c3d45d801745cbbf/USER'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_1400_100mm_13TeV_2016MC_Reco'
    #config.Data.inputDataset = '/StopToLB_M_1400_100mm_13TeV_2016MC/jalimena-DigiRawHlt-16ca0fac1b892ff3c3d45d801745cbbf/USER'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_1500_1mm_13TeV_2016MC_Reco'
    #config.Data.inputDataset = '/StopToLB_M_1500_1mm_13TeV_2016MC/jalimena-DigiRawHlt-16ca0fac1b892ff3c3d45d801745cbbf/USER'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_1700_1000mm_13TeV_2016MC_Reco'
    #config.Data.inputDataset = '/StopToLB_M_1700_1000mm_13TeV_2016MC/jalimena-DigiRawHlt-16ca0fac1b892ff3c3d45d801745cbbf/USER'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_1800_1000mm_13TeV_2016MC_Reco'
    #config.Data.inputDataset = '/StopToLB_M_1800_1000mm_13TeV_2016MC/jalimena-DigiRawHlt-16ca0fac1b892ff3c3d45d801745cbbf/USER'
    #submit(config)

