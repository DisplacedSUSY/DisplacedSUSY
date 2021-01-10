#!/usr/bin/env python

# simple script to calculate the abcd estimate systematic uncertainty in the more-displaced signal
# regions following the procedure outlined in elog 1860

# specify closure test results as (ratio, err_lo, err_hi)
ratio1 = (1.79, 0.74, 0.61)
ratio2 = (0.46, 0.20, 0.26)

def get_deviation(ratio):
    return [abs(ratio1[0] - ratio1[1] - 1), abs(ratio1[0] + ratio1[2] - 1)]

max_deviation = max(get_deviation(ratio1) + get_deviation(ratio2))

print "systematic:", round(max_deviation, 2)
