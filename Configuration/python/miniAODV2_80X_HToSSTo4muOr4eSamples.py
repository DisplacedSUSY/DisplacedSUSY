#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD V2 DATASETS  ####################################################################
############################################################################################################

bg_mc_samples = {
    #DY
    'DYJetsToLL_50'     : ['/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM', # 63M
                           '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM'], # 63M
    'DYJetsToLL_10to50' : '/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 35M

    #DYBBJets
    'DYBBJetsToLL' : '/DYBBJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 3M

    'DYJetsToTauTauLeptonic' : ['/DYJetsToTauTau_ForcedMuEleDecay_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_ext1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM',#26M
                                '/DYJetsToTauTau_ForcedMuEleDecay_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',#27M
                                '/DYJetsToTauTau_ForcedMuDecay_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'],#2M


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
    'QCD_EMEnriched_15to20'   : '', #not available
    'QCD_EMEnriched_20to30'   :   '/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 9M
    'QCD_EMEnriched_30to50'   :  ['/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 5M
                                  '/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'], # 7M
    'QCD_EMEnriched_50to80'   :   '/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM', # 23M
    'QCD_EMEnriched_80to120'  : ['/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 36M
                                 '/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'], # 42M
    'QCD_EMEnriched_120to170' : '/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    'QCD_EMEnriched_170to300' : '/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 12M
    'QCD_EMEnriched_300toInf' : '/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 7M

    #QCD DoubleEMEnriched
    'QCD_DoubleEMEnriched_HighMass_30to40'  : '/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',#18M
    'QCD_DoubleEMEnriched_LowMass_30toInf'  : '/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',#38M
    'QCD_DoubleEMEnriched_HighMass_40toInf' : '/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',#21M

#    #QCD bcToE
    'QCD_bcToE_15to20'   :  '/QCD_Pt_15to20_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    'QCD_bcToE_20to30'   :  '/QCD_Pt_20to30_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 11M
    'QCD_bcToE_30to80'   :  '/QCD_Pt_30to80_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 15M
    'QCD_bcToE_80to170'  :  '/QCD_Pt_80to170_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_backup_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
    'QCD_bcToE_170to250' :  '/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 10M
    'QCD_bcToE_250toInf' :  '/QCD_Pt_250toInf_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', # 10M

    #Cosmics
    #'Cosmics' : '/CosmicMuonsMCPrivate/lpcmetx-RunIISummer15DR80_LooseMuCosmic_38T_pt10_3000_DIGIRAW_step2_AOD_CMSSW_8_0_21-0f111def6b9b94823916592fdafc5ec9/USER',
    'Cosmics' : '/TKCosmic_38T_p20-3000/RunIISummer16MiniAODv3-NoPUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',

    'NoBPTX_2016G' : '/NoBPTX/Run2016G-07Aug17-v1/MINIAOD',
    'NoBPTX_2016H' : '/NoBPTX/Run2016H-07Aug17-v1/MINIAOD',
}

data_samples = {
    # SingleElectron 07Aug17 rereco
    'SingleEle_2016B'         : ['/SingleElectron/Run2016B-07Aug17_ver1-v1/MINIAOD',
                                 '/SingleElectron/Run2016B-07Aug17_ver2-v1/MINIAOD'], # 246M
    'SingleEle_2016C'         : '/SingleElectron/Run2016C-07Aug17-v1/MINIAOD', # 97M
    'SingleEle_2016D'         : '/SingleElectron/Run2016D-07Aug17-v1/MINIAOD', # 148M
    'SingleEle_2016E'         : '/SingleElectron/Run2016E-07Aug17-v1/MINIAOD', # 117M
    'SingleEle_2016F'         : '/SingleElectron/Run2016F-07Aug17-v1/MINIAOD', # 71M
    'SingleEle_2016G'         : '/SingleElectron/Run2016G-07Aug17-v1/MINIAOD', # 153M
    'SingleEle_2016H'         : '/SingleElectron/Run2016H-07Aug17-v1/MINIAOD', # 127M

    # SingleMuon 07Aug17 rereco
    'SingleMu_2016B'         : ['/SingleMuon/Run2016B-07Aug17_ver1-v1/MINIAOD',
                                '/SingleMuon/Run2016B-07Aug17_ver2-v1/MINIAOD'], # 158M
    'SingleMu_2016C'         : '/SingleMuon/Run2016C-07Aug17-v1/MINIAOD', # 67M
    'SingleMu_2016D'         : '/SingleMuon/Run2016D-07Aug17-v1/MINIAOD', # 98M
    'SingleMu_2016E'         : '/SingleMuon/Run2016E-07Aug17-v1/MINIAOD', # 91M
    'SingleMu_2016F'         : '/SingleMuon/Run2016F-07Aug17-v1/MINIAOD', # 65M
    'SingleMu_2016G'         : '/SingleMuon/Run2016G-07Aug17-v1/MINIAOD', # 150M
    'SingleMu_2016H'         : '/SingleMuon/Run2016H-07Aug17-v1/MINIAOD', # 171M

    # DoubleEG 07Aug17 rereco
    'DoubleEG_2016B'         :  ['/DoubleEG/Run2016B-07Aug17_ver1-v1/MINIAOD',
                                 '/DoubleEG/Run2016B-07Aug17_ver2-v1/MINIAOD'],# 143M
    'DoubleEG_2016C'         :  '/DoubleEG/Run2016C-07Aug17-v1/MINIAOD',# 48M
    'DoubleEG_2016D'         :  '/DoubleEG/Run2016D-07Aug17-v1/MINIAOD',# 53M
    'DoubleEG_2016E'         :  '/DoubleEG/Run2016E-07Aug17-v1/MINIAOD',# 50M
    'DoubleEG_2016F'         :  '/DoubleEG/Run2016F-07Aug17-v1/MINIAOD',# 35M
    'DoubleEG_2016G'         :  '/DoubleEG/Run2016G-07Aug17-v1/MINIAOD',# 79M
    'DoubleEG_2016H'         :  '/DoubleEG/Run2016H-07Aug17-v1/MINIAOD',# 84M

    # DoubleMuon 07Aug17 rereco
    'DoubleMu_2016B'         : ['/DoubleMuon/Run2016B-07Aug17_ver1-v1/MINIAOD',
                                '/DoubleMuon/Run2016B-07Aug17_ver2-v1/MINIAOD'], # 83M
    'DoubleMu_2016C'         :  '/DoubleMuon/Run2016C-07Aug17-v1/MINIAOD',# 28M
    'DoubleMu_2016D'         :  '/DoubleMuon/Run2016D-07Aug17-v1/MINIAOD',# 34M
    'DoubleMu_2016E'         :  '/DoubleMuon/Run2016E-07Aug17-v1/MINIAOD',# 28M
    'DoubleMu_2016F'         :  '/DoubleMuon/Run2016F-07Aug17-v1/MINIAOD',# 20M
    'DoubleMu_2016G'         :  '/DoubleMuon/Run2016G-07Aug17-v1/MINIAOD',# 45M
    'DoubleMu_2016H'         :  '/DoubleMuon/Run2016H-07Aug17-v1/MINIAOD',# 48M

    # MuonEG 07Aug17 rereco
    'MuonEG_2016B'         : ['/MuonEG/Run2016B-07Aug17_ver1-v1/MINIAOD', #225k
                              '/MuonEG/Run2016B-07Aug17_ver2-v1/MINIAOD'],#33M
    'MuonEG_2016C'         : '/MuonEG/Run2016C-07Aug17-v1/MINIAOD', # 15M
    'MuonEG_2016D'         : '/MuonEG/Run2016D-07Aug17-v1/MINIAOD', # 23M
    'MuonEG_2016E'         : '/MuonEG/Run2016E-07Aug17-v1/MINIAOD', # 23M
    'MuonEG_2016F'         : '/MuonEG/Run2016F-07Aug17-v1/MINIAOD', # 16M
    'MuonEG_2016G'         : '/MuonEG/Run2016G-07Aug17-v1/MINIAOD', # 34M
    'MuonEG_2016H'         : '/MuonEG/Run2016H-07Aug17-v1/MINIAOD', # 29M

    # MET 07Aug17 rereco
    'MET_2016G' :  '/MET/Run2016G-07Aug17-v1/MINIAOD',
    'MET_2016H' :  '/MET/Run2016H-07Aug17-v1/MINIAOD',
}

signal_mc_samples = {
    #DisplacedSUSY Signal MC MiniAOD - 90k events/sample
    'stopToLB100_1000mm' : "/StopToLB_M_100_1000mm_13TeV_2016MC/jalimena-MiniAod-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",
    'stopToLB100_100mm'  : "/StopToLB_M_100_100mm_13TeV_2016MC/jalimena-MiniAod-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",
    'stopToLB100_10mm'   : "/StopToLB_M_100_10mm_13TeV_2016MC/jalimena-MiniAod-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",
    'stopToLB100_1mm'    : "/StopToLB_M_100_1mm_13TeV_2016MC/jalimena-MiniAod-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",
    'stopToLB100_0p1mm'  : "/StopToLBottom_M_100_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB200_1mm'    : "/DisplacedSUSY_StopToBL_M-200_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB200_10mm'   : "/DisplacedSUSY_StopToBL_M-200_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB200_100mm'  : "/DisplacedSUSY_StopToBL_M-200_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB200_1000mm' : "/DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB200_0p1mm'  : "/StopToLBottom_M_200_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB300_1mm'    : "/DisplacedSUSY_StopToBL_M-300_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB300_10mm'   : "/DisplacedSUSY_StopToBL_M-300_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB300_100mm'  : "/DisplacedSUSY_StopToBL_M-300_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB300_1000mm' : "/DisplacedSUSY_StopToBL_M-300_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB300_0p1mm'  : "/StopToLBottom_M_300_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB400_1mm'    : "/DisplacedSUSY_StopToBL_M-400_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB400_10mm'   : "/DisplacedSUSY_StopToBL_M-400_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB400_100mm'  : "/DisplacedSUSY_StopToBL_M-400_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB400_1000mm' : "/DisplacedSUSY_StopToBL_M-400_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB400_0p1mm'  : "/StopToLBottom_M_400_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB500_1mm'    : "/DisplacedSUSY_StopToBL_M-500_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB500_10mm'   : "/DisplacedSUSY_StopToBL_M-500_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB500_100mm'  : "/DisplacedSUSY_StopToBL_M-500_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB500_1000mm' : "/DisplacedSUSY_StopToBL_M-500_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB500_0p1mm'  : "/StopToLBottom_M_500_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB600_1mm'    : "/DisplacedSUSY_StopToBL_M-600_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB600_10mm'   : "/DisplacedSUSY_StopToBL_M-600_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB600_100mm'  : "/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB600_1000mm' : "/DisplacedSUSY_StopToBL_M-600_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB600_0p1mm'  : "/StopToLBottom_M_600_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB700_1mm'    : "/DisplacedSUSY_StopToBL_M-700_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB700_10mm'   : "/DisplacedSUSY_StopToBL_M-700_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB700_100mm'  : "/DisplacedSUSY_StopToBL_M-700_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB700_1000mm' : "/DisplacedSUSY_StopToBL_M-700_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB700_0p1mm'  : "/StopToLBottom_M_700_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB800_1mm'    : "/DisplacedSUSY_StopToBL_M-800_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB800_10mm'   : "/DisplacedSUSY_StopToBL_M-800_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB800_100mm'  : "/DisplacedSUSY_StopToBL_M-800_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB800_1000mm' : "/DisplacedSUSY_StopToBL_M-800_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB800_0p1mm'  : "/StopToLBottom_M_800_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB900_1mm'    : "/DisplacedSUSY_StopToBL_M-900_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB900_10mm'   : "/DisplacedSUSY_StopToBL_M-900_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB900_100mm'  : "/DisplacedSUSY_StopToBL_M-900_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB900_1000mm' : "/DisplacedSUSY_StopToBL_M-900_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB900_0p1mm'  : "/StopToLBottom_M_900_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB1000_1mm'   : "/DisplacedSUSY_StopToBL_M-1000_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB1000_10mm'  : "/DisplacedSUSY_StopToBL_M-1000_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB1000_100mm' : "/DisplacedSUSY_StopToBL_M-1000_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB1000_1000mm': "/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB1000_0p1mm' : "/StopToLBottom_M_1000_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB1100_1mm'   : "/DisplacedSUSY_StopToBL_M-1100_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB1100_10mm'  : "/DisplacedSUSY_StopToBL_M-1100_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB1100_100mm' : "/DisplacedSUSY_StopToBL_M-1100_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB1100_1000mm': "/DisplacedSUSY_StopToBL_M-1100_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB1100_0p1mm' : "/StopToLBottom_M_1100_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB1200_1mm'   : "/DisplacedSUSY_StopToBL_M-1200_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB1200_10mm'  : "/DisplacedSUSY_StopToBL_M-1200_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB1200_100mm' : "/DisplacedSUSY_StopToBL_M-1200_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB1200_1000mm': "/DisplacedSUSY_StopToBL_M-1200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",
    'stopToLB1200_0p1mm' : "/StopToLBottom_M_1200_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB1300_1000mm': "/DisplacedSUSY_stopToBottom_M_1300_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1300_100mm' : "/DisplacedSUSY_stopToBottom_M_1300_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1300_10mm'  : "/DisplacedSUSY_stopToBottom_M_1300_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1300_1mm'   : "/StopToLB_M_1300_1mm_13TeV_2016MC/jalimena-MiniAod-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",
    'stopToLB1300_0p1mm' : "/StopToLBottom_M_1300_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB1400_1000mm': "/DisplacedSUSY_stopToBottom_M_1400_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1400_100mm' : "/StopToLB_M_1400_100mm_13TeV_2016MC/jalimena-MiniAod-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",
    'stopToLB1400_10mm'  : "/DisplacedSUSY_stopToBottom_M_1400_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1400_1mm'   : "/DisplacedSUSY_stopToBottom_M_1400_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1400_0p1mm' : "/StopToLBottom_M_1400_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB1500_1000mm': "/DisplacedSUSY_stopToBottom_M_1500_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1500_100mm' : "/DisplacedSUSY_stopToBottom_M_1500_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1500_10mm'  : "/DisplacedSUSY_stopToBottom_M_1500_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1500_1mm'   : "/StopToLB_M_1500_1mm_13TeV_2016MC/jalimena-MiniAod-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",
    'stopToLB1500_0p1mm' : "/StopToLBottom_M_1500_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB1600_1000mm': "/DisplacedSUSY_stopToBottom_M_1600_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1600_100mm' : "/DisplacedSUSY_stopToBottom_M_1600_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1600_10mm'  : "/DisplacedSUSY_stopToBottom_M_1600_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1600_1mm'   : "/DisplacedSUSY_stopToBottom_M_1600_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1600_0p1mm' : "/StopToLBottom_M_1600_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB1700_1000mm': "/StopToLB_M_1700_1000mm_13TeV_2016MC/jalimena-MiniAod-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",
    'stopToLB1700_100mm' : "/DisplacedSUSY_stopToBottom_M_1700_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1700_10mm'  : "/DisplacedSUSY_stopToBottom_M_1700_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1700_1mm'   : "/DisplacedSUSY_stopToBottom_M_1700_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1700_0p1mm' : "/StopToLBottom_M_1700_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLB1800_1000mm_private' : "/StopToLB_M_1800_1000mm_13TeV_2016MC/jalimena-MiniAod-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",
    'stopToLB1800_1000mm': "/DisplacedSUSY_stopToBottom_M_1800_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1800_100mm' : "/DisplacedSUSY_stopToBottom_M_1800_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1800_10mm'  : "/DisplacedSUSY_stopToBottom_M_1800_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1800_1mm'   : "/DisplacedSUSY_stopToBottom_M_1800_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLB1800_0p1mm' : "/StopToLBottom_M_1800_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",


    'stopToLD100_1000mm' : "/StopToLD_M_100_1000mm_13TeV_2016MC/jalimena-MiniAod-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",
    'stopToLD100_100mm'  : "/StopToLD_M_100_100mm_13TeV_2016MC/jalimena-MiniAod-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",
    'stopToLD100_10mm'   : "/StopToLD_M_100_10mm_13TeV_2016MC/jalimena-MiniAod-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",
    'stopToLD100_1mm'    : "/StopToLD_M_100_1mm_13TeV_2016MC/jalimena-MiniAod-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",
    'stopToLD100_0p1mm'  : "/StopToLD_M_100_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD200_1000mm'  : "/DisplacedSUSY_stopToLD_M_200_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD200_100mm'   : "/DisplacedSUSY_stopToLD_M_200_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD200_10mm'    : "/DisplacedSUSY_stopToLD_M_200_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD200_1mm'     : "/DisplacedSUSY_stopToLD_M_200_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD200_0p1mm'   : "/StopToLD_M_200_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD300_1000mm'  : "/DisplacedSUSY_stopToLD_M_300_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD300_100mm'   : "/DisplacedSUSY_stopToLD_M_300_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD300_10mm'    : "/DisplacedSUSY_stopToLD_M_300_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD300_1mm'     : "/DisplacedSUSY_stopToLD_M_300_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD300_0p1mm'   : "/StopToLD_M_300_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD400_1000mm'  : "/DisplacedSUSY_stopToLD_M_400_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD400_100mm'   : "/DisplacedSUSY_stopToLD_M_400_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD400_10mm'    : "/DisplacedSUSY_stopToLD_M_400_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD400_1mm'     : "/DisplacedSUSY_stopToLD_M_400_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD400_0p1mm'   : "/StopToLD_M_400_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD500_1000mm'  : "/DisplacedSUSY_stopToLD_M_500_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD500_100mm'   : "/DisplacedSUSY_stopToLD_M_500_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD500_10mm'    : "/DisplacedSUSY_stopToLD_M_500_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD500_1mm'     : "/DisplacedSUSY_stopToLD_M_500_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD500_0p1mm'   : "/StopToLD_M_500_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD600_1000mm'  : "/DisplacedSUSY_stopToLD_M_600_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD600_100mm'   : "/DisplacedSUSY_stopToLD_M_600_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD600_10mm'    : "/DisplacedSUSY_stopToLD_M_600_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD600_1mm'     : "/DisplacedSUSY_stopToLD_M_600_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD600_0p1mm'   : "/StopToLD_M_600_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD700_1000mm'  : "/DisplacedSUSY_stopToLD_M_700_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD700_100mm'   : "/DisplacedSUSY_stopToLD_M_700_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD700_10mm'    : "/DisplacedSUSY_stopToLD_M_700_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD700_1mm'     : "/DisplacedSUSY_stopToLD_M_700_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD700_0p1mm'   : "/StopToLD_M_700_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD800_1000mm'  : "/DisplacedSUSY_stopToLD_M_800_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD800_100mm'   : "/DisplacedSUSY_stopToLD_M_800_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD800_10mm'    : "/DisplacedSUSY_stopToLD_M_800_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD800_1mm'     : "/DisplacedSUSY_stopToLD_M_800_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD800_0p1mm'   : "/StopToLD_M_800_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD900_1000mm'  : "/DisplacedSUSY_stopToLD_M_900_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD900_100mm'   : "/DisplacedSUSY_stopToLD_M_900_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD900_10mm'    : "/DisplacedSUSY_stopToLD_M_900_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD900_1mm'     : "/DisplacedSUSY_stopToLD_M_900_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD900_0p1mm'   : "/StopToLD_M_900_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD1000_1000mm' : "/DisplacedSUSY_stopToLD_M_1000_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1000_100mm'  : "/DisplacedSUSY_stopToLD_M_1000_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1000_10mm'   : "/DisplacedSUSY_stopToLD_M_1000_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1000_1mm'    : "/DisplacedSUSY_stopToLD_M_1000_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1000_0p1mm'  : "/StopToLD_M_1000_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD1100_1000mm' : "/DisplacedSUSY_stopToLD_M_1100_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1100_100mm'  : "/DisplacedSUSY_stopToLD_M_1100_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1100_10mm'   : "/DisplacedSUSY_stopToLD_M_1100_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1100_1mm'    : "/DisplacedSUSY_stopToLD_M_1100_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1100_0p1mm'  : "/StopToLD_M_1100_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD1200_1000mm' : "/DisplacedSUSY_stopToLD_M_1200_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1200_100mm'  : "/DisplacedSUSY_stopToLD_M_1200_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1200_10mm'   : "/DisplacedSUSY_stopToLD_M_1200_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1200_1mm'    : "/DisplacedSUSY_stopToLD_M_1200_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1200_0p1mm'  : "/StopToLD_M_1200_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD1300_1000mm' : "/DisplacedSUSY_stopToLD_M_1300_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1300_100mm'  : "/DisplacedSUSY_stopToLD_M_1300_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1300_10mm'   : "/DisplacedSUSY_stopToLD_M_1300_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1300_1mm'    : "/DisplacedSUSY_stopToLD_M_1300_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1300_0p1mm'  : "/StopToLD_M_1300_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD1400_1000mm' : "/DisplacedSUSY_stopToLD_M_1400_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1400_100mm'  : "/DisplacedSUSY_stopToLD_M_1400_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1400_10mm'   : "/DisplacedSUSY_stopToLD_M_1400_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1400_1mm'    : "/DisplacedSUSY_stopToLD_M_1400_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1400_0p1mm'  : "/StopToLD_M_1400_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD1500_1000mm' : "/DisplacedSUSY_stopToLD_M_1500_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1500_100mm'  : "/DisplacedSUSY_stopToLD_M_1500_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1500_10mm'   : "/DisplacedSUSY_stopToLD_M_1500_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1500_1mm'    : "/DisplacedSUSY_stopToLD_M_1500_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1500_0p1mm'  : "/StopToLD_M_1500_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD1600_1000mm' : "/DisplacedSUSY_stopToLD_M_1600_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1600_100mm'  : "/DisplacedSUSY_stopToLD_M_1600_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1600_10mm'   : "/DisplacedSUSY_stopToLD_M_1600_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1600_1mm'    : "/DisplacedSUSY_stopToLD_M_1600_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1600_0p1mm'  : "/StopToLD_M_1600_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD1700_1000mm' : "/DisplacedSUSY_stopToLD_M_1700_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1700_100mm'  : "/DisplacedSUSY_stopToLD_M_1700_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1700_10mm'   : "/DisplacedSUSY_stopToLD_M_1700_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1700_1mm'    : "/DisplacedSUSY_stopToLD_M_1700_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1700_0p1mm'  : "/StopToLD_M_1700_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'stopToLD1800_1000mm' : "/DisplacedSUSY_stopToLD_M_1800_1000mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1800_100mm'  : "/DisplacedSUSY_stopToLD_M_1800_100mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1800_10mm'   : "/DisplacedSUSY_stopToLD_M_1800_10mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1800_1mm'    : "/DisplacedSUSY_stopToLD_M_1800_1mm_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM",
    'stopToLD1800_0p1mm'  : "/StopToLD_M_1800_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    # 2016 slepton and stau samples must be run in 9_4_X
    'sleptons50_0p01mm'    : "/Sleptons_M_50_0p01mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons50_0p1mm'     : "/Sleptons_M_50_0p1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons50_1mm'       : "/Sleptons_M_50_1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons50_10mm'      : "/Sleptons_M_50_10mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons50_100mm'     : "/Sleptons_M_50_100mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons50_1000mm'    : ["/Sleptons_M_50_1000mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
                              "/Sleptons_M_50_1000mm_13TeV_2016MC_v2/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER"],

    'sleptons100_0p01mm'   : "/Sleptons_M_100_0p01mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons100_0p1mm'    : "/Sleptons_M_100_0p1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons100_1mm'      : "/Sleptons_M_100_1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons100_10mm'     : "/Sleptons_M_100_10mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons100_100mm'    : "/Sleptons_M_100_100mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons100_1000mm'   : ["/Sleptons_M_100_1000mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
                              "/Sleptons_M_100_1000mm_13TeV_2016MC_v2/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER"],

    'sleptons200_0p01mm'   : "/Sleptons_M_200_0p01mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons200_0p1mm'    : "/Sleptons_M_200_0p1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons200_1mm'      : "/Sleptons_M_200_1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons200_10mm'     : "/Sleptons_M_200_10mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons200_100mm'    : "/Sleptons_M_200_100mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons200_1000mm'   : ["/Sleptons_M_200_1000mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
                              "/Sleptons_M_200_1000mm_13TeV_2016MC_v2/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER"],

    'sleptons300_0p01mm'   : "/Sleptons_M_300_0p01mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons300_0p1mm'    : "/Sleptons_M_300_0p1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons300_1mm'      : "/Sleptons_M_300_1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons300_10mm'     : "/Sleptons_M_300_10mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons300_100mm'    : "/Sleptons_M_300_100mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons300_1000mm'   : ["/Sleptons_M_300_1000mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
                              "/Sleptons_M_300_1000mm_13TeV_2016MC_v2/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER"],

    'sleptons400_0p01mm'   : "/Sleptons_M_400_0p01mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons400_0p1mm'    : "/Sleptons_M_400_0p1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons400_1mm'      : "/Sleptons_M_400_1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons400_10mm'     : "/Sleptons_M_400_10mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons400_100mm'    : "/Sleptons_M_400_100mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons400_1000mm'   : "/Sleptons_M_400_1000mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'sleptons500_0p01mm'   : "/Sleptons_M_500_0p01mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons500_0p1mm'    : "/Sleptons_M_500_0p1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons500_1mm'      : "/Sleptons_M_500_1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons500_10mm'     : "/Sleptons_M_500_10mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons500_100mm'    : "/Sleptons_M_500_100mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons500_1000mm'   : "/Sleptons_M_500_1000mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'sleptons600_0p01mm'   : "/Sleptons_M_600_0p01mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons600_0p1mm'    : "/Sleptons_M_600_0p1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons600_1mm'      : "/Sleptons_M_600_1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons600_10mm'     : "/Sleptons_M_600_10mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons600_100mm'    : "/Sleptons_M_600_100mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons600_1000mm'   : "/Sleptons_M_600_1000mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'sleptons700_0p01mm'   : "/Sleptons_M_700_0p01mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons700_0p1mm'    : "/Sleptons_M_700_0p1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons700_1mm'      : "/Sleptons_M_700_1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons700_10mm'     : "/Sleptons_M_700_10mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons700_100mm'    : "/Sleptons_M_700_100mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons700_1000mm'   : "/Sleptons_M_700_1000mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'sleptons800_0p01mm'   : "/Sleptons_M_800_0p01mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons800_0p1mm'    : "/Sleptons_M_800_0p1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons800_1mm'      : "/Sleptons_M_800_1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons800_10mm'     : "/Sleptons_M_800_10mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons800_100mm'    : "/Sleptons_M_800_100mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons800_1000mm'   : "/Sleptons_M_800_1000mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'sleptons900_0p01mm'   : "/Sleptons_M_900_0p01mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons900_0p1mm'    : "/Sleptons_M_900_0p1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons900_1mm'      : "/Sleptons_M_900_1mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons900_10mm'     : "/Sleptons_M_900_10mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons900_100mm'    : "/Sleptons_M_900_100mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'sleptons900_1000mm'   : "/Sleptons_M_900_1000mm_13TeV_2016MC/bcardwel-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",


    'staus50_0p01mm'   : "/Staus_LeptonFilter_M_50_0p01mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus50_0p1mm'    : "/Staus_LeptonFilter_M_50_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus50_1mm'      : "/Staus_LeptonFilter_M_50_1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus50_10mm'     : "/Staus_LeptonFilter_M_50_10mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus50_100mm'    : "/Staus_LeptonFilter_M_50_100mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus50_1000mm'   : "/Staus_LeptonFilter_M_50_1000mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'staus100_0p01mm'   : "/Staus_LeptonFilter_M_100_0p01mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus100_0p1mm'    : "/Staus_LeptonFilter_M_100_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus100_1mm'      : "/Staus_LeptonFilter_M_100_1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus100_10mm'     : "/Staus_LeptonFilter_M_100_10mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus100_100mm'    : "/Staus_LeptonFilter_M_100_100mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus100_1000mm'   : "/Staus_LeptonFilter_M_100_1000mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'staus200_0p01mm'   : "/Staus_LeptonFilter_M_200_0p01mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus200_0p1mm'    : "/Staus_LeptonFilter_M_200_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus200_1mm'      : "/Staus_LeptonFilter_M_200_1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus200_10mm'     : "/Staus_LeptonFilter_M_200_10mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus200_100mm'    : "/Staus_LeptonFilter_M_200_100mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus200_1000mm'   : "/Staus_LeptonFilter_M_200_1000mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'staus300_0p01mm'   : "/Staus_LeptonFilter_M_300_0p01mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus300_0p1mm'    : "/Staus_LeptonFilter_M_300_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus300_1mm'      : "/Staus_LeptonFilter_M_300_1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus300_10mm'     : "/Staus_LeptonFilter_M_300_10mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus300_100mm'    : "/Staus_LeptonFilter_M_300_100mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus300_1000mm'   : "/Staus_LeptonFilter_M_300_1000mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'staus400_0p01mm'   : "/Staus_LeptonFilter_M_400_0p01mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus400_0p1mm'    : "/Staus_LeptonFilter_M_400_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus400_1mm'      : "/Staus_LeptonFilter_M_400_1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus400_10mm'     : "/Staus_LeptonFilter_M_400_10mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus400_100mm'    : "/Staus_LeptonFilter_M_400_100mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus400_1000mm'   : "/Staus_LeptonFilter_M_400_1000mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",

    'staus500_0p01mm'   : "/Staus_LeptonFilter_M_500_0p01mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus500_0p1mm'    : "/Staus_LeptonFilter_M_500_0p1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus500_1mm'      : "/Staus_LeptonFilter_M_500_1mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus500_10mm'     : "/Staus_LeptonFilter_M_500_10mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus500_100mm'    : "/Staus_LeptonFilter_M_500_100mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",
    'staus500_1000mm'   : "/Staus_LeptonFilter_M_500_1000mm_13TeV_2016MC/jalimena-MiniAod-53f8667ba4b240d5eafd36e71bf34742/USER",


    'HToSSTo4L125_30_10000mm'     : "/ggH_HToSSTo4l_MH-125_MS-30_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L125_30_1000mm'      : "/ggH_HToSSTo4l_MH-125_MS-30_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L125_30_100mm'       : "/ggH_HToSSTo4l_MH-125_MS-30_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L125_30_10mm'        : "/ggH_HToSSTo4l_MH-125_MS-30_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L125_30_1mm'         : "/ggH_HToSSTo4l_MH-125_MS-30_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L125_50_10000mm'     : "/ggH_HToSSTo4l_MH-125_MS-50_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L125_50_1000mm'      : "/ggH_HToSSTo4l_MH-125_MS-50_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L125_50_100mm'       : "/ggH_HToSSTo4l_MH-125_MS-50_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L125_50_10mm'        : "/ggH_HToSSTo4l_MH-125_MS-50_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L125_50_1mm'         : "/ggH_HToSSTo4l_MH-125_MS-50_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L300_20_10000mm'     : "/ggH_HToSSTo4l_MH-300_MS-20_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L300_20_1000mm'      : "/ggH_HToSSTo4l_MH-300_MS-20_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L300_20_100mm'       : "/ggH_HToSSTo4l_MH-300_MS-20_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L300_20_10mm'        : "/ggH_HToSSTo4l_MH-300_MS-20_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L300_20_1mm'         : "/ggH_HToSSTo4l_MH-300_MS-20_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L300_50_10000mm'     : "/ggH_HToSSTo4l_MH-300_MS-50_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L300_50_1000mm'      : "/ggH_HToSSTo4l_MH-300_MS-50_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L300_50_100mm'       : "/ggH_HToSSTo4l_MH-300_MS-50_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L300_50_10mm'        : "/ggH_HToSSTo4l_MH-300_MS-50_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L300_50_1mm'         : "/ggH_HToSSTo4l_MH-300_MS-50_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L300_150_10000mm'    : "/ggH_HToSSTo4l_MH-300_MS-150_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L300_150_1000mm'     : "/ggH_HToSSTo4l_MH-300_MS-150_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L300_150_100mm'      : "/ggH_HToSSTo4l_MH-300_MS-150_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L300_150_10mm'       : "/ggH_HToSSTo4l_MH-300_MS-150_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L300_150_1mm'        : "/ggH_HToSSTo4l_MH-300_MS-150_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L400_50_10000mm'     : "/ggH_HToSSTo4l_MH-400_MS-50_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L400_50_1000mm'      : "/ggH_HToSSTo4l_MH-400_MS-50_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L400_50_100mm'       : "/ggH_HToSSTo4l_MH-400_MS-50_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L400_50_10mm'        : "/ggH_HToSSTo4l_MH-400_MS-50_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L400_50_1mm'         : "/ggH_HToSSTo4l_MH-400_MS-50_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L400_150_10000mm'    : "/ggH_HToSSTo4l_MH-400_MS-150_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L400_150_1000mm'     : "/ggH_HToSSTo4l_MH-400_MS-150_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L400_150_100mm'      : "/ggH_HToSSTo4l_MH-400_MS-150_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L400_150_10mm'       : "/ggH_HToSSTo4l_MH-400_MS-150_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L400_150_1mm'        : "/ggH_HToSSTo4l_MH-400_MS-150_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L600_50_10000mm'     : "/ggH_HToSSTo4l_MH-600_MS-50_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L600_50_1000mm'      : "/ggH_HToSSTo4l_MH-600_MS-50_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L600_50_100mm'       : "/ggH_HToSSTo4l_MH-600_MS-50_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L600_50_10mm'        : "/ggH_HToSSTo4l_MH-600_MS-50_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L600_50_1mm'         : "/ggH_HToSSTo4l_MH-600_MS-50_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L600_150_10000mm'    : "/ggH_HToSSTo4l_MH-600_MS-150_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L600_150_1000mm'     : "/ggH_HToSSTo4l_MH-600_MS-150_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L600_150_100mm'      : "/ggH_HToSSTo4l_MH-600_MS-150_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L600_150_10mm'       : "/ggH_HToSSTo4l_MH-600_MS-150_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L600_150_1mm'        : "/ggH_HToSSTo4l_MH-600_MS-150_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L800_50_10000mm'     : "/ggH_HToSSTo4l_MH-800_MS-50_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L800_50_1000mm'      : "/ggH_HToSSTo4l_MH-800_MS-50_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L800_50_100mm'       : "/ggH_HToSSTo4l_MH-800_MS-50_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L800_50_10mm'        : "/ggH_HToSSTo4l_MH-800_MS-50_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L800_50_1mm'         : "/ggH_HToSSTo4l_MH-800_MS-50_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L800_150_10000mm'    : "/ggH_HToSSTo4l_MH-800_MS-150_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L800_150_1000mm'     : "/ggH_HToSSTo4l_MH-800_MS-150_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L800_150_100mm'      : "/ggH_HToSSTo4l_MH-800_MS-150_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L800_150_10mm'       : "/ggH_HToSSTo4l_MH-800_MS-150_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L800_150_1mm'        : "/ggH_HToSSTo4l_MH-800_MS-150_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L800_250_10000mm'    : "/ggH_HToSSTo4l_MH-800_MS-250_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L800_250_1000mm'     : "/ggH_HToSSTo4l_MH-800_MS-250_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L800_250_100mm'      : "/ggH_HToSSTo4l_MH-800_MS-250_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L800_250_10mm'       : "/ggH_HToSSTo4l_MH-800_MS-250_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L800_250_1mm'        : "/ggH_HToSSTo4l_MH-800_MS-250_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L1000_30_10000mm'    : "/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L1000_30_1000mm'     : "/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L1000_30_100mm'      : "/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L1000_30_10mm'       : "/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L1000_30_1mm'        : "/ggH_HToSSTo4l_MH-1000_MS-30_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L1000_150_10000mm'   : "/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L1000_150_1000mm'    : "/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L1000_150_100mm'     : "/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L1000_150_10mm'      : "/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L1000_150_1mm'       : "/ggH_HToSSTo4l_MH-1000_MS-150_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",

    'HToSSTo4L1000_350_10000mm'   : "/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-10000_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L1000_350_1000mm'    : "/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-1000_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L1000_350_100mm'     : "/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-100_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L1000_350_10mm'      : "/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-10_TuneCUEP8M1_13TeV-powheg-pythia8-v2/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",
    'HToSSTo4L1000_350_1mm'       : "/ggH_HToSSTo4l_MH-1000_MS-350_ctauS-1_TuneCUEP8M1_13TeV-powheg-pythia8/jalimena-MiniAod_4muOr4eGenFilter_2016-6e1874bd67587cdee6a49868d75e88be/USER",


}

# create composite dictionary of all samples
dataset_names = {}
dataset_names.update(bg_mc_samples)
dataset_names.update(data_samples)
dataset_names.update(signal_mc_samples)

########################################################################################
### code to propagate displaced SUSY sample names to the lifetime-reweighted samples ###
########################################################################################

def renameReweightedSamples(dataset_names):
    from OSUT3Analysis.Configuration.configurationOptions import signal_datasets, rulesForLifetimeReweighting

    for sample in signal_datasets:
        base_name = sample[:sample.find('_')]
        src_ctau = 10*rulesForLifetimeReweighting[sample][0].srcCTaus[0]
        src_ctau = "{:g}".format(src_ctau).replace('.','p')
        dataset_names[sample] = dataset_names["{}_{}mm".format(base_name, src_ctau)]

# Propagate displaced SUSY sample names to the lifetime-reweighted samples
renameReweightedSamples(dataset_names)
