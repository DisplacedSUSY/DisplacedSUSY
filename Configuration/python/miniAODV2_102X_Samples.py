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

    'DYJetsToTauTauLeptonic' : '/DYJetsToTauTau_ForcedMuEleDecay_M-50_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM',#48M

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

parkedData_samples = {
    #'ParkingBPH5_Run2018D' : '/ParkingBPH5/Run2018D-20Mar2019-v1/MINIAOD',
    'ParkingBPH4_Run2018A' : '/ParkingBPH4/Run2018A-14May2018-v1/MINIAOD',
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
    'EGamma_2018D' : ['/EGamma/Run2018D-22Jan2019-v1/MINIAOD',
                      '/EGamma/Run2018D-22Jan2019-v2/MINIAOD'],

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

    'NoBPTX_2018A' : '/NoBPTX/Run2018A-17Sep2018-v1/MINIAOD',
    'NoBPTX_2018B' : '/NoBPTX/Run2018B-17Sep2018-v1/MINIAOD',
    'NoBPTX_2018C' : '/NoBPTX/Run2018C-17Sep2018-v1/MINIAOD',
    'NoBPTX_2018D' : '/NoBPTX/Run2018D-PromptReco-v2/MINIAOD',
}

signal_mc_samples = {
    #DisplacedSUSY Signal (stop --> l+b) MC MiniAOD - 100k events/sample
    'stopToLB100_1000mm' : "/StopToLB_M_100_1000mm_13TeV_2018MC/bcardwel-MiniAod-3ee3afd6b5a1410aea6d0b4d52723d06/USER",
    'stopToLB100_100mm'  : "/StopToLB_M_100_100mm_13TeV_2018MC/bcardwel-MiniAod-3ee3afd6b5a1410aea6d0b4d52723d06/USER",
    'stopToLB100_10mm'   : "/StopToLB_M_100_10mm_13TeV_2018MC/bcardwel-MiniAod-3ee3afd6b5a1410aea6d0b4d52723d06/USER",
    'stopToLB100_1mm'    : "/StopToLB_M_100_1mm_13TeV_2018MC/bcardwel-MiniAod-3ee3afd6b5a1410aea6d0b4d52723d06/USER",
    'stopToLB100_0p1mm'  : "/StopToLBottom_M_100_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB150_1000mm' : "/StopToLBottom_M_150_1000mm_13TeV_2018MC/manunezo-MiniAod-3ee3afd6b5a1410aea6d0b4d52723d06/USER",
    'stopToLB150_1mm'    : "/StopToLBottom_M_150_1mm_13TeV_2018MC/manunezo-MiniAod-3ee3afd6b5a1410aea6d0b4d52723d06/USER",

    'stopToLB175_1000mm' : "/StopToLBottom_M_175_1000mm_13TeV_2018MC/manunezo-MiniAod-3ee3afd6b5a1410aea6d0b4d52723d06/USER",
    'stopToLB175_1mm'    : "/StopToLBottom_M_175_1mm_13TeV_2018MC/manunezo-MiniAod-3ee3afd6b5a1410aea6d0b4d52723d06/USER",

    'stopToLB200_1000mm' : "/DisplacedSUSY_stopToBottom_M_200_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB200_100mm'  : "/DisplacedSUSY_stopToBottom_M_200_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB200_10mm'   : "/DisplacedSUSY_stopToBottom_M_200_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB200_1mm'    : "/DisplacedSUSY_stopToBottom_M_200_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB200_0p1mm'  : "/StopToLBottom_M_200_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB300_1000mm' : "/DisplacedSUSY_stopToBottom_M_300_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB300_100mm'  : "/DisplacedSUSY_stopToBottom_M_300_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB300_10mm'   : "/DisplacedSUSY_stopToBottom_M_300_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB300_1mm'    : "/DisplacedSUSY_stopToBottom_M_300_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB300_0p1mm'  : "/StopToLBottom_M_300_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB400_1000mm' : "/DisplacedSUSY_stopToBottom_M_400_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB400_100mm'  : "/DisplacedSUSY_stopToBottom_M_400_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB400_10mm'   : "/DisplacedSUSY_stopToBottom_M_400_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB400_1mm'    : "/DisplacedSUSY_stopToBottom_M_400_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB400_0p1mm'  : "/StopToLBottom_M_400_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB500_1000mm' : "/DisplacedSUSY_stopToBottom_M_500_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB500_100mm'  : "/DisplacedSUSY_stopToBottom_M_500_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM ",
    'stopToLB500_10mm'   : "/DisplacedSUSY_stopToBottom_M_500_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB500_1mm'    : "/DisplacedSUSY_stopToBottom_M_500_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB500_0p1mm'  : "/StopToLBottom_M_500_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB600_1000mm' : "/DisplacedSUSY_stopToBottom_M_600_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB600_100mm'  : "/DisplacedSUSY_stopToBottom_M_600_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB600_10mm'   : "/DisplacedSUSY_stopToBottom_M_600_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB600_1mm'    : "/DisplacedSUSY_stopToBottom_M_600_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB600_0p1mm'  : "/StopToLBottom_M_600_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB700_1000mm' : "/DisplacedSUSY_stopToBottom_M_700_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB700_100mm'  : "/DisplacedSUSY_stopToBottom_M_700_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB700_10mm'   : "/DisplacedSUSY_stopToBottom_M_700_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB700_1mm'    : "/DisplacedSUSY_stopToBottom_M_700_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB700_0p1mm'  : "/StopToLBottom_M_700_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB800_1000mm' : "/DisplacedSUSY_stopToBottom_M_800_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB800_100mm'  : "/DisplacedSUSY_stopToBottom_M_800_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB800_10mm'   : "/DisplacedSUSY_stopToBottom_M_800_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB800_1mm'    : "/DisplacedSUSY_stopToBottom_M_800_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB800_0p1mm'  : "/StopToLBottom_M_800_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB900_1000mm' : "/DisplacedSUSY_stopToBottom_M_900_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB900_100mm'  : "/DisplacedSUSY_stopToBottom_M_900_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB900_10mm'   : "/DisplacedSUSY_stopToBottom_M_900_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB900_1mm'    : "/DisplacedSUSY_stopToBottom_M_900_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB900_0p1mm'  : "/StopToLBottom_M_900_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB1000_1000mm': "/DisplacedSUSY_stopToBottom_M_1000_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1000_100mm' : "/DisplacedSUSY_stopToBottom_M_1000_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1000_10mm'  : "/DisplacedSUSY_stopToBottom_M_1000_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1000_1mm'   : "/DisplacedSUSY_stopToBottom_M_1000_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1000_0p1mm' : "/StopToLBottom_M_1000_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",
    'stopToLB1000_0p01mm': "/StopToLBottom_M_1000_0p01mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB1100_1000mm': "/DisplacedSUSY_stopToBottom_M_1100_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1100_100mm' : "/DisplacedSUSY_stopToBottom_M_1100_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1100_10mm'  : "/DisplacedSUSY_stopToBottom_M_1100_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1100_1mm'   : "/DisplacedSUSY_stopToBottom_M_1100_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1100_0p1mm' : "/StopToLBottom_M_1100_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB1200_1000mm': "/DisplacedSUSY_stopToBottom_M_1200_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1200_100mm' : "/DisplacedSUSY_stopToBottom_M_1200_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1200_10mm'  : "/DisplacedSUSY_stopToBottom_M_1200_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1200_1mm'   : "/DisplacedSUSY_stopToBottom_M_1200_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1200_0p1mm' : "/StopToLBottom_M_1200_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB1300_1000mm': "/DisplacedSUSY_stopToBottom_M_1300_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1300_100mm' : "/DisplacedSUSY_stopToBottom_M_1300_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1300_10mm'  : "/DisplacedSUSY_stopToBottom_M_1300_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1300_1mm'   : "/DisplacedSUSY_stopToBottom_M_1300_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1300_0p1mm' : "/StopToLBottom_M_1300_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB1400_1000mm': "/DisplacedSUSY_stopToBottom_M_1400_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",
    'stopToLB1400_100mm' : "/DisplacedSUSY_stopToBottom_M_1400_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1400_10mm'  : "/DisplacedSUSY_stopToBottom_M_1400_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1400_1mm'   : "/DisplacedSUSY_stopToBottom_M_1400_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1400_0p1mm' : "/StopToLBottom_M_1400_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB1500_1000mm': "/DisplacedSUSY_stopToBottom_M_1500_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1500_100mm' : "/DisplacedSUSY_stopToBottom_M_1500_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1500_10mm'  : "/DisplacedSUSY_stopToBottom_M_1500_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1500_1mm'   : "/DisplacedSUSY_stopToBottom_M_1500_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1500_0p1mm' : "/StopToLBottom_M_1500_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB1600_1000mm': "/DisplacedSUSY_stopToBottom_M_1600_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1600_100mm' : "/DisplacedSUSY_stopToBottom_M_1600_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1600_10mm'  : "/DisplacedSUSY_stopToBottom_M_1600_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1600_1mm'   : "/DisplacedSUSY_stopToBottom_M_1600_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1600_0p1mm' : "/StopToLBottom_M_1600_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB1700_1000mm': "/DisplacedSUSY_stopToBottom_M_1700_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1700_100mm' : "/DisplacedSUSY_stopToBottom_M_1700_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1700_10mm'  : "/DisplacedSUSY_stopToBottom_M_1700_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1700_1mm'   : "/DisplacedSUSY_stopToBottom_M_1700_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1700_0p1mm' : "/StopToLBottom_M_1700_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLB1800_1000mm': "/DisplacedSUSY_stopToBottom_M_1800_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1800_100mm' : "/DisplacedSUSY_stopToBottom_M_1800_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1800_10mm'  : "/DisplacedSUSY_stopToBottom_M_1800_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1800_1mm'   : "/DisplacedSUSY_stopToBottom_M_1800_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLB1800_0p1mm' : "/StopToLBottom_M_1800_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD100_1000mm' : "/StopToLD_M_100_1000mm_13TeV_2018MC/bcardwel-MiniAod-3ee3afd6b5a1410aea6d0b4d52723d06/USER",
    'stopToLD100_100mm'  : "/StopToLD_M_100_100mm_13TeV_2018MC/bcardwel-MiniAod-3ee3afd6b5a1410aea6d0b4d52723d06/USER",
    'stopToLD100_10mm'   : "/StopToLD_M_100_10mm_13TeV_2018MC/bcardwel-MiniAod-3ee3afd6b5a1410aea6d0b4d52723d06/USER",
    'stopToLD100_1mm'    : "/StopToLD_M_100_1mm_13TeV_2018MC/bcardwel-MiniAod-3ee3afd6b5a1410aea6d0b4d52723d06/USER",
    'stopToLD100_0p1mm'  : "/StopToLD_M_100_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD200_1000mm'  : "/DisplacedSUSY_stopToLD_M_200_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD200_100mm'   : "/DisplacedSUSY_stopToLD_M_200_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD200_10mm'    : "/DisplacedSUSY_stopToLD_M_200_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD200_1mm'     : "/DisplacedSUSY_stopToLD_M_200_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD200_0p1mm'   : "/StopToLD_M_200_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD300_1000mm'  : "/DisplacedSUSY_stopToLD_M_300_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD300_100mm'   : "/DisplacedSUSY_stopToLD_M_300_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD300_10mm'    : "/DisplacedSUSY_stopToLD_M_300_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD300_1mm'     : "/DisplacedSUSY_stopToLD_M_300_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD300_0p1mm'   : "/StopToLD_M_300_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD400_1000mm'  : "/DisplacedSUSY_stopToLD_M_400_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD400_100mm'   : "/DisplacedSUSY_stopToLD_M_400_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD400_10mm'    : "/DisplacedSUSY_stopToLD_M_400_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD400_1mm'     : "/DisplacedSUSY_stopToLD_M_400_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD400_0p1mm'   : "/StopToLD_M_400_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD500_1000mm'  : "/DisplacedSUSY_stopToLD_M_500_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD500_100mm'   : "/DisplacedSUSY_stopToLD_M_500_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD500_10mm'    : "/DisplacedSUSY_stopToLD_M_500_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD500_1mm'     : "/DisplacedSUSY_stopToLD_M_500_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD500_0p1mm'   : "/StopToLD_M_500_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD600_1000mm'  : "/DisplacedSUSY_stopToLD_M_600_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD600_100mm'   : "/DisplacedSUSY_stopToLD_M_600_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD600_10mm'    : "/DisplacedSUSY_stopToLD_M_600_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD600_1mm'     : "/DisplacedSUSY_stopToLD_M_600_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD600_0p1mm'   : "/StopToLD_M_600_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD700_1000mm'  : "/DisplacedSUSY_stopToLD_M_700_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD700_100mm'   : "/DisplacedSUSY_stopToLD_M_700_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD700_10mm'    : "/DisplacedSUSY_stopToLD_M_700_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD700_1mm'     : "/DisplacedSUSY_stopToLD_M_700_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD700_0p1mm'   : "/StopToLD_M_700_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD800_1000mm'  : "/DisplacedSUSY_stopToLD_M_800_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD800_100mm'   : "/DisplacedSUSY_stopToLD_M_800_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD800_10mm'    : "/DisplacedSUSY_stopToLD_M_800_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD800_1mm'     : "/DisplacedSUSY_stopToLD_M_800_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD800_0p1mm'   : "/StopToLD_M_800_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD900_1000mm'  : "/DisplacedSUSY_stopToLD_M_900_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD900_100mm'   : "/DisplacedSUSY_stopToLD_M_900_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD900_10mm'    : "/DisplacedSUSY_stopToLD_M_900_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD900_1mm'     : "/DisplacedSUSY_stopToLD_M_900_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD900_0p1mm'   : "/StopToLD_M_900_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD1000_1000mm' : "/DisplacedSUSY_stopToLD_M_1000_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1000_100mm'  : "/DisplacedSUSY_stopToLD_M_1000_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1000_10mm'   : "/DisplacedSUSY_stopToLD_M_1000_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1000_1mm'    : "/DisplacedSUSY_stopToLD_M_1000_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1000_0p1mm'  : "/StopToLD_M_1000_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD1100_1000mm' : "/DisplacedSUSY_stopToLD_M_1100_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1100_100mm'  : "/DisplacedSUSY_stopToLD_M_1100_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1100_10mm'   : "/DisplacedSUSY_stopToLD_M_1100_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1100_1mm'    : "/DisplacedSUSY_stopToLD_M_1100_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1100_0p1mm'  : "/StopToLD_M_1100_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD1200_1000mm' : "/DisplacedSUSY_stopToLD_M_1200_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1200_100mm'  : "/DisplacedSUSY_stopToLD_M_1200_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1200_10mm'   : "/DisplacedSUSY_stopToLD_M_1200_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1200_1mm'    : "/DisplacedSUSY_stopToLD_M_1200_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1200_0p1mm'  : "/StopToLD_M_1200_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD1300_1000mm' : "/DisplacedSUSY_stopToLD_M_1300_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1300_100mm'  : "/DisplacedSUSY_stopToLD_M_1300_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1300_10mm'   : "/DisplacedSUSY_stopToLD_M_1300_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1300_1mm'    : "/DisplacedSUSY_stopToLD_M_1300_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1300_0p1mm'  : "/StopToLD_M_1300_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD1400_1000mm' : "/DisplacedSUSY_stopToLD_M_1400_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1400_100mm'  : "/DisplacedSUSY_stopToLD_M_1400_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1400_10mm'   : "/DisplacedSUSY_stopToLD_M_1400_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1400_1mm'    : "/DisplacedSUSY_stopToLD_M_1400_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",
    'stopToLD1400_0p1mm'  : "/StopToLD_M_1400_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD1500_1000mm' : "/DisplacedSUSY_stopToLD_M_1500_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1500_100mm'  : "/DisplacedSUSY_stopToLD_M_1500_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1500_10mm'   : "/DisplacedSUSY_stopToLD_M_1500_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1500_1mm'    : "/DisplacedSUSY_stopToLD_M_1500_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1500_0p1mm'  : "/StopToLD_M_1500_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD1600_1000mm' : "/DisplacedSUSY_stopToLD_M_1600_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1600_100mm'  : "/DisplacedSUSY_stopToLD_M_1600_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1600_10mm'   : "/DisplacedSUSY_stopToLD_M_1600_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1600_1mm'    : "/DisplacedSUSY_stopToLD_M_1600_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1600_0p1mm'  : "/StopToLD_M_1600_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD1700_1000mm' : "/DisplacedSUSY_stopToLD_M_1700_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1700_100mm'  : "/DisplacedSUSY_stopToLD_M_1700_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1700_10mm'   : "/DisplacedSUSY_stopToLD_M_1700_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1700_1mm'    : "/DisplacedSUSY_stopToLD_M_1700_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1700_0p1mm'  : "/StopToLD_M_1700_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'stopToLD1800_1000mm' : "/DisplacedSUSY_stopToLD_M_1800_1000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1800_100mm'  : "/DisplacedSUSY_stopToLD_M_1800_100mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1800_10mm'   : "/DisplacedSUSY_stopToLD_M_1800_10mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1800_1mm'    : "/DisplacedSUSY_stopToLD_M_1800_1mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",
    'stopToLD1800_0p1mm'  : "/StopToLD_M_1800_0p1mm_13TeV_2018MC/jalimena-MiniAod-c21dec93027231dc6f615dfe5c662834/USER",

    'HTo4Mu125_50_50mm'   : "/HTo2LongLivedTo4mu_MH-125_MFF-50_CTau-50mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM",
    'HTo4Mu125_50_500mm'  : "/HTo2LongLivedTo4mu_MH-125_MFF-50_CTau-500mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",
    'HTo4Mu125_50_5000mm' : "/HTo2LongLivedTo4mu_MH-125_MFF-50_CTau-5000mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",

    'HTo4Mu125_20_13mm'   : "/HTo2LongLivedTo4mu_MH-125_MFF-20_CTau-13mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",
    'HTo4Mu125_20_130mm'  : "/HTo2LongLivedTo4mu_MH-125_MFF-20_CTau-130mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM",
    'HTo4Mu125_20_1300mm' : "/HTo2LongLivedTo4mu_MH-125_MFF-20_CTau-1300mm_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",
}

# create composite dictionary of all samples
dataset_names = {}
dataset_names.update(bg_mc_samples)
dataset_names.update(data_samples)
dataset_names.update(signal_mc_samples)
dataset_names.update(parkedData_samples)

# Propagate displaced SUSY sample names to the lifetime-reweighted samples
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import renameReweightedSamples
renameReweightedSamples(dataset_names)
