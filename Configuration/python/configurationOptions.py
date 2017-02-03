#!/usr/bin/env python

config_file = "standardConfig_cfg.py"


intLumi = 36773 #2016 final rereco

datasets = [

   #data

   'SingleMu_2016',
   'SingleMu_2016B',
   'SingleMu_2016C',
   'SingleMu_2016D',
   'SingleMu_2016E',
   'SingleMu_2016F',
   'SingleMu_2016G',
   'SingleMu_2016H',

   'SingleEle_2016',
   'SingleEle_2016B',
   'SingleEle_2016C',
   'SingleEle_2016D',
   'SingleEle_2016E',
   'SingleEle_2016F',
   'SingleEle_2016G',
   'SingleEle_2016H',

   'DoubleMu_2016',
   'DoubleMu_2016B',
   'DoubleMu_2016C',
   'DoubleMu_2016D',
   'DoubleMu_2016E',
   'DoubleMu_2016F',
   'DoubleMu_2016G',
   'DoubleMu_2016H',

   'DoubleEG_2016',
   'DoubleEG_2016B',
   'DoubleEG_2016C',
   'DoubleEG_2016D',
   'DoubleEG_2016E',
   'DoubleEG_2016F',
   'DoubleEG_2016G',
   'DoubleEG_2016H',

   'MuonEG_2016',
   'MuonEG_2016B',
   'MuonEG_2016C',
   'MuonEG_2016D',
   'MuonEG_2016E',
   'MuonEG_2016F',
   'MuonEG_2016G',
   'MuonEG_2016H',

   # background MC

   'DYJetsToLL',
   'WJetsToLNu',
   'TTJets_Lept',
   'Diboson',
   'QCD_MuEnriched',
   'QCD_EMEnriched',
   'QCD_bcToE',

   #Sum of all backgrounds
   'Background',
]

composite_dataset_definitions = {
    'DYJetsToLL' : [
        'DYJetsToLL_50',
        'DYJetsToLL_10to50',
    ],
    'Diboson' : [
        # WW
        'WWToLNuLNu',
        'WWToLNuQQ',
        # WZ
        'WZToLNu2QorQQ2L',
        'WZToLNuNuNu',
        'WZToLLLNu',
        # ZZ
        'ZZToNuNuQQ',
        'ZZToLLQQ',
        'ZZToLLNuNu',
        'ZZToLLLL',
        # Vgamma
        'WG',
        'ZG',
    ],
    'SingleTop' : [
        'SingleTop_s_channel',
        'SingleTop_t_channel_top',
        'SingleTop_t_channel_antitop',
        'SingleTop_tW',
        'SingleTop_tbarW',
    ],
    'TTJets_Lept' : [
        'TTJets_DiLept',
        'TTJets_SingleLeptFromT',
        'TTJets_SingleLeptFromTbar',
    ],
    'QCD_MuEnriched' : [
        'QCD_MuEnriched_15to20',
        'QCD_MuEnriched_20to30',
        'QCD_MuEnriched_30to50',
        'QCD_MuEnriched_50to80',
        'QCD_MuEnriched_80to120',
        'QCD_MuEnriched_120to170',
        'QCD_MuEnriched_170to300',
        'QCD_MuEnriched_300to470',
        'QCD_MuEnriched_470to600',
        'QCD_MuEnriched_600to800',
        'QCD_MuEnriched_800to1000',
        'QCD_MuEnriched_1000toInf',
    ],
    'QCD_EMEnriched' : [
        'QCD_EMEnriched_20to30',
        'QCD_EMEnriched_30to50',
        'QCD_EMEnriched_50to80',
        'QCD_EMEnriched_80to120',
#        'QCD_EMEnriched_120to170',  # Moriond17 sample doesn't exist yet
        'QCD_EMEnriched_170to300',
        'QCD_EMEnriched_300toInf',
    ],
    'QCD_bcToE' : [
        'QCD_bcToE_20to30',
        'QCD_bcToE_30to80',
#        'QCD_bcToE_80to170',  # Moriond17 sample doesn't exist yet
        'QCD_bcToE_170to250',
        'QCD_bcToE_250toInf',
    ],

    'SingleMu_2016' : [
        'SingleMu_2016B',
        'SingleMu_2016C',
        'SingleMu_2016D',
        'SingleMu_2016E',
        'SingleMu_2016F',
        'SingleMu_2016G',
        'SingleMu_2016H',
    ],
    'SingleEle_2016' : [
        'SingleEle_2016B',
        'SingleEle_2016C',
        'SingleEle_2016D',
        'SingleEle_2016E',
        'SingleEle_2016F',
        'SingleEle_2016G',
        'SingleEle_2016H',
    ],
    'DoubleMu_2016' : [
        'DoubleMu_2016B',
        'DoubleMu_2016C',
        'DoubleMu_2016D',
        'DoubleMu_2016E',
        'DoubleMu_2016F',
        'DoubleMu_2016G',
        'DoubleMu_2016H',
    ],
    'DoubleEG_2016' : [
        'DoubleEG_2016B',
        'DoubleEG_2016C',
        'DoubleEG_2016D',
        'DoubleEG_2016E',
        'DoubleEG_2016F',
        'DoubleEG_2016G',
        'DoubleEG_2016H',
    ],
    'MuonEG_2016' : [
        'MuonEG_2016B',
        'MuonEG_2016C',
        'MuonEG_2016D',
        'MuonEG_2016E',
        'MuonEG_2016F',
        'MuonEG_2016G',
        'MuonEG_2016H',
    ],
}


############################################################################################################
#########  DATASET-SPECIFIC OPTIONS  ########################################################################
############################################################################################################

#### NOTE: dataset_names dictionary has been moved outside this file, please import the desired list separately


nJobs = {
    ############################################################################
    # set number of jobs to correpond to roughly 50k events/job


    #DY
    'DYJetsToLL_50'  :  999,
    'DYJetsToLL_10to50'    : 999,

    #WJets
    'WJetsToLNu'  : 999,

    #WW
    'WWToLNuQQ'   : 999,
    'WWToLNuLNu'  : 999,

    #WZ
    'WZToLNuNuNu'     : 999,
    'WZToLLLNu'       : 999,
    'WZToLNu2QorQQ2L' : 999,

    #ZZ
    'ZZToNuNuQQ'  : 999,
    'ZZToLLQQ'    : 999,
    'ZZToLLNuNu'  : 999,
    'ZZToLLLL'    : 999,

    #VG
    'WG'  : 999,
    'ZG'  : 999,

    #SingleTop
    'SingleTop_s_channel'           : 999,
    'SingleTop_t_channel'           : 999,
    'SingleTop_t_channel_top'       : 999,
    'SingleTop_t_channel_antitop'   : 999,
    'SingleTop_tW'                  : 999,
    'SingleTop_tbarW'               : 999,

    #TTJet s
    'TTJets_DiLept'                 : 300,
    'TTJets_SingleLeptFromT'        : 300,
    'TTJets_SingleLeptFromTbar'     : 300,

    #QCD MuEnriched
    'QCD_MuEnriched_15to20'         : 999,
    'QCD_MuEnriched_20to30'         : 999,
    'QCD_MuEnriched_30to50'         : 999,
    'QCD_MuEnriched_50to80'         : 999,
    'QCD_MuEnriched_80to120'        : 999,
    'QCD_MuEnriched_120to170'       : 999,
    'QCD_MuEnriched_170to300'       : 999,
    'QCD_MuEnriched_300to470'       : 999,
    'QCD_MuEnriched_470to600'       : 999,
    'QCD_MuEnriched_600to800'       : 999,
    'QCD_MuEnriched_800to1000'      : 999,
    'QCD_MuEnriched_1000toInf'      : 999,

    #QCD EMEnriched
    'QCD_EMEnriched_15to20'         : 69,
    'QCD_EMEnriched_20to30'         : 261,
    'QCD_EMEnriched_30to50'         : 135,
    'QCD_EMEnriched_50to80'         : 145,
    'QCD_EMEnriched_80to120'        : 201,
    'QCD_EMEnriched_120to170'       : 233,
    'QCD_EMEnriched_170to300'       : 130,
    'QCD_EMEnriched_300toInf'       : 114,

    #QCD bcToE
    'QCD_bcToE_15to20'              : 21,
    'QCD_bcToE_20to30'              : 123,
    'QCD_bcToE_30to80'              : 129,
    'QCD_bcToE_80to170'             : 153,
    'QCD_bcToE_170to250'            : 98,
    'QCD_bcToE_250toInf'            : 99,

    'SingleMu_2016B'  : 1000,
    'SingleMu_2016C'  : 1000,
    'SingleMu_2016D'  : 1000,
    'SingleMu_2016E'  : 1000,
    'SingleMu_2016F'  : 1000,
    'SingleMu_2016G'  : 1000,
    'SingleMu_2016H'  : 1000,

    'SingleEle_2016B' : 1000,
    'SingleEle_2016C' : 1000,
    'SingleEle_2016D' : 1000,
    'SingleEle_2016E' : 1000,
    'SingleEle_2016F' : 1000,
    'SingleEle_2016G' : 1000,
    'SingleEle_2016H' : 1000,

    'DoubleMu_2016B'  : 1000,
    'DoubleMu_2016C'  : 1000,
    'DoubleMu_2016D'  : 1000,
    'DoubleMu_2016E'  : 1000,
    'DoubleMu_2016F'  : 1000,
    'DoubleMu_2016G'  : 1000,

    'DoubleEG_2016B'  : 1000,
    'DoubleEG_2016C'  : 1000,
    'DoubleEG_2016D'  : 1000,
    'DoubleEG_2016E'  : 1000,
    'DoubleEG_2016F'  : 1000,
    'DoubleEG_2016G'  : 1000,
    'DoubleEG_2016H'  : 1000,

    'DoubleMu_2016B'  : 1000,
    'DoubleMu_2016C'  : 1000,
    'DoubleMu_2016D'  : 1000,
    'DoubleMu_2016E'  : 1000,
    'DoubleMu_2016F'  : 1000,
    'DoubleMu_2016G'  : 1000,
    'DoubleMu_2016H'  : 1000,

    'MuonEG_2016B'    : 1000,
    'MuonEG_2016C'    : 1000,
    'MuonEG_2016D'    : 1000,
    'MuonEG_2016E'    : 1000,
    'MuonEG_2016F'    : 1000,
    'MuonEG_2016G'    : 1000,
    'MuonEG_2016H'    : 1000,

    ############################################################################


}

maxEvents = {
    ############################################################################
    #MiniAOD stored on T3.
    ############################################################################
    #DY
    'DYJetsToLL_50'  :  -1,
    'DYJetsToLL_10to50'        : -1,

    #WJets
    'WJetsToLNu'  :  -1,

    #WW
    'WWToLNuQQ'   :  -1,
    'WWToLNuLNu'  :  -1,

    #WZ
    'WZToLNuNuNu'  :  -1,
    'WZToLLLNu'    :  -1,
    'WZToLNu2QorQQ2L' : -1,
    #ZZ
    'ZZToNuNuQQ'  :  -1,
    'ZZToLLQQ'    :  -1,
    'ZZToLLNuNu'  :  -1,
    'ZZToLLLL'    :  -1,

    #VG
    'WG'  :  -1,
    'ZG'  :  -1,

    #SingleTop
    'SingleTop_s_channel'          :  -1,
    'SingleTop_t_channel'          :  -1,
    'SingleTop_t_channel_top'      :  -1,
    'SingleTop_t_channel_antitop'  :  -1,
    'SingleTop_tW'                 :  -1,
    'SingleTop_tbarW'              :  -1,

    #TTJets
    'TTJets_DiLept'              :  -1,
    'TTJets_SingleLeptFromT'     :  -1,
    'TTJets_SingleLeptFromTbar'  :  -1,

    #QCD MuEnriched
    'QCD_MuEnriched_15to20'         : -1,
    'QCD_MuEnriched_20to30'         : -1,
    'QCD_MuEnriched_30to50'         : -1,
    'QCD_MuEnriched_50to80'         : -1,
    'QCD_MuEnriched_80to120'        : -1,
    'QCD_MuEnriched_120to170'       : -1,
    'QCD_MuEnriched_170to300'       : -1,
    'QCD_MuEnriched_300to470'       : -1,
    'QCD_MuEnriched_470to600'       : -1,
    'QCD_MuEnriched_600to800'       : -1,
    'QCD_MuEnriched_800to1000'      : -1,
    'QCD_MuEnriched_1000toInf'      : -1,

    #QCD EMEnriched
    'QCD_EMEnriched_15to20'         : -1,
    'QCD_EMEnriched_20to30'         : -1,
    'QCD_EMEnriched_30to50'         : -1,
    'QCD_EMEnriched_50to80'         : -1,
    'QCD_EMEnriched_80to120'        : -1,
    'QCD_EMEnriched_120to170'       : -1,
    'QCD_EMEnriched_170to300'       : -1,
    'QCD_EMEnriched_300toInf'       : -1,

    #QCD bcToE
    'QCD_bcToE_15to20'              : -1,
    'QCD_bcToE_20to30'              : -1,
    'QCD_bcToE_30to80'              : -1,
    'QCD_bcToE_80to170'             : -1,
    'QCD_bcToE_170to250'            : -1,
    'QCD_bcToE_250toInf'            : -1,

    'DoubleMu_2016B' : -1,
    'DoubleMu_2016C' : -1,
    'DoubleMu_2016D' : -1,
    'DoubleMu_2016E' : -1,
    'DoubleMu_2016F' : -1,
    'DoubleMu_2016G' : -1,

    'SingleMu_2016B'       : -1,
    'SingleMu_2016C'       : -1,
    'SingleMu_2016D'       : -1,
    'SingleMu_2016E'       : -1,
    'SingleMu_2016F'       : -1,
    'SingleMu_2016G'       : -1,
    'SingleMu_2016H'       : -1,
    'SingleMu_2016'        : -1,

    'SingleEle_2016B'       : -1,
    'SingleEle_2016C'       : -1,
    'SingleEle_2016D'       : -1,
    'SingleEle_2016E'       : -1,
    'SingleEle_2016F'       : -1,
    'SingleEle_2016G'       : -1,
    'SingleEle_2016H'       : -1,
    'SingleEle_2016'        : -1,

    'DoubleEG_2016B'     : -1,
    'DoubleEG_2016C'     : -1,
    'DoubleEG_2016D'     : -1,
    'DoubleEG_2016E'     : -1,
    'DoubleEG_2016F'     : -1,
    'DoubleEG_2016G'     : -1,
    'DoubleEG_2016H'     : -1,

    'DoubleMu_2016B'     : -1,
    'DoubleMu_2016C'     : -1,
    'DoubleMu_2016D'     : -1,
    'DoubleMu_2016E'     : -1,
    'DoubleMu_2016F'     : -1,
    'DoubleMu_2016G'     : -1,
    'DoubleMu_2016H'     : -1,

    'MuonEG_2016B'     : -1,
    'MuonEG_2016C'     : -1,
    'MuonEG_2016D'     : -1,
    'MuonEG_2016E'     : -1,
    'MuonEG_2016F'     : -1,
    'MuonEG_2016G'     : -1,
    'MuonEG_2016H'     : -1,

    ############################################################################

}

# bgMC => background MC process
# signalMC => signal MC process
# data => data
types = {
    ############################################################################
    #MiniAOD stored on T3.
    ############################################################################
    #DY
    'DYJetsToLL'  :  "bgMC",
    'DYJetsToLL_50'  :  "bgMC",
    'DYJetsToLL_10to50'      : "bgMC",

    #WJets
    'WJetsToLNu'  :  "bgMC",

    'Diboson'                : "bgMC",

    #WW
    'WWToLNuQQ'   :  "bgMC",
    'WWToLNuLNu'  :  "bgMC",

    #WZ
    'WZToLNuNuNu'  :  "bgMC",
    'WZToLLLNu'    :  "bgMC",
    'WZToLNu2QorQQ2L'    :  "bgMC",

    #ZZ
    'ZZToNuNuQQ'  :  "bgMC",
    'ZZToLLQQ'    :  "bgMC",
    'ZZToLLNuNu'  :  "bgMC",
    'ZZToLLLL'    :  "bgMC",

    #VG
    'WG'  :  "bgMC",
    'ZG'  :  "bgMC",

    #SingleTop
    'SingleTop'                    :  "bgMC",
    'SingleTop_s_channel'          :  "bgMC",
    'SingleTop_t_channel'          :  "bgMC",
    'SingleTop_t_channel_top'      :  "bgMC",
    'SingleTop_t_channel_antitop'  :  "bgMC",
    'SingleTop_tW'                 :  "bgMC",
    'SingleTop_tbarW'              :  "bgMC",

    #TTJets
    'TTJets_Lept'                :  "bgMC",
    'TTJets_DiLept'              :  "bgMC",
    'TTJets_SingleLeptFromT'     :  "bgMC",
    'TTJets_SingleLeptFromTbar'  :  "bgMC",

    ############################################################################

    #QCD MuEnriched
    'QCD_MuEnriched'                : "bgMC",
    'QCD_MuEnriched_15to20'         : "bgMC",
    'QCD_MuEnriched_20to30'         : "bgMC",
    'QCD_MuEnriched_30to50'         : "bgMC",
    'QCD_MuEnriched_50to80'         : "bgMC",
    'QCD_MuEnriched_80to120'        : "bgMC",
    'QCD_MuEnriched_120to170'       : "bgMC",
    'QCD_MuEnriched_170to300'       : "bgMC",
    'QCD_MuEnriched_300to470'       : "bgMC",
    'QCD_MuEnriched_470to600'       : "bgMC",
    'QCD_MuEnriched_600to800'       : "bgMC",
    'QCD_MuEnriched_800to1000'      : "bgMC",
    'QCD_MuEnriched_1000toInf'      : "bgMC",

    #QCD EMEnriched
    'QCD_EMEnriched'                : "bgMC",
    'QCD_EMEnriched_15to20'         : "bgMC",
    'QCD_EMEnriched_20to30'         : "bgMC",
    'QCD_EMEnriched_30to50'         : "bgMC",
    'QCD_EMEnriched_50to80'         : "bgMC",
    'QCD_EMEnriched_80to120'        : "bgMC",
    'QCD_EMEnriched_120to170'       : "bgMC",
    'QCD_EMEnriched_170to300'       : "bgMC",
    'QCD_EMEnriched_300toInf'       : "bgMC",

    #QCD bcToE
    'QCD_bcToE'                     : "bgMC",
    'QCD_bcToE_15to20'              : "bgMC",
    'QCD_bcToE_20to30'              : "bgMC",
    'QCD_bcToE_30to80'              : "bgMC",
    'QCD_bcToE_80to170'             : "bgMC",
    'QCD_bcToE_170to250'            : "bgMC",
    'QCD_bcToE_250toInf'            : "bgMC",

    'QCDFromData' : "bgMC",

    'DoubleMu_2016'    : "data",
    'DoubleMu_2016B'   : "data",
    'DoubleMu_2016C'   : "data",
    'DoubleMu_2016D'   : "data",
    'DoubleMu_2016E'   : "data",
    'DoubleMu_2016F'   : "data",
    'DoubleMu_2016G'   : "data",
    'DoubleMu_2016H'   : "data",

    'SingleMu_2016'     : "data",
    'SingleMu_2016B'    : "data",
    'SingleMu_2016C'    : "data",
    'SingleMu_2016D'    : "data",
    'SingleMu_2016E'    : "data",
    'SingleMu_2016F'    : "data",
    'SingleMu_2016G'    : "data",
    'SingleMu_2016H'    : "data",


    'SingleEle_2016'    : "data",
    'SingleEle_2016B'   : "data",
    'SingleEle_2016C'   : "data",
    'SingleEle_2016D'   : "data",
    'SingleEle_2016E'   : "data",
    'SingleEle_2016F'   : "data",
    'SingleEle_2016G'   : "data",
    'SingleEle_2016H'   : "data",

    'DoubleEG_2016'    : "data",
    'DoubleEG_2016B'   : "data",
    'DoubleEG_2016C'   : "data",
    'DoubleEG_2016D'   : "data",
    'DoubleEG_2016E'   : "data",
    'DoubleEG_2016F'   : "data",
    'DoubleEG_2016G'   : "data",
    'DoubleEG_2016H'   : "data",

    'MuonEG_2016'    : "data",
    'MuonEG_2016B'   : "data",
    'MuonEG_2016C'   : "data",
    'MuonEG_2016D'   : "data",
    'MuonEG_2016E'   : "data",
    'MuonEG_2016F'   : "data",
    'MuonEG_2016G'   : "data",
    'MuonEG_2016H'   : "data",

    ###########################################################################

}

colors = {
    ############################################################################
    #MiniAOD stored on T3.
    ############################################################################
    #DY
    'DYJetsToLL'          : 410,
    'DYJetsToLL_10to50'   : 409,
    'DYJetsToLL_50'  :  411,

    #WJets
    'WJetsToLNu'             :  852,

    'Diboson'             : 393,

    #WW
    'WWToLNuQQ'   :  390,
    'WWToLNuLNu'  :  390,

    #WZ
    'WZToLNuNuNu'  :  393,
    'WZToLLLNu'    :  393,
    'WZToLNu2QorQQ2L'    :  393,

    #ZZ
    'ZZToNuNuQQ'  :  397,
    'ZZToLLQQ'    :  397,
    'ZZToLLNuNu'  :  397,
    'ZZToLLLL'    :  397,

    #VG
    'WG'  :  399,
    'ZG'  :  398,

    #SingleTop
    'SingleTop'                    :  607,
    'SingleTop_s_channel'          :  905,
    'SingleTop_t_channel'          :  907,
    'SingleTop_t_channel_top'      :  907,
    'SingleTop_t_channel_antitop'  :  908,
    'SingleTop_tW'                 :  909,
    'SingleTop_tbarW'              :  910,

    #TTJets
    'TTJets_Lept'                :  872,
    'TTJets_DiLept'              :  873,
    'TTJets_SingleLeptFromT'     :  874,
    'TTJets_SingleLeptFromTbar'  :  875,

    #QCD MuEnriched
    'QCD_MuEnriched'                : 623,
    'QCD_MuEnriched_15to20'         : 623,
    'QCD_MuEnriched_20to30'         : 623,
    'QCD_MuEnriched_30to50'         : 623,
    'QCD_MuEnriched_50to80'         : 623,
    'QCD_MuEnriched_80to120'        : 623,
    'QCD_MuEnriched_120to170'       : 623,
    'QCD_MuEnriched_170to300'       : 623,
    'QCD_MuEnriched_300to470'       : 623,
    'QCD_MuEnriched_470to600'       : 623,
    'QCD_MuEnriched_600to800'       : 623,
    'QCD_MuEnriched_800to1000'      : 623,
    'QCD_MuEnriched_1000toInf'      : 623,

    #QCD EMEnriched
    'QCD_EMEnriched'                : 791,
    'QCD_EMEnriched_15to20'         : 791,
    'QCD_EMEnriched_20to30'         : 791,
    'QCD_EMEnriched_30to50'         : 791,
    'QCD_EMEnriched_50to80'         : 791,
    'QCD_EMEnriched_80to120'        : 791,
    'QCD_EMEnriched_120to170'       : 791,
    'QCD_EMEnriched_170to300'       : 791,
    'QCD_EMEnriched_300toInf'       : 791,

    #QCD bcToE
    'QCD_bcToE'                     : 794,
    'QCD_bcToE_15to20'              : 794,
    'QCD_bcToE_20to30'              : 794,
    'QCD_bcToE_30to80'              : 794,
    'QCD_bcToE_80to170'             : 794,
    'QCD_bcToE_170to250'            : 794,
    'QCD_bcToE_250toInf'            : 794,

    'QCDFromData' : 791,

    'DoubleMu_2016'         : 1,
    'DoubleMu_2016B'        : 1,
    'DoubleMu_2016C'        : 1,
    'DoubleMu_2016D'        : 1,
    'DoubleMu_2016E'        : 1,
    'DoubleMu_2016F'        : 1,
    'DoubleMu_2016G'        : 1,
    'DoubleMu_2016H'        : 1,

    'SingleMu_2016'    : 1,
    'SingleMu_2016B'   : 1,
    'SingleMu_2016C'   : 1,
    'SingleMu_2016D'   : 1,
    'SingleMu_2016E'   : 1,
    'SingleMu_2016F'   : 1,
    'SingleMu_2016G'   : 1,
    'SingleMu_2016H'   : 1,


    'SingleEle_2016'    : 1,
    'SingleEle_2016B'   : 1,
    'SingleEle_2016C'   : 1,
    'SingleEle_2016D'   : 1,
    'SingleEle_2016E'   : 1,
    'SingleEle_2016F'   : 1,
    'SingleEle_2016G'   : 1,
    'SingleEle_2016H'   : 1,

    'DoubleEG_2016'    : 1,
    'DoubleEG_2016B'   : 1,
    'DoubleEG_2016C'   : 1,
    'DoubleEG_2016D'   : 1,
    'DoubleEG_2016E'   : 1,
    'DoubleEG_2016F'   : 1,
    'DoubleEG_2016G'   : 1,
    'DoubleEG_2016H'    : 1,

    'MuonEG_2016'    : 1,
    'MuonEG_2016B'   : 1,
    'MuonEG_2016C'   : 1,
    'MuonEG_2016D'   : 1,
    'MuonEG_2016E'   : 1,
    'MuonEG_2016F'   : 1,
    'MuonEG_2016G'   : 1,
    'MuonEG_2016H'   : 1,


    ###########################################################################

}

labels = {
    ############################################################################
    #MiniAOD stored on T3.
    ############################################################################
    #DY
    'DYJetsToLL'     :  "Z#rightarrowl^{+}l^{-}",
    'DYJetsToLL_50'  :  "Z#rightarrowl^{+}l^{-} M(50+)",
    'DYJetsToLL_10to50'     :  "Z#rightarrowl^{+}l^{-} M(10-50)",

    #WJets
    'WJetsToLNu'            :  "W#rightarrowl#nu",

    'Diboson'                   : "diboson",

    #WW
    'WWToLNuQQ'   :  "WW#rightarrowl#nuqq",
    'WWToLNuLNu'  :  "WW#rightarrowl#nul#nu",

    #WZ
    'WZToLNuNuNu'  :  "WZ#rightarrowl#nu#nu#nu",
    'WZToLLLNu'    :  "WZ#rightarrowl#null",
    'WZToLNu2QorQQ2L'    :  "WZ#rightarrowqqll/l#nuqq",

    #ZZ
    'ZZToNuNuQQ'  :  "ZZ#rightarrow#nu#nuqq",
    'ZZToLLQQ'    :  "ZZ#rightarrowllqq",
    'ZZToLLNuNu'  :  "ZZ#rightarrowll#nu#nu",
    'ZZToLLLL'    :  "ZZ#rightarrowllll",

    #VG
    'WG'  :  "W#gamma#rightarrowl#nu#gamma",
    'ZG'  :  "Z#gamma#rightarrowll#gamma",

    #SingleTop
    'SingleTop'                    :  "Single top",
    'SingleTop_s_channel'          :  "Single top (s-channel)",
    'SingleTop_t_channel'          :  "Single top (t-channel)",
    'SingleTop_t_channel_top'      :  "Single top(top) (t-channel)",
    'SingleTop_t_channel_antitop'  :  "Single top(antitop) (t-channel)",
    'SingleTop_tW'                 :  "Single top (tW)",
    'SingleTop_tbarW'              :  "Single top (#bar{t}W)",

    #TTJets
    'TTJets_Lept'                :  "t#bar{t}",
    'TTJets_DiLept'              :  "t#bar{t} (fully leptonic)",
    'TTJets_SingleLeptFromT'     :  "t#bar{t} (single lepton from t)",
    'TTJets_SingleLeptFromTbar'  :  "t#bar{t} (single lepton from #bar{t})",

    #QCD MuEnriched
    'QCD_MuEnriched'                : "QCD MuEnriched",
    'QCD_MuEnriched_15to20'         : "QCD MuEnriched Pt 15-20",
    'QCD_MuEnriched_20to30'         : "QCD MuEnriched Pt 20-30",
    'QCD_MuEnriched_30to50'         : "QCD MuEnriched Pt 30-50",
    'QCD_MuEnriched_50to80'         : "QCD MuEnriched Pt 50-80",
    'QCD_MuEnriched_80to120'        : "QCD MuEnriched Pt 80-120",
    'QCD_MuEnriched_120to170'       : "QCD MuEnriched Pt 120-170",
    'QCD_MuEnriched_170to300'       : "QCD MuEnriched Pt 170-300",
    'QCD_MuEnriched_300to470'       : "QCD MuEnriched Pt 300-470",
    'QCD_MuEnriched_470to600'       : "QCD MuEnriched Pt 470-600",
    'QCD_MuEnriched_600to800'       : "QCD MuEnriched Pt 600-800",
    'QCD_MuEnriched_800to1000'      : "QCD MuEnriched Pt 800-1000",
    'QCD_MuEnriched_1000toInf'      : "QCD MuEnriched Pt 1000-Inf",

    #QCD EMEnriched
    'QCD_EMEnriched'                : "QCD EMEnriched",
    'QCD_EMEnriched_15to20'         : "QCD EMEnriched Pt 15-20",
    'QCD_EMEnriched_20to30'         : "QCD EMEnriched Pt 20-30",
    'QCD_EMEnriched_30to50'         : "QCD EMEnriched Pt 30-50",
    'QCD_EMEnriched_50to80'         : "QCD EMEnriched Pt 50-80",
    'QCD_EMEnriched_80to120'        : "QCD EMEnriched Pt 80-120",
    'QCD_EMEnriched_120to170'       : "QCD EMEnriched Pt 120-170",
    'QCD_EMEnriched_170to300'       : "QCD EMEnriched Pt 170-300",
    'QCD_EMEnriched_300toInf'       : "QCD EMEnriched Pt 300-Inf",

    #QCD bcToE
    'QCD_bcToE'                     : "QCD bcToE",
    'QCD_bcToE_15to20'              : "QCD bcToE Pt 15-20",
    'QCD_bcToE_20to30'              : "QCD bcToE Pt 20-30",
    'QCD_bcToE_30to80'              : "QCD bcToE Pt 30-80",
    'QCD_bcToE_80to170'             : "QCD bcToE Pt 80-170",
    'QCD_bcToE_170to250'            : "QCD bcToE Pt 170-250",
    'QCD_bcToE_250toInf'            : "QCD bcToE Pt 250-Inf",

    'QCDFromData'     : "data-driven QCD",

    'DoubleMu_2016'   : "Double Muon data",
    'DoubleMu_2016B'  : "DoubleMu 2016B data",
    'DoubleMu_2016C'  : "DoubleMu 2016C data",
    'DoubleMu_2016D'  : "DoubleMu 2016D data",
    'DoubleMu_2016E'  : "DoubleMu 2016E data",
    'DoubleMu_2016F'  : "DoubleMu 2016F data",
    'DoubleMu_2016G'  : "DoubleMu 2016G data",
    'DoubleMu_2016H'  : "DoubleMu 2016H data",

    'SingleMu_2016'      : "Single Muon data",
    'SingleMu_2016B'     : "SingleMuon 2016B data",
    'SingleMu_2016C'     : "SingleMuon 2016C data",
    'SingleMu_2016D'     : "SingleMuon 2016D data",
    'SingleMu_2016E'     : "SingleMuon 2016E data",
    'SingleMu_2016F'     : "SingleMuon 2016F data",
    'SingleMu_2016G'     : "SingleMuon 2016G data",
    'SingleMu_2016H'     : "SingleMuon 2016H data",

    'SingleEle_2016'      : "Single Electron data",
    'SingleEle_2016B'     : "SingleElectron 2016B data",
    'SingleEle_2016C'     : "SingleElectron 2016C data",
    'SingleEle_2016D'     : "SingleElectron 2016D data",
    'SingleEle_2016E'     : "SingleElectron 2016E data",
    'SingleEle_2016F'     : "SingleElectron 2016F data",
    'SingleEle_2016G'     : "SingleElectron 2016G data",
    'SingleEle_2016H'     : "SingleElectron 2016H data",

    'DoubleEG_2016'     : "Double Electron data",
    'DoubleEG_2016B'    : "DoubleEG 2016B data",
    'DoubleEG_2016C'    : "DoubleEG 2016C data",
    'DoubleEG_2016D'    : "DoubleEG 2016D data",
    'DoubleEG_2016E'    : "DoubleEG 2016E data",
    'DoubleEG_2016F'    : "DoubleEG 2016F data",
    'DoubleEG_2016G'    : "DoubleEG 2016G data",
    'DoubleEG_2016H'    : "DoubleEG 2016H data",

    'MuonEG_2016'      : "Electron Muon data",
    'MuonEG_2016B'     : "MuonEG 2016B data",
    'MuonEG_2016C'     : "MuonEG 2016C data",
    'MuonEG_2016D'     : "MuonEG 2016D data",
    'MuonEG_2016E'     : "MuonEG 2016E data",
    'MuonEG_2016F'     : "MuonEG 2016F data",
    'MuonEG_2016G'     : "MuonEG 2016G data",
    'MuonEG_2016H'     : "MuonEG 2016H data",

    ###########################################################################


}

crossSections = {

    # taken from here: https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns

    'DYJetsToLL_10to50'        : 18610.0,
    'DYJetsToLL_50'            : 5765.4,
    'WJetsToLNu'               : 61526.7,

    'WWToLNuQQ'   :  49.997,
    'WWToLNuLNu'  :  12.178,
    'WZToLNuNuNu' :  3.03,
    'WZToLLLNu'   :  4.42965,
    'WZToLNu2QorQQ2L'  :  9.82423165827, # ???
    'ZZToNuNuQQ'  :  4.04,
    'ZZToLLQQ'    :  3.22,
    'ZZToLLNuNu'  :  0.5644,
    'ZZToLLLL'    :  1.256,
    'WG'  :  405.271,
    'ZG'  :  117.864,

    'SingleTop_s_channel'          :  3.36,
    'SingleTop_t_channel_top'      :  44.3151,
    'SingleTop_t_channel_antitop'  :  26.3734,
    'SingleTop_tW'                 :  35.85, # ???
    'SingleTop_tbarW'              :  35.85, # ???

    'TTJets_DiLept'                :  87.31, # ??? 
    'TTJets_SingleLeptFromT'       :  182.7, # ???
    'TTJets_SingleLeptFromTbar'    :  182.7, # ???

    ###########################################################################

    'QCD_MuEnriched_15to20'    :  1273190000.0*0.003,
    'QCD_MuEnriched_20to30'    :   558528000.0*0.0053,
    'QCD_MuEnriched_30to50'    :   139803000.0*0.01182,
    'QCD_MuEnriched_50to80'    :    19222500.0*0.02276,
    'QCD_MuEnriched_80to120'   :     2758420.0*0.03844,
    'QCD_MuEnriched_120to170'  :      469797.0*0.05362,
    'QCD_MuEnriched_170to300'  :      117989.0*0.07335,
    'QCD_MuEnriched_300to470'  :       7820.25*0.10196,
    'QCD_MuEnriched_470to600'  :       645.528*0.12242,
    'QCD_MuEnriched_600to800'  :       187.109*0.13412,
    'QCD_MuEnriched_800to1000' :       32.3486*0.14552,
    'QCD_MuEnriched_1000toInf' :       10.4305*0.15544,

    'QCD_EMEnriched_15to20'    :  1279000000.0*0.0018,
    'QCD_EMEnriched_20to30'    :   557600000.0*0.0096,
    'QCD_EMEnriched_30to50'    :   136000000.0*0.073,
    'QCD_EMEnriched_50to80'    :    19800000.0*0.146,
    'QCD_EMEnriched_80to120'   :     2800000.0*0.125,
    'QCD_EMEnriched_120to170'  :      477000.0*0.132,
    'QCD_EMEnriched_170to300'  :      114000.0*0.1650,
    'QCD_EMEnriched_300toInf'  :        9000.0*0.1500,

    'QCD_bcToE_15to20'         :  1272980000.0*0.0002,
    'QCD_bcToE_20to30'         :   557627000.0*0.00059,
    'QCD_bcToE_30to80'         :   159068000.0*0.00255,
    'QCD_bcToE_80to170'        :     3221000.0*0.01183,
    'QCD_bcToE_170to250'       :      105771.0*0.02492,
    'QCD_bcToE_250toInf'       :       21094.1*0.03375,

    ###########################################################################



}

InputCondorArguments = {}

pdgIdsForLifetimeReweighting = {
    # Defines the PDG IDs of the particles to be used for lifetime reweighting.
    # The keys are dataset labels and the values are either single PDG IDs or
    # lists of PDG IDs, e.g.:
    # 'stop1200_50mm'               : 1000006,
    # 'stopAndGluino1200_50mm_30mm' : [1000006, 1000021],
}

srcCTauForLifetimeReweighting = {
    # Defines the proper lifetimes (in units of cm/c) of the particles defined
    # by pdgIdsForLifetimeReweighting in the original samples before lifetime
    # reweighting. The keys are dataset labels and the values are either single
    # lifetime values or lists of lifetimes, e.g.:
    # 'stop1200_50mm'               : 10.0,
    # 'stopAndGluino1200_50mm_30mm' : [10.0, 10.0],
}

dstCTauForLifetimeReweighting = {
    # Defines the target proper lifetimes (in units of cm/c) of the particles
    # defined by pdgIdsForLifetimeReweighting to which the sample should be
    # reweighted.  The keys are dataset labels and the values are either single
    # lifetime values or lists of lifetimes, e.g.:
    # 'stop1200_50mm'               : 10.0,
    # 'stopAndGluino1200_50mm_30mm' : [5.0, 3.0],
}

pdgIdsForISRReweighting = {
    # Defines the PDG IDs of the particles to be used for ISR reweighting.
    # This will calculate the vector PT of all hard interaction particles with
    # these IDs, and use it a proxy for the ISR recoil
    # They keys are dataset labels and the values are either single PDG IDs or
    # lists of PDG IDs, e.g:
    # 'stop1200_50mm' : 1000006,
    # 'stopAndGluino1200_50mm_30mm' : [1000006, 1000021],
}

##########################################################################
### code to set relevant parameters for displaced SUSY signal samples, ###
### which are a scan in the plane of stop mass and lifetime            ###
##########################################################################

import math

def mass(sample):
    start = sample.find("stop")+4
    end = sample.find("_")
    return sample[start:end]

def lifetime(sample):
    start = sample.find("_")+1
    end = sample.find("mm")
    lt = sample[start:end]
    return lt.replace("p",".")

##########################################################################

# generate list of masses
masses = [str(i*100) for i in range(2,13)]
# generate list of lifetimes
lifetimes = ["%g" % (0.1*i*(pow(10,j))) for j in range(4) for i in range(1,10)]
lifetimes.append("1000")
lifetimes = [lt.replace(".","p") for lt in lifetimes]

# generate list of sample names from masses, lifetimes
signal_datasets = ["stop%s_%smm" % (m,ctau) for m in masses for ctau in lifetimes]

datasets.extend(signal_datasets)
composite_dataset_definitions['DisplacedSUSYSignal'] = signal_datasets

signal_crossSections = {
    '200'  : 64.5085,
    '300'  : 8.51615,
    '400'  : 1.83537,
    '500'  : 0.51848,
    '600'  : 0.174599,
    '700'  : 0.0670476,
    '800'  : 0.0283338,
    '900'  : 0.0128895,
    '1000' : 0.00615134,
    '1100' : 0.00307413,
    '1200' : 0.00159844,
}

##########################################################################

for index, sample in enumerate(signal_datasets):
    nJobs[sample] = 99
    maxEvents[sample] = -1
    types[sample] = 'signalMC'
    labels[sample] = "#tilde{t}#tilde{t} M(%s) c#tau(%smm)" % (mass(sample), lifetime(sample))
    colors[sample] = 20 + index
    crossSections[sample] = signal_crossSections[mass(sample)]
    pdgIdsForLifetimeReweighting[sample] = 1000006
    dstCTauForLifetimeReweighting[sample] = 0.1*float(lifetime(sample))
    srcCTauForLifetimeReweighting[sample] = 0.1*10**(math.ceil(math.log10(float(lifetime(sample)))))
    # special case
    if lifetime(sample) == "0.1":
        srcCTauForLifetimeReweighting[sample] = 0.1*1.0
