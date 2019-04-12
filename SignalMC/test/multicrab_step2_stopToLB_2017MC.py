from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGIPREMIX_S2_DATAMIX_L1_DIGI2RAW_HLT_2017MC.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8

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

    config.General.requestName = 'stopToLB_M_200_1mm_13TeV_2017MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_200_1mm_13TeV_2017MC/jalimena-GenSim-e217d25a75fda0e5e4cda775d3307369/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_200_10mm_13TeV_2017MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_200_10mm_13TeV_2017MC/jalimena-GenSim-c5503e0b0b269cb6ba1761d99480943f/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_200_100mm_13TeV_2017MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_200_100mm_13TeV_2017MC/jalimena-GenSim-e104d143a174e3697ee5fc6ccfc67106/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_200_1000mm_13TeV_2017MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_200_1000mm_13TeV_2017MC/jalimena-GenSim-03c87cf93b603ecd45de30d940865994/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_300_1mm_13TeV_2017MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_300_1mm_13TeV_2017MC/jalimena-GenSim-85e5fc8a06429597d847a9bb02ae8ec9/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_300_10mm_13TeV_2017MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_300_10mm_13TeV_2017MC/jalimena-GenSim-eb13259d7e36528875945174aeb86e5a/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_300_100mm_13TeV_2017MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_300_100mm_13TeV_2017MC/jalimena-GenSim-1a7174c8876a26f86da2ce5d18a7374c/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_300_1000mm_13TeV_2017MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_300_1000mm_13TeV_2017MC/jalimena-GenSim-30788422f79274a607d2141dfe8411ce/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_400_1mm_13TeV_2017MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_400_1mm_13TeV_2017MC/jalimena-GenSim-3ea665a5e91013854d7643224463adbb/USER'
    submit(config)
