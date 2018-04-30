import numpy
output_file_name = 'trigEff_pT.root'

plots = [
    {
    "channel"      : "smallBins_ee_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
            "pass_hist"      : 'trigMETandEEtrigPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
            "pass_hist"      : 'trigMETandEEtrigPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_DiLept',
            "type"           : 'mc',
            },
        ]
    },
    {
    "channel"      : "smallBins_ee_tag_e_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
            "pass_hist"      : 'trigMETandEEtrigTagElectronPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETTagElectronPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
            "pass_hist"      : 'trigMETandEEtrigTagElectronPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETTagElectronPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_DiLept',
            "type"           : 'mc',
            },
        ]
    },
    {
    "channel"      : "smallBins_ee_HLTDiphoton30_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
            "pass_hist"      : 'TTbarForHLTDiphoton30Plotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
            "pass_hist"      : 'TTbarForHLTDiphoton30Plotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_DiLept',
            "type"           : 'mc',
            },
        ]
    },
    {
    "channel"      : "smallBins_ee_eTag_HLTDiphoton30_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
            "pass_hist"      : 'TTbarForHLTDiphoton30eTagPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETTagElectronPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
            "pass_hist"      : 'TTbarForHLTDiphoton30eTagPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETTagElectronPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_DiLept',
            "type"           : 'mc',
            },
        ]
    },
    {
    "channel"      : "smallBinsee_HLTDoublePhoton60_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
            "pass_hist"      : 'TTbarForHLTDoublePhoton60Plotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
            "pass_hist"      : 'TTbarForHLTDoublePhoton60Plotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_DiLept',
            "type"           : 'mc',
            },
        ]
    },
    {
    "channel"      : "smallBins_e_eTag_HLTDoublePhoton60_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
            "pass_hist"      : 'TTbarForHLTDoublePhoton60eTagPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETTagElectronPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
            "pass_hist"      : 'TTbarForHLTDoublePhoton60eTagPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETTagElectronPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_DiLept',
            "type"           : 'mc',
            },
        ]
    },
    {
    "channel"      : "ee_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,80,120,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
            "pass_hist"      : 'trigMETandEEtrigPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
            "pass_hist"      : 'trigMETandEEtrigPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_DiLept',
            "type"           : 'mc',
            },
        ]
    },
    {
    "channel"      : "ee_tag_e_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,80,120,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
            "pass_hist"      : 'trigMETandEEtrigTagElectronPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETTagElectronPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
            "pass_hist"      : 'trigMETandEEtrigTagElectronPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETTagElectronPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_DiLept',
            "type"           : 'mc',
            },
        ]
    },
    {
    "channel"      : "ee_HLTDiphoton30_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,80,120,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
            "pass_hist"      : 'TTbarForHLTDiphoton30Plotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
            "pass_hist"      : 'TTbarForHLTDiphoton30Plotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_DiLept',
            "type"           : 'mc',
            },
        ]
    },
    {
    "channel"      : "ee_eTag_HLTDiphoton30_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,80,120,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
            "pass_hist"      : 'TTbarForHLTDiphoton30eTagPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETTagElectronPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
            "pass_hist"      : 'TTbarForHLTDiphoton30eTagPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETTagElectronPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_DiLept',
            "type"           : 'mc',
            },
        ]
    },
    {
    "channel"      : "ee_HLTDoublePhoton60_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,80,120,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
            "pass_hist"      : 'TTbarForHLTDoublePhoton60Plotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
            "pass_hist"      : 'TTbarForHLTDoublePhoton60Plotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_DiLept',
            "type"           : 'mc',
            },
        ]
    },
    {
    "channel"      : "ee_eTag_HLTDoublePhoton60_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [20,25,30,35,40,80,120,300],
    "hist_pairs"   :
        [
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
            "pass_hist"      : 'TTbarForHLTDoublePhoton60eTagPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETTagElectronPlotter/Electron Plots/electronPt',
            "color"          : 1,
            "label"          : 'MET_2016 G and H',
            "type"           : 'data',
            },
            {
            "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
            "pass_hist"      : 'TTbarForHLTDoublePhoton60eTagPlotter/Electron Plots/electronPt',
            "total_hist"     : 'trigMETTagElectronPlotter/Electron Plots/electronPt',
            "color"          : 2,
            "label"          : 'TTJets_DiLept',
            "type"           : 'mc',
            },
        ]
    },
    # {
    # "channel"      : "ee_trig_eff_vs_e_pt",
    # "x_axis_title" : 'Electron p_{T} [GeV]',
    # "bins"         : [20,25,30,35,40,80,120,300],
    # "hist_pairs"   :
    #     [
    #         {
    #         "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
    #         "pass_hist"      : 'trigMETandEEtrigPlotter/Electron Plots/electronPt',
    #         "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
    #         "color"          : 1,
    #         "label"          : 'MET_2016 G and H',
    #         "type"           : 'data',
    #         },
    #         {
    #         "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
    #         "pass_hist"      : 'trigMETandEEtrigPlotter/Electron Plots/electronPt',
    #         "total_hist"     : 'trigMETPlotter/Electron Plots/electronPt',
    #         "color"          : 2,
    #         "label"          : 'TTJets_DiLept',
    #         "type"           : 'mc',
    #         },
    #     ]
    # },
    # {
    # "channel"      : "ee_trig_eff_vs_e_pt",
    # "x_axis_title" : 'Electron p_{T} [GeV]',
    # "bins"         : [20,25,30,35,40,80,120,300],
    # "hist_pairs"   :
    #     [
    #         {
    #         "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/MET_2016_postHIP.root',
    #         "pass_hist"      : 'TTbarForTrigEff38HighPtEPlotter/Muon Plots/muonPt',
    #         "total_hist"     : 'TTbarForTrigEffHighPtEPlotter/Muon Plots/muonPt',
    #         "color"          : 1,
    #         "label"          : 'MET_2016 G and H',
    #         "type"           : 'data',
    #         },
    #         {
    #         "input_file"     : '/data/users/mnunezornelas/condor/TTbarForEETriggerEfficiency_April_20/TTJets_DiLept.root',
    #         "pass_hist"      : 'TTbarForTrigEff38HighPtEPlotter/Muon Plots/muonPt',
    #         "total_hist"     : 'TTbarForTrigEffHighPtEPlotter/Muon Plots/muonPt',
    #         "color"          : 2,
    #         "label"          : 'TTJets_DiLept',
    #         "type"           : 'mc',
    #         },
    #     ]
    # },
]

