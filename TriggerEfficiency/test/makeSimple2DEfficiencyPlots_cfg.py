output_file_name = 'trigEff2D_pT.root'

input_files = [
    {
    "input_file" : '/data/users/bcardwell/condor/MuMu_TrigEfficiency_17_10_06/JetHT_2017.root',
    "hist_pairs" :
        [
            {
            "pass_hist"      : 'TTbarForTrigEff43Plotter/Muon Plots/muonPtLeadingVsSubleading',
            "total_hist"     : 'TTbarForTrigEffNoTrigPlotter/Muon Plots/muonPtLeadingVsSubleading',
            "eff_plot_title" : 'HLT_DoubleMu43NoFiltersNoVtx',
            "x_axis_title"   : 'Subleading muon p_{T} [GeV]',
            "y_axis_title"   : 'Leading muon p_{T} [GeV]',
            },
            {
            "pass_hist"      : 'TTbarForTrigEff48Plotter/Muon Plots/muonPtLeadingVsSubleading',
            "total_hist"     : 'TTbarForTrigEffNoTrigPlotter/Muon Plots/muonPtLeadingVsSubleading',
            "eff_plot_title" : 'HLT_DoubleMu48NoFiltersNoVtx',
            "x_axis_title"   : 'Subleading muon p_{T} [GeV]',
            "y_axis_title"   : 'Leading muon p_{T} [GeV]',
            },
        ]
    },
    {
    "input_file" : '/data/users/bcardwell/condor/EMu_TrigEfficiency_17_10_06/JetHT_2017.root',
    "hist_pairs" :
        [
            {
            "pass_hist"      : 'TTbarForTrigEff43Plotter/Electron-muon Plots/electronPtMuonPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigPlotter/Electron-muon Plots/electronPtMuonPt',
            "eff_plot_title" : 'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL',
            "x_axis_title"   : 'Muon p_{T} [GeV]',
            "y_axis_title"   : 'Electron p_{T} [GeV]',
            },
            {
            "pass_hist"      : 'TTbarForTrigEff48Plotter/Electron-muon Plots/electronPtMuonPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigPlotter/Electron-muon Plots/electronPtMuonPt',
            "eff_plot_title" : 'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL',
            "x_axis_title"   : 'Muon p_{T} [GeV]',
            "y_axis_title"   : 'Electron p_{T} [GeV]',
            },
        ]
    },
]

