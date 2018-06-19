#!/bin/csh

# https://twiki.cern.ch/twiki/bin/view/CMS/PileupJSONFileforData#Pileup_JSON_Files_For_Run_II

#####################################################################
# Define JSONs, min-bias xsecs, and number of bins for the given year
#####################################################################

switch ( $CMSSW_VERSION )
    case "CMSSW_8_0*":
        echo "Detected CMSSW 80X. Calculating 2016 PU"

        set json_dir=https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final
        set json=Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
        set pu_json_dir=https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/PileUp
        set pu_json=pileup_latest.txt

        # Split up 2016 into GH
        # https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2016Analysis
        set filter_json=Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON_GH.txt
        set min_run=278820
        set max_run=284044

        breaksw

    case "CMSSW_9_4*":
        echo "Detected CMSSW 94X. Calculating 2017 PU"

        set json_dir=https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco
        set json=Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt
        set pu_json_dir=https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/PileUp
        set pu_json=pileup_latest.txt

        # Split up 2017 into CDEF
        # made filter json from (2017 golden rereco) OR (C OR D OR E OR F)
        # min and max from https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2017Analysis
        set filter_json=Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_CDEF.txt
        set min_run=299337
        set max_run=306462

        breaksw

    default:
        echo "Unrecognized CMSSW release"
        exit 1
endsw

# use 2016 minBias for 2016 and 2017 until official 2017 values appear
set minBias=69200
set minBiasUncertainty=0.046
set nBinsX=100

########################################################
# Set up and get JSONs
########################################################

set minBiasUp=`echo "print $minBias * (1 + $minBiasUncertainty)" | python`
set minBiasDown=`echo "print $minBias * (1 - $minBiasUncertainty)" | python`

source /cvmfs/cms.cern.ch/cmsset_default.csh
eval `scram runtime -csh`

curl $pu_json_dir/$pu_json > pileup.txt
wget $json_dir/$json

########################################################
# Split given year into subsets used in analysis
########################################################

filterJSON.py --min $min_run --max $max_run $json --output $filter_json

########################################################
# Get data distributions using JSONs as masks
########################################################

pileupCalc.py -i $json --inputLumiJSON pileup.txt --calcMode true --minBiasXsec $minBias --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_central.root
echo "finished pileupcalc 1/6"
pileupCalc.py -i $json --inputLumiJSON pileup.txt --calcMode true --minBiasXsec $minBiasUp --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_up.root
echo "finished pileupcalc 2/6"
pileupCalc.py -i $json --inputLumiJSON pileup.txt --calcMode true --minBiasXsec $minBiasDown --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_down.root
echo "finished pileupcalc 3/6"

pileupCalc.py -i $filter_json --inputLumiJSON pileup.txt --calcMode true --minBiasXsec $minBias --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_filtered_central.root
echo "finished pileupcalc 4/6"
pileupCalc.py -i $filter_json --inputLumiJSON pileup.txt --calcMode true --minBiasXsec $minBiasUp --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_filtered_up.root
echo "finished pileupcalc 5/6"
pileupCalc.py -i $filter_json --inputLumiJSON pileup.txt --calcMode true --minBiasXsec $minBiasDown --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_filtered_down.root
echo "finished pileupcalc 6/6"

########################################################
# Combine ROOT files and clean up
########################################################

root -b -q -l CombineDataFiles.C

rm puData_central.root
rm puData_up.root
rm puData_down.root
rm puData_filtered_central.root
rm puData_filtered_up.root
rm puData_filtered_down.root

echo "Created combined file puData.root"
