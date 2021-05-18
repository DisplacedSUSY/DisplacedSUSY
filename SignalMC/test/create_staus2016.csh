#!/bin/tcsh

foreach i (100 200 300 400 500) #staus prioritize these
#foreach i (50 150 250 350 450) #staus then maybe do these
   foreach j (0p1 1 10 100 1000) #prioritize these
   #foreach j (0p01 10000) #then maybe do these
	cmsDriver.py Configuration/Generator/python/Staus_M_${i}_${j}mm_TuneCUETP8M1_13TeV_pythia8_cff.py --fileout file:staus${i}_${j}mm.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi.customise,DisplacedSUSY/SignalMC/genParticlePlusGeant.customizeKeep,DisplacedSUSY/SignalMC/genParticlePlusGeant.customizeProduce --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN,SIM --magField 38T_PostLS1 --no_exec
        sed -i "s/process.generation_step = cms.Path(process.pgen)/process.generation_step = cms.Path(process.pgen+process.leptonicTauDecayGenFilter)/" Staus_M_${i}_${j}mm_TuneCUETP8M1_13TeV_pythia8_cff_py_LHE_GEN_SIM.py
        sed "s/XXX/$i/" crab_step1_staus_M_XXX_YYYmm_2016MC.py | sed "s/YYY/$j/" > crab_step1_staus_M_${i}_${j}mm_2016MC.py
        #bash -c "crab submit --proxy=`voms-proxy-info -path` crab_step1_staus_M_${i}_${j}mm_2016MC.py"
        #bash -c "crab status  --proxy=`voms-proxy-info -path` -d crab/crab_staus_leptonFilter_M_${i}_${j}mm_13TeV_2016MC_GenSim"
        #bash -c "crab resubmit  --proxy=`voms-proxy-info -path` --sitewhitelist T1_US_FNAL,T2_US_Nebraska,T2_US_Vanderbilt -d crab/crab_staus_leptonFilter_M_${i}_${j}mm_13TeV_2016MC_GenSim"

        #sed "s/XXX/$i/" crab_step2_staus_M_XXX_YYYmm_2016MC.py | sed "s/YYY/$j/" > crab_step2_staus_M_${i}_${j}mm_2016MC.py
        #crab submit crab_step2_staus_M_${i}_${j}mm_2016MC.py
        #crab status -d crab/crab_staus_leptonFilter_M_${i}_${j}mm_13TeV_2016MC_DigiRawHlt
        #crab resubmit -d crab/crab_staus_leptonFilter_M_${i}_${j}mm_13TeV_2016MC_DigiRawHlt --sitewhitelist T1_US_FNAL,T2_US_Nebraska,T2_US_Vanderbilt

	#sed "s/XXX/$i/" crab_step3_staus_M_XXX_YYYmm_2016MC.py | sed "s/YYY/$j/" > crab_step3_staus_M_${i}_${j}mm_2016MC.py
	#crab submit crab_step3_staus_M_${i}_${j}mm_2016MC.py
	#crab status -d crab/crab_staus_M_${i}_${j}mm_13TeV_2016MC_Reco
	#crab resubmit -d crab/crab_staus_M_${i}_${j}mm_13TeV_2016MC_Reco --sitewhitelist T1_US_FNAL,T2_US_Nebraska,T2_US_Vanderbilt

	#sed "s/XXX/$i/" crab_step4_staus_M_XXX_YYYmm_2016MC.py | sed "s/YYY/$j/" > crab_step4_staus_M_${i}_${j}mm_2016MC.py
	#crab submit crab_step4_staus_M_${i}_${j}mm_2016MC.py
	#crab status -d crab/crab_staus_M_${i}_${j}mm_13TeV_2016MC_MiniAod
	#crab resubmit -d crab/crab_staus_M_${i}_${j}mm_13TeV_2016MC_MiniAod --sitewhitelist T1_US_FNAL,T2_US_Nebraska,T2_US_Vanderbilt
    end
end
