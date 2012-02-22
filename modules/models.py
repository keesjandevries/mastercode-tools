#! /usr/bin/env python

import constraint_dict as cd
import lhood_dict as ld
import lhood_module as lhm
from math import sqrt


class Constraint( object ) :
    def __init__( self, l ) :
        self.mode  = l[2]  
        self.value = l[0]
        self.error = sqrt( sum( [x*x for x in l[1] ] ) )
        self.axis  = l[3]
    def __str__( self ) :
        s = "%s:%g +/- %g \"%s\"" % ( self.mode.ljust(7), self.value, self.error, self.axis )
        return s
    def get_name( self ) :
        return self.axis
    def get_n_sigma( self, val ) :
        n_sigma = 0
        if (self.mode == 'GAUSS') or (self.mode == 'UL' and val>self.value) or \
        (self.mode == 'LL' and val<self.value) :
            n_sigma = abs( val - self.value ) / self.error     
        return n_sigma
    def get_chi2( self, val ) :
        n_sigma = self.get_n_sigma( val )
        chi2 = n_sigma*n_sigma
        return chi2

class LHood( object ) :
    def __init__( self, var_pos, lh ) :
        self.var_pos = var_pos # i.e. [1,2] for m0,m12
        lh_type = lh[0]
        self.name = lh[2]
        if lh_type == "CONT" :
            self.LH = lhm.ContourLikelihood( *lh[1] )
        if lh_type == "LH1D" :
            self.LH = lhm.Likelihood1D( *lh[1] )

    def get_chi2( self, vals ) :
        args = [ vals[x] for x in self.var_pos ]
        chi2 = self.LH.getChi2( *args  )
        return chi2

def get_lhood_from_file( filename ) :
    d = ld.get_lhood_dict()

    out = {}
    with open(filename, 'rb') as f:
        for line in f :
            l = line.split()
            name = l[0]
            variables = l[1:]
            var_ints = [ int(x) for x in variables ]
            if name in d :
                out[name] = LHood( var_ints, d[name] )
    return out

def get_model_from_file( filename ) :
    d = cd.get_constraint_dict()
    
    out = {}
    with open(filename, 'rb') as f:
        for line in f :
            l = line.split()
            index = l[0]
            c_name = l[1]
            if c_name in d :
                out[int(index)] = Constraint( d[c_name] )   
            else :
                print ">", c_name, "< not in model"
    return out
