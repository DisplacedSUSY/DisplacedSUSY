#!/usr/bin/env python

# makes all the signal systematics
# for this to work, need to have: PreselectionOptions.py point to all the (main point) signal samples, links to condor directories in each /test directory
import os

# 2018
#if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
#    os.chdir('/uscms_data/d3/alimena/DisplacedLeptons/CMSSW_10_2_12/src/')
#    os.system('scram runtime -sh')
#    os.chdir('DisplacedSUSY/EMuChannel/test')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2018Analysis_Signal_5Dec2020 -s electronD0Smearing')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2018Analysis_Signal_5Dec2020 -s muonD0Smearing')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2018Analysis_Signal_5Dec2020 -s pileup')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2018Analysis_Signal_5Dec2020 -s electronIDandIso')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2018Analysis_Signal_5Dec2020 -s muonIDandIso')

#    os.chdir('../../EEChannel/test')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2018Analysis_Signal_5Dec2020 -s electronD0Smearing')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2018Analysis_Signal_5Dec2020 -s pileup')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2018Analysis_Signal_5Dec2020 -s electronIDandIso')

#    os.chdir('../../MuMuChannel/test')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2018Analysis_Signal_5Dec2020 -s muonD0Smearing')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2018Analysis_Signal_5Dec2020 -s pileup')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2018Analysis_Signal_5Dec2020 -s muonIDandIso')

# 2017
#elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
#    os.chdir('/uscms_data/d3/alimena/DisplacedLeptons/94normal/CMSSW_9_4_8/src/')
#    os.system('scram runtime -sh')
#    os.chdir('DisplacedSUSY/EMuChannel/test')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2017Analysis_Signal_5Dec2020 -s electronD0Smearing')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2017Analysis_Signal_5Dec2020 -s muonD0Smearing')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2017Analysis_Signal_5Dec2020 -s pileup')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2017Analysis_Signal_5Dec2020 -s electronIDandIso')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2017Analysis_Signal_5Dec2020 -s muonIDandIso')

#    os.chdir('../../EEChannel/test')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2017Analysis_Signal_5Dec2020 -s electronD0Smearing')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2017Analysis_Signal_5Dec2020 -s pileup')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2017Analysis_Signal_5Dec2020 -s electronIDandIso')

#    os.chdir('../../MuMuChannel/test')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2017Analysis_Signal_5Dec2020 -s muonD0Smearing')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2017Analysis_Signal_5Dec2020 -s pileup')
#    os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2017Analysis_Signal_5Dec2020 -s muonIDandIso')

# 2016
#elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
os.chdir('/uscms_data/d3/alimena/DisplacedLeptons/CMSSW_9_4_8/src/')
os.system('scram runtime -sh')
os.chdir('DisplacedSUSY/EMuChannel/test')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2016Analysis_HToSS_19Apr2021 -s pileup')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2016Analysis_HToSS_19Apr2021 -s electronIDandIso')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2016Analysis_HToSS_19Apr2021 -s muonIDandIso')

os.chdir('../../EEChannel/test')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2016Analysis_HToSS_19Apr2021 -s pileup')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w EEPreselection_2016Analysis_HToSS_19Apr2021 -s electronIDandIso')

os.chdir('../../MuMuChannel/test')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2016Analysis_HToSS_19Apr2021 -s pileup')
os.system('../../Configuration/scripts/makeSystematicTextFileFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_2016Analysis_HToSS_19Apr2021 -s muonIDandIso')


# to be run when all of the above is done, in order to get the lifetime reweighted samples into the text files:
#if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
#os.chdir('/uscms_data/d3/alimena/DisplacedLeptons/CMSSW_10_2_12/src/')
#os.system('scram runtime -sh')
#os.system('python addRewtLifetimesToSyst.py')
