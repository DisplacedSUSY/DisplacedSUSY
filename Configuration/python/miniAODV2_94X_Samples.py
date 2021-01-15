#!/Usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD V2 DATASETS  ####################################################################
############################################################################################################

bg_mc_samples = {
    #DY
    'DYJetsToLL_50'     : ['/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#49M
                           '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'],#49M

    'DYJetsToLL_10to50' : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM',# 39M

    #DYBBJets
    'DYBBJetsToLL' : ['/DYBBJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',# 3M
                      '/DYBBJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'],#2M

    'DYJetsToTauTauLeptonic' : ['/DYJetsToTauTau_ForcedMuEleDecay_M-50_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM',#47M
                                '/DYJetsToTauTau_ForcedMuEleDecay_M-50_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#48M
                                '/DYJetsToTauTau_ForcedMuDecay_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'],#1M

    #WJets
    'WJetsToLNu' : ['/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',#36M
                    '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#21M
                    '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#14M
                    '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#22M
                    '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#20M
                    '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#20M
                    '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM'],#21M

    #WW
    'WWToLNuLNu' : ['/WWTo2L2Nu_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM',#2M
                    '/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'],#2M
    'WWToLNuQQ'  : ['/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#9M
                    '/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM',#10M
                    '/WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'],#9M

    #WZ
    'WZToLNu2QorQQ2L' : ['/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',#19M
                         '/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'],#28M
    'WZToLNuNuNu'     : '/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#5M
    'WZToLLLNu'       : ['/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#11M
                         '/WZTo3LNu_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'],#1M

    #ZZ
    'ZZToNuNuQQ' : '/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#62M
    'ZZToLLQQ'   : '/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#28M
    'ZZToLLNuNu' : '/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#9M
    'ZZToLLLL'   : ['/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#7M
                    '/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'],#98M

    #VG
    'WG' : '/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#6M
    'ZG' : '',#doesn't exist for 2017 MC yet

    #SingleTop
    'SingleTop_s_channel'         : ['/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#9M
                                     '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'],#10M
    'SingleTop_t_channel_top'     : '/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',#6M
    'SingleTop_t_channel_antitop' : '/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#4M
    'SingleTop_tbarW'             : ['/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',#6M
                                     '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#5M
                                     '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',#6M
                                     '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'],#6M

    'SingleTop_tW'                : ['/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#5M
                                     '/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'],#5M

    #TTJets
    'TTJets_inclusive'          : '/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#153M
    'TTJets_SingleLeptFromT'    : '/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#62M
    'TTJets_DiLept'             : '/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#28M
    'TTJets_SingleLeptFromTbar' : '/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',#57M

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
}

data_samples = {
    # MuonEG 2017,31Mar2018 rereco
    'MuonEG_2017B' : '/MuonEG/Run2017B-31Mar2018-v1/MINIAOD',
    'MuonEG_2017C' : '/MuonEG/Run2017C-31Mar2018-v1/MINIAOD',
    'MuonEG_2017D' : '/MuonEG/Run2017D-31Mar2018-v1/MINIAOD',
    'MuonEG_2017E' : '/MuonEG/Run2017E-31Mar2018-v1/MINIAOD',
    'MuonEG_2017F' : '/MuonEG/Run2017F-31Mar2018-v1/MINIAOD',

    # DoubleMuon 2017,31Mar2018 rereco
    'DoubleMu_2017B' : '/DoubleMuon/Run2017B-31Mar2018-v1/MINIAOD',
    'DoubleMu_2017C' : '/DoubleMuon/Run2017C-31Mar2018-v1/MINIAOD',
    'DoubleMu_2017D' : '/DoubleMuon/Run2017D-31Mar2018-v1/MINIAOD',
    'DoubleMu_2017E' : '/DoubleMuon/Run2017E-31Mar2018-v1/MINIAOD',
    'DoubleMu_2017F' : '/DoubleMuon/Run2017F-31Mar2018-v1/MINIAOD',

    # DoubleEG 2017,31Mar2018 rereco
    'DoubleEG_2017B' : '/DoubleEG/Run2017B-31Mar2018-v1/MINIAOD',
    'DoubleEG_2017C' : '/DoubleEG/Run2017C-31Mar2018-v1/MINIAOD',
    'DoubleEG_2017D' : '/DoubleEG/Run2017D-31Mar2018-v1/MINIAOD',
    'DoubleEG_2017E' : '/DoubleEG/Run2017E-31Mar2018-v1/MINIAOD',
    'DoubleEG_2017F' : '/DoubleEG/Run2017F-31Mar2018-v1/MINIAOD',

    # MET 2017,31Mar2018 rereco
    'MET_2017B' : '/MET/Run2017B-31Mar2018-v1/MINIAOD',
    'MET_2017C' : '/MET/Run2017C-31Mar2018-v1/MINIAOD',
    'MET_2017D' : '/MET/Run2017D-31Mar2018-v1/MINIAOD',
    'MET_2017E' : '/MET/Run2017E-31Mar2018-v1/MINIAOD',
    'MET_2017F' : '/MET/Run2017F-31Mar2018-v1/MINIAOD',

    # JetHT 2017,31Mar2018 rereco
    'JetHT_2017B' : '/JetHT/Run2017B-31Mar2018-v1/MINIAOD',
    'JetHT_2017C' : '/JetHT/Run2017C-31Mar2018-v1/MINIAOD',
    'JetHT_2017D' : '/JetHT/Run2017D-31Mar2018-v1/MINIAOD',
    'JetHT_2017E' : '/JetHT/Run2017E-31Mar2018-v1/MINIAOD',
    'JetHT_2017F' : '/JetHT/Run2017F-31Mar2018-v1/MINIAOD',

    # SingleEle 2017,31Mar2018 rereco
    'SingleEle_2017B' : '/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD',
    'SingleEle_2017C' : '/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD',
    'SingleEle_2017D' : '/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD',
    'SingleEle_2017E' : '/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD',
    'SingleEle_2017F' : '/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD',

    # SingleMu 2017,31Mar2018 rereco
    'SingleMu_2017B' : '/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD',
    'SingleMu_2017C' : '/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD',
    'SingleMu_2017D' : '/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD',
    'SingleMu_2017E' : '/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD',
    'SingleMu_2017F' : '/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD',

    'NoBPTX_2017B' : '/NoBPTX/Run2017B-31Mar2018-v1/MINIAOD',
    'NoBPTX_2017C' : '/NoBPTX/Run2017C-31Mar2018-v1/MINIAOD',
    'NoBPTX_2017D' : '/NoBPTX/Run2017D-31Mar2018-v1/MINIAOD',
    'NoBPTX_2017E' : '/NoBPTX/Run2017E-31Mar2018-v1/MINIAOD',
    'NoBPTX_2017F' : '/NoBPTX/Run2017F-31Mar2018-v1/MINIAOD',
}

signal_mc_samples = {
    #DisplacedSUSY Signal (stop --> l+b) MC MiniAOD - 100k events/sample
    'stopToLB100_1000mm' : "/StopToLB_M_100_1000mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLB100_100mm'  : "/StopToLB_M_100_100mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLB100_10mm'   : "/StopToLB_M_100_10mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLB100_1mm'    : "/StopToLB_M_100_1mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLB100_0p1mm'  : "/StopToLB_M_100_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB200_1000mm' : "/StopToLB_M_200_1000mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLB200_100mm'  : "/StopToLB_M_200_100mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLB200_10mm'   : "/StopToLB_M_200_10mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLB200_1mm'    : "/StopToLB_M_200_1mm_13TeV_2017MC/jalimena-MiniAOD-18783c0a07109245951450a1a4f55409/USER",
    'stopToLB200_0p1mm'  : "/StopToLB_M_200_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB300_1000mm' : "/StopToLB_M_300_1000mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLB300_100mm'  : "/StopToLB_M_300_100mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLB300_10mm'   : "/StopToLB_M_300_10mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLB300_1mm'    : "/StopToLB_M_300_1mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLB300_0p1mm'  : "/StopToLB_M_300_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB400_1000mm' : "/DisplacedSUSY_stopToBottom_M_400_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB400_100mm'  : "/DisplacedSUSY_stopToBottom_M_400_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB400_10mm'   : "/DisplacedSUSY_stopToBottom_M_400_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB400_1mm'    : "/DisplacedSUSY_stopToBottom_M_400_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB400_1mm_private' : "/StopToLB_M_400_1mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLB400_0p1mm'  : "/StopToLB_M_400_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB500_1000mm' : "/DisplacedSUSY_stopToBottom_M_500_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLB500_100mm'  : "/DisplacedSUSY_stopToBottom_M_500_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB500_10mm'   : "/DisplacedSUSY_stopToBottom_M_500_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB500_1mm'    : "/DisplacedSUSY_stopToBottom_M_500_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB500_0p1mm'  : "/StopToLB_M_500_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB600_1000mm' : "/DisplacedSUSY_stopToBottom_M_600_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB600_100mm'  : "/DisplacedSUSY_stopToBottom_M_600_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB600_10mm'   : "/DisplacedSUSY_stopToBottom_M_600_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB600_1mm'    : "/DisplacedSUSY_stopToBottom_M_600_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB600_0p1mm'  : "/StopToLB_M_600_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB700_1000mm' : "/DisplacedSUSY_stopToBottom_M_700_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLB700_100mm'  : "/DisplacedSUSY_stopToBottom_M_700_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB700_10mm'   : "/DisplacedSUSY_stopToBottom_M_700_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLB700_1mm'    : "/DisplacedSUSY_stopToBottom_M_700_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB700_0p1mm'  : "/StopToLB_M_700_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB800_1000mm' : "/DisplacedSUSY_stopToBottom_M_800_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB800_100mm'  : "/DisplacedSUSY_stopToBottom_M_800_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB800_10mm'   : "/DisplacedSUSY_stopToBottom_M_800_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB800_1mm'    : "/DisplacedSUSY_stopToBottom_M_800_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLB800_0p1mm'  : "/StopToLB_M_800_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB900_1000mm' : "/DisplacedSUSY_stopToBottom_M_900_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLB900_100mm'  : "/DisplacedSUSY_stopToBottom_M_900_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB900_10mm'   : "/DisplacedSUSY_stopToBottom_M_900_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLB900_1mm'    : "/DisplacedSUSY_stopToBottom_M_900_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLB900_0p1mm'  : "/StopToLB_M_900_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB1000_1000mm': "/DisplacedSUSY_stopToBottom_M_1000_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1000_100mm' : "/DisplacedSUSY_stopToBottom_M_1000_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1000_10mm'  : "/DisplacedSUSY_stopToBottom_M_1000_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1000_1mm'   : "/DisplacedSUSY_stopToBottom_M_1000_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1000_0p1mm' : "/StopToLB_M_1000_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB1100_1000mm': "/DisplacedSUSY_stopToBottom_M_1100_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1100_100mm' : "/DisplacedSUSY_stopToBottom_M_1100_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1100_10mm'  : "/DisplacedSUSY_stopToBottom_M_1100_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1100_1mm'   : "/DisplacedSUSY_stopToBottom_M_1100_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1100_0p1mm' : "/StopToLB_M_1100_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB1200_1000mm': "/DisplacedSUSY_stopToBottom_M_1200_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1200_100mm' : "/DisplacedSUSY_stopToBottom_M_1200_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLB1200_10mm'  : "/DisplacedSUSY_stopToBottom_M_1200_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1200_1mm'   : "/DisplacedSUSY_stopToBottom_M_1200_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1200_0p1mm' : "/StopToLB_M_1200_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB1300_1000mm': "/DisplacedSUSY_stopToBottom_M_1300_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1300_100mm' : "/DisplacedSUSY_stopToBottom_M_1300_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLB1300_10mm'  : "/DisplacedSUSY_stopToBottom_M_1300_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1300_1mm'   : "/DisplacedSUSY_stopToBottom_M_1300_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1300_0p1mm' : "/StopToLB_M_1300_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB1400_1000mm': "/DisplacedSUSY_stopToBottom_M_1400_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1400_100mm' : "/DisplacedSUSY_stopToBottom_M_1400_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1400_10mm'  : "/DisplacedSUSY_stopToBottom_M_1400_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1400_1mm'   : "/DisplacedSUSY_stopToBottom_M_1400_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1400_0p1mm' : "/StopToLB_M_1400_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB1500_1000mm': "/DisplacedSUSY_stopToBottom_M_1500_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1500_100mm' : "/DisplacedSUSY_stopToBottom_M_1500_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1500_10mm'  : "/DisplacedSUSY_stopToBottom_M_1500_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1500_1mm'   : "/DisplacedSUSY_stopToBottom_M_1500_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1500_0p1mm' : "/StopToLB_M_1500_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB1600_1000mm': "/DisplacedSUSY_stopToBottom_M_1600_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1600_100mm' : "/DisplacedSUSY_stopToBottom_M_1600_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1600_10mm'  : "/DisplacedSUSY_stopToBottom_M_1600_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1600_1mm'   : "/DisplacedSUSY_stopToBottom_M_1600_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLB1600_0p1mm' : "/StopToLB_M_1600_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB1700_1000mm': "/DisplacedSUSY_stopToBottom_M_1700_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1700_100mm' : "/DisplacedSUSY_stopToBottom_M_1700_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1700_10mm'  : "/DisplacedSUSY_stopToBottom_M_1700_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1700_1mm'   : "/DisplacedSUSY_stopToBottom_M_1700_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1700_0p1mm' : "/StopToLB_M_1700_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLB1800_1000mm': "/DisplacedSUSY_stopToBottom_M_1800_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1800_100mm' : "/DisplacedSUSY_stopToBottom_M_1800_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1800_10mm'  : "/DisplacedSUSY_stopToBottom_M_1800_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1800_1mm'   : "/DisplacedSUSY_stopToBottom_M_1800_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'stopToLB1800_0p1mm' : "/StopToLB_M_1800_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    #privately produced
    #'stopToLD1000_1mm'    : "/StopToLD_M_1000_1mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    #'stopToLD1000_100mm'  : "/StopToLD_M_1000_100mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",

    'stopToLD100_1000mm' : "/StopToLD_M_100_1000mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLD100_100mm'  : "/StopToLD_M_100_100mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLD100_10mm'   : "/StopToLD_M_100_10mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLD100_1mm'    : "/StopToLD_M_100_1mm_13TeV_2017MC/jalimena-MiniAod-18783c0a07109245951450a1a4f55409/USER",
    'stopToLD100_0p1mm'  : "/StopToLD_M_100_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    #centrally produced
    'stopToLD200_1000mm'  : "/DisplacedSUSY_stopToLD_M_200_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD200_100mm'   : "/DisplacedSUSY_stopToLD_M_200_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD200_10mm'    : "/DisplacedSUSY_stopToLD_M_200_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD200_1mm'     : "/DisplacedSUSY_stopToLD_M_200_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD200_0p1mm' : "/StopToLD_M_200_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD300_1000mm'  : "/DisplacedSUSY_stopToLD_M_300_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD300_100mm'   : "/DisplacedSUSY_stopToLD_M_300_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD300_10mm'    : "/DisplacedSUSY_stopToLD_M_300_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD300_1mm'     : "/DisplacedSUSY_stopToLD_M_300_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD300_0p1mm'   : "/StopToLD_M_300_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD400_1000mm'  : "/DisplacedSUSY_stopToLD_M_400_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD400_100mm'   : "/DisplacedSUSY_stopToLD_M_400_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD400_10mm'    : "/DisplacedSUSY_stopToLD_M_400_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD400_1mm'     : "/DisplacedSUSY_stopToLD_M_400_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD400_0p1mm'   : "/StopToLD_M_400_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD500_1000mm'  : "/DisplacedSUSY_stopToLD_M_500_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD500_100mm'   : "/DisplacedSUSY_stopToLD_M_500_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD500_10mm'    : "/DisplacedSUSY_stopToLD_M_500_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD500_1mm'     : "/DisplacedSUSY_stopToLD_M_500_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD500_0p1mm'   : "/StopToLD_M_500_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD600_1000mm'  : "/DisplacedSUSY_stopToLD_M_600_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD600_100mm'   : "/DisplacedSUSY_stopToLD_M_600_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD600_10mm'    : "/DisplacedSUSY_stopToLD_M_600_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD600_1mm'     : "/DisplacedSUSY_stopToLD_M_600_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD600_0p1mm'   : "/StopToLD_M_600_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD700_1000mm'  : "/DisplacedSUSY_stopToLD_M_700_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD700_100mm'   : "/DisplacedSUSY_stopToLD_M_700_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD700_10mm'    : "/DisplacedSUSY_stopToLD_M_700_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD700_1mm'     : "/DisplacedSUSY_stopToLD_M_700_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD700_0p1mm'   : "/StopToLD_M_700_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD800_1000mm'  : "/DisplacedSUSY_stopToLD_M_800_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD800_100mm'   : "/DisplacedSUSY_stopToLD_M_800_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD800_10mm'    : "/DisplacedSUSY_stopToLD_M_800_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD800_1mm'     : "/DisplacedSUSY_stopToLD_M_800_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD800_0p1mm'   : "/StopToLD_M_800_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD900_1000mm'  : "/DisplacedSUSY_stopToLD_M_900_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD900_100mm'   : "/DisplacedSUSY_stopToLD_M_900_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD900_10mm'    : "/DisplacedSUSY_stopToLD_M_900_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD900_1mm'     : "/DisplacedSUSY_stopToLD_M_900_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD900_0p1mm'   : "/StopToLD_M_900_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD1000_1000mm' : "/DisplacedSUSY_stopToLD_M_1000_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1000_100mm'  : "/DisplacedSUSY_stopToLD_M_1000_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1000_10mm'   : "/DisplacedSUSY_stopToLD_M_1000_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1000_1mm'    : "/DisplacedSUSY_stopToLD_M_1000_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1000_0p1mm'  : "/StopToLD_M_1000_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD1100_1000mm' : "/DisplacedSUSY_stopToLD_M_1100_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1100_100mm'  : "/DisplacedSUSY_stopToLD_M_1100_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1100_10mm'   : "/DisplacedSUSY_stopToLD_M_1100_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1100_1mm'    : "/DisplacedSUSY_stopToLD_M_1100_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1100_0p1mm'  : "/StopToLD_M_1100_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD1200_1000mm' : "/DisplacedSUSY_stopToLD_M_1200_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1200_100mm'  : "/DisplacedSUSY_stopToLD_M_1200_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1200_10mm'   : "/DisplacedSUSY_stopToLD_M_1200_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1200_1mm'    : "/DisplacedSUSY_stopToLD_M_1200_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1200_0p1mm'  : "/StopToLD_M_1200_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD1300_1000mm' : "/DisplacedSUSY_stopToLD_M_1300_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1300_100mm'  : "/DisplacedSUSY_stopToLD_M_1300_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1300_10mm'   : "/DisplacedSUSY_stopToLD_M_1300_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1300_1mm'    : "/DisplacedSUSY_stopToLD_M_1300_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1300_0p1mm'  : "/StopToLD_M_1300_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD1400_1000mm' : "/DisplacedSUSY_stopToLD_M_1400_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1400_100mm'  : "/DisplacedSUSY_stopToLD_M_1400_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1400_10mm'   : "/DisplacedSUSY_stopToLD_M_1400_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1400_1mm'    : "/DisplacedSUSY_stopToLD_M_1400_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1400_0p1mm'  : "/StopToLD_M_1400_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD1500_1000mm' : "/DisplacedSUSY_stopToLD_M_1500_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1500_100mm'  : "/DisplacedSUSY_stopToLD_M_1500_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1500_10mm'   : "/DisplacedSUSY_stopToLD_M_1500_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1500_1mm'    : "/DisplacedSUSY_stopToLD_M_1500_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1500_0p1mm'  : "/StopToLD_M_1500_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD1600_1000mm' : "/DisplacedSUSY_stopToLD_M_1600_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1600_100mm'  : "/DisplacedSUSY_stopToLD_M_1600_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1600_10mm'   : "/DisplacedSUSY_stopToLD_M_1600_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1600_1mm'    : "/DisplacedSUSY_stopToLD_M_1600_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1600_0p1mm'  : "/StopToLD_M_1600_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD1700_1000mm' : "/DisplacedSUSY_stopToLD_M_1700_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1700_100mm'  : "/DisplacedSUSY_stopToLD_M_1700_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1700_10mm'   : "/DisplacedSUSY_stopToLD_M_1700_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1700_1mm'    : "/DisplacedSUSY_stopToLD_M_1700_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1700_0p1mm'  : "/StopToLD_M_1700_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",

    'stopToLD1800_1000mm' : "/DisplacedSUSY_stopToLD_M_1800_1000mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1800_100mm'  : "/DisplacedSUSY_stopToLD_M_1800_100mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1800_10mm'   : "/DisplacedSUSY_stopToLD_M_1800_10mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1800_1mm'    : "/DisplacedSUSY_stopToLD_M_1800_1mm_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'stopToLD1800_0p1mm'  : "/StopToLD_M_1800_0p1mm_13TeV_2017MC/bcardwel-MiniAod-4fe98f39b775e67c69bc92a03424ad6b/USER",


    'HToSSTo4L110_10_1000000mm'   : "/ggH_HToSSTo4l_MH-110_MS-10_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L110_10_100000mm'    : "/ggH_HToSSTo4l_MH-110_MS-10_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_10_10000mm'     : "/ggH_HToSSTo4l_MH-110_MS-10_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_10_1000mm'      : "/ggH_HToSSTo4l_MH-110_MS-10_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_10_100mm'       : "/ggH_HToSSTo4l_MH-110_MS-10_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_10_10mm'        : "/ggH_HToSSTo4l_MH-110_MS-10_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L110_10_1mm'         : "/ggH_HToSSTo4l_MH-110_MS-10_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",

    'HToSSTo4L110_20_1000000mm'   : "/ggH_HToSSTo4l_MH-110_MS-20_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_20_100000mm'    : "/ggH_HToSSTo4l_MH-110_MS-20_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L110_20_10000mm'     : "/ggH_HToSSTo4l_MH-110_MS-20_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L110_20_1000mm'      : "/ggH_HToSSTo4l_MH-110_MS-20_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_20_100mm'       : "/ggH_HToSSTo4l_MH-110_MS-20_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L110_20_10mm'        : "/ggH_HToSSTo4l_MH-110_MS-20_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_20_1mm'         : "/ggH_HToSSTo4l_MH-110_MS-20_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L110_30_1000000mm'   : "/ggH_HToSSTo4l_MH-110_MS-30_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L110_30_100000mm'    : "/ggH_HToSSTo4l_MH-110_MS-30_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L110_30_10000mm'     : "/ggH_HToSSTo4l_MH-110_MS-30_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_30_1000mm'      : "/ggH_HToSSTo4l_MH-110_MS-30_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L110_30_100mm'       : "/ggH_HToSSTo4l_MH-110_MS-30_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L110_30_10mm'        : "/ggH_HToSSTo4l_MH-110_MS-30_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_30_1mm'         : "/ggH_HToSSTo4l_MH-110_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L110_50_1000000mm'   : "/ggH_HToSSTo4l_MH-110_MS-50_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_50_100000mm'    : "/ggH_HToSSTo4l_MH-110_MS-50_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_50_10000mm'     : "/ggH_HToSSTo4l_MH-110_MS-50_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_50_1000mm'      : "/ggH_HToSSTo4l_MH-110_MS-50_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_50_100mm'       : "/ggH_HToSSTo4l_MH-110_MS-50_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L110_50_10mm'        : "/ggH_HToSSTo4l_MH-110_MS-50_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L110_50_1mm'         : "/ggH_HToSSTo4l_MH-110_MS-50_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L125_10_1000000mm'   : "/ggH_HToSSTo4l_MH-125_MS-10_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_10_100000mm'    : "/ggH_HToSSTo4l_MH-125_MS-10_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L125_10_10000mm'     : "/ggH_HToSSTo4l_MH-125_MS-10_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L125_10_1000mm'      : "/ggH_HToSSTo4l_MH-125_MS-10_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L125_10_100mm'       : "/ggH_HToSSTo4l_MH-125_MS-10_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L125_10_10mm'        : "/ggH_HToSSTo4l_MH-125_MS-10_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L125_10_1mm'         : "/ggH_HToSSTo4l_MH-125_MS-10_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L125_20_1000000mm'   : "/ggH_HToSSTo4l_MH-125_MS-20_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_20_100000mm'    : "/ggH_HToSSTo4l_MH-125_MS-20_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_20_10000mm'     : "/ggH_HToSSTo4l_MH-125_MS-20_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_20_1000mm'      : "/ggH_HToSSTo4l_MH-125_MS-20_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_20_100mm'       : "/ggH_HToSSTo4l_MH-125_MS-20_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_20_10mm'        : "/ggH_HToSSTo4l_MH-125_MS-20_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_20_1mm'         : "/ggH_HToSSTo4l_MH-125_MS-20_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L125_30_1000000mm'   : "/ggH_HToSSTo4l_MH-125_MS-30_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_30_100000mm'    : "/ggH_HToSSTo4l_MH-125_MS-30_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L125_30_10000mm'     : "/ggH_HToSSTo4l_MH-125_MS-30_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_30_1000mm'      : "/ggH_HToSSTo4l_MH-125_MS-30_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_30_100mm'       : "/ggH_HToSSTo4l_MH-125_MS-30_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_30_10mm'        : "/ggH_HToSSTo4l_MH-125_MS-30_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_30_1mm'         : "/ggH_HToSSTo4l_MH-125_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L125_50_1000000mm'   : "/ggH_HToSSTo4l_MH-125_MS-50_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_50_100000mm'    : "/ggH_HToSSTo4l_MH-125_MS-50_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L125_50_10000mm'     : "/ggH_HToSSTo4l_MH-125_MS-50_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_50_1000mm'      : "/ggH_HToSSTo4l_MH-125_MS-50_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_50_100mm'       : "/ggH_HToSSTo4l_MH-125_MS-50_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_50_10mm'        : "/ggH_HToSSTo4l_MH-125_MS-50_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L125_50_1mm'         : "/ggH_HToSSTo4l_MH-125_MS-50_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L150_10_1000000mm'   : "/ggH_HToSSTo4l_MH-150_MS-10_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_10_100000mm'    : "/ggH_HToSSTo4l_MH-150_MS-10_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_10_10000mm'     : "/ggH_HToSSTo4l_MH-150_MS-10_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_10_1000mm'      : "/ggH_HToSSTo4l_MH-150_MS-10_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_10_100mm'       : "/ggH_HToSSTo4l_MH-150_MS-10_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_10_10mm'        : "/ggH_HToSSTo4l_MH-150_MS-10_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L150_10_1mm'         : "/ggH_HToSSTo4l_MH-150_MS-10_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L150_20_1000000mm'   : "/ggH_HToSSTo4l_MH-150_MS-20_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_20_100000mm'    : "/ggH_HToSSTo4l_MH-150_MS-20_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_20_10000mm'     : "/ggH_HToSSTo4l_MH-150_MS-20_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_20_1000mm'      : "/ggH_HToSSTo4l_MH-150_MS-20_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_20_100mm'       : "/ggH_HToSSTo4l_MH-150_MS-20_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_20_10mm'        : "/ggH_HToSSTo4l_MH-150_MS-20_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L150_20_1mm'         : "/ggH_HToSSTo4l_MH-150_MS-20_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L150_30_1000000mm'   : "/ggH_HToSSTo4l_MH-150_MS-30_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_30_100000mm'    : "/ggH_HToSSTo4l_MH-150_MS-30_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L150_30_10000mm'     : "/ggH_HToSSTo4l_MH-150_MS-30_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L150_30_1000mm'      : "/ggH_HToSSTo4l_MH-150_MS-30_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L150_30_100mm'       : "/ggH_HToSSTo4l_MH-150_MS-30_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_30_10mm'        : "/ggH_HToSSTo4l_MH-150_MS-30_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_30_1mm'         : "/ggH_HToSSTo4l_MH-150_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L150_50_1000000mm'   : "/ggH_HToSSTo4l_MH-150_MS-50_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L150_50_100000mm'    : "/ggH_HToSSTo4l_MH-150_MS-50_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_50_10000mm'     : "/ggH_HToSSTo4l_MH-150_MS-50_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L150_50_1000mm'      : "/ggH_HToSSTo4l_MH-150_MS-50_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_50_100mm'       : "/ggH_HToSSTo4l_MH-150_MS-50_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_50_10mm'        : "/ggH_HToSSTo4l_MH-150_MS-50_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L150_50_1mm'         : "/ggH_HToSSTo4l_MH-150_MS-50_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L200_10_1000000mm'   : "/ggH_HToSSTo4l_MH-200_MS-10_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_10_100000mm'    : "/ggH_HToSSTo4l_MH-200_MS-10_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_10_10000mm'     : "/ggH_HToSSTo4l_MH-200_MS-10_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_10_1000mm'      : "/ggH_HToSSTo4l_MH-200_MS-10_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_10_100mm'       : "/ggH_HToSSTo4l_MH-200_MS-10_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_10_10mm'        : "/ggH_HToSSTo4l_MH-200_MS-10_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_10_1mm'         : "/ggH_HToSSTo4l_MH-200_MS-10_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L200_20_1000000mm'   : "/ggH_HToSSTo4l_MH-200_MS-20_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_20_100000mm'    : "/ggH_HToSSTo4l_MH-200_MS-20_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_20_10000mm'     : "/ggH_HToSSTo4l_MH-200_MS-20_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_20_1000mm'      : "/ggH_HToSSTo4l_MH-200_MS-20_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L200_20_100mm'       : "/ggH_HToSSTo4l_MH-200_MS-20_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_20_10mm'        : "/ggH_HToSSTo4l_MH-200_MS-20_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L200_20_1mm'         : "/ggH_HToSSTo4l_MH-200_MS-20_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L200_30_1000000mm'   : "/ggH_HToSSTo4l_MH-200_MS-30_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_30_100000mm'    : "/ggH_HToSSTo4l_MH-200_MS-30_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_30_10000mm'     : "/ggH_HToSSTo4l_MH-200_MS-30_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L200_30_1000mm'      : "/ggH_HToSSTo4l_MH-200_MS-30_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_30_100mm'       : "/ggH_HToSSTo4l_MH-200_MS-30_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_30_10mm'        : "/ggH_HToSSTo4l_MH-200_MS-30_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_30_1mm'         : "/ggH_HToSSTo4l_MH-200_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L200_50_1000000mm'   : "/ggH_HToSSTo4l_MH-200_MS-50_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_50_100000mm'    : "/ggH_HToSSTo4l_MH-200_MS-50_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_50_10000mm'     : "/ggH_HToSSTo4l_MH-200_MS-50_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L200_50_1000mm'      : "/ggH_HToSSTo4l_MH-200_MS-50_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_50_100mm'       : "/ggH_HToSSTo4l_MH-200_MS-50_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L200_50_10mm'        : "/ggH_HToSSTo4l_MH-200_MS-50_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L200_50_1mm'         : "/ggH_HToSSTo4l_MH-200_MS-50_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L300_10_1000000mm'   : "/ggH_HToSSTo4l_MH-300_MS-10_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L300_10_100000mm'    : "/ggH_HToSSTo4l_MH-300_MS-10_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_10_10000mm'     : "/ggH_HToSSTo4l_MH-300_MS-10_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L300_10_1000mm'      : "/ggH_HToSSTo4l_MH-300_MS-10_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_10_100mm'       : "/ggH_HToSSTo4l_MH-300_MS-10_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_10_10mm'        : "/ggH_HToSSTo4l_MH-300_MS-10_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_10_1mm'         : "/ggH_HToSSTo4l_MH-300_MS-10_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L300_20_1000000mm'   : "/ggH_HToSSTo4l_MH-300_MS-20_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_20_100000mm'    : "/ggH_HToSSTo4l_MH-300_MS-20_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_20_10000mm'     : "/ggH_HToSSTo4l_MH-300_MS-20_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_20_1000mm'      : "/ggH_HToSSTo4l_MH-300_MS-20_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L300_20_100mm'       : "/ggH_HToSSTo4l_MH-300_MS-20_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_20_10mm'        : "/ggH_HToSSTo4l_MH-300_MS-20_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_20_1mm'         : "/ggH_HToSSTo4l_MH-300_MS-20_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L300_30_1000000mm'   : "/ggH_HToSSTo4l_MH-300_MS-30_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_30_100000mm'    : "/ggH_HToSSTo4l_MH-300_MS-30_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L300_30_10000mm'     : "/ggH_HToSSTo4l_MH-300_MS-30_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_30_1000mm'      : "/ggH_HToSSTo4l_MH-300_MS-30_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L300_30_100mm'       : "/ggH_HToSSTo4l_MH-300_MS-30_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_30_10mm'        : "/ggH_HToSSTo4l_MH-300_MS-30_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L300_30_1mm'         : "/ggH_HToSSTo4l_MH-300_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L300_50_1000000mm'   : "/ggH_HToSSTo4l_MH-300_MS-50_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_50_100000mm'    : "/ggH_HToSSTo4l_MH-300_MS-50_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_50_10000mm'     : "/ggH_HToSSTo4l_MH-300_MS-50_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_50_1000mm'      : "/ggH_HToSSTo4l_MH-300_MS-50_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_50_100mm'       : "/ggH_HToSSTo4l_MH-300_MS-50_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_50_10mm'        : "/ggH_HToSSTo4l_MH-300_MS-50_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_50_1mm'         : "/ggH_HToSSTo4l_MH-300_MS-50_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L300_150_1000000mm'  : "/ggH_HToSSTo4l_MH-300_MS-150_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L300_150_100000mm'   : "/ggH_HToSSTo4l_MH-300_MS-150_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L300_150_10000mm'    : "/ggH_HToSSTo4l_MH-300_MS-150_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_150_1000mm'     : "/ggH_HToSSTo4l_MH-300_MS-150_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_150_100mm'      : "/ggH_HToSSTo4l_MH-300_MS-150_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_150_10mm'       : "/ggH_HToSSTo4l_MH-300_MS-150_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L300_150_1mm'        : "/ggH_HToSSTo4l_MH-300_MS-150_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L400_10_1000000mm'   : "/ggH_HToSSTo4l_MH-400_MS-10_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_10_100000mm'    : "/ggH_HToSSTo4l_MH-400_MS-10_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_10_10000mm'     : "/ggH_HToSSTo4l_MH-400_MS-10_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_10_1000mm'      : "/ggH_HToSSTo4l_MH-400_MS-10_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L400_10_100mm'       : "/ggH_HToSSTo4l_MH-400_MS-10_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L400_10_10mm'        : "/ggH_HToSSTo4l_MH-400_MS-10_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L400_10_1mm'         : "/ggH_HToSSTo4l_MH-400_MS-10_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L400_20_1000000mm'   : "/ggH_HToSSTo4l_MH-400_MS-20_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_20_100000mm'    : "/ggH_HToSSTo4l_MH-400_MS-20_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_20_10000mm'     : "/ggH_HToSSTo4l_MH-400_MS-20_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L400_20_1000mm'      : "/ggH_HToSSTo4l_MH-400_MS-20_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_20_100mm'       : "/ggH_HToSSTo4l_MH-400_MS-20_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_20_10mm'        : "/ggH_HToSSTo4l_MH-400_MS-20_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_20_1mm'         : "/ggH_HToSSTo4l_MH-400_MS-20_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L400_30_1000000mm'   : "/ggH_HToSSTo4l_MH-400_MS-30_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_30_100000mm'    : "/ggH_HToSSTo4l_MH-400_MS-30_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L400_30_10000mm'     : "/ggH_HToSSTo4l_MH-400_MS-30_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L400_30_1000mm'      : "/ggH_HToSSTo4l_MH-400_MS-30_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_30_100mm'       : "/ggH_HToSSTo4l_MH-400_MS-30_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_30_10mm'        : "/ggH_HToSSTo4l_MH-400_MS-30_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_30_1mm'         : "/ggH_HToSSTo4l_MH-400_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L400_50_1000000mm'   : "/ggH_HToSSTo4l_MH-400_MS-50_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_50_100000mm'    : "/ggH_HToSSTo4l_MH-400_MS-50_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L400_50_10000mm'     : "/ggH_HToSSTo4l_MH-400_MS-50_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_50_1000mm'      : "/ggH_HToSSTo4l_MH-400_MS-50_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L400_50_100mm'       : "/ggH_HToSSTo4l_MH-400_MS-50_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_50_10mm'        : "/ggH_HToSSTo4l_MH-400_MS-50_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_50_1mm'         : "/ggH_HToSSTo4l_MH-400_MS-50_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L400_150_1000000mm'  : "/ggH_HToSSTo4l_MH-400_MS-150_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_150_100000mm'   : "/ggH_HToSSTo4l_MH-400_MS-150_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L400_150_10000mm'    : "/ggH_HToSSTo4l_MH-400_MS-150_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_150_1000mm'     : "/ggH_HToSSTo4l_MH-400_MS-150_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_150_100mm'      : "/ggH_HToSSTo4l_MH-400_MS-150_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L400_150_10mm'       : "/ggH_HToSSTo4l_MH-400_MS-150_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L400_150_1mm'        : "/ggH_HToSSTo4l_MH-400_MS-150_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L450_10_1000000mm'   : "/ggH_HToSSTo4l_MH-450_MS-10_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_10_100000mm'    : "/ggH_HToSSTo4l_MH-450_MS-10_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_10_10000mm'     : "/ggH_HToSSTo4l_MH-450_MS-10_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_10_1000mm'      : "/ggH_HToSSTo4l_MH-450_MS-10_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L450_10_100mm'       : "/ggH_HToSSTo4l_MH-450_MS-10_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_10_10mm'        : "/ggH_HToSSTo4l_MH-450_MS-10_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_10_1mm'         : "/ggH_HToSSTo4l_MH-450_MS-10_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L450_20_1000000mm'   : "/ggH_HToSSTo4l_MH-450_MS-20_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_20_100000mm'    : "/ggH_HToSSTo4l_MH-450_MS-20_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_20_10000mm'     : "/ggH_HToSSTo4l_MH-450_MS-20_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_20_1000mm'      : "/ggH_HToSSTo4l_MH-450_MS-20_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L450_20_100mm'       : "/ggH_HToSSTo4l_MH-450_MS-20_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L450_20_10mm'        : "/ggH_HToSSTo4l_MH-450_MS-20_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_20_1mm'         : "/ggH_HToSSTo4l_MH-450_MS-20_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L450_30_1000000mm'   : "/ggH_HToSSTo4l_MH-450_MS-30_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_30_100000mm'    : "/ggH_HToSSTo4l_MH-450_MS-30_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L450_30_10000mm'     : "/ggH_HToSSTo4l_MH-450_MS-30_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L450_30_1000mm'      : "/ggH_HToSSTo4l_MH-450_MS-30_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_30_100mm'       : "/ggH_HToSSTo4l_MH-450_MS-30_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_30_10mm'        : "/ggH_HToSSTo4l_MH-450_MS-30_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_30_1mm'         : "/ggH_HToSSTo4l_MH-450_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L450_50_1000000mm'   : "/ggH_HToSSTo4l_MH-450_MS-50_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_50_100000mm'    : "/ggH_HToSSTo4l_MH-450_MS-50_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_50_10000mm'     : "/ggH_HToSSTo4l_MH-450_MS-50_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_50_1000mm'      : "/ggH_HToSSTo4l_MH-450_MS-50_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L450_50_100mm'       : "/ggH_HToSSTo4l_MH-450_MS-50_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_50_10mm'        : "/ggH_HToSSTo4l_MH-450_MS-50_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L450_50_1mm'         : "/ggH_HToSSTo4l_MH-450_MS-50_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L450_150_1000000mm'  : "/ggH_HToSSTo4l_MH-450_MS-150_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_150_100000mm'   : "/ggH_HToSSTo4l_MH-450_MS-150_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_150_10000mm'    : "/ggH_HToSSTo4l_MH-450_MS-150_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L450_150_1000mm'     : "/ggH_HToSSTo4l_MH-450_MS-150_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_150_100mm'      : "/ggH_HToSSTo4l_MH-450_MS-150_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_150_10mm'       : "/ggH_HToSSTo4l_MH-450_MS-150_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L450_150_1mm'        : "/ggH_HToSSTo4l_MH-450_MS-150_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L500_10_1000000mm'   : "/ggH_HToSSTo4l_MH-500_MS-10_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L500_10_100000mm'    : "/ggH_HToSSTo4l_MH-500_MS-10_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_10_10000mm'     : "/ggH_HToSSTo4l_MH-500_MS-10_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_10_1000mm'      : "/ggH_HToSSTo4l_MH-500_MS-10_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_10_100mm'       : "/ggH_HToSSTo4l_MH-500_MS-10_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L500_10_10mm'        : "/ggH_HToSSTo4l_MH-500_MS-10_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_10_1mm'         : "/ggH_HToSSTo4l_MH-500_MS-10_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L500_20_1000000mm'   : "/ggH_HToSSTo4l_MH-500_MS-20_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_20_100000mm'    : "/ggH_HToSSTo4l_MH-500_MS-20_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_20_10000mm'     : "/ggH_HToSSTo4l_MH-500_MS-20_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L500_20_1000mm'      : "/ggH_HToSSTo4l_MH-500_MS-20_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L500_20_100mm'       : "/ggH_HToSSTo4l_MH-500_MS-20_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_20_10mm'        : "/ggH_HToSSTo4l_MH-500_MS-20_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_20_1mm'         : "/ggH_HToSSTo4l_MH-500_MS-20_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L500_30_1000000mm'   : "/ggH_HToSSTo4l_MH-500_MS-30_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L500_30_100000mm'    : "/ggH_HToSSTo4l_MH-500_MS-30_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L500_30_10000mm'     : "/ggH_HToSSTo4l_MH-500_MS-30_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L500_30_1000mm'      : "/ggH_HToSSTo4l_MH-500_MS-30_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L500_30_100mm'       : "/ggH_HToSSTo4l_MH-500_MS-30_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_30_10mm'        : "/ggH_HToSSTo4l_MH-500_MS-30_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_30_1mm'         : "/ggH_HToSSTo4l_MH-500_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L500_50_1000000mm'   : "/ggH_HToSSTo4l_MH-500_MS-50_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L500_50_100000mm'    : "/ggH_HToSSTo4l_MH-500_MS-50_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L500_50_10000mm'     : "/ggH_HToSSTo4l_MH-500_MS-50_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_50_1000mm'      : "/ggH_HToSSTo4l_MH-500_MS-50_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_50_100mm'       : "/ggH_HToSSTo4l_MH-500_MS-50_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_50_10mm'        : "/ggH_HToSSTo4l_MH-500_MS-50_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L500_50_1mm'         : "/ggH_HToSSTo4l_MH-500_MS-50_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L500_150_1000000mm'  : "/ggH_HToSSTo4l_MH-500_MS-150_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_150_100000mm'   : "/ggH_HToSSTo4l_MH-500_MS-150_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L500_150_10000mm'    : "/ggH_HToSSTo4l_MH-500_MS-150_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_150_1000mm'     : "/ggH_HToSSTo4l_MH-500_MS-150_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L500_150_100mm'      : "/ggH_HToSSTo4l_MH-500_MS-150_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_150_10mm'       : "/ggH_HToSSTo4l_MH-500_MS-150_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L500_150_1mm'        : "/ggH_HToSSTo4l_MH-500_MS-150_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L600_10_1000000mm'   : "/ggH_HToSSTo4l_MH-600_MS-10_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L600_10_100000mm'    : "/ggH_HToSSTo4l_MH-600_MS-10_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L600_10_10000mm'     : "/ggH_HToSSTo4l_MH-600_MS-10_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_10_1000mm'      : "/ggH_HToSSTo4l_MH-600_MS-10_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_10_100mm'       : "/ggH_HToSSTo4l_MH-600_MS-10_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_10_10mm'        : "/ggH_HToSSTo4l_MH-600_MS-10_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_10_1mm'         : "/ggH_HToSSTo4l_MH-600_MS-10_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L600_20_1000000mm'   : "/ggH_HToSSTo4l_MH-600_MS-20_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_20_100000mm'    : "/ggH_HToSSTo4l_MH-600_MS-20_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_20_10000mm'     : "/ggH_HToSSTo4l_MH-600_MS-20_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_20_1000mm'      : "/ggH_HToSSTo4l_MH-600_MS-20_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L600_20_100mm'       : "/ggH_HToSSTo4l_MH-600_MS-20_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L600_20_10mm'        : "/ggH_HToSSTo4l_MH-600_MS-20_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_20_1mm'         : "/ggH_HToSSTo4l_MH-600_MS-20_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L600_30_1000000mm'   : "/ggH_HToSSTo4l_MH-600_MS-30_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_30_100000mm'    : "/ggH_HToSSTo4l_MH-600_MS-30_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L600_30_10000mm'     : "/ggH_HToSSTo4l_MH-600_MS-30_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L600_30_1000mm'      : "/ggH_HToSSTo4l_MH-600_MS-30_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L600_30_100mm'       : "/ggH_HToSSTo4l_MH-600_MS-30_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_30_10mm'        : "/ggH_HToSSTo4l_MH-600_MS-30_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_30_1mm'         : "/ggH_HToSSTo4l_MH-600_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L600_50_1000000mm'   : "/ggH_HToSSTo4l_MH-600_MS-50_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_50_100000mm'    : "/ggH_HToSSTo4l_MH-600_MS-50_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_50_10000mm'     : "/ggH_HToSSTo4l_MH-600_MS-50_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_50_1000mm'      : "/ggH_HToSSTo4l_MH-600_MS-50_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_50_100mm'       : "/ggH_HToSSTo4l_MH-600_MS-50_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L600_50_10mm'        : "/ggH_HToSSTo4l_MH-600_MS-50_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L600_50_1mm'         : "/ggH_HToSSTo4l_MH-600_MS-50_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L600_150_1000000mm'  : "/ggH_HToSSTo4l_MH-600_MS-150_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_150_100000mm'   : "/ggH_HToSSTo4l_MH-600_MS-150_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_150_10000mm'    : "/ggH_HToSSTo4l_MH-600_MS-150_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_150_1000mm'     : "/ggH_HToSSTo4l_MH-600_MS-150_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_150_100mm'      : "/ggH_HToSSTo4l_MH-600_MS-150_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_150_10mm'       : "/ggH_HToSSTo4l_MH-600_MS-150_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L600_150_1mm'        : "/ggH_HToSSTo4l_MH-600_MS-150_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L750_10_1000000mm'   : "/ggH_HToSSTo4l_MH-750_MS-10_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_10_100000mm'    : "/ggH_HToSSTo4l_MH-750_MS-10_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_10_10000mm'     : "/ggH_HToSSTo4l_MH-750_MS-10_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L750_10_1000mm'      : "/ggH_HToSSTo4l_MH-750_MS-10_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L750_10_100mm'       : "/ggH_HToSSTo4l_MH-750_MS-10_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_10_10mm'        : "/ggH_HToSSTo4l_MH-750_MS-10_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_10_1mm'         : "/ggH_HToSSTo4l_MH-750_MS-10_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L750_20_1000000mm'   : "/ggH_HToSSTo4l_MH-750_MS-20_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_20_100000mm'    : "/ggH_HToSSTo4l_MH-750_MS-20_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_20_10000mm'     : "/ggH_HToSSTo4l_MH-750_MS-20_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_20_1000mm'      : "/ggH_HToSSTo4l_MH-750_MS-20_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_20_100mm'       : "/ggH_HToSSTo4l_MH-750_MS-20_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L750_20_10mm'        : "/ggH_HToSSTo4l_MH-750_MS-20_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_20_1mm'         : "/ggH_HToSSTo4l_MH-750_MS-20_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L750_30_1000000mm'   : "/ggH_HToSSTo4l_MH-750_MS-30_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_30_100000mm'    : "/ggH_HToSSTo4l_MH-750_MS-30_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L750_30_10000mm'     : "/ggH_HToSSTo4l_MH-750_MS-30_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L750_30_1000mm'      : "/ggH_HToSSTo4l_MH-750_MS-30_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_30_100mm'       : "/ggH_HToSSTo4l_MH-750_MS-30_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L750_30_10mm'        : "/ggH_HToSSTo4l_MH-750_MS-30_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_30_1mm'         : "/ggH_HToSSTo4l_MH-750_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L750_50_1000000mm'   : "/ggH_HToSSTo4l_MH-750_MS-50_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L750_50_100000mm'    : "/ggH_HToSSTo4l_MH-750_MS-50_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_50_10000mm'     : "/ggH_HToSSTo4l_MH-750_MS-50_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_50_1000mm'      : "/ggH_HToSSTo4l_MH-750_MS-50_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_50_100mm'       : "/ggH_HToSSTo4l_MH-750_MS-50_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_50_10mm'        : "/ggH_HToSSTo4l_MH-750_MS-50_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_50_1mm'         : "/ggH_HToSSTo4l_MH-750_MS-50_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L750_150_1000000mm'  : "/ggH_HToSSTo4l_MH-750_MS-150_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_150_100000mm'   : "/ggH_HToSSTo4l_MH-750_MS-150_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_150_10000mm'    : "/ggH_HToSSTo4l_MH-750_MS-150_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_150_1000mm'     : "/ggH_HToSSTo4l_MH-750_MS-150_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_150_100mm'      : "/ggH_HToSSTo4l_MH-750_MS-150_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L750_150_10mm'       : "/ggH_HToSSTo4l_MH-750_MS-150_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L750_150_1mm'        : "/ggH_HToSSTo4l_MH-750_MS-150_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L750_350_1000000mm'  : "/ggH_HToSSTo4l_MH-750_MS-350_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_350_100000mm'   : "/ggH_HToSSTo4l_MH-750_MS-350_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_350_10000mm'    : "/ggH_HToSSTo4l_MH-750_MS-350_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_350_1000mm'     : "/ggH_HToSSTo4l_MH-750_MS-350_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L750_350_100mm'      : "/ggH_HToSSTo4l_MH-750_MS-350_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_350_10mm'       : "/ggH_HToSSTo4l_MH-750_MS-350_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L750_350_1mm'        : "/ggH_HToSSTo4l_MH-750_MS-350_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L800_10_1000000mm'   : "/ggH_HToSSTo4l_MH-800_MS-10_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_10_100000mm'    : "/ggH_HToSSTo4l_MH-800_MS-10_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_10_10000mm'     : "/ggH_HToSSTo4l_MH-800_MS-10_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_10_1000mm'      : "/ggH_HToSSTo4l_MH-800_MS-10_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L800_10_100mm'       : "/ggH_HToSSTo4l_MH-800_MS-10_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L800_10_10mm'        : "/ggH_HToSSTo4l_MH-800_MS-10_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_10_1mm'         : "/ggH_HToSSTo4l_MH-800_MS-10_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L800_20_1000000mm'   : "/ggH_HToSSTo4l_MH-800_MS-20_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L800_20_100000mm'    : "/ggH_HToSSTo4l_MH-800_MS-20_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L800_20_10000mm'     : "/ggH_HToSSTo4l_MH-800_MS-20_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_20_1000mm'      : "/ggH_HToSSTo4l_MH-800_MS-20_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_20_100mm'       : "/ggH_HToSSTo4l_MH-800_MS-20_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_20_10mm'        : "/ggH_HToSSTo4l_MH-800_MS-20_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_20_1mm'         : "/ggH_HToSSTo4l_MH-800_MS-20_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L800_30_1000000mm'   : "/ggH_HToSSTo4l_MH-800_MS-30_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L800_30_100000mm'    : "/ggH_HToSSTo4l_MH-800_MS-30_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_30_10000mm'     : "/ggH_HToSSTo4l_MH-800_MS-30_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_30_1000mm'      : "/ggH_HToSSTo4l_MH-800_MS-30_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_30_100mm'       : "/ggH_HToSSTo4l_MH-800_MS-30_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L800_30_10mm'        : "/ggH_HToSSTo4l_MH-800_MS-30_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_30_1mm'         : "/ggH_HToSSTo4l_MH-800_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L800_50_1000000mm'   : "/ggH_HToSSTo4l_MH-800_MS-50_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_50_100000mm'    : "/ggH_HToSSTo4l_MH-800_MS-50_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L800_50_10000mm'     : "/ggH_HToSSTo4l_MH-800_MS-50_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_50_1000mm'      : "/ggH_HToSSTo4l_MH-800_MS-50_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_50_100mm'       : "/ggH_HToSSTo4l_MH-800_MS-50_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L800_50_10mm'        : "/ggH_HToSSTo4l_MH-800_MS-50_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_50_1mm'         : "/ggH_HToSSTo4l_MH-800_MS-50_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L800_150_1000000mm'  : "/ggH_HToSSTo4l_MH-800_MS-150_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_150_100000mm'   : "/ggH_HToSSTo4l_MH-800_MS-150_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_150_10000mm'    : "/ggH_HToSSTo4l_MH-800_MS-150_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L800_150_1000mm'     : "/ggH_HToSSTo4l_MH-800_MS-150_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L800_150_100mm'      : "/ggH_HToSSTo4l_MH-800_MS-150_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_150_10mm'       : "/ggH_HToSSTo4l_MH-800_MS-150_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L800_150_1mm'        : "/ggH_HToSSTo4l_MH-800_MS-150_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L800_350_1000000mm'  : "/ggH_HToSSTo4l_MH-800_MS-350_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L800_350_100000mm'   : "/ggH_HToSSTo4l_MH-800_MS-350_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_350_10000mm'    : "/ggH_HToSSTo4l_MH-800_MS-350_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_350_1000mm'     : "/ggH_HToSSTo4l_MH-800_MS-350_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L800_350_100mm'      : "/ggH_HToSSTo4l_MH-800_MS-350_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_350_10mm'       : "/ggH_HToSSTo4l_MH-800_MS-350_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L800_350_1mm'        : "/ggH_HToSSTo4l_MH-800_MS-350_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L900_10_1000000mm'   : "/ggH_HToSSTo4l_MH-900_MS-10_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_10_100000mm'    : "/ggH_HToSSTo4l_MH-900_MS-10_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_10_10000mm'     : "/ggH_HToSSTo4l_MH-900_MS-10_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_10_1000mm'      : "/ggH_HToSSTo4l_MH-900_MS-10_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_10_100mm'       : "/ggH_HToSSTo4l_MH-900_MS-10_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_10_10mm'        : "/ggH_HToSSTo4l_MH-900_MS-10_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_10_1mm'         : "/ggH_HToSSTo4l_MH-900_MS-10_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L900_20_1000000mm'   : "/ggH_HToSSTo4l_MH-900_MS-20_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L900_20_100000mm'    : "/ggH_HToSSTo4l_MH-900_MS-20_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L900_20_10000mm'     : "/ggH_HToSSTo4l_MH-900_MS-20_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_20_1000mm'      : "/ggH_HToSSTo4l_MH-900_MS-20_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_20_100mm'       : "/ggH_HToSSTo4l_MH-900_MS-20_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_20_10mm'        : "/ggH_HToSSTo4l_MH-900_MS-20_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_20_1mm'         : "/ggH_HToSSTo4l_MH-900_MS-20_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L900_30_1000000mm'   : "/ggH_HToSSTo4l_MH-900_MS-30_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_30_100000mm'    : "/ggH_HToSSTo4l_MH-900_MS-30_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_30_10000mm'     : "/ggH_HToSSTo4l_MH-900_MS-30_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_30_1000mm'      : "/ggH_HToSSTo4l_MH-900_MS-30_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_30_100mm'       : "/ggH_HToSSTo4l_MH-900_MS-30_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_30_10mm'        : "/ggH_HToSSTo4l_MH-900_MS-30_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_30_1mm'         : "/ggH_HToSSTo4l_MH-900_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L900_50_1000000mm'   : "/ggH_HToSSTo4l_MH-900_MS-50_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_50_100000mm'    : "/ggH_HToSSTo4l_MH-900_MS-50_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_50_10000mm'     : "/ggH_HToSSTo4l_MH-900_MS-50_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_50_1000mm'      : "/ggH_HToSSTo4l_MH-900_MS-50_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_50_100mm'       : "/ggH_HToSSTo4l_MH-900_MS-50_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_50_10mm'        : "/ggH_HToSSTo4l_MH-900_MS-50_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_50_1mm'         : "/ggH_HToSSTo4l_MH-900_MS-50_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L900_150_1000000mm'  : "/ggH_HToSSTo4l_MH-900_MS-150_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_150_100000mm'   : "/ggH_HToSSTo4l_MH-900_MS-150_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_150_10000mm'    : "/ggH_HToSSTo4l_MH-900_MS-150_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_150_1000mm'     : "/ggH_HToSSTo4l_MH-900_MS-150_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_150_100mm'      : "/ggH_HToSSTo4l_MH-900_MS-150_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_150_10mm'       : "/ggH_HToSSTo4l_MH-900_MS-150_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_150_1mm'        : "/ggH_HToSSTo4l_MH-900_MS-150_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",

    'HToSSTo4L900_350_1000000mm'  : "/ggH_HToSSTo4l_MH-900_MS-350_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_350_100000mm'   : "/ggH_HToSSTo4l_MH-900_MS-350_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_350_10000mm'    : "/ggH_HToSSTo4l_MH-900_MS-350_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_350_1000mm'     : "/ggH_HToSSTo4l_MH-900_MS-350_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L900_350_100mm'      : "/ggH_HToSSTo4l_MH-900_MS-350_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_350_10mm'       : "/ggH_HToSSTo4l_MH-900_MS-350_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L900_350_1mm'        : "/ggH_HToSSTo4l_MH-900_MS-350_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L1000_10_1000000mm'  : "/ggH_HToSSTo4l_MH-1000_MS-10_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_10_100000mm'   : "/ggH_HToSSTo4l_MH-1000_MS-10_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_10_10000mm'    : "/ggH_HToSSTo4l_MH-1000_MS-10_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_10_1000mm'     : "/ggH_HToSSTo4l_MH-1000_MS-10_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_10_100mm'      : "/ggH_HToSSTo4l_MH-1000_MS-10_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_10_10mm'       : "/ggH_HToSSTo4l_MH-1000_MS-10_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_10_1mm'        : "/ggH_HToSSTo4l_MH-1000_MS-10_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L1000_20_1000000mm'  : "/ggH_HToSSTo4l_MH-1000_MS-20_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_20_100000mm'   : "/ggH_HToSSTo4l_MH-1000_MS-20_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_20_10000mm'    : "/ggH_HToSSTo4l_MH-1000_MS-20_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L1000_20_1000mm'     : "/ggH_HToSSTo4l_MH-1000_MS-20_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L1000_20_100mm'      : "/ggH_HToSSTo4l_MH-1000_MS-20_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L1000_20_10mm'       : "/ggH_HToSSTo4l_MH-1000_MS-20_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_20_1mm'        : "/ggH_HToSSTo4l_MH-1000_MS-20_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L1000_30_1000000mm'  : "/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_30_100000mm'   : "/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_30_10000mm'    : "/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_30_1000mm'     : "/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_30_100mm'      : "/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_30_10mm'       : "/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L1000_30_1mm'        : "/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L1000_50_1000000mm'  : "/ggH_HToSSTo4l_MH-1000_MS-50_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_50_100000mm'   : "/ggH_HToSSTo4l_MH-1000_MS-50_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_50_10000mm'    : "/ggH_HToSSTo4l_MH-1000_MS-50_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_50_1000mm'     : "/ggH_HToSSTo4l_MH-1000_MS-50_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L1000_50_100mm'      : "/ggH_HToSSTo4l_MH-1000_MS-50_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L1000_50_10mm'       : "/ggH_HToSSTo4l_MH-1000_MS-50_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L1000_50_1mm'        : "/ggH_HToSSTo4l_MH-1000_MS-50_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L1000_150_1000000mm' : "/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_150_100000mm'  : "/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_150_10000mm'   : "/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_150_1000mm'    : "/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_150_100mm'     : "/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",
    'HToSSTo4L1000_150_10mm'      : "/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_150_1mm'       : "/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

    'HToSSTo4L1000_350_1000000mm' : "/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-1000000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L1000_350_100000mm'  : "/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-100000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM",
    'HToSSTo4L1000_350_10000mm'   : "/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-10000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_350_1000mm'    : "/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-1000_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_350_100mm'     : "/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-100_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_350_10mm'      : "/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-10_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",
    'HToSSTo4L1000_350_1mm'       : "/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-1_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",

}

# create composite dictionary of all samples
dataset_names = {}
dataset_names.update(bg_mc_samples)
dataset_names.update(data_samples)
dataset_names.update(signal_mc_samples)

# Propagate displaced SUSY sample names to the lifetime-reweighted samples
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import renameReweightedSamples
renameReweightedSamples(dataset_names)
