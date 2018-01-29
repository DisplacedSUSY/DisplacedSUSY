import numpy
output_file_name = 'trigEff_pT.root'

plots = [
    {
    "channel"      : "emu_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,80,120,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_MET_18_01_25/MET_2016_postHIP.root',
            "pass_hist"      : 'TTbarForTrigEff38HighPtMuPlotter/Electron Plots/electronPt',
            "total_hist"     : 'TTbarForTrigEffHighPtMuPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_MET_18_01_25/TTJets_DiLept.root',
            "pass_hist"      : 'TTbarForTrigEff38HighPtMuPlotter/Electron Plots/electronPt',
            "total_hist"     : 'TTbarForTrigEffHighPtMuPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_DiLept',
            "type"           : 'mc',
            },
        ]
    },
    {
    "channel"      : "emu_trig_eff_vs_mu_pt",
    "x_axis_title" : 'Muon p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,80,120,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_MET_18_01_25/MET_2016_postHIP.root',
            "pass_hist"      : 'TTbarForTrigEff38HighPtEPlotter/Muon Plots/muonPt',
            "total_hist"     : 'TTbarForTrigEffHighPtEPlotter/Muon Plots/muonPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_MET_18_01_25/TTJets_DiLept.root',
            "pass_hist"      : 'TTbarForTrigEff38HighPtEPlotter/Muon Plots/muonPt',
            "total_hist"     : 'TTbarForTrigEffHighPtEPlotter/Muon Plots/muonPt',
            "color"          : 2,
            "label"          : 'TTJets_Lept',
            "type"           : 'mc',
            },
        ]
    },
    #{
    #"channel"      : "emu_trig_eff_vs_e_pt_combineBins",
    #"x_axis_title" : 'Electron p_{T} [GeV]',
    #"bins"         : [20,30,33,300],
    #"hist_pairs"   :
    #    [
    #        {
    #        "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_17_10_30/JetHT_2016_postHIP.root',
    #        "pass_hist"      : 'TTbarForTrigEffStandardTrigHighPtMuPlotter/Electron Plots/electronPt',
    #        "total_hist"     : 'TTbarForTrigEffNoTrigHighPtMuPlotter/Electron Plots/electronPt',
    #        "color"          : 1,
    #        "label"          : 'JetHT_2016 G and H',
    #        },
    #        {
    #        "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_17_10_30/TTJets_Lept.root',
    #        "pass_hist"      : 'TTbarForTrigEffStandardTrigHighPtMuPlotter/Electron Plots/electronPt',
    #        "total_hist"     : 'TTbarForTrigEffNoTrigHighPtMuPlotter/Electron Plots/electronPt',
    #        "color"          : 2,
    #        "label"          : 'TTJets_Lept',
    #        },
    #    ]
    #},
    #{
    #"channel"      : "emu_trig_eff_vs_mu_pt_combineBins",
    #"x_axis_title" : 'Muon p_{T} [GeV]',
    #"bins"         : [20,30,33,300],
    #"hist_pairs"   :
    #    [
    #        {
    #        "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_17_10_30/JetHT_2016_postHIP.root',
    #        "pass_hist"      : 'TTbarForTrigEffStandardTrigHighPtEPlotter/Muon Plots/muonPt',
    #        "total_hist"     : 'TTbarForTrigEffNoTrigHighPtEPlotter/Muon Plots/muonPt',
    #        "color"          : 1,
    #        "label"          : 'JetHT_2016 G and H',
    #        },
    #        {
    #        "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_17_10_30/TTJets_Lept.root',
    #        "pass_hist"      : 'TTbarForTrigEffStandardTrigHighPtEPlotter/Muon Plots/muonPt',
    #        "total_hist"     : 'TTbarForTrigEffNoTrigHighPtEPlotter/Muon Plots/muonPt',
    #        "color"          : 2,
    #        "label"          : 'TTJets_Lept',
    #        },
    #    ]
    #},
]

