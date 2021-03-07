#!/usr/bin/env python

# calculate pulls from any text file with any number of rows that follow the following format, which
# is based on the output of HiggsAnalysis/CombinedLimit/test/mlfitNormsToText.py.

# sample row for norms_file:
# bin_name   postfit_val +/- one_sigma_err   postfit_val +/- one_sigma_err
# e.g.
# emu_2016_SR_I_loPt        7.153 +/- 2.025       3.807 +/- 3.911


from ROOT import TFile, TH1F

norms_file = "pull_inputs.txt"

class Pull(object):
    def __init__(self, region, obs, est, est_err):
        self.region = region
        self.obs = float(obs)
        self.est = float(est)
        self.est_err = float(est_err)

        self.channel = '_'.join(self.region.split('_')[:2])
        self.pull = (self.obs - self.est)/self.est_err

pulls = []

with open(norms_file, 'r') as norms:
    for line in norms:
        line = line.split()
        if len(line) != 7 or "SR" not in line[0]:
            continue
        print line
        pulls.append(Pull(line[0], line[1], line[4], line[6]))

pull_distribution = TH1F("pulls", "pulls", 24, -3, 3)

processed_channels = []
for p in pulls:
    if p.channel not in processed_channels:
        processed_channels.append(p.channel)
        print
        print p.channel

    print round(p.pull, 2)
    pull_distribution.Fill(p.pull)

f = TFile("pulls.root", "recreate")
pull_distribution.Write()
f.Close()
