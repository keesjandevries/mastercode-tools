#! /usr/bin/env python

import lhood_dict as ld
import lhood_module as lhm
import variables as v

from math import sqrt

def get_lhood_from_file( mcf ) :
    d = ld.get_lhood_dict()
    mcvars=v.mc_variables()
    out = {}
    filename=getattr( mcf, "LHoodFile", None )
    if filename is not None :
        with open(filename, 'rb') as f:
            for line in f :
                l = line.split()
                name = l[0]
                var_ints = [ mcvars[x].getIndex(mcf) for x in l[1:] ]
                if name in d :
                    out[name] = lhm.LHood( var_ints, d[name] )
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
