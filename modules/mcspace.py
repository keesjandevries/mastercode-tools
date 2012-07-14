#! /usr/bin/env python
from operator import mul

class MCSpace( object ) : # file specific object version of MCVariable
    def __init__( self, MCF, Vars, options ) :
        # MCSpace based on Variable instead of MCVariable. Hence the fact that mcf is now an attribute, and an MCSPace has no more indicis
        assert len(Vars) == len(options["nbins"]), \
            "Wrong number of Variables or Options to make a space"
        self.log = options.get( 'logaxes' ,[False]*len(Vars)) # FIXME

        self.KOhack      = options.get('KOhack',False)
        self.noxenon2011 = options.get('noxenon2011',False)
        self.dimension   = len(Vars)
        self.min_vals    = [ r[0] for r in options["ranges"] ]
        self.max_vals    = [ r[1] for r in options["ranges"] ]
        self.names       = [ v.long_name for v in Vars ]
        self.short_names = [ v.short_name for v in Vars ]
        self.nbins       = options["nbins"]
        self.mcf         = MCF

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

    def get_short_names( self ) :
        return self.short_names

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
