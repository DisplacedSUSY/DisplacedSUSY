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


# raise exception if cut or histogram definitions contain invalid attributes
# function expects a pset or vpset of either cuts or hists and assumes all members are the same type
def check_definitions(psets):

    valid_cut_attributes = [
        'inputCollection',
        'cutString',
        'alias',
        'numberRequired',
        'isVeto',
        '_isFrozen',
        '_ParameterTypeBase__isTracked',
        '_isModified',
        '_Parameterizable__parameterNames',
    ]

    valid_hist_attributes = [
        'name',
        'title',
        'binsX', 'binsY', 'binsZ',
        'indexX', 'indexY', 'indexZ',
        'inputVariables',
        '_isFrozen',
        '_ParameterTypeBase__isTracked',
        '_isModified',
        '_Parameterizable__parameterNames',
    ]

    invalid_defs = {}
    for pset in psets:
        if hasattr(pset, 'cuts'):
            def_type = 'cut'
            definitions = pset.cuts
            valid_attributes = valid_cut_attributes
        elif hasattr(pset, 'histograms'):
            def_type = 'hist'
            definitions = pset.histograms
            valid_attributes = valid_hist_attributes
        else:
            raise AttributeError("invalid pset has neither cuts nor hists: {}", pset)

        # find all cuts or hists with invalid attributes
        for d in definitions:
            attributes = d.__dict__.keys()
            invalid_attributes = list(set(attributes) - set(valid_attributes))
            if len(invalid_attributes) > 0:
                if def_type is 'cut':
                    name = d.alias if hasattr(d, 'alias') else d.cutString
                else:
                    name = d.name
                invalid_defs[str(name)[12:-2]] = invalid_attributes

    # if necessary, raise exception listing all cuts or hists with invalid attributes
    if invalid_defs:
        exception_string = ""
        for name, attributes in invalid_defs.iteritems():
            exception_string += "\n{} '{}' contains invalid attributes: {}".format(def_type, name, attributes)
        raise AttributeError(exception_string)
