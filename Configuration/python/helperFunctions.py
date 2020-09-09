#!/usr/bin/env python
from math import sqrt
import FWCore.ParameterSet.Config as cms

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

# make cut to filter a given object collection to only include objects that would pass a predefined
# selection without removing events; only cuts with a single input collection are supported
def make_selection_filter(physics_object, selection, alias):

    # get cutstring without the 'cms.string()'
    def get_cutstring(cut):
       return str(cut.cutString)[12:-2]

    # get all selection cuts where specified object is sole inputCollection
    object_cuts = [c for c in selection.cuts if physics_object in c.inputCollection]
    filter_cuts = [get_cutstring(c) for c in object_cuts if len(c.inputCollection) == 1]

    # build cutstring
    filter_cutstring = "({})".format(filter_cuts[0])
    for c in filter_cuts[1:]:
        filter_cutstring += " & ({})".format(c)

    return cms.PSet(
        inputCollection = cms.vstring(physics_object),
        cutString = cms.string(filter_cutstring),
        numberRequired = cms.string(">= 0"),
        alias = cms.string(alias)
        )
