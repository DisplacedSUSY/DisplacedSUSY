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
    for ctau in 1 100 10000
    do
    totSedString="$beginSedStrig$CoreSedString$M$CoreSedString2$ctau$CoreSedString3$endSedString"
    StringToAppendTofile="$stringM$M$stringctau$ctau"
    echo "Processing $M $ctau"

    ### make the turn on curves for the 3 different signal regions
    # for the electron
    sed -e $totSedString el_3D0_SignalVarPlotConfig.py > el_3D0_SignalVarPlotConfig_$StringToAppendTofile.py
    makeEfficiencyComparisonPlot.py -l el_3D0_SignalVarPlotConfig_$StringToAppendTofile.py --pdf
    mv efficiency_plot.root ModelTestingPlotOutput/el_3D0_$StringToAppendTofile.root
    mv efficiency_plot.pdf ModelTestingPlotOutput/el_3D0_$StringToAppendTofile.pdf
    rm el_3D0_SignalVarPlotConfig_$StringToAppendTofile.py
    # for the muon
    sed -e $totSedString mu_3D0_SignalVarPlotConfig.py > mu_3D0_SignalVarPlotConfig_$StringToAppendTofile.py
    makeEfficiencyComparisonPlot.py -l mu_3D0_SignalVarPlotConfig_$StringToAppendTofile.py --pdf
    mv efficiency_plot.root ModelTestingPlotOutput/mu_3D0_$StringToAppendTofile.root
    mv efficiency_plot.pdf ModelTestingPlotOutput/mu_3D0_$StringToAppendTofile.pdf
    rm mu_3D0_SignalVarPlotConfig_$StringToAppendTofile.py
    ###

    # make the turn on curves for the cut on the muon and the electron
    sed -e $totSedString muon_el_SignalVarPlotConfig.py > muon_el_SignalVarPlotConfig_$StringToAppendTofile.py
    makeEfficiencyComparisonPlot.py -l muon_el_SignalVarPlotConfig_$StringToAppendTofile.py --pdf
    mv efficiency_plot.root ModelTestingPlotOutput/muon_el_cut_$StringToAppendTofile.root
    mv efficiency_plot.pdf ModelTestingPlotOutput/muon_el_cut_$StringToAppendTofile.pdf
    rm muon_el_SignalVarPlotConfig_$StringToAppendTofile.py
    done
done
