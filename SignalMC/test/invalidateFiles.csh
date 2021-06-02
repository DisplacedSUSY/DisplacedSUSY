#!/bin/tcsh
#first setup crab3
#then run this script with: source invalidateFiles.csh

# stau masses
#foreach i (50 100 200 300 400 500)

# slepton masses
#foreach i (50 100 200 300 400 500 600 700 800 900 1000)

# ctaus
#    foreach j (0p1 1 10 100 1000)

foreach i (50 100 200)
    foreach j (0p1 1 10 100 1000)
        echo ${i} ${j}
        dasgoclient -query="file dataset=/Sleptons_M_${i}_${j}mm_13TeV_2016MC/bcardwel-DigiRawHlt-d7be11d1b7ccd4eae71d369feee8910d/USER instance=prod/phys03" > listOfFilesToInvalidate_${i}_${j}mm.txt
        python $DBS3_CLIENT_ROOT/examples/DataOpsScripts/DBS3SetFileStatus.py --files=listOfFilesToInvalidate_${i}_${j}mm.txt --url=https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter --status=invalid --recursive=False
    end
end
