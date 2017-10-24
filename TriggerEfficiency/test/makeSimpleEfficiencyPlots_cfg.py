import numpy
output_file_name = 'trigEff_pT.root'
#bins_array = numpy.geomspace(20,300,20)

plots = [
    {
    "channel"      : "emu_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,30,35,37,42,50,60,100,180,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_17_10_13/JetHT_2016_postHIP.root',
            "pass_hist"      : 'TTbarForTrigEff38HighPtMuPlotter/Electron Plots/electronPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigHighPtMuPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'JetHT_2016 G and H',
            },
            {
            "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_17_10_13/TTJets_Lept.root',
            "pass_hist"      : 'TTbarForTrigEff38HighPtMuPlotter/Electron Plots/electronPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigHighPtMuPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_Lept',
            },
        ]
    },
    {
    "channel"      : "emu_trig_eff_vs_mu_pt",
    "x_axis_title" : 'Muon p_{T} [GeV]',
    "bins"         : [20,30,35,37,40,50,60,100,180,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_17_10_13/JetHT_2016_postHIP.root',
            "pass_hist"      : 'TTbarForTrigEff38HighPtEPlotter/Muon Plots/muonPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigHighPtEPlotter/Muon Plots/muonPt',
            "color"          : 1,
            "label"          : 'JetHT_2016 G and H',
            },
            {
            "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_17_10_13/TTJets_Lept.root',
            "pass_hist"      : 'TTbarForTrigEff38HighPtEPlotter/Muon Plots/muonPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigHighPtEPlotter/Muon Plots/muonPt',
            "color"          : 2,
            "label"          : 'TTJets_Lept',
            },
        ]
    },
    {
    "channel"      : "emu_trig_eff_vs_e_pt_combineBins",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,35,42,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_17_10_13/JetHT_2016_postHIP.root',
            "pass_hist"      : 'TTbarForTrigEff38HighPtMuPlotter/Electron Plots/electronPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigHighPtMuPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'JetHT_2016 G and H',
            },
            {
            "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_17_10_13/TTJets_Lept.root',
            "pass_hist"      : 'TTbarForTrigEff38HighPtMuPlotter/Electron Plots/electronPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigHighPtMuPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_Lept',
            },
        ]
    },
    {
    "channel"      : "emu_trig_eff_vs_mu_pt_combineBins",
    "x_axis_title" : 'Muon p_{T} [GeV]',
    "bins"         : [20,35,40,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_17_10_13/JetHT_2016_postHIP.root',
            "pass_hist"      : 'TTbarForTrigEff38HighPtEPlotter/Muon Plots/muonPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigHighPtEPlotter/Muon Plots/muonPt',
            "color"          : 1,
            "label"          : 'JetHT_2016 G and H',
            },
            {
            "input_file"     : '/data/users/bcardwell/condor/EMu_TrigEfficiency2016_17_10_13/TTJets_Lept.root',
            "pass_hist"      : 'TTbarForTrigEff38HighPtEPlotter/Muon Plots/muonPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigHighPtEPlotter/Muon Plots/muonPt',
            "color"          : 2,
            "label"          : 'TTJets_Lept',
            },
        ]
    },
]

