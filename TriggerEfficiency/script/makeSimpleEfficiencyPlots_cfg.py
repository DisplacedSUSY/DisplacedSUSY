import numpy
output_file_name = 'trigEff_pT.root'
#bins_array = numpy.geomspace(20,300,20)

plots = [
    {
    "channel"      : "mumu",
    "input_file"   : '/data/users/bcardwell/condor/MuMu_TrigEfficiency_17_10_06/JetHT_2017.root',
    "x_axis_title" : 'Muon p_{T} [GeV]',
    "bins"         : [20,30,40,42,45,47,50,60,100,180,300],
    "hist_pairs"   :
        [
            {
            "pass_hist"      : 'TTbarForTrigEffTagMuon43Plotter/Muon Plots/muonPt',
            "total_hist"     : 'TTbarForTrigEffTagMuonNoTrigPlotter/Muon Plots/muonPt',
            "color"          : 2,
            "label"          : 'HLT_DoubleMu43NoFiltersNoVtx',
            },
            {
            "pass_hist"      : 'TTbarForTrigEffTagMuon48Plotter/Muon Plots/muonPt',
            "total_hist"     : 'TTbarForTrigEffTagMuonNoTrigPlotter/Muon Plots/muonPt',
            "color"          : 1,
            "label"          : 'HLT_DoubleMu48NoFiltersNoVtx',
            },
        ]
    },
    {
    "channel"      : "emu_vs_e_pt",
    "input_file"   : '/data/users/bcardwell/condor/EMu_TrigEfficiency_17_10_06/JetHT_2017.root',
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,30,40,42,45,47,50,60,100,180,300],
    "hist_pairs"   :
        [
            {
            "pass_hist"      : 'TTbarForTrigEff43HighPtMuPlotter/Electron Plots/electronPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigHighPtMuPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL',
            },
            {
            "pass_hist"      : 'TTbarForTrigEff48HighPtMuPlotter/Electron Plots/electronPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigHighPtMuPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL',
            },
        ]
    },
    {
    "channel"      : "emu_vs_mu_pt",
    "input_file"   : '/data/users/bcardwell/condor/EMu_TrigEfficiency_17_10_06/JetHT_2017.root',
    "x_axis_title" : 'Muon p_{T} [GeV]',
    "bins"         : [20,30,40,42,45,47,50,60,100,180,300],
    "hist_pairs"   :
        [
            {
            "pass_hist"      : 'TTbarForTrigEff43HighPtEPlotter/Muon Plots/muonPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigHighPtEPlotter/Muon Plots/muonPt',
            "color"          : 1,
            "label"          : 'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL',
            },
            {
            "pass_hist"      : 'TTbarForTrigEff48HighPtEPlotter/Muon Plots/muonPt',
            "total_hist"     : 'TTbarForTrigEffNoTrigHighPtEPlotter/Muon Plots/muonPt',
            "color"          : 2,
            "label"          : 'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL',
            },
        ]
    },
    #{
    #"input_file" : '/data/users/bcardwell/condor/EMu_TrigEfficiency_17_10_06/JetHT_2017.root',
    #"hist_pairs" :
    #    [
    #        {
    #        "pass_hist"      : 'TTbarForTrigEff43HighPtEPlotter/Muon Plots/muonPt',
    #        "total_hist"     : 'TTbarForTrigEffNoTrigHighPtEPlotter/Muon Plots/muonPt',
    #        "eff_plot_title" : 'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL',
    #        "x_axis_title"   : 'Muon p_{T} [GeV]',
    #        "bins"           : [20,30,40,42,45,47,50,60,100,180,300],
    #        },
    #        {
    #        "pass_hist"      : 'TTbarForTrigEff43HighPtMuPlotter/Electron Plots/electronPt',
    #        "total_hist"     : 'TTbarForTrigEffNoTrigHighPtMuPlotter/Electron Plots/electronPt',
    #        "eff_plot_title" : 'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL',
    #        "x_axis_title"   : 'Electron p_{T} [GeV]',
    #        "bins"           : [20,30,40,42,45,47,50,60,100,180,300],
    #        },
    #        {
    #        "pass_hist"      : 'TTbarForTrigEff48HighPtEPlotter/Muon Plots/muonPt',
    #        "total_hist"     : 'TTbarForTrigEffNoTrigHighPtEPlotter/Muon Plots/muonPt',
    #        "eff_plot_title" : 'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL',
    #        "x_axis_title"   : 'Muon p_{T} [GeV]',
    #        "bins"           : [20,30,40,42,45,47,49,52,60,100,180,300],
    #        },
    #        {
    #        "pass_hist"      : 'TTbarForTrigEff48HighPtMuPlotter/Electron Plots/electronPt',
    #        "total_hist"     : 'TTbarForTrigEffNoTrigHighPtMuPlotter/Electron Plots/electronPt',
    #        "eff_plot_title" : 'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL',
    #        "x_axis_title"   : 'Electron p_{T} [GeV]',
    #        "bins"           : [20,30,40,42,45,47,49,52,60,100,180,300],
    #        },
    #    ]
    #},
]

