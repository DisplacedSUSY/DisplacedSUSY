import os

#enable git hooks
os.system("ln -s $CMSSW_BASE/src/OSUT3Analysis/githooks/* $CMSSW_BASE/src/DisplacedSUSY/.git/hooks/")
