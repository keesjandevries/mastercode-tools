#! /usr/bin/env python

import lhood_dict as ld
import lhood_module as lhm
import variables as v

from math import sqrt
from collections import OrderedDict

def get_lhood_from_file( mcf ) :
    lhs = ld.get_lhood_dict()
    mcvars=v.mc_variables()
    out = OrderedDict()
    filename=getattr( mcf, "LHoodFile", None )
    if filename is not None :
        with open(filename, 'rb') as f:
            for line in f :
                name = line[:-1] #cut EOL
                if name in lhs :
                    var_ints = [ mcvars[varname].getIndex(mcf) for varname in lhs[name]["vars"]  ]
                    out[name] = lhm.LHood( var_ints, lhs[name] )
                else :
                    print "Unknown Likelihood: %s, ignoring!" % name
    return out

def get_model_from_file( mcf ) :
    d = v.mc_variables()
    out = []
    filename = getattr( mcf, "ModelFile" ) # fail cos this doesn't make any sense
    with open(filename, 'rb') as f:
        for line in f :
            constraint = line[:-1]
            if constraint in d :
                out.append(d[constraint])
            else :
                print ">", constraint, "< not in variable list (check modules/variables.py)"
    return out
