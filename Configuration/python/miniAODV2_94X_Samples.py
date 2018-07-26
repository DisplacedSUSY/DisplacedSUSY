 #!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD V2 DATASETS  ####################################################################
############################################################################################################

dataset_names = {
    #DY
    'DYJetsToLL_50'     : ['/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#49M
                           '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'],#49M

    'DYJetsToLL_10to50' : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM',# 39M

    #DYBBJets
    'DYBBJetsToLL' : '/DYBBJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',# 3M

    #WJets
    'WJetsToLNu' : ['/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#21M
                    '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#14M
                    '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#22M
                    '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#20M
                    '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#20M
                    '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM'],#21M

    #WW
    'WWToLNuLNu' : '/WWTo2L2Nu_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM',#2M
    'WWToLNuQQ'  : ['/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#9M
                    '/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'],#10M

    #WZ
    'WZToLNu2QorQQ2L' : ['/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',#19M
                         '/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'],#28M
    'WZToLNuNuNu'     : '',#doesn't exist for 2017 MC yet
    'WZToLLLNu'       : '/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#11M

    #ZZ
    'ZZToNuNuQQ' : '',#doesn't exist for 2017 MC yet
    'ZZToLLQQ'   : '/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#28M
    'ZZToLLNuNu' : '/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM',#8M #need to update to MiniAODv2 when available
    'ZZToLLLL'   : ['/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#7M
                    '/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'],#98M

    #VG
    'WG' : '',#doesn't exist for 2017 MC yet
    'ZG' : '',#doesn't exist for 2017 MC yet

    #SingleTop
    'SingleTop_s_channel'         : '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#9M
    'SingleTop_t_channel_top'     : '/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',#6M
    'SingleTop_t_channel_antitop' : '/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#4M
    'SingleTop_tbarW'             : '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',#6M
    'SingleTop_tW'                : '/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#5M

    #TTJets
    'TTJets_inclusive'          : '/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#153M
    'TTJets_SingleLeptFromT'    : '/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#62M
    'TTJets_DiLept'             : '',#doesn't exist for 2017 MC yet
    'TTJets_SingleLeptFromTbar' : '',#doesn't exist for 2017 MC yet

    #QCD MuEnriched
    'QCD_MuEnriched_15to20'    : '/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#6M
    'QCD_MuEnriched_20to30'    : '/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#3M
    'QCD_MuEnriched_30to50'    : '/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#29M
    'QCD_MuEnriched_50to80'    : '/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#24M
    'QCD_MuEnriched_80to120'   : '/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#23M
    'QCD_MuEnriched_120to170'  : '/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#21M
    'QCD_MuEnriched_170to300'  : '/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#46M
    'QCD_MuEnriched_300to470'  : '/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM',# 18M #need to update to MiniAODv2
    'QCD_MuEnriched_470to600'  : '/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#24M
    'QCD_MuEnriched_600to800'  : '/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM',# 16M #need to update to MiniAODv2
    'QCD_MuEnriched_800to1000' : '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM',# 16M #need to update to MiniAODv2
    'QCD_MuEnriched_1000toInf' : '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM',# 11M #need to update to MiniAODv2

    #QCD EMEnriched
    'QCD_EMEnriched_15to20'   : '/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#11M
    'QCD_EMEnriched_20to30'   : '/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#11M
    'QCD_EMEnriched_30to50'   : '/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#15M
    'QCD_EMEnriched_50to80'   : '/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#10M
    'QCD_EMEnriched_80to120'  : '/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM',# 8M #need to update to MiniAODv2
    'QCD_EMEnriched_120to170' : '/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM',# 9M #need to update to MiniAODv2
    'QCD_EMEnriched_170to300' : '/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM',# 4M #need to update to MiniAODv2
    'QCD_EMEnriched_300toInf' : '/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#3M

    #QCD DoubleEMEnriched
    'QCD_DoubleEMEnriched_HighMass_30to40' : '/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#15M
    'QCD_DoubleEMEnriched_LowMass_30toInf' : '/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#42M
    'QCD_DoubleEMEnriched_HighMass_40toInf' : '/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#21M

    #QCD bcToE
    'QCD_bcToE_15to20'   : '/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v11-v1/MINIAODSIM',#2M #need to update to MiniAODv2
    'QCD_bcToE_20to30'   : '/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#10M
    'QCD_bcToE_30to80'   : '/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#16M
    'QCD_bcToE_80to170'  : '/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#16M
    'QCD_bcToE_170to250' : '/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#10M
    'QCD_bcToE_250toInf' : '/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#10M

    ############################################################################

    ############################################################################
    # MuonEG 2017,31Mar2018 rereco
    'MuonEG_2017B' : '/MuonEG/Run2017B-31Mar2018-v1/MINIAOD',
    'MuonEG_2017C' : '/MuonEG/Run2017C-31Mar2018-v1/MINIAOD',
    'MuonEG_2017D' : '/MuonEG/Run2017D-31Mar2018-v1/MINIAOD',
    'MuonEG_2017E' : '/MuonEG/Run2017E-31Mar2018-v1/MINIAOD',
    'MuonEG_2017F' : '/MuonEG/Run2017F-31Mar2018-v1/MINIAOD',
    ############################################################################

    ############################################################################
    # DoubleMuon 2017,31Mar2018 rereco
    'DoubleMu_2017B' : '/DoubleMuon/Run2017B-31Mar2018-v1/MINIAOD',
    'DoubleMu_2017C' : '/DoubleMuon/Run2017C-31Mar2018-v1/MINIAOD',
    'DoubleMu_2017D' : '/DoubleMuon/Run2017D-31Mar2018-v1/MINIAOD',
    'DoubleMu_2017E' : '/DoubleMuon/Run2017E-31Mar2018-v1/MINIAOD',
    'DoubleMu_2017F' : '/DoubleMuon/Run2017F-31Mar2018-v1/MINIAOD',
    ############################################################################

    ############################################################################
    # DoubleEG 2017,31Mar2018 rereco
    'DoubleEG_2017B' : '/DoubleEG/Run2017B-31Mar2018-v1/MINIAOD',
    'DoubleEG_2017C' : '/DoubleEG/Run2017C-31Mar2018-v1/MINIAOD',
    'DoubleEG_2017D' : '/DoubleEG/Run2017D-31Mar2018-v1/MINIAOD',
    'DoubleEG_2017E' : '/DoubleEG/Run2017E-31Mar2018-v1/MINIAOD',
    'DoubleEG_2017F' : '/DoubleEG/Run2017F-31Mar2018-v1/MINIAOD',
    ############################################################################

    ############################################################################
    # MET 2017,31Mar2018 rereco
    'MET_2017B' : '/MET/Run2017B-31Mar2018-v1/MINIAOD',
    'MET_2017C' : '/MET/Run2017C-31Mar2018-v1/MINIAOD',
    'MET_2017D' : '/MET/Run2017D-31Mar2018-v1/MINIAOD',
    'MET_2017E' : '/MET/Run2017E-31Mar2018-v1/MINIAOD',
    'MET_2017F' : '/MET/Run2017F-31Mar2018-v1/MINIAOD',
    ############################################################################

    ############################################################################
    # JetHT 2017,31Mar2018 rereco
    'JetHT_2017B' : '/JetHT/Run2017B-31Mar2018-v1/MINIAOD',
    'JetHT_2017C' : '/JetHT/Run2017C-31Mar2018-v1/MINIAOD',
    'JetHT_2017D' : '/JetHT/Run2017D-31Mar2018-v1/MINIAOD',
    'JetHT_2017E' : '/JetHT/Run2017E-31Mar2018-v1/MINIAOD',
    'JetHT_2017F' : '/JetHT/Run2017F-31Mar2018-v1/MINIAOD',
    ############################################################################

    #DisplacedSUSY Signal (stop --> l+b) MC MiniAOD - 100k events/sample
    'stop400_1000mm' : "/DisplacedSUSY_stopToBottom_M_400_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop400_100mm'  : "/DisplacedSUSY_stopToBottom_M_400_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop400_10mm'   : "/DisplacedSUSY_stopToBottom_M_400_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop400_10mm'   : "/DisplacedSUSY_stopToBottom_M_400_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'stop500_1000mm' : "/DisplacedSUSY_stopToBottom_M_500_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stop500_100mm'  : "/DisplacedSUSY_stopToBottom_M_500_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop500_10mm'   : "/DisplacedSUSY_stopToBottom_M_500_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop500_1mm'    : "/DisplacedSUSY_stopToBottom_M_500_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'stop600_1000mm' : "/DisplacedSUSY_stopToBottom_M_600_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop600_100mm'  : "/DisplacedSUSY_stopToBottom_M_600_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop600_10mm'   : "/DisplacedSUSY_stopToBottom_M_600_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop600_1mm'    : "/DisplacedSUSY_stopToBottom_M_600_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'stop700_1000mm' : "/DisplacedSUSY_stopToBottom_M_700_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stop700_100mm'  : "/DisplacedSUSY_stopToBottom_M_700_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop700_10mm'   : "/DisplacedSUSY_stopToBottom_M_700_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stop700_1mm'    : "/DisplacedSUSY_stopToBottom_M_700_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'stop800_1000mm' : "/DisplacedSUSY_stopToBottom_M_800_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop800_100mm'  : "/DisplacedSUSY_stopToBottom_M_800_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop800_10mm'   : "/DisplacedSUSY_stopToBottom_M_800_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'stop900_1000mm' : "/DisplacedSUSY_stopToBottom_M_900_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stop900_100mm'  : "/DisplacedSUSY_stopToBottom_M_900_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop900_10mm'   : "/DisplacedSUSY_stopToBottom_M_900_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stop900_1mm'    : "/DisplacedSUSY_stopToBottom_M_900_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'stop1000_1000mm': "/DisplacedSUSY_stopToBottom_M_1000_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1000_100mm' : "/DisplacedSUSY_stopToBottom_M_1000_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1000_10mm'  : "/DisplacedSUSY_stopToBottom_M_1000_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1000_1mm'   : "/DisplacedSUSY_stopToBottom_M_1000_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'stop1100_1000mm': "/DisplacedSUSY_stopToBottom_M_1100_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1100_100mm' : "/DisplacedSUSY_stopToBottom_M_1100_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stop1100_1mm'   : "/DisplacedSUSY_stopToBottom_M_1100_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'stop1300_1000mm': "/DisplacedSUSY_stopToBottom_M_1300_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1300_100mm' : "/DisplacedSUSY_stopToBottom_M_1300_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'stop1400_1000mm': "/DisplacedSUSY_stopToBottom_M_1400_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1400_100mm' : "/DisplacedSUSY_stopToBottom_M_1400_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1400_10mm'  : "/DisplacedSUSY_stopToBottom_M_1400_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1400_1mm'   : "/DisplacedSUSY_stopToBottom_M_1400_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'stop1500_1000mm': "/DisplacedSUSY_stopToBottom_M_1500_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1500_100mm' : "/DisplacedSUSY_stopToBottom_M_1500_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1500_10mm'  : "/DisplacedSUSY_stopToBottom_M_1500_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1500_1mm'   : "/DisplacedSUSY_stopToBottom_M_1500_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'stop1600_1000mm': "/DisplacedSUSY_stopToBottom_M_1600_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1600_100mm' : "/DisplacedSUSY_stopToBottom_M_1600_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1600_1mm'   : "/DisplacedSUSY_stopToBottom_M_1600_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'stop1700_100mm' : "/DisplacedSUSY_stopToBottom_M_1700_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1700_10mm'  : "/DisplacedSUSY_stopToBottom_M_1700_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stop1700_1mm'   : "/DisplacedSUSY_stopToBottom_M_1700_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    ############################################################################

    #DisplacedSUSY Signal (stop --> l+d) MC MiniAOD - 100k events/sample

}
