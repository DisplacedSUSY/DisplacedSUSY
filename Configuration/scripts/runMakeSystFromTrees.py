#!/usr/bin/env python

# makes all the signal systematics
# for this to work, need to have: PreselectionOptions.py point to all the (main point) signal samples, links to condor directories in each /test directory
import os

# 2018
os.chdir('/uscms_data/d3/alimena/DisplacedLeptons/CMSSW_10_2_12/src/')
os.system('scram runtime -sh')
os.chdir('DisplacedSUSY/EMuChannel/test')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2018Analysis_Signal_5Dec2020 -s electronD0Smearing')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2018Analysis_Signal_5Dec2020 -s muonD0Smearing')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2018Analysis_Signal_5Dec2020 -s pileup')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2018Analysis_Signal_5Dec2020 -s electronIDandIso')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2018Analysis_Signal_5Dec2020 -s muonIDandIso')

os.chdir('../../EEChannel/test')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2018Analysis_Signal_5Dec2020 -s electronD0Smearing')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2018Analysis_Signal_5Dec2020 -s pileup')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2018Analysis_Signal_5Dec2020 -s electronIDandIso')

os.chdir('../../MuMuChannel/test')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2018Analysis_Signal_5Dec2020 -s muonD0Smearing')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2018Analysis_Signal_5Dec2020 -s pileup')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2018Analysis_Signal_5Dec2020 -s muonIDandIso')

# 2017
#os.chdir('/uscms_data/d3/alimena/DisplacedLeptons/94normal/CMSSW_9_4_8/src/')
#os.system('scram runtime -sh')
#os.chdir('DisplacedSUSY/EMuChannel/test')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2017Analysis_Signal_5Dec2020 -s electronD0Smearing')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2017Analysis_Signal_5Dec2020 -s muonD0Smearing')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2017Analysis_Signal_5Dec2020 -s pileup')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2017Analysis_Signal_5Dec2020 -s electronIDandIso')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2017Analysis_Signal_5Dec2020 -s muonIDandIso')

#os.chdir('../../EEChannel/test')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2017Analysis_Signal_5Dec2020 -s electronD0Smearing')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2017Analysis_Signal_5Dec2020 -s pileup')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2017Analysis_Signal_5Dec2020 -s electronIDandIso')

#os.chdir('../../MuMuChannel/test')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2017Analysis_Signal_5Dec2020 -s muonD0Smearing')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2017Analysis_Signal_5Dec2020 -s pileup')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2017Analysis_Signal_5Dec2020 -s muonIDandIso')

# 2016
#os.chdir('/uscms_data/d3/alimena/DisplacedLeptons/CMSSW_9_4_8/src/')
#os.system('scram runtime -sh')
#os.chdir('DisplacedSUSY/EMuChannel/test')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2016Analysis_Signal_5Dec2020 -s pileup')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2016Analysis_Signal_5Dec2020 -s electronIDandIso')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2016Analysis_Signal_5Dec2020 -s muonIDandIso')

#os.chdir('../../EEChannel/test')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2016Analysis_Signal_5Dec2020 -s pileup')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2016Analysis_Signal_5Dec2020 -s electronIDandIso')

#os.chdir('../../MuMuChannel/test')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2016Analysis_Signal_5Dec2020 -s pileup')
#os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2016Analysis_Signal_5Dec2020 -s muonIDandIso')
