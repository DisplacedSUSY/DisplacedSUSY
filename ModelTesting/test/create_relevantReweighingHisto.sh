beginSedStrig='s/ToBeSet/'
endSedString='/g'
CoreSedString='stopHadron'
CoreSedString2='toBl_'
CoreSedString3='.0mm'
stringM='M_'
stringctau='ctau_'

# loop on the masses    
for M in 200 600 1000
do
    # loop on the ctaus
    for ctau in 1 100 # 10000 has 0 stat
    do
    if [ 0 == 0 ]
    then
	totSedString="$beginSedStrig$CoreSedString$M$CoreSedString2$ctau$CoreSedString3$endSedString"
	StringToAppendTofile="$stringM$M$stringctau$ctau"
	echo "Creating the for histograms for signal sample with mass=$M and ctau=$ctau"
	
	# Create the histo for the efficiency to reco electrons
	sed -e $totSedString ElrecoEffPlotConfig.py > ElrecoEffPlotConfig_$StringToAppendTofile.py
	makeEfficiencyComparisonPlot.py -l ElrecoEffPlotConfig_$StringToAppendTofile.py --noTGraph -o recoElectron_$StringToAppendTofile.root
	rm ElrecoEffPlotConfig_$StringToAppendTofile.p*
	mv recoElectron_$StringToAppendTofile.root ../../../OSUT3Analysis/Configuration/data/
	
	# Create the histo for the efficiency to reco muons
	sed -e $totSedString MurecoEffPlotConfig.py > MurecoEffPlotConfig_$StringToAppendTofile.py
	makeEfficiencyComparisonPlot.py -l MurecoEffPlotConfig_$StringToAppendTofile.py --noTGraph -o recoMuon_$StringToAppendTofile.root
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

#    sed -e 's/ToBeSet/allSample/'  MurecoEffPlotConfig.py > MurecoEffPlotConfig_allSample.py

    # Create the histo for the efficiency to reco electrons
    if [ 0 == 0 ]
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
	
done

echo "end of script!!!!!"
