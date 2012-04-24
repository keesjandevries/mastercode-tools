#! /usr/bin/env python
from operator import mul

class Space( object ) :
    def __init__( self, indices = [], min_vals = [], max_vals = [], nbins = [],
                  names = [], log = [], short_names = [] ) :
        assert len(indices) == len(min_vals) ==  len( max_vals ) == \
            len( nbins ) == len( names ) == len( log ), \
            "Must initialize space with lists of equal length"

        self.dimension = len(indices)
        for o in ["indices", "min_vals", "max_vals", "nbins", "names", "log", "short_names"] :
            exec("self.%s = %s" % ( o, o ) )

        self.bins = reduce(mul, nbins)
        self.name = "( %s )" % ( ", ".join(self.names) )

    def __str__( self ) :
        return self.name

    def __repr__( self ) :
        r_f = "(%s) %s" + ("[%4.2e, %4.2e]{%d}")*self.dimension
        l = []
        [ l.extend( [ smin, smax, sbin ] ) for smin, smax, sbin in 
            zip (self.min_vals, self.max_vals, self.nbins ) ]
        return r_f % tuple(  [", ".join( [ str(index) for index in self.indices ] ), self.name] + l )

    def get_indices( self ) :
        return self.indices

    def get_bins( self ) :
        return self.bins
