#! /usr/bin/env python
from operator import mul

class MCSpace( object ) : # file specific object version of MCVariable
    def __init__( self, MCF, MCVs, options ) :
        assert len(MCVs) == len(options["nbins"]), \
            "Wrong number of Variables or Options to make a space"
        self.log = options.get( 'logaxes' ,[False]*len(MCVs)) # FIXME

        self.dimension   = len(MCVs)
        self.indices     = [ v.get_index(MCF) for v in MCVs ]
        self.min_vals    = [ r[0] for r in options["ranges"] ]
        self.max_vals    = [ r[1] for r in options["ranges"] ]
        self.names       = [ v.long_name for v in MCVs ]
        self.short_names = [ v.short_name for v in MCVs ]
        self.nbins       = options["nbins"]

        self.bins = reduce(mul, self.nbins)
        self.name = "( %s )" % ( ", ".join(self.names) )

    def __str__( self ) :
        return "(%s)" % " ,".join(self.short_names)

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

class MCContribution( object ) :
    def __init__( self, MCF, MCV ) :
        self.index = MCV.get_index(MCF)
        self.name = MCV.long_name
        self.short_name = MCV.short_name

    def __str__(self ):
        return self.short_name

    def __repr__( self):
        return "{:} {:} {:} ".format( self.short_name, self.index, self.name)
