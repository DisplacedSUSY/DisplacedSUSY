###                                                                                   
### This macro will run many times SinglePlot.py in order to compare the distribution of reco lepton with gen-level lepton after the closure test.

### needs one argument, which the name of the output condor where the ClosureTest was run
#It will put all the plot under the same directory name in the current directory.
### needs four confing files: el_d0_samplePlotConfig.py, el_pt_samplePlotConfig.py, mu_d0_samplePlotConfig.py and mu_pt_samplePlotConfig.py
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
beginSedStringCond='s/scondor_dir2=.*/'
endSedStringCond='/g'
scondordir=$1  # This parameter is set to the first argument of the script                                                                                                         
singleket="'"
scondor_dir2="scondor_dir2="
totSedStringCond="$beginSedStringCond$scondor_dir2$singleket$scondordir$singleket$endSedStringCond"
##                                                                                                                                                                                 

# Edit all the config files to put the right condor_dir                                                                                                                            
sedmu_d0_samplePlotConfig.py -i $totSedStringCond el_d0_samplePlotConfig.py
sed -i $totSedStringCond el_pt_samplePlotConfig.py
sed -i $totSedStringCond mu_d0_samplePlotConfig.py
sed -i $totSedStringCond mu_pt_samplePlotConfig.py



mkdir $1

# loop on the masses    
for M in 200 600 1000 # All
do
    # loop on the ctaus
    for ctau in 1 10 100 1000 # All
    do
    totSedString="$beginSedStrig$CoreSedString$M$CoreSedString2$ctau$CoreSedString3$endSedString"
    StringToAppendTofile="$stringM$M$stringctau$ctau"
    echo "Processing $M $ctau"

    if [ 0 == 0 ]
    then
    # el d0 comparison
    sed -e $totSedString el_d0_samplePlotConfig.py > el_d0_samplePlotConfig_$StringToAppendTofile.py
    makeSinglePlot.py -l el_d0_samplePlotConfig_$StringToAppendTofile.py -b 20 -r --pdf
    mv simple_plot.root $1/el_d0$StringToAppendTofile.root
    mv simple_plot.pdf $1/el_d0$StringToAppendTofile.pdf
    rm el_d0_samplePlotConfig_$StringToAppendTofile.py

    # el pt comparison
    sed -e $totSedString el_pt_samplePlotConfig.py > el_pt_samplePlotConfig_$StringToAppendTofile.py
    makeSinglePlot.py -l el_pt_samplePlotConfig_$StringToAppendTofile.py -b 20 -r --pdf
    mv simple_plot.root $1/el_pt$StringToAppendTofile.root
    mv simple_plot.pdf $1/el_pt$StringToAppendTofile.pdf
    rm el_pt_samplePlotConfig_$StringToAppendTofile.py
    fi

    if [ 0 == 0 ]
    then
    # mu d0 comparison  
    sed -e $totSedString mu_d0_samplePlotConfig.py > mu_d0_samplePlotConfig_$StringToAppendTofile.py
    makeSinglePlot.py -l mu_d0_samplePlotConfig_$StringToAppendTofile.py -b 10 -r --pdf
    mv simple_plot.root $1/mu_d0_$StringToAppendTofile.root
    mv simple_plot.pdf $1/mu_d0_$StringToAppendTofile.pdf
    rm mu_d0_samplePlotConfig_$StringToAppendTofile.py

    # mu pt comparison
    sed -e $totSedString mu_pt_samplePlotConfig.py > mu_pt_samplePlotConfig_$StringToAppendTofile.py
    makeSinglePlot.py -l mu_pt_samplePlotConfig_$StringToAppendTofile.py -b 10 -r --pdf
    mv simple_plot.root $1/mu_pt_$StringToAppendTofile.root
    mv simple_plot.pdf $1/mu_pt_$StringToAppendTofile.pdf
    rm mu_pt_samplePlotConfig_$StringToAppendTofile.py
    fi

    done
done

echo "Loop over ctau and masses done!"


### The following part will probably crash as it has not been updated

if [ 1 == 0 ]
then
### Missing some stuff here!!!!!!!
### !!!!!!!!!!!!!!!!!!!!!

# make the reco efficiency for electron and muon
sed -e 's/ToBeSet/allSample/' recoEffPlotConfig.py > recoEffPlotConfig_allSample.py
makeSinglePlot.py -l recoEffPlotConfig_allSample.py -b 20 -r -f --pdf
mv simple_plot.root $1/recoEff_allSample.root
mv simple_plot.pdf $1/recoEff_allSample.pdf
rm recoEffPlotConfig_allSample.py

# make the selection efficiency for electron and muon 
sed -e 's/ToBeSet/allSample/' selectionEffPlotConfig.py > selectionEffPlotConfig_allSample.py
makeSinglePlot.py -l selectionEffPlotConfig_allSample.py -b 10 -r -f --pdf
mv simple_plot.root $1/selectionEff_allSample.root
mv simple_plot.pdf $1/selectionEff_allSample.pdf
rm selectionEffPlotConfig_allSample.py
fi

echo "end of script!!!"
