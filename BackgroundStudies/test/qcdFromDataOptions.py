#!/usr/bin/env python

datasets = [
    'MuEG_22Jan2013'
]
impurities = [
]
qcd_from_data = {
    'scale_factor' : 0.02209,
    'scale_factor_error' : (0),

    # This is a map from channels in the output from data to the channels you
    # want in QCDFromData.root; e.g., below, the histograms in the
    # "AntiIsolated" channel will be used to create an "Isolated" and
    # "AntiIsolated" channel in QCDFromData.root.
    'channel_map' : {
        'Anti_Iso_Blinded_Preselection' : ['Blinded_Preselection'],
#        'AntiIsolated' : ['Isolated', 'AntiIsolated'],
#        'AntiIsolated_Prompt' : ['Isolated_Prompt', 'AntiIsolated_Prompt'],
#        'AntiIsolated_NonPrompt' : ['Isolated_NonPrompt', 'AntiIsolated_NonPrompt'],
    }
}
