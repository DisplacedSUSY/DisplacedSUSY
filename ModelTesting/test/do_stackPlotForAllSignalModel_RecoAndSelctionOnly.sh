###                                                                                        
### This macro create plot to compare the 4 histograms that will be used for the reweighting (do not create the histograms them self, use create_relevantReweighingHisto.sh for that) for all the different sample.                                                            
### needs one argument, which the name of the output condor dir. It will put all the plot under the same directory in the current directory.                                         
### needs two config files recoEffPlotConfig.py and selectionEffPlotConfig.py
### uses example                                                                           
### source create_relevantReweighingHisto.sh ModelTestingMoreCTau                          
###  


### All the string necessary to edit the desired files with sed
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
sed -i $totSedStringCond recoEffPlotConfig.py
sed -i $totSedStringCond selectionEffPlotConfig.py



mkdir $1

# loop on the masses    
for M in 200 600 1000 All
do
    # loop on the ctaus
    for ctau in 1 10 100 1000 All # 10000 has 0 stat
    do
    totSedString="$beginSedStrig$CoreSedString$M$CoreSedString2$ctau$CoreSedString3$endSedString"
    StringToAppendTofile="$stringM$M$stringctau$ctau"
    echo "Processing $M $ctau"
    
    if [ 0 == 0 ]
    then
    # make the reco efficiency for electron and muon
    sed -e $totSedString recoEffPlotConfig.py > recoEffPlotConfig_$StringToAppendTofile.py
    makeEfficiencyComparisonPlot.py -l recoEffPlotConfig_$StringToAppendTofile.py -b 20 --pdf
    mv efficiency_plot.root $1/recoEff_$StringToAppendTofile.root
    mv efficiency_plot.pdf $1/recoEff_$StringToAppendTofile.pdf
    rm recoEffPlotConfig_$StringToAppendTofile.py
    fi

    if [ 0 == 0 ]
    then
    # make the selection efficiency for electron and muon 
    sed -e $totSedString selectionEffPlotConfig.py > selectionEffPlotConfig_$StringToAppendTofile.py
    makeEfficiencyComparisonPlot.py -l selectionEffPlotConfig_$StringToAppendTofile.py -b 10 --pdf
    mv efficiency_plot.root $1/selectionEff_$StringToAppendTofile.root
    mv efficiency_plot.pdf $1/selectionEff_$StringToAppendTofile.pdf
    rm selectionEffPlotConfig_$StringToAppendTofile.py
    fi

    done
done

echo "Loop over ctau and masses done!"

if [ 1 == 0 ]
then
# make the reco efficiency for electron and muon
sed -e 's/ToBeSet/allSample/' recoEffPlotConfig.py > recoEffPlotConfig_allSample.py
makeEfficiencyComparisonPlot.py -l recoEffPlotConfig_allSample.py -b 20 -f --pdf
mv efficiency_plot.root $1/recoEff_allSample.root
mv efficiency_plot.pdf $1/recoEff_allSample.pdf
rm recoEffPlotConfig_allSample.py

# make the selection efficiency for electron and muon 
sed -e 's/ToBeSet/allSample/' selectionEffPlotConfig.py > selectionEffPlotConfig_allSample.py
makeEfficiencyComparisonPlot.py -l selectionEffPlotConfig_allSample.py -b 10 -f --pdf
mv efficiency_plot.root $1/selectionEff_allSample.root
mv efficiency_plot.pdf $1/selectionEff_allSample.pdf
rm selectionEffPlotConfig_allSample.py
fi

echo "end of script!!!"
