 #!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD V2 DATASETS  ####################################################################
############################################################################################################

dataset_names = {

    #DY
    'DYJetsToLL_50'     : ['/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM', # 63M
                           '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM'], # 63M
    'DYJetsToLL_10to50' : '/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 35M

    #DYBBJets
    'DYBBJetsToLL' : '/DYBBJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 3M

    #WJets
    'WJetsToLNu' : ['/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 30M
                    '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM'], # 57M

    #WW
    'WWToLNuLNu' : '/WWTo2L2Nu_13TeV-powheg/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 2M
    'WWToLNuQQ'  : ['/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 2M
                    '/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'], # 7M

    #WZ
    'WZToLNu2QorQQ2L' : '/WZToLNu2QorQQ2L_aTGC_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 2M
    'WZToLNuNuNu'     : '/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 2M
    'WZToLLLNu'       : '/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 2M

    #ZZ
    'ZZToNuNuQQ' : '/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 30M
    'ZZToLLQQ'   : '/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 15M
    'ZZToLLNuNu' : '/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 9M
    'ZZToLLLL'   : '/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 6M

    #VG
    'WG' : '/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 6M
    'ZG' : '/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM', # 15M

    #SingleTop
    'SingleTop_s_channel'         : '/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 1M
    'SingleTop_t_channel_top'     : '/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 67M
    'SingleTop_t_channel_antitop' : '/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 39M
    'SingleTop_tbarW'             : ['/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 5M
                                     '/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'], # 3M
    'SingleTop_tW'                : ['/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 5M
                                     '/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'], # 3M

    #TTJets
    'TTJets_DiLept'             :             ['/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 6M
                                               '/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'], # 24M
    'TTJets_SingleLeptFromT'    :    ['/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 12M
                                      '/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'], # 50M
    'TTJets_SingleLeptFromTbar' : ['/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 12M
                                   '/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'], # 48M

    #Samples used in AN2017_022
    'TT_AN2017_022'        :     ['/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
                                  '/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_backup_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'],
    'SingleTop_tW_AN2017_022' : '/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    'SingleTop_tbarW_AN2017_022' : '/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',

#    #QCD MuEnriched
    'QCD_MuEnriched_15to20'    :     '/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 4M
    'QCD_MuEnriched_20to30'    :     '/QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 31M
    'QCD_MuEnriched_30to50'    :     '/QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 30M
    'QCD_MuEnriched_50to80'    :     '/QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 20M
    'QCD_MuEnriched_80to120'   :   ['/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 14M
                                    '/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v3/MINIAODSIM'], # 10M
    'QCD_MuEnriched_120to170'  :  ['/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'], # 8M
    'QCD_MuEnriched_170to300'  :  ['/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 8M
                                   '/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'], # 9M
    'QCD_MuEnriched_300to470'  :  ['/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 8M
                                   '/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM', # 16M
                                   '/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM'], # 25M
    'QCD_MuEnriched_470to600'  :  ['/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 4M
                                   '/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM', # 6M
                                   '/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM'], # 10M
    'QCD_MuEnriched_600to800'  :  ['/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 4M
                                   '/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'], # 6M
    'QCD_MuEnriched_800to1000' : ['/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 4M
                                  '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM', # 6M
                                  '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM'], # 10M
    'QCD_MuEnriched_1000toInf' : ['/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 4M
                                  '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v3/MINIAODSIM'], # 10M


#    #QCD EMEnriched
    'QCD_EMEnriched_20to30'   :   '/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 9M
    'QCD_EMEnriched_30to50'   :  ['/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 5M
                                  '/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'], # 7M
    'QCD_EMEnriched_50to80'   :   '/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM', # 23M
    'QCD_EMEnriched_80to120'  : ['/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 36M
                                 '/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'], # 42M
    # !!! No sample!!!    'QCD_EMEnriched_120to170' :
    'QCD_EMEnriched_170to300' : '/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 12M
    'QCD_EMEnriched_300toInf' : '/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 7M

#    #QCD bcToE
    'QCD_bcToE_20to30'   :   '/QCD_Pt_20to30_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 11M
    'QCD_bcToE_30to80'   :   '/QCD_Pt_30to80_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 15M
    # !!! No sample!!!    'QCD_bcToE_80to170'  : '',
    'QCD_bcToE_170to250' : '/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 10M
    'QCD_bcToE_250toInf' : '/QCD_Pt_250toInf_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 10M

    ############################################################################
    # SingleElectron 23Sep rereco
    'SingleEle_2016B'         : '/SingleElectron/Run2016B-23Sep2016-v3/MINIAOD', # 246M
    'SingleEle_2016C'         : '/SingleElectron/Run2016C-23Sep2016-v1/MINIAOD', # 97M
    'SingleEle_2016D'         : '/SingleElectron/Run2016D-23Sep2016-v1/MINIAOD', # 148M
    'SingleEle_2016E'         : '/SingleElectron/Run2016E-23Sep2016-v1/MINIAOD', # 117M
    'SingleEle_2016F'         : '/SingleElectron/Run2016F-23Sep2016-v1/MINIAOD', # 71M
    'SingleEle_2016G'         : '/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD', # 153M
    'SingleEle_2016H'         : ['/SingleElectron/Run2016H-PromptReco-v2/MINIAOD', # 127M
                                 '/SingleElectron/Run2016H-PromptReco-v3/MINIAOD'], # 3M
    ############################################################################

    ############################################################################
    # SingleElectron 03Feb2017 rereco
    'SingleEle_2016B_03Feb2017' : '/SingleElectron/Run2016B-03Feb2017_ver2-v2/MINIAOD',
    'SingleEle_2016C_03Feb2017' : '/SingleElectron/Run2016C-03Feb2017-v1/MINIAOD',
    'SingleEle_2016D_03Feb2017' : '/SingleElectron/Run2016D-03Feb2017-v1/MINIAOD',
    'SingleEle_2016E_03Feb2017' : '/SingleElectron/Run2016E-03Feb2017-v1/MINIAOD',
    'SingleEle_2016F_03Feb2017' : '/SingleElectron/Run2016F-03Feb2017-v1/MINIAOD',
    'SingleEle_2016G_03Feb2017' : '/SingleElectron/Run2016G-03Feb2017-v1/MINIAOD',
    'SingleEle_2016H_03Feb2017' : ['/SingleElectron/Run2016H-03Feb2017_ver2-v1/MINIAOD',
                                   '/SingleElectron/Run2016H-03Feb2017_ver3-v1/MINIAOD'],
    ############################################################################

    ############################################################################
    # SingleMuon 23Sep rereco
    'SingleMu_2016B'         : '/SingleMuon/Run2016B-23Sep2016-v3/MINIAOD', # 158M
    'SingleMu_2016C'         : '/SingleMuon/Run2016C-23Sep2016-v1/MINIAOD', # 67M
    'SingleMu_2016D'         : '/SingleMuon/Run2016D-23Sep2016-v1/MINIAOD', # 98M
    'SingleMu_2016E'         : '/SingleMuon/Run2016E-23Sep2016-v1/MINIAOD', # 91M
    'SingleMu_2016F'         : '/SingleMuon/Run2016F-23Sep2016-v1/MINIAOD', # 65M
    'SingleMu_2016G'         : '/SingleMuon/Run2016G-23Sep2016-v1/MINIAOD', # 150M
    'SingleMu_2016H'         : ['/SingleMuon/Run2016H-PromptReco-v2/MINIAOD', # 171M
                                '/SingleMuon/Run2016H-PromptReco-v3/MINIAOD'], # 4M
    ############################################################################

    ############################################################################
    # SingleMuon 03Feb2017 rereco
    'SingleMu_2016B_03Feb2017' : '/SingleMuon/Run2016B-03Feb2017_ver2-v2/MINIAOD',
    'SingleMu_2016C_03Feb2017' : '/SingleMuon/Run2016C-03Feb2017-v1/MINIAOD',
    'SingleMu_2016D_03Feb2017' : '/SingleMuon/Run2016D-03Feb2017-v1/MINIAOD',
    'SingleMu_2016E_03Feb2017' : '/SingleMuon/Run2016E-03Feb2017-v1/MINIAOD',
    'SingleMu_2016F_03Feb2017' : '/SingleMuon/Run2016F-03Feb2017-v1/MINIAOD',
    'SingleMu_2016G_03Feb2017' : '/SingleMuon/Run2016G-03Feb2017-v1/MINIAOD',
    'SingleMu_2016H_03Feb2017' : ['/SingleMuon/Run2016H-03Feb2017_ver2-v1/MINIAOD',
                                  '/SingleMuon/Run2016H-03Feb2017_ver3-v1/MINIAOD'],
    ############################################################################

    ############################################################################
    # DoubleEG 23Sep rereco
    'DoubleEG_2016B'         : '/DoubleEG/Run2016B-23Sep2016-v3/MINIAOD', # 143M
    'DoubleEG_2016C'         : '/DoubleEG/Run2016C-23Sep2016-v1/MINIAOD', # 48M
    'DoubleEG_2016D'         : '/DoubleEG/Run2016D-23Sep2016-v1/MINIAOD', # 53M
    'DoubleEG_2016E'         : '/DoubleEG/Run2016E-23Sep2016-v1/MINIAOD', # 50M
    'DoubleEG_2016F'         : '/DoubleEG/Run2016F-23Sep2016-v1/MINIAOD', # 35M
    'DoubleEG_2016G'         : '/DoubleEG/Run2016G-23Sep2016-v1/MINIAOD', # 79M
    'DoubleEG_2016H'         : ['/DoubleEG/Run2016H-PromptReco-v2/MINIAOD', # 84M
                                '/DoubleEG/Run2016H-PromptReco-v3/MINIAOD'], # 2M
    ############################################################################

    ############################################################################
    # DoubleMuon 23Sep rereco
    'DoubleMu_2016B'         : '/DoubleMuon/Run2016B-23Sep2016-v3/MINIAOD', # 83M
    'DoubleMu_2016C'         : '/DoubleMuon/Run2016C-23Sep2016-v1/MINIAOD', # 28M
    'DoubleMu_2016D'         : '/DoubleMuon/Run2016D-23Sep2016-v1/MINIAOD', # 34M
    'DoubleMu_2016E'         : '/DoubleMuon/Run2016E-23Sep2016-v1/MINIAOD', # 28M
    'DoubleMu_2016F'         : '/DoubleMuon/Run2016F-23Sep2016-v1/MINIAOD', # 20M
    'DoubleMu_2016G'         : '/DoubleMuon/Run2016G-23Sep2016-v1/MINIAOD', # 45M
    'DoubleMu_2016H'         : ['/DoubleMuon/Run2016H-PromptReco-v2/MINIAOD', # 48M
                                '/DoubleMuon/Run2016H-PromptReco-v3/MINIAOD'], # 1M
    ############################################################################

    ############################################################################
    # MuonEG 23Sep rereco
    'MuonEG_2016B'         : '/MuonEG/Run2016B-23Sep2016-v3/MINIAOD',    # 33M
    'MuonEG_2016C'         : '/MuonEG/Run2016C-23Sep2016-v1/MINIAOD',    # 15M
    'MuonEG_2016D'         : '/MuonEG/Run2016D-23Sep2016-v1/MINIAOD',    # 23M
    'MuonEG_2016E'         : '/MuonEG/Run2016E-23Sep2016-v1/MINIAOD',    # 23M
    'MuonEG_2016F'         : '/MuonEG/Run2016F-23Sep2016-v1/MINIAOD',    # 16M
    'MuonEG_2016G'         : '/MuonEG/Run2016G-23Sep2016-v1/MINIAOD',    # 34M
    'MuonEG_2016H'         : ['/MuonEG/Run2016H-PromptReco-v2/MINIAOD',  # 29M
                              '/MuonEG/Run2016H-PromptReco-v3/MINIAOD'], # 1M
    ############################################################################

    ############################################################################
    # MuonEG 03Feb2017 rereco
    'MuonEG_2016B_03Feb2017' : '/MuonEG/Run2016B-03Feb2017_ver2-v2/MINIAOD',
    'MuonEG_2016C_03Feb2017' : '/MuonEG/Run2016C-03Feb2017-v1/MINIAOD',
    'MuonEG_2016D_03Feb2017' : '/MuonEG/Run2016D-03Feb2017-v1/MINIAOD',
    'MuonEG_2016E_03Feb2017' : '/MuonEG/Run2016E-03Feb2017-v1/MINIAOD',
    'MuonEG_2016F_03Feb2017' : '/MuonEG/Run2016F-03Feb2017-v1/MINIAOD',
    'MuonEG_2016G_03Feb2017' : '/MuonEG/Run2016G-03Feb2017-v1/MINIAOD',
    'MuonEG_2016H_03Feb2017' : ['/MuonEG/Run2016H-03Feb2017_ver2-v1/MINIAOD',
                                '/MuonEG/Run2016H-03Feb2017_ver3-v1/MINIAOD'],
    ############################################################################

    ############################################################################
    # MuonEG 2017 prompt reco
    # Need to check if every v1, v2, etc is necessary
    'MuonEG_2017B' : ['/MuonEG/Run2017B-PromptReco-v1/MINIAOD'
                      '/MuonEG/Run2017B-PromptReco-v2/MINIAOD'],
    'MuonEG_2017C' : ['/MuonEG/Run2017C-PromptReco-v1/MINIAOD',
                      '/MuonEG/Run2017C-PromptReco-v2/MINIAOD',
                      '/MuonEG/Run2017C-PromptReco-v3/MINIAOD'],
    'MuonEG_2017D' : '/MuonEG/Run2017D-PromptReco-v1/MINIAOD',
    ############################################################################

    ############################################################################
    # MET 2017 prompt reco
    'MET_2017D' : '/MET/Run2017D-PromptReco-v1/MINIAOD',
    ############################################################################

    ############################################################################
    # JetHT 2017 prompt reco
    'JetHT_2017D' : '/JetHT/Run2017D-PromptReco-v1/MINIAOD',
    ############################################################################

    ############################################################################
    #DisplacedSUSY Signal MC MiniAOD - 90k events/sample
    'stop200_1mm'    : "/DisplacedSUSY_StopToBL_M-200_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop200_10mm'   : "/DisplacedSUSY_StopToBL_M-200_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop200_100mm'  : "/DisplacedSUSY_StopToBL_M-200_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop200_1000mm' : "/DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop300_1mm'    : "/DisplacedSUSY_StopToBL_M-300_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop300_10mm'   : "/DisplacedSUSY_StopToBL_M-300_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop300_100mm'  : "/DisplacedSUSY_StopToBL_M-300_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop300_1000mm' : "/DisplacedSUSY_StopToBL_M-300_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop400_1mm'    : "/DisplacedSUSY_StopToBL_M-400_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop400_10mm'   : "/DisplacedSUSY_StopToBL_M-400_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop400_100mm'  : "/DisplacedSUSY_StopToBL_M-400_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop400_1000mm' : "/DisplacedSUSY_StopToBL_M-400_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop500_1mm'    : "/DisplacedSUSY_StopToBL_M-500_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop500_10mm'   : "/DisplacedSUSY_StopToBL_M-500_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop500_100mm'  : "/DisplacedSUSY_StopToBL_M-500_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop500_1000mm' : "/DisplacedSUSY_StopToBL_M-500_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop600_1mm'    : "/DisplacedSUSY_StopToBL_M-600_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop600_10mm'   : "/DisplacedSUSY_StopToBL_M-600_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop600_100mm'  : "/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop600_1000mm' : "/DisplacedSUSY_StopToBL_M-600_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop700_1mm'    : "/DisplacedSUSY_StopToBL_M-700_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop700_10mm'   : "/DisplacedSUSY_StopToBL_M-700_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop700_100mm'  : "/DisplacedSUSY_StopToBL_M-700_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop700_1000mm' : "/DisplacedSUSY_StopToBL_M-700_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop800_1mm'    : "/DisplacedSUSY_StopToBL_M-800_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop800_10mm'   : "/DisplacedSUSY_StopToBL_M-800_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop800_100mm'  : "/DisplacedSUSY_StopToBL_M-800_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop800_1000mm' : "/DisplacedSUSY_StopToBL_M-800_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop900_1mm'    : "/DisplacedSUSY_StopToBL_M-900_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop900_10mm'   : "/DisplacedSUSY_StopToBL_M-900_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop900_100mm'  : "/DisplacedSUSY_StopToBL_M-900_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop900_1000mm' : "/DisplacedSUSY_StopToBL_M-900_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop1000_1mm'   : "/DisplacedSUSY_StopToBL_M-1000_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop1000_10mm'  : "/DisplacedSUSY_StopToBL_M-1000_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop1000_100mm' : "/DisplacedSUSY_StopToBL_M-1000_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop1000_1000mm': "/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop1100_1mm'   : "/DisplacedSUSY_StopToBL_M-1100_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop1100_10mm'  : "/DisplacedSUSY_StopToBL_M-1100_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop1100_100mm' : "/DisplacedSUSY_StopToBL_M-1100_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop1100_1000mm': "/DisplacedSUSY_StopToBL_M-1100_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop1200_1mm'   : "/DisplacedSUSY_StopToBL_M-1200_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop1200_10mm'  : "/DisplacedSUSY_StopToBL_M-1200_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop1200_100mm' : "/DisplacedSUSY_StopToBL_M-1200_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stop1200_1000mm': "/DisplacedSUSY_StopToBL_M-1200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    ############################################################################


}




########################################################################################
### code to propagate displaced SUSY sample names to the lifetime-reweighted samples ###
########################################################################################

def mass(sample):
    start = sample.find('stop')+4
    end = sample.find('_')
    return sample[start:end]

from OSUT3Analysis.Configuration.configurationOptions import signal_datasets, srcCTauForLifetimeReweighting

for sample in signal_datasets:
    dataset_names[sample] = dataset_names['stop'+mass(sample)+'_'+'%g' % (10*srcCTauForLifetimeReweighting[sample])+'mm']

########################################################################################
