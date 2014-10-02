###                                                                                        
### This macro create plot to compare the 4 histograms that will be used for the reweighting (do not create the histograms them self, use create_relevantReweighingHisto.sh for that) for all the different sample.                                                            
### needs one argument, which the name of the output condor dir. It will put all the plot under the same directory in the current directory.                                         
### needs two config files recoEffPlotConfig.py and selectionEffPlotConfig.py
### uses example                                                                           
### source create_relevantReweighingHisto.sh ModelTestingMoreCTau                          
###


# To change the condor directory 
### Some string that will be use to sed the conginf files
### first the "cst" string

# Begining Of String (BOS) 
BOS='s/'
# Equals sign Followed By Any string (EFBA)
EFBA='=.*/'
# Equals Sign (ES)
ES='='
# End Of String (EOS) 
EOS='/g'

# Single Ket (SK)
SK="'"

# Create the output directory
mkdir $1

### To change condor_dir
# Search For (SF) this is fixed
SF_Cond='scondor_dir'
Comp_SF_Cond=$SF_Cond$EFBA$SF_Cond
## Replacement String (RS) this the variable to be set 
RS_Cond=$1
Comp_RS_Cond=$SK$RS_Cond$SK
TOT_Cond=$BOS$Comp_SF_Cond$ES$Comp_RS_Cond$EOS
echo $TOT_Cond

sed -i $TOT_Cond SameCtauAllMass.py
sed -i $TOT_Cond SameMassAllCtau.py


### To change the Initial channel
# Search For (SF) this is fixed
SF_Init='sMcInitialChannel'
Comp_SF_Init=$SF_Init$EFBA$SF_Init
## Replacement String (RS) this the variable to be set 
RS_Init='McPartInitial'
Comp_RS_Init=$SK$RS_Init$SK
TOT_Init=$BOS$Comp_SF_Init$ES$Comp_RS_Init$EOS
echo $TOT_Init


### To change the efficiency type 
# Search For (SF) this is fixed
SF_EffType='sefficiencyType'
Comp_SF_EffType=$SF_EffType$EFBA$SF_EffType
## Replacement String (RS) this the variable to be set 
RS_EffType='noeff'
Comp_RS_EffType=$SK$RS_EffType$SK
TOT_EffType=$BOS$Comp_SF_EffType$ES$Comp_RS_EffType$EOS
echo $TOT_EffType



## To change the Ctau in the fixed mass plots
# Search For (SF) this is fixed
SF_Ctau='sCtau'
Comp_SF_Ctau=$SF_Ctau$EFBA$SF_Ctau
## Replacement String (RS) this the variable to be set
RS_Ctau='noctau'
Comp_RS_Ctau=$SK$RS_Ctau$SK
TOT_Ctau=$BOS$Comp_SF_Ctau$ES$Comp_RS_Ctau$EOS
echo $TOT_Ctau	


## To change the Mass in the fixed Ctau plots
# Search For (SF) this is fixed
SF_Mass='sMass'
Comp_SF_Mass=$SF_Mass$EFBA$SF_Mass
## Replacement String (RS) this the variable to be set
RS_Mass='mas'
Comp_RS_Mass=$SK$RS_Mass$SK
TOT_Mass=$BOS$Comp_SF_Mass$ES$Comp_RS_Mass$EOS
echo $TOT_Mass	


## To change the name of the outputfile
CoreSameCtau="Ctau"
CoreSameMass="Mass"

for efficiency_type in el_reco mu_reco el_sel mu_sel
    do
    RS_EffType=$efficiency_type
    Comp_RS_EffType=$SK$RS_EffType$SK
    TOT_EffType=$BOS$Comp_SF_EffType$ES$Comp_RS_EffType$EOS
    sed -i $TOT_EffType SameCtauAllMass.py
    sed -i $TOT_EffType SameMassAllCtau.py
    for Ctau in 1 10 100 1000
	do 
	echo "process" $efficiency_type $Ctau
	RS_Ctau=$Ctau
	Comp_RS_Ctau=$SK$RS_Ctau$SK
	TOT_Ctau=$BOS$Comp_SF_Ctau$ES$Comp_RS_Ctau$EOS
	sed -i $TOT_Ctau SameCtauAllMass.py
	OutputSameCtau=$efficiency_type$CoreSameCtau$Ctau
	makeEfficiencyComparisonPlot.py -l SameCtauAllMass.py -b 20 --pdf
	mv efficiency_plot.root $1/$OutputSameCtau.root
	mv efficiency_plot.pdf $1/$OutputSameCtau.pdf
	done
	echo "Loop over Ctau is finished!!!"

    for Mass in 200 600 1000
	do 
	echo "process" $efficiency_type $Mass
	RS_Mass=$Mass
	Comp_RS_Mass=$SK$RS_Mass$SK
	TOT_Mass=$BOS$Comp_SF_Mass$ES$Comp_RS_Mass$EOS
	sed -i $TOT_Mass SameMassAllCtau.py
	OutputSameMass=$efficiency_type$CoreSameMass$Mass
	makeEfficiencyComparisonPlot.py -l SameMassAllCtau.py -b 20 --pdf
	mv efficiency_plot.root $1/$OutputSameMass.root
	mv efficiency_plot.pdf $1/$OutputSameMass.pdf
	done
	echo "Loop over Mass is finished!!!"
    done


echo "adding cutflow table"
cp condor/$1/cutFlow.pdf $1/cutFlow.pdf
