#!/bin/tcsh
#taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVslepslep#NLO_NLL_any_single_generation_su

foreach i (50 100 150 200 250 300 350 400 450 500) #staus
    if ($i == '50') then
        set xs=5.368
    endif
    if ($i == '100') then
        set xs=0.3657
    endif
    if ($i == '150') then
        set xs=0.08712
    endif
    if ($i == '200') then
        set xs=0.03031
    endif
    if ($i == '250') then
        set xs=0.01292
    endif
    if ($i == '300') then
        set xs=0.006254
    endif
    if ($i == '350') then
        set xs=0.002931
    endif
    if ($i == '400') then
	set xs=0.001859
    endif
    if ($i == '450') then
	set xs=0.001216
    endif
    if ($i == '500') then
	set xs=0.0006736
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
	    sed "s/XXX/$i/" Staus_M_XXX_YYYmm_TuneCUETP8M1_13TeV_pythia8_cff.py | sed "s/YYY/0.01/" | sed "s/ZZZ/$xs/" | sed "s/AAA/$exp/" | sed "s/BBB/$j/" > Staus_M_${i}_${j}mm_TuneCUETP8M1_13TeV_pythia8_cff.py
	    sed "s/XXX/$i/" ../../data/geant4_staus_XXX_YYYmm.txt | sed "s/YYY/0.01/" | sed "s/AAA/$exp/" > ../../data/geant4_staus_${i}_${j}mm.txt

	else if ($j == '0p1') then
	    sed "s/XXX/$i/" Staus_M_XXX_YYYmm_TuneCUETP8M1_13TeV_pythia8_cff.py | sed "s/YYY/0.1/" | sed "s/ZZZ/$xs/" | sed "s/AAA/$exp/" | sed "s/BBB/$j/" > Staus_M_${i}_${j}mm_TuneCUETP8M1_13TeV_pythia8_cff.py
	    sed "s/XXX/$i/" ../../data/geant4_staus_XXX_YYYmm.txt | sed "s/YYY/0.1/" | sed "s/AAA/$exp/" > ../../data/geant4_staus_${i}_${j}mm.txt

	else
	    sed "s/XXX/$i/" Staus_M_XXX_YYYmm_TuneCUETP8M1_13TeV_pythia8_cff.py | sed "s/YYY/$j/" | sed "s/ZZZ/$xs/" | sed "s/AAA/$exp/" | sed "s/BBB/$j/" > Staus_M_${i}_${j}mm_TuneCUETP8M1_13TeV_pythia8_cff.py
	    sed "s/XXX/$i/" ../../data/geant4_staus_XXX_YYYmm.txt | sed "s/YYY/$j/" | sed "s/AAA/$exp/" > ../../data/geant4_staus_${i}_${j}mm.txt

	endif
    end
end
