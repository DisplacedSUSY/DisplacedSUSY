#!/bin/tcsh

foreach i (100 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500 1600 1700 1800)
    sed "s/XXX/$i/" crab_step4_stopToLD_M_XXX_0p1mm_2018MC.py > crab_step4_stopToLD_M_${i}_0p1mm_2018MC.py
    #crab submit crab_step4_stopToLD_M_${i}_0p1mm_2018MC.py
end
