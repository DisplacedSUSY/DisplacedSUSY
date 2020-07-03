#!/usr/bin/env python

# Script to combine run periods into single cards for running limits.
# run with combineDatacards.py -l combineYearsLimit_cfg.py -w COMBINED_LIMITDIR

import os, sys, glob, re, subprocess
from threading import Thread, Semaphore, Lock
from multiprocessing import cpu_count

from OSUT3Analysis.Configuration.ProgressIndicator import ProgressIndicator

from DisplacedSUSY.Configuration.limitOptions import *

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified"
    sys.exit(0)

if arguments.condorDir:
    if not os.path.exists("limits/"+arguments.condorDir):
        os.system("mkdir limits/"+arguments.condorDir)
else:
    print "No output directory specified"
    sys.exit(0)

def makeCombinedCard (i, N, combinedCard, sample):
    global semaphore
    global printLock
    global progress

    semaphore.acquire ()

    printLock.acquire ()
    progress.setPercentDone(float(i+1) / N * 100.0)
    progress.printProgress(False)
    printLock.release ()

    # create the combined card
    outputCardFile = 'limits/' + combinedCard + '/datacard_' + sample + '.txt'
    cmd = 'combineCards.py'
    cardsExist = False

    for inputDir in inputDirs:
        inputCardFile = 'limits/' + inputDir + '/datacard_' + sample + '.txt'
        # if an input card is missing, skip this bin in the combined card
        if not os.path.isfile(inputCardFile):
            continue
        else:
            cardsExist = True
        cmd += ' ' + inputCardFile

    # if no input cards exist, there's nothing to combine
    if not cardsExist:
        semaphore.release()
        return

    subprocess.call(cmd + ' > ' + outputCardFile, shell = True)

    semaphore.release ()

#######################################################################

semaphore = Semaphore (cpu_count () + 1)
printLock = Lock ()
nCards = len(signal_points)
progressTitle = 'Combining ' + str(nCards) + ' datacards into "{0}"'
progress = ProgressIndicator("")

for combinedCard in datacardCombinations:
    progress = ProgressIndicator(progressTitle.format(combinedCard))
    progress.printProgress(False)

    threads = []
    i = 0

    for signal in signal_points:
        # rename sub-mm samples to match sample names
        signal = signal.replace('.', 'p')
        i += 1
        threads.append(Thread(target = makeCombinedCard, args = (i, nCards, arguments.condorDir, signal)))
        threads[-1].start()

    for thread in threads:
        thread.join()

    progress.setPercentDone(100.0)
    progress.printProgress(True)

print
print 'All done!'
print
