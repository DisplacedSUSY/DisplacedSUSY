#!/usr/bin/env python
from math import sqrt

def propagateError(func, a, a_err, b, b_err):
    a = float(a)
    b = float(b)
    if func is "sum":
        return (a+b, sqrt(a_err**2 + b_err**2))
    elif func is "product":
        try:
            return (a*b, a*b * sqrt((a_err/a)**2 + (b_err/b)**2))
        except ZeroDivisionError:
            print "Division by 0!"
            return -1
    elif func is "quotient":
        try:
            return (a/b, a/b * sqrt((a_err/a)**2 + (b_err/b)**2))
        except ZeroDivisionError:
            print "Division by 0!"
            return -1
    else:
        print "Unrecognized function"
        return -1
