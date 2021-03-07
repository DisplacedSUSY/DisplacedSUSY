#!/usr/bin/env python

# simple script to calculate the abcd estimate correction and systematic uncertainty in the
# most-prompt signal region following the procedure outlined in elog 1919

from DisplacedSUSY.Configuration.helperFunctions import propagateError

# specify extraploated ratios and their uncertainties
ratios = [0.42, 0.83]
errs   = [0.85, 0.85]

(avg_ratio, avg_err) = propagateError('sum', ratios[0], errs[0], ratios[1], errs[1])
(avg_ratio, avg_err) = (0.5*avg_ratio, 0.5*avg_err)
(avg_ratio, avg_err) = (round(avg_ratio, 2), round(avg_err, 2))

avg_ratio = avg_ratio if avg_ratio > 1 else 1.00

print "Correction: {} +- {}".format(avg_ratio, avg_err)
