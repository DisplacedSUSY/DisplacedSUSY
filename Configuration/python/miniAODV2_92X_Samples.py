 #!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD V2 DATASETS  ####################################################################
############################################################################################################

dataset_names = {

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
    'JetHT_2017C' : ['/JetHT/Run2017C-PromptReco-v1/MINIAOD',
                     '/JetHT/Run2017C-PromptReco-v2/MINIAOD',
                     '/JetHT/Run2017C-PromptReco-v3/MINIAOD'],
    ############################################################################

}
