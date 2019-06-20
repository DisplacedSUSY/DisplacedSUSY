import os
from DisplacedSUSY.StandardAnalysis.Options import *

intLumi = 59740

default_datasets = [
    'ParkingBPH4_Run2018A',
]

print "normalizing MC to " + str(intLumi) + " 1/pb"

InputCondorArguments = {}
