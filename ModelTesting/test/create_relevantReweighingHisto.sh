###
### This macro create plot to compare the 4 histograms that will be used for the reweighting (do not create the histograms them self, use create_relevantReweighingHisto.sh for that) for all the different sample.
### needs one argument, which the name of the output condor dir. It will put all the plot under the same directory in the current directory.
### needs for config files ElrecoEffPlotConfig.py, MurecoEffPlotConfig.py, ElselectionEffPlotConfig.py and  MuselectionEffPlotConfig.py
### uses example
### source create_relevantReweighingHisto.sh ModelTestingMoreCTau
###

## All the string necessary to use sed with variable changes
# To change the dataset used
beginSedStrig='s/ToBeSet/'
endSedString='/g'
CoreSedString='stopHadron'
CoreSedString2='toBl_'
CoreSedString3='.0mm'
stringM='M_'
stringctau='ctau_'

# To change the condor directory used
beginSedStringCond='s/scondor_dir=.*/'
endSedStringCond='/g'
scondordir=$1  # This parameter is set to the first argument of the script 
singleket="'"
scondor_dir="scondor_dir="
totSedStringCond="$beginSedStringCond$scondor_dir$singleket$scondordir$singleket$endSedStringCond"
##

# Edit all the config files to put the right condor_dir
sed -i $totSedStringCond ElrecoEffPlotConfig.py
sed -i $totSedStringCond MurecoEffPlotConfig.py
sed -i $totSedStringCond ElselectionEffPlotConfig.py
sed -i $totSedStringCond MuselectionEffPlotConfig.py


# loop on the masses    
for M in 200 600 1000 All # 
do
    # loop on the ctaus
    for ctau in 1 10 100 1000 All # 
    do
    if [ 0 == 0 ]
    then
	totSedString="$beginSedStrig$CoreSedString$M$CoreSedString2$ctau$CoreSedString3$endSedString"
	StringToAppendTofile="$stringM$M$stringctau$ctau"
	echo "Creating the for histograms for signal sample with mass=$M and ctau=$ctau"
	
	# Create the histo for the efficiency to reco electrons
	sed -e $totSedString ElrecoEffPlotConfig.py > ElrecoEffPlotConfig_$StringToAppendTofile.py
	makeEfficiencyComparisonPlot.py -l ElrecoEffPlotConfig_$StringToAppendTofile.py --noTGraph -b 20 -o recoElectron_$StringToAppendTofile.root
	rm ElrecoEffPlotConfig_$StringToAppendTofile.p*
	mv recoElectron_$StringToAppendTofile.root ../../../OSUT3Analysis/Configuration/data/
	
	# Create the histo for the efficiency to reco muons
	sed -e $totSedString MurecoEffPlotConfig.py > MurecoEffPlotConfig_$StringToAppendTofile.py
	makeEfficiencyComparisonPlot.py -l MurecoEffPlotConfig_$StringToAppendTofile.py --noTGraph -b 20 -o recoMuon_$StringToAppendTofile.root
	rm MurecoEffPlotConfig_$StringToAppendTofile.p*
	mv recoMuon_$StringToAppendTofile.root ../../../OSUT3Analysis/Configuration/data/
	
	# Create the histo for the efficiency to select electrons
	sed -e $totSedString ElselectionEffPlotConfig.py > ElselectionEffPlotConfig_$StringToAppendTofile.py
	makeEfficiencyComparisonPlot.py -l ElselectionEffPlotConfig_$StringToAppendTofile.py --noTGraph -o electronCut_$StringToAppendTofile.root
	rm ElselectionEffPlotConfig_$StringToAppendTofile.p*
	mv electronCut_$StringToAppendTofile.root ../../../OSUT3Analysis/Configuration/data/
	
	# Create the histo for the efficiency to select muons
	sed -e $totSedString MuselectionEffPlotConfig.py > MuselectionEffPlotConfig_$StringToAppendTofile.py
	makeEfficiencyComparisonPlot.py -l MuselectionEffPlotConfig_$StringToAppendTofile.py --noTGraph -o muonCut_$StringToAppendTofile.root
	rm MuselectionEffPlotConfig_$StringToAppendTofile.p*
	mv muonCut_$StringToAppendTofile.root ../../../OSUT3Analysis/Configuration/data/
	echo "ok, next!!"
	echo ""
    fi

    done

done




    ### Below is probaply outdated kepp if [ 1 == 0 ] to ignore
    # Create the histo for the efficiency to reco electrons
    if [ 1 == 0 ]
    then 
	sed -e 's/ToBeSet/allSample/' ElrecoEffPlotConfig.py > ElrecoEffPlotConfig_allSample.py
	makeEfficiencyComparisonPlot.py -l ElrecoEffPlotConfig_allSample.py --noTGraph -o recoElectron_allSample.root
	rm ElrecoEffPlotConfig_allSample.p*
	mv recoElectron_allSample.root ../../../OSUT3Analysis/Configuration/data/
	
	# Create the histo for the efficiency to reco muons
	sed -e 's/ToBeSet/allSample/' MurecoEffPlotConfig.py > MurecoEffPlotConfig_allSample.py
	makeEfficiencyComparisonPlot.py -l MurecoEffPlotConfig_allSample.py --noTGraph -o recoMuon_allSample.root
	rm MurecoEffPlotConfig_allSample.p*
	mv recoMuon_allSample.root ../../../OSUT3Analysis/Configuration/data/
	
	# Create the histo for the efficiency to select electrons
	sed -e 's/ToBeSet/allSample/' ElselectionEffPlotConfig.py > ElselectionEffPlotConfig_allSample.py
	makeEfficiencyComparisonPlot.py -l ElselectionEffPlotConfig_allSample.py --noTGraph -o electronCut_allSample.root
	rm ElselectionEffPlotConfig_allSample.p*
	mv electronCut_allSample.root ../../../OSUT3Analysis/Configuration/data/
	
	# Create the histo for the efficiency to select muons
	sed -e 's/ToBeSet/allSample/' MuselectionEffPlotConfig.py > MuselectionEffPlotConfig_allSample.py
	makeEfficiencyComparisonPlot.py -l MuselectionEffPlotConfig_allSample.py --noTGraph -o muonCut_allSample.root
	rm MuselectionEffPlotConfig_allSample.p*
	mv muonCut_allSample.root ../../../OSUT3Analysis/Configuration/data/
    fi

echo "end of script!!!!!"
