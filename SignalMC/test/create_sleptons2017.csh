#!/bin/tcsh

#selectrons and smuons
foreach i (50 100 200 300 400) #bryan
#foreach i (500 600 700 800 900) #juliette
    foreach j (0p1 1 10 100 1000) #prioritize these
    #foreach j (0p01 10000) #then maybe do these
	cmsDriver.py Configuration/Generator/python/Sleptons_M_${i}_${j}mm_TuneCP5_13TeV_pythia8_2017_cff.py --fileout file:sleptons${i}_${j}mm.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN,SIM --geometry DB:Extended --era Run2_2017 --customise SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi.customise,DisplacedSUSY/SignalMC/genParticlePlusGeant.customizeKeep,DisplacedSUSY/SignalMC/genParticlePlusGeant.customizeProduce --no_exec
	#sed "s/XXX/$i/" crab_step1_sleptons_M_XXX_YYYmm_2017MC.py | sed "s/YYY/$j/" > crab_step1_sleptons_M_${i}_${j}mm_2017MC.py
	#crab submit crab_step1_sleptons_M_${i}_${j}mm_2017MC.py
	#crab status -d crab/crab_sleptons_M_${i}_${j}mm_13TeV_2017MC_GenSim
	#crab resubmit -d crab/crab_sleptons_M_${i}_${j}mm_13TeV_2017MC_GenSim --sitewhitelist T1_US_FNAL,T2_US_Nebraska,T2_US_Vanderbilt

	#sed "s/XXX/$i/" crab_step2_sleptons_M_XXX_YYYmm_2017MC.py | sed "s/YYY/$j/" > crab_step2_sleptons_M_${i}_${j}mm_2017MC.py
	#crab submit crab_step2_sleptons_M_${i}_${j}mm_2017MC.py
	#crab status -d crab/crab_sleptons_M_${i}_${j}mm_13TeV_2017MC_DigiRawHlt
	#crab resubmit -d crab/crab_sleptons_M_${i}_${j}mm_13TeV_2017MC_DigiRawHlt --sitewhitelist T1_US_FNAL,T2_US_Nebraska,T2_US_Vanderbilt

	#sed "s/XXX/$i/" crab_step3_sleptons_M_XXX_YYYmm_2017MC.py | sed "s/YYY/$j/" > crab_step3_sleptons_M_${i}_${j}mm_2017MC.py
	#crab submit crab_step3_sleptons_M_${i}_${j}mm_2017MC.py
	#crab status -d crab/crab_sleptons_M_${i}_${j}mm_13TeV_2017MC_Reco
	#crab resubmit -d crab/crab_sleptons_M_${i}_${j}mm_13TeV_2017MC_Reco --sitewhitelist T1_US_FNAL,T2_US_Nebraska,T2_US_Vanderbilt

	#sed "s/XXX/$i/" crab_step4_sleptons_M_XXX_YYYmm_2017MC.py | sed "s/YYY/$j/" > crab_step4_sleptons_M_${i}_${j}mm_2017MC.py
	#crab submit crab_step4_sleptons_M_${i}_${j}mm_2017MC.py
	#crab status -d crab/crab_sleptons_M_${i}_${j}mm_13TeV_2017MC_MiniAod
	#crab resubmit -d crab/crab_sleptons_M_${i}_${j}mm_13TeV_2017MC_MiniAod --sitewhitelist T1_US_FNAL,T2_US_Nebraska,T2_US_Vanderbilt
    end
end
