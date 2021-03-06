#!/bin/tcsh

foreach i (200 1000 1800)
    foreach j (0p01 0p1 1 10 100 1000 10000)
	#sed "s/XXX/$i/" crab_step1_stopToLB_M_XXX_YYYmm_withCloudModel_2018MC.py | sed "s/YYY/$j/" > crab_step1_stopToLB_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab submit crab_step1_stopToLB_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab status -d crab/crab_stopToLB_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_GenSim
	#crab resubmit -d crab/crab_stopToLB_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_GenSim

	#sed "s/XXX/$i/" crab_step2_stopToLB_M_XXX_YYYmm_withCloudModel_2018MC.py | sed "s/YYY/$j/" > crab_step2_stopToLB_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab submit crab_step2_stopToLB_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab status -d crab/crab_stopToLB_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_DigiRawHlt
	#crab resubmit -d crab/crab_stopToLB_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_DigiRawHlt

	#sed "s/XXX/$i/" crab_step3_stopToLB_M_XXX_YYYmm_withCloudModel_2018MC.py | sed "s/YYY/$j/" > crab_step3_stopToLB_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab submit crab_step3_stopToLB_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab status -d crab/crab_stopToLB_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_Reco
	#crab resubmit -d crab/crab_stopToLB_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_Reco

	#sed "s/XXX/$i/" crab_step4_stopToLB_M_XXX_YYYmm_withCloudModel_2018MC.py | sed "s/YYY/$j/" > crab_step4_stopToLB_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab submit crab_step4_stopToLB_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab status -d crab/crab_stopToLB_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_MiniAod
	#crab resubmit -d crab/crab_stopToLB_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_MiniAod
    end
end
