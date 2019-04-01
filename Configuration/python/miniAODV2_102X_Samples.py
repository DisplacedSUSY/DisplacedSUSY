#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD V2 DATASETS  ####################################################################
############################################################################################################

bg_mc_samples = {
    #DY
    'DYJetsToLL_50'     : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#100M

    'DYJetsToLL_10to50' : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',# 39M

    #DYBBJets
    'DYBBJetsToLL' : '/DYBBJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#5M

    #WJets
    'WJetsToLNu' : ['/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#29M
		    '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#25M
                    '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#5M
                    '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#19M
                    '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#8M
                    '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#6M
                    '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'],#3M

    #WW
    'WWToLNuLNu' : '/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#7.8M
    'WWToLNuQQ'  : '/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#19M

    #WZ
    'WZToLNu2QorQQ2L' : '/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#28M
    #['/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'],#19M DOESN'T EXIST YET
    'WZToLNuNuNu'     : '/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#1.7M
    'WZToLLLNu'       : ['/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM',#11M
                         '/WZTo3LNu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#2M

    #ZZ
    'ZZToNuNuQQ' : '/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#58M
    'ZZToLLQQ'   : '/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#28M
    'ZZToLLNuNu' : ['/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM',#400K
                     '/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#8M
    'ZZToLLLL'   : ['/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM',#800K
                    '/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#6M

    #VG
    'WG' : '/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#6M
    'ZG' : "",

    #SingleTop
    'SingleTop_s_channel'         : ['/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM',#19M
				     '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v4/MINIAODSIM'],#19M
    'SingleTop_t_channel_top'     : '/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#154M
    'SingleTop_t_channel_antitop' : '/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#79M
    'SingleTop_tbarW'             : ['/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM',#600K
                                     '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM',#5M
                                     '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#1M
    'SingleTop_tW'                : ['/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM',#600K
                                     '/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM',#7M
                                     '/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#1M

    #TTJets
    'TTJets_inclusive'          : '/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM',#72M
    'TTJets_SingleLeptFromT'    : '/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#62M
    'TTJets_DiLept'             : '/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#29M
    'TTJets_SingleLeptFromTbar' : '/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#59M

    #QCD MuEnriched
    'QCD_MuEnriched_15to20'    : '/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM',#5M
    'QCD_MuEnriched_20to30'    : '/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v4/MINIAODSIM',#30M
    'QCD_MuEnriched_30to50'    : '/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM',#29M
    'QCD_MuEnriched_50to80'    : '/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM',#20M
    'QCD_MuEnriched_80to120'   :['/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#600K
                                 '/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#25M
    'QCD_MuEnriched_120to170'  : ['/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#600K
                                  '/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#20M
    'QCD_MuEnriched_170to300'  : '/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM',#35M
    'QCD_MuEnriched_300to470'  : ['/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM',#400K
                                  '/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext3-v1/MINIAODSIM'],#28M
    'QCD_MuEnriched_470to600'  : ['/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#400K
                                  '/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#20M
    'QCD_MuEnriched_600to800'  : '/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',# 16M
    'QCD_MuEnriched_800to1000' : '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext3-v2/MINIAODSIM',#17M
    'QCD_MuEnriched_1000toInf' : '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',# 10M

    #QCD EMEnriched
    'QCD_EMEnriched_15to20'   : ['/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM',#10M
                                 '/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#14M
    'QCD_EMEnriched_20to30'   : '/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#14M
    'QCD_EMEnriched_30to50'   : ['/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM',#2M
                                 '/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM'],#15M
    'QCD_EMEnriched_50to80'   : ['/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#10M
                                 '/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM'],#10M
    'QCD_EMEnriched_80to120'  : ['/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#9M
                                 '/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM'],#9M
    'QCD_EMEnriched_120to170' : ['/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#9M
                                 '/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM'],#9M
    'QCD_EMEnriched_170to300' : ['/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#3M
                                '/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM'],#3M
    'QCD_EMEnriched_300toInf' : ['/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#2M
                                 '/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall18MiniAOD-102X_upgrade2018_realistic_v12-v1/MINIAODSIM'],#2M

    #QCD DoubleEMEnriched
    'QCD_DoubleEMEnriched_HighMass_30to40' : "",#'/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#15M DOESN'T EXIST YET
    'QCD_DoubleEMEnriched_LowMass_30toInf' : "",#'/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#42M DOESN'T EXIST YET
    'QCD_DoubleEMEnriched_HighMass_40toInf' : "",#'/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#21M DOESN'T EXIST YET

    #QCD bcToE
    'QCD_bcToE_15to20'   : "",#'/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#2M DOESN'T EXIST YET
    'QCD_bcToE_20to30'   : "",#'/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#10M DOESN'T EXIST YET
    'QCD_bcToE_30to80'   : "",#'/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#16M DOESN'T EXIST YET
    'QCD_bcToE_80to170'  : "",#'/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#16M DOESN'T EXIST YET
    'QCD_bcToE_170to250' : "",#'/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#10M DOESN'T EXIST YET
    'QCD_bcToE_250toInf' : "",#'/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM',#10M DOESN'T EXIST YET
}

data_samples = {
    # MuonEG 2018,17Sep2018 rereco
    'MuonEG_2018A' : '/MuonEG/Run2018A-17Sep2018-v1/MINIAOD',
    'MuonEG_2018B' : '/MuonEG/Run2018B-17Sep2018-v1/MINIAOD',
    'MuonEG_2018C' : '/MuonEG/Run2018C-17Sep2018-v1/MINIAOD',
    'MuonEG_2018D' : '/MuonEG/Run2018D-PromptReco-v2/MINIAOD',

    # DoubleMuon 2018,17Sep2018 rereco
    'DoubleMu_2018A' : '/DoubleMuon/Run2018A-17Sep2018-v2/MINIAOD',
    'DoubleMu_2018B' : '/DoubleMuon/Run2018B-17Sep2018-v1/MINIAOD',
    'DoubleMu_2018C' : '/DoubleMuon/Run2018C-17Sep2018-v1/MINIAOD',
    'DoubleMu_2018D' : '/DoubleMuon/Run2018D-PromptReco-v2/MINIAOD',

    # EGamma 2018,17Sep2018 rereco
    'EGamma_2018A' : '/EGamma/Run2018A-17Sep2018-v2/MINIAOD',
    'EGamma_2018B' : '/EGamma/Run2018B-17Sep2018-v1/MINIAOD',
    'EGamma_2018C' : '/EGamma/Run2018C-17Sep2018-v1/MINIAOD',
    'EGamma_2018D' : ['/EGamma/Run2018D-PromptReco-v1/MINIAOD',
                      '/EGamma/Run2018D-PromptReco-v2/MINIAOD'],

    # MET 2018,17Sep2018 rereco
    'MET_2018A' : '/MET/Run2018A-17Sep2018-v1/MINIAOD',
    'MET_2018B' : '/MET/Run2018B-17Sep2018-v1/MINIAOD',
    'MET_2018C' : '/MET/Run2018C-17Sep2018-v1/MINIAOD',
    'MET_2018D' : ['/MET/Run2018D-PromptReco-v1/MINIAOD',
                   '/MET/Run2018D-PromptReco-v2/MINIAOD'],

    # JetHT 2018,17Sep2018 rereco
    'JetHT_2018A' : '/JetHT/Run2018A-17Sep2018-v1/MINIAOD',
    'JetHT_2018B' : '/JetHT/Run2018B-17Sep2018-v1/MINIAOD',
    'JetHT_2018C' : '/JetHT/Run2018C-17Sep2018-v1/MINIAOD',
    'JetHT_2018D' : ['/JetHT/Run2018D-PromptReco-v1/MINIAOD',
                     '/JetHT/Run2018D-PromptReco-v2/MINIAOD'],

    # SingleMu 2018,17Sep2018 rereco
    'SingleMu_2018A' : '/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD',
    'SingleMu_2018B' : '/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD',
    'SingleMu_2018C' : '/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD',
    'SingleMu_2018D' : '/SingleMuon/Run2018D-PromptReco-v2/MINIAOD',

}

signal_mc_samples = {
    #DisplacedSUSY Signal (stop --> l+b) MC MiniAOD - 100k events/sample
    'stop200_1000mm' : "",#doesn't exist for 2018 MC yet
    'stop200_100mm'  : "",#doesn't exist for 2018 MC yet
    'stop200_10mm'   : "",#doesn't exist for 2018 MC yet
    'stop200_1mm'    : "",#doesn't exist for 2018 MC yet

    'stop300_1000mm' : "",#doesn't exist for 2018 MC yet
    'stop300_100mm'  : "",#doesn't exist for 2018 MC yet
    'stop300_10mm'   : "",#doesn't exist for 2018 MC yet
    'stop300_1mm'    : "",#doesn't exist for 2018 MC yet

    'stop400_1000mm' : "",#doesn't exist for 2018 MC yet
    'stop400_100mm'  : "",#doesn't exist for 2018 MC yet
    'stop400_10mm'   : "",#doesn't exist for 2018 MC yet
    'stop400_1mm'    : "",#doesn't exist for 2018 MC yet

    'stop500_1000mm' : "",#doesn't exist for 2018 MC yet
    'stop500_100mm'  : "",#doesn't exist for 2018 MC yet
    'stop500_10mm'   : "",#doesn't exist for 2018 MC yet
    'stop500_1mm'    : "",#doesn't exist for 2018 MC yet

    'stop600_1000mm' : "",#doesn't exist for 2018 MC yet
    'stop600_100mm'  : "",#doesn't exist for 2018 MC yet
    'stop600_10mm'   : "",#doesn't exist for 2018 MC yet
    'stop600_1mm'    : "",#doesn't exist for 2018 MC yet

    'stop700_1000mm' : "",#doesn't exist for 2018 MC yet
    'stop700_100mm'  : "",#doesn't exist for 2018 MC yet
    'stop700_10mm'   : "",#doesn't exist for 2018 MC yet
    'stop700_1mm'    : "",#doesn't exist for 2018 MC yet

    'stop800_1000mm' : "",#doesn't exist for 2018 MC yet
    'stop800_100mm'  : "",#doesn't exist for 2018 MC yet
    'stop800_10mm'   : "",#doesn't exist for 2018 MC yet
    'stop800_1mm'    : "",#doesn't exist for 2018 MC yet

    'stop900_1000mm' : "",#doesn't exist for 2018 MC yet
    'stop900_100mm'  : "",#doesn't exist for 2018 MC yet
    'stop900_10mm'   : "",#doesn't exist for 2018 MC yet
    'stop900_1mm'    : "",#doesn't exist for 2018 MC yet

    'stop1000_1000mm': "",#doesn't exist for 2018 MC yet
    'stop1000_100mm' : "",#doesn't exist for 2018 MC yet
    'stop1000_10mm'  : "",#doesn't exist for 2018 MC yet
    'stop1000_1mm'   : "",#doesn't exist for 2018 MC yet

    'stop1100_1000mm': "",#doesn't exist for 2018 MC yet
    'stop1100_100mm' : "",#doesn't exist for 2018 MC yet
    'stop1100_10mm'  : "",#doesn't exist for 2018 MC yet
    'stop1100_1mm'   : "",#doesn't exist for 2018 MC yet

    'stop1200_1000mm': "",#doesn't exist for 2018 MC yet
    'stop1200_100mm' : "",#doesn't exist for 2018 MC yet
    'stop1200_10mm'  : "",#doesn't exist for 2018 MC yet
    'stop1200_1mm'   : "",#doesn't exist for 2018 MC yet

    'stop1300_1000mm': "",#doesn't exist for 2018 MC yet
    'stop1300_100mm' : "",#doesn't exist for 2018 MC yet
    'stop1300_10mm'  : "",#doesn't exist for 2018 MC yet
    'stop1300_1mm'   : "",#doesn't exist for 2018 MC yet

    'stop1400_1000mm': "",#doesn't exist for 2018 MC yet
    'stop1400_100mm' : "",#doesn't exist for 2018 MC yet
    'stop1400_10mm'  : "",#doesn't exist for 2018 MC yet
    'stop1400_1mm'   : "",#doesn't exist for 2018 MC yet

    'stop1500_1000mm': "",#doesn't exist for 2018 MC yet
    'stop1500_100mm' : "",#doesn't exist for 2018 MC yet
    'stop1500_10mm'  : "",#doesn't exist for 2018 MC yet
    'stop1500_1mm'   : "",#doesn't exist for 2018 MC yet

    'stop1600_1000mm': "",#doesn't exist for 2018 MC yet
    'stop1600_100mm' : "",#doesn't exist for 2018 MC yet
    'stop1600_10mm'  : "",#doesn't exist for 2018 MC yet
    'stop1600_1mm'   : "",#doesn't exist for 2018 MC yet

    'stop1700_1000mm': "",#doesn't exist for 2018 MC yet
    'stop1700_100mm' : "",#doesn't exist for 2018 MC yet
    'stop1700_10mm'  : "",#doesn't exist for 2018 MC yet
    'stop1700_1mm'   : "",#doesn't exist for 2018 MC yet

    'stop1800_1000mm': "",#doesn't exist for 2018 MC yet
    'stop1800_100mm' : "",#doesn't exist for 2018 MC yet
    'stop1800_10mm'  : "",#doesn't exist for 2018 MC yet
    'stop1800_1mm'   : "",#doesn't exist for 2018 MC yet



    'stopToLD200_1000mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD200_100mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD200_10mm'    : "",#doesn't exist for 2018 MC yet
    'stopToLD200_1mm'     : "",#doesn't exist for 2018 MC yet

    'stopToLD300_1000mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD300_100mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD300_10mm'    : "",#doesn't exist for 2018 MC yet
    'stopToLD300_1mm'     : "",#doesn't exist for 2018 MC yet

    'stopToLD400_1000mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD400_100mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD400_10mm'    : "",#doesn't exist for 2018 MC yet
    'stopToLD400_1mm'     : "",#doesn't exist for 2018 MC yet

    'stopToLD500_1000mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD500_100mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD500_10mm'    : "",#doesn't exist for 2018 MC yet
    'stopToLD500_1mm'     : "",#doesn't exist for 2018 MC yet

    'stopToLD600_1000mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD600_100mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD600_10mm'    : "",#doesn't exist for 2018 MC yet
    'stopToLD600_1mm'     : "",#doesn't exist for 2018 MC yet

    'stopToLD700_1000mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD700_100mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD700_10mm'    : "",#doesn't exist for 2018 MC yet
    'stopToLD700_1mm'     : "",#doesn't exist for 2018 MC yet

    'stopToLD800_1000mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD800_100mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD800_10mm'    : "",#doesn't exist for 2018 MC yet
    'stopToLD800_1mm'     : "",#doesn't exist for 2018 MC yet

    'stopToLD900_1000mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD900_100mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD900_10mm'    : "",#doesn't exist for 2018 MC yet
    'stopToLD900_1mm'     : "",#doesn't exist for 2018 MC yet

    'stopToLD1000_1000mm' : "",#doesn't exist for 2018 MC yet
    'stopToLD1000_100mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD1000_10mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD1000_1mm'    : "",#doesn't exist for 2018 MC yet

    'stopToLD1100_1000mm' : "",#doesn't exist for 2018 MC yet
    'stopToLD1100_100mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD1100_10mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD1100_1mm'    : "",#doesn't exist for 2018 MC yet

    'stopToLD1200_1000mm' : "",#doesn't exist for 2018 MC yet
    'stopToLD1200_100mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD1200_10mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD1200_1mm'    : "",#doesn't exist for 2018 MC yet

    'stopToLD1300_1000mm' : "",#doesn't exist for 2018 MC yet
    'stopToLD1300_100mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD1300_10mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD1300_1mm'    : "",#doesn't exist for 2018 MC yet

    'stopToLD1400_1000mm' : "",#doesn't exist for 2018 MC yet
    'stopToLD1400_100mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD1400_10mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD1400_1mm'    : "",#doesn't exist for 2018 MC yet

    'stopToLD1500_1000mm' : "",#doesn't exist for 2018 MC yet
    'stopToLD1500_100mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD1500_10mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD1500_1mm'    : "",#doesn't exist for 2018 MC yet

    'stopToLD1600_1000mm' : "",#doesn't exist for 2018 MC yet
    'stopToLD1600_100mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD1600_10mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD1600_1mm'    : "",#doesn't exist for 2018 MC yet

    'stopToLD1700_1000mm' : "",#doesn't exist for 2018 MC yet
    'stopToLD1700_100mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD1700_10mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD1700_1mm'    : "",#doesn't exist for 2018 MC yet

    'stopToLD1800_1000mm' : "",#doesn't exist for 2018 MC yet
    'stopToLD1800_100mm'  : "",#doesn't exist for 2018 MC yet
    'stopToLD1800_10mm'   : "",#doesn't exist for 2018 MC yet
    'stopToLD1800_1mm'    : "",#doesn't exist for 2018 MC yet

}

# create composite dictionary of all samples
dataset_names = {}
dataset_names.update(bg_mc_samples)
dataset_names.update(data_samples)
dataset_names.update(signal_mc_samples)

# Propagate displaced SUSY sample names to the lifetime-reweighted samples
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import renameReweightedSamples
renameReweightedSamples(dataset_names)
