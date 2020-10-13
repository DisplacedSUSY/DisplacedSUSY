#!/bin/tcsh

foreach i (100 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500 1600 1700 1800)
#foreach i (200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500 1600 1700 1800)
#foreach i (600 700 800 900 1000 1100 1200 1300 1400 1500 1600 1700 1800)
    #sed "s/XXX/$i/" crab_step4_stopToLD_M_XXX_0p1mm_2018MC.py > crab_step4_stopToLD_M_${i}_0p1mm_2018MC.py
    #sed "s/XXX/$i/" crab_step1_stopToBottom_M_XXX_0p1mm_2016MC.py > crab_step1_stopToBottom_M_${i}_0p1mm_2016MC.py
    #sed "s/XXX/$i/" crab_step1_stopToLD_M_XXX_0p1mm_2016MC.py > crab_step1_stopToLD_M_${i}_0p1mm_2016MC.py
    #sed "s/XXX/$i/" crab_step2_stopToLB_M_XXX_0p1mm_2016MC.py > crab_step2_stopToLB_M_${i}_0p1mm_2016MC.py
    #sed "s/XXX/$i/" crab_step2_stopToLD_M_XXX_0p1mm_2016MC.py > crab_step2_stopToLD_M_${i}_0p1mm_2016MC.py
    #sed "s/XXX/$i/" crab_step3_stopToLB_M_XXX_0p1mm_2016MC.py > crab_step3_stopToLB_M_${i}_0p1mm_2016MC.py
    #sed "s/XXX/$i/" crab_step3_stopToLD_M_XXX_0p1mm_2016MC.py > crab_step3_stopToLD_M_${i}_0p1mm_2016MC.py
    #sed "s/XXX/$i/" crab_step4_stopToLD_M_XXX_0p1mm_2016MC.py > crab_step4_stopToLD_M_${i}_0p1mm_2016MC.py
    #crab submit crab_step4_stopToLD_M_${i}_0p1mm_2018MC.py
    #crab submit crab_step1_stopToBottom_M_${i}_0p1mm_2016MC.py
    #crab submit crab_step1_stopToLD_M_${i}_0p1mm_2016MC.py
    #crab submit crab_step2_stopToLB_M_${i}_0p1mm_2016MC.py
    #crab submit crab_step2_stopToLD_M_${i}_0p1mm_2016MC.py
    #crab submit crab_step3_stopToLB_M_${i}_0p1mm_2016MC.py
    #crab submit crab_step3_stopToLD_M_${i}_0p1mm_2016MC.py
    crab submit crab_step4_stopToLD_M_${i}_0p1mm_2016MC.py
    #crab resubmit -d crab/crab_stopToLBottom_M_${i}_0p1mm_13TeV_2016MC_GenSim
    #cmsDriver.py Configuration/Generator/python/DisplacedSUSY_stopToBottom_M_${i}_0p1mm_TuneCUETP8M1_13TeV_pythia8_cff.py --fileout file:stopToLB.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM --magField 38T_PostLS1 --no_exec
    #cmsDriver.py Configuration/Generator/python/DisplacedSUSY_stopToLD_M_${i}_0p1mm_TuneCUETP8M1_13TeV_pythia8_cff.py --fileout file:stopToLD.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM --magField 38T_PostLS1 --no_exec
    #crab status -d crab/crab_stopToLBottom_M_${i}_0p1mm_13TeV_2016MC_GenSim
    #crab status -d crab/crab_stopToLD_M_${i}_0p1mm_13TeV_2016MC_GenSim
    #crab resubmit -d crab/crab_stopToLBottom_M_${i}_0p1mm_13TeV_2016MC_GenSim
    #crab resubmit -d crab/crab_stopToLD_M_${i}_0p1mm_13TeV_2016MC_GenSim
    #crab status -d crab/crab_stopToLB_M_${i}_0p1mm_13TeV_2016MC_DigiRawHlt
    #crab status -d crab/crab_stopToLD_M_${i}_0p1mm_13TeV_2018MC_DigiRawHlt #this is really 2016
    #crab resubmit -d crab/crab_stopToLD_M_${i}_0p1mm_13TeV_2018MC_DigiRawHlt #this is really 2016
    ##crab status -d crab/crab_stopToLB_M_${i}_0p1mm_13TeV_2016MC_Reco
    #crab resubmit -d crab/crab_stopToLB_M_${i}_0p1mm_13TeV_2016MC_Reco
    #crab status -d crab/crab_stopToLD_M_${i}_0p1mm_13TeV_2016MC_Reco
    ##crab status -d crab/crab_stopToLD_M_${i}_0p1mm_13TeV_2016MC_MiniAod
    #eosrm -r /eos/uscms/store/user/alimena/StopToLD_M_${i}_0p1mm_13TeV_2016MC/GenSim/
end
