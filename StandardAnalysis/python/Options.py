#!/usr/bin/env python
import os

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *
    print "using 80X samples"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    from DisplacedSUSY.Configuration.miniAODV2_94X_Samples import *
    print "using 94X samples"
else:
    print "What CMSSW release are you in? We expect the samples to be imported from the 80X or 94X list"

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

InputCondorArguments = {}
