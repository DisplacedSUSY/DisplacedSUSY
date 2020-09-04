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

# make cut to veto a given physics object that passes a predefined selection and one extra cut
# currently skips cuts in which the same object appears more than once in inputCollection
def make_overlap_veto(physics_object, selection, extra_cut, alias):

    # get cutstring and without the 'cms.string()'
    def get_cutstring(cut):
       return str(cut.cutString)[12:-2]

    # get all selection cuts where physics object appears exactly once in inputCollection
    object_cuts = [c for c in selection.cuts if c.inputCollection.count(physics_object) == 1]
    veto_cuts = object_cuts + [extra_cut]

    # build veto inputCollection and cutstring
    veto_input_collections = set()
    veto_cutstring = "({})".format(get_cutstring(veto_cuts[0]))
    for c in veto_cuts[1:]:
        veto_input_collections.update(c.inputCollection)
        veto_cutstring += " & ({})".format(get_cutstring(c))

    return cms.PSet(
        inputCollection = cms.vstring(veto_input_collections),
        cutString = cms.string(veto_cutstring),
        numberRequired = cms.string("== 0"),
        alias = cms.string(alias)
        )
