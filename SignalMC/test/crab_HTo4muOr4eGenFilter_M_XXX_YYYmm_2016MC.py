import CRABClient
from CRABClient.UserUtilities import config
config = config()


config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'HTo4muOr4eGenFilter_cfg.py'

config.Data.outputDatasetTag = 'MiniAod_4muOr4eGenFilter_2016'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True
config.Data.outLFNDirBase = '/store/group/lpclonglived/DisplacedLeptons/'

config.Site.whitelist = ["T1_US_FNAL","T2_US_Nebraska","T2_US_Vanderbilt"]
config.Site.storageSite = 'T3_US_FNALLPC'


if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    def resubmit(dir):
        try:
            crabCommand('resubmit', dir = 'crab/crab_'+config.General.requestName)
        except HTTPException as hte:
            print "Failed resubmitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed resubmitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    config.General.requestName = 'HTo4muOr4eGenFilter_M_125_30_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-125_MS-30_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_125_30_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-125_MS-30_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_125_30_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-125_MS-30_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_125_30_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-125_MS-30_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_125_30_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-125_MS-30_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_125_50_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-125_MS-50_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_125_50_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-125_MS-50_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_125_50_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-125_MS-50_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_125_50_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-125_MS-50_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_125_50_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-125_MS-50_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_20_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-20_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_20_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-20_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_20_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-20_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_20_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-20_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_20_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-20_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_50_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-50_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_50_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-50_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_50_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-50_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_50_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-50_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_50_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-50_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_150_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-150_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_150_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-150_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_150_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-150_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_150_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-150_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_300_150_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-300_MS-150_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_400_50_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-400_MS-50_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_400_50_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-400_MS-50_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_400_50_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-400_MS-50_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_400_50_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-400_MS-50_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_400_50_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-400_MS-50_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_400_150_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-400_MS-150_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_400_150_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-400_MS-150_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_400_150_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-400_MS-150_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_400_150_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-400_MS-150_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_400_150_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-400_MS-150_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_600_50_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-600_MS-50_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_600_50_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-600_MS-50_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_600_50_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-600_MS-50_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_600_50_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-600_MS-50_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_600_50_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-600_MS-50_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_600_150_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-600_MS-150_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_600_150_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-600_MS-150_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_600_150_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-600_MS-150_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_600_150_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-600_MS-150_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_600_150_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-600_MS-150_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_50_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-50_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_50_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-50_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_50_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-50_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_50_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-50_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_50_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-50_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_150_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-150_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_150_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-150_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_150_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-150_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_150_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-150_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_150_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-150_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_250_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-250_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_250_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-250_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_250_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-250_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_250_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-250_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_800_250_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-800_MS-250_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_30_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_30_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_30_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_30_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_30_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_150_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_150_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_150_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_150_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_150_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_350_10000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_350_1000mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_350_100mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_350_10mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/pablom-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)

    config.General.requestName = 'HTo4muOr4eGenFilter_M_1000_350_1mm_13TeV_2016MC'
    config.Data.inputDataset = '/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8/fernance-RunIISummer16MiniAODv3ext-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
    submit(config)
    #resubmit('crab/crab_'+config.General.requestName)
