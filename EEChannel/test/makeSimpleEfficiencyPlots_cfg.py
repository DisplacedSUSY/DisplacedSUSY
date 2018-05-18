import numpy
output_file_name = 'trigEff_pT.root'

plots = [
    {
    "channel"      : "ee_tag_e_trig_eff_vs_e_pt",
    "x_axis_title" : 'Electron p_{T} [GeV]',
    "bins"         : [5,10,15,20,25,30,35,40,45,50,55,60,65,500],
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
]
