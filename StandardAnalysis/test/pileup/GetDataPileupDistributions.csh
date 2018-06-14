#!/bin/csh

# https://twiki.cern.ch/twiki/bin/view/CMS/PileupJSONFileforData#Pileup_JSON_Files_For_Run_II

########################################################
# Define JSONs and min-bias xsecs and number of bins
########################################################

set json16=Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
set minBias16=69200
set minBiasUncertainty16=0.046

set nBinsX=100

########################################################
# Set up and get JSONs
########################################################

set minBias16Up=`echo "print $minBias16 * (1 + $minBiasUncertainty16)" | python`
set minBias16Down=`echo "print $minBias16 * (1 - $minBiasUncertainty16)" | python`

source /cvmfs/cms.cern.ch/cmsset_default.csh
eval `scram runtime -csh`

curl https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/PileUp/pileup_latest.txt > pileup_2016.txt
wget https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/$json16

########################################################
# Split up 2016 into GH
# https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2016Analysis
########################################################

set json16GH=Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON_GH.txt

filterJSON.py --min 278820 --max 284044 $json16 --output $json16GH

########################################################
# Get data distributions using JSONs as masks
########################################################

pileupCalc.py -i $json16 --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16 --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016_central.root
pileupCalc.py -i $json16 --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16Up --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016_up.root
pileupCalc.py -i $json16 --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16Down --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016_down.root

pileupCalc.py -i $json16GH --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16 --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016GH_central.root
pileupCalc.py -i $json16GH --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16Up --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016GH_up.root
pileupCalc.py -i $json16GH --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16Down --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016GH_down.root

########################################################
# Combine ROOT files and clean up
########################################################

root -b -q -l CombineDataFiles.C

rm puData_2016*.root

echo "Created combined file puData.root"
