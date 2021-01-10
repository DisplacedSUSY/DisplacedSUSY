#!/usr/bin/env python

# simple script to calculate the abcd estimate correction and systematic uncertainty in the
# most-prompt signal region following the procedure outlined in elog 1852

from DisplacedSUSY.Configuration.helperFunctions import propagateError

# specify extraploated ratios and their uncertainties
ratios = [1.36, 2.02]
errs   = [0.66, 0.79]

(avg_ratio, avg_err) = propagateError('sum', ratios[0], errs[0], ratios[1], errs[1])
(avg_ratio, avg_err) = (0.5*avg_ratio, 0.5*avg_err)
(avg_ratio, avg_err) = (round(avg_ratio, 2), round(avg_err, 2))

if avg_ratio >= 1:
    print "Correction: {} +- {}".format(avg_ratio, avg_err)
else:
    err_hi = (avg_ratio + avg_err) - 1
    err_lo = 1 - (avg_ratio - avg_err)
    if err_lo > 1:
        err_lo = 1.00
    print "Correction: 1.00 +{}-{}".format(err_hi, err_lo)
