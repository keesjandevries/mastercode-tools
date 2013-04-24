#! /usr/bin/env python

import lhood_dict as ld
import constraint_dict as cd
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
                    var_ints = [ mcvars[varname].get_index(mcf) for varname in lhs[name]["vars"]  ]
                    out[name] = lhm.LHood( var_ints, lhs[name] )
                else :
                    print "Unknown Likelihood: %s, ignoring!" % name
        f.close()
    return out

def get_lhood_names( mcf ) :
    lhd = ld.get_lhood_dict()
    out = OrderedDict()
    mcvars=v.mc_variables()
    filename=getattr( mcf, "LHoodFile", None )
    if filename is not None :
        with open(filename, 'rb') as f:
            for line in f :
                name = line[:-1] #cut EOL
                out[name] = lhd[name]["name"] 
        f.close()
    return out

def get_model_from_file( mcf ) :
    d=cd.get_constraint_dict()
    out = []
    filename = getattr( mcf, "ModelFile" ) # fail cos this doesn't make any sense
    with open(filename, 'rb') as f:
        for line in f :
            constraint = line[:-1]
            if constraint in d :#FIXME: do we want to check here if the shortname for the contraint also exists?
                out.append(d[constraint])
            else :
                print ">", constraint, "< not in variable list (check modules/constraint_dict.py)"
    f.close()
    return out
