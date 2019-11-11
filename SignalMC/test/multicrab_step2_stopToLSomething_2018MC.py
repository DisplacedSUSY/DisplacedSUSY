from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI_DATAMIX_L1_DIGI2RAW_HLT_2018MC.py'
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

#    config.General.requestName = 'stopToLB_M_100_1mm_13TeV_2018MC_DigiRawHlt'
#    config.Data.inputDataset = '/StopToLB_M_100_1mm_13TeV_2018MC/bcardwel-GenSim-af1dcb41744d95b4df6cacf413f309d7/USER'
#    submit(config)

    config.General.requestName = 'stopToLB_M_100_10mm_13TeV_2018MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_100_10mm_13TeV_2018MC/bcardwel-GenSim-2fc42ee20f4b3d6c369dbf7defe08082/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_100_100mm_13TeV_2018MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_100_100mm_13TeV_2018MC/bcardwel-GenSim-cb7529a3169bac6481071ef3f03e0941/USER'
    submit(config)

    config.General.requestName = 'stopToLB_M_100_1000mm_13TeV_2018MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLB_M_100_1000mm_13TeV_2018MC/bcardwel-GenSim-d204ae9b0f5f5af5858ba34802b7767f/USER'
    submit(config)

    config.General.requestName = 'stopToLD_M_100_1mm_13TeV_2018MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLD_M_100_1mm_13TeV_2018MC/bcardwel-GenSim-016a08e11f39e9daf4ae423eea0b9d36/USER'
    submit(config)

    config.General.requestName = 'stopToLD_M_100_10mm_13TeV_2018MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLD_M_100_10mm_13TeV_2018MC/bcardwel-GenSim-235af62878407306bfff8c1078104043/USER'
    submit(config)

    config.General.requestName = 'stopToLD_M_100_100mm_13TeV_2018MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLD_M_100_100mm_13TeV_2018MC/bcardwel-GenSim-eddedbdb041107c6adb4948f4ecad947/USER'
    submit(config)

    config.General.requestName = 'stopToLD_M_100_1000mm_13TeV_2018MC_DigiRawHlt'
    config.Data.inputDataset = '/StopToLD_M_100_1000mm_13TeV_2018MC/bcardwel-GenSim-212cbb91c3738ab8dcd5def8f093efbc/USER'
    submit(config)
