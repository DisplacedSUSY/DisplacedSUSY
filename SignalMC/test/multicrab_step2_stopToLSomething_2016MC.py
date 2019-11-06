from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGIPREMIX_S2_DATAMIX_L1_DIGI2RAW_HLT_2016MC.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 4

config.Data.outputDatasetTag = 'DigiRawHlt'
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

    config.General.requestName = 'stopToLD_M_100_1mm_13TeV_2016MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLD_M_100_1mm_13TeV_2016MC/jalimena-GenSim-afa0612471b64ef5adb7c494f1dc01a5/USER'
    submit(config)

    config.General.requestName = 'stopToLD_M_100_10mm_13TeV_2016MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLD_M_100_10mm_13TeV_2016MC/jalimena-GenSim-457df939784093b8cafad91877cec960/USER'
    submit(config)

    config.General.requestName = 'stopToLD_M_100_100mm_13TeV_2016MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLD_M_100_100mm_13TeV_2016MC/jalimena-GenSim-91b7d60313f73834a3904a1b09779607/USER'
    submit(config)

    config.General.requestName = 'stopToLD_M_100_1000mm_13TeV_2016MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLD_M_100_1000mm_13TeV_2016MC/jalimena-GenSim-e691b80c590e2e2186f2a8e460b6d318/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_100_1mm_13TeV_2016MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_100_1mm_13TeV_2016MC/jalimena-GenSim-afa0612471b64ef5adb7c494f1dc01a5/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_100_10mm_13TeV_2016MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_100_10mm_13TeV_2016MC/jalimena-GenSim-457df939784093b8cafad91877cec960/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_100_100mm_13TeV_2016MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_100_100mm_13TeV_2016MC/jalimena-GenSim-91b7d60313f73834a3904a1b09779607/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_100_1000mm_13TeV_2016MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_100_1000mm_13TeV_2016MC/jalimena-GenSim-e691b80c590e2e2186f2a8e460b6d318/USER'
    submit(config)

    #config.General.requestName = 'stopToLB_M_1300_1mm_13TeV_2016MC_DigiRawHlt'
    #config.Data.inputDataset = '/StopToLB_M_1300_1mm_13TeV_2016MC/jalimena-GenSim-571cb03f0156f0653d0706e7312a8d9d/USER'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_1400_100mm_13TeV_2016MC_DigiRawHlt'
    #config.Data.inputDataset = '/StopToLB_M_1400_100mm_13TeV_2016MC/jalimena-GenSim-323f31bea03f2709e855922575f454c1/USER'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_1500_1mm_13TeV_2016MC_DigiRawHlt'
    #config.Data.inputDataset = '/StopToLB_M_1500_1mm_13TeV_2016MC/jalimena-GenSim-a96bf78cd7374423a6d0d4668c4ea784/USER'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_1700_1000mm_13TeV_2016MC_DigiRawHlt'
    #config.Data.inputDataset = '/StopToLB_M_1700_1000mm_13TeV_2016MC/jalimena-GenSim-75d6b5bdd566f46523eda82d35aaa0a5/USER'
    #submit(config)

    #config.General.requestName = 'stopToLB_M_1800_1000mm_13TeV_2016MC_DigiRawHlt'
    #config.Data.inputDataset = '/StopToLB_M_1800_1000mm_13TeV_2016MC/jalimena-GenSim-f3d89c44409ab81720d3cba915ffca55/USER'
    #submit(config)

