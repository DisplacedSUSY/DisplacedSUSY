#!/bin/tcsh

foreach i (200 1000)
    foreach j (0p1 10 1000)
	#cmsDriver.py Configuration/Generator/python/DisplacedSUSY_stopToLB_M_${i}_${j}mm_TuneCP5_13TeV_pythia8_withCloudModel_cff.py --fileout file:stopToLB${i}_${j}mm_withCloudModel.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN,SIM --nThreads 8 --geometry DB:Extended --era Run2_2018 --customise SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi.customise,DisplacedSUSY/SignalMC/genParticlePlusGeant.customizeKeep,DisplacedSUSY/SignalMC/genParticlePlusGeant.customizeProduce --no_exec
	sed "s/XXX/$i/" crab_step1_stopToLpi_M_XXX_YYYmm_withCloudModel_2018MC.py | sed "s/YYY/$j/" > crab_step1_stopToLpi_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab submit crab_step1_stopToLpi_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab status -d crab/crab_stopToLpi_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_GenSim
	#crab resubmit -d crab/crab_stopToLpi_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_GenSim

	#sed "s/XXX/$i/" crab_step2_stopToLpi_M_XXX_YYYmm_withCloudModel_2018MC.py | sed "s/YYY/$j/" > crab_step2_stopToLpi_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab submit crab_step2_stopToLpi_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab status -d crab/crab_stopToLpi_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_DigiRawHlt
	#crab resubmit -d crab/crab_stopToLpi_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_DigiRawHlt

	#sed "s/XXX/$i/" crab_step3_stopToLpi_M_XXX_YYYmm_withCloudModel_2018MC.py | sed "s/YYY/$j/" > crab_step3_stopToLpi_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab submit crab_step3_stopToLpi_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab status -d crab/crab_stopToLpi_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_Reco
	#crab resubmit -d crab/crab_stopToLpi_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_Reco

	#sed "s/XXX/$i/" crab_step4_stopToLpi_M_XXX_YYYmm_withCloudModel_2018MC.py | sed "s/YYY/$j/" > crab_step4_stopToLpi_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab submit crab_step4_stopToLpi_M_${i}_${j}mm_withCloudModel_2018MC.py
	#crab status -d crab/crab_stopToLpi_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_MiniAod
	#crab resubmit -d crab/crab_stopToLpi_M_${i}_${j}mm_13TeV_2018MC_withCloudModel_MiniAod
    end
end
