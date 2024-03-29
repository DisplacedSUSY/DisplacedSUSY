#!/bin/tcsh
#taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVslepslep#NLO_NLL_any_single_generation_su

foreach i (50 100 200 300 400 500 600 700 800 900 1000) #selectrons and smuons
    if ($i == '50') then
        set xs=5.368
    endif
    if ($i == '100') then
        set xs=0.3657
    endif
    if ($i == '200') then
        set xs=0.03031
    endif
    if ($i == '300') then
        set xs=0.006254
    endif
    if ($i == '400') then
	set xs=0.001859
    endif
    if ($i == '500') then
	set xs=0.0006736
    endif
    if ($i == '600') then
	set xs=0.0002763
    endif
    if ($i == '700') then
	set xs=0.0001235
    endif
    if ($i == '800') then
	set xs=5.863e-05
    endif
    if ($i == '900') then
	set xs=2.918e-05
    endif
    if ($i == '1000') then
	set xs=1.504e-05
    endif

    foreach j (0p01 0p1 1 10 100 1000 10000)
	if ($j == '0p01') then
	    set exp=11
	endif
	if ($j == '0p1') then
	    set exp=12
	endif
	if ($j == '1') then
	    set exp=13
	endif
	if ($j == '10') then
	    set exp=14
	endif
	if ($j == '100') then
	    set exp=15
	endif
	if ($j == '1000') then
	    set exp=16
	endif
	if ($j == '10000') then
	    set exp=17
	endif

	if ($j == '0p01') then
	    sed "s/XXX/$i/" Sleptons_M_XXX_YYYmm_TuneCP5_13TeV_pythia8_2017_cff.py | sed "s/YYY/0.01/" | sed "s/ZZZ/$xs/" | sed "s/AAA/$exp/" | sed "s/BBB/$j/" > Sleptons_M_${i}_${j}mm_TuneCP5_13TeV_pythia8_2017_cff.py
	    sed "s/XXX/$i/" ../../data/geant4_sleptons_XXX_YYYmm.txt | sed "s/YYY/0.01/" | sed "s/AAA/$exp/" > ../../data/geant4_sleptons_${i}_${j}mm.txt

	else if ($j == '0p1') then
	    sed "s/XXX/$i/" Sleptons_M_XXX_YYYmm_TuneCP5_13TeV_pythia8_2017_cff.py | sed "s/YYY/0.1/" | sed "s/ZZZ/$xs/" | sed "s/AAA/$exp/" | sed "s/BBB/$j/" > Sleptons_M_${i}_${j}mm_TuneCP5_13TeV_pythia8_2017_cff.py
	    sed "s/XXX/$i/" ../../data/geant4_sleptons_XXX_YYYmm.txt | sed "s/YYY/0.1/" | sed "s/AAA/$exp/" > ../../data/geant4_sleptons_${i}_${j}mm.txt

	else
	    sed "s/XXX/$i/" Sleptons_M_XXX_YYYmm_TuneCP5_13TeV_pythia8_2017_cff.py | sed "s/YYY/$j/" | sed "s/ZZZ/$xs/" | sed "s/AAA/$exp/" | sed "s/BBB/$j/" > Sleptons_M_${i}_${j}mm_TuneCP5_13TeV_pythia8_2017_cff.py
	    sed "s/XXX/$i/" ../../data/geant4_sleptons_XXX_YYYmm.txt | sed "s/YYY/$j/" | sed "s/AAA/$exp/" > ../../data/geant4_sleptons_${i}_${j}mm.txt

	endif
    end
end
