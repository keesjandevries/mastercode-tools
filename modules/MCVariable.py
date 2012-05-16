from math import sqrt
from math import fabs

from copy import deepcopy

zvalue_functions = { # there might be a better way of doing this... not really sure yet
    None    : lambda o, x : 0,
    "GAUSS" : lambda o, x : fabs(o.limit_value - x)/o.error,
    "UL"    : lambda o, x : fabs(x - o.limit_value)/o.error if x > o.limit_value else 0.,
    "LL"    : lambda o, x : fabs(o.limit_value - x)/o.error if x < o.limit_value else 0.,
}

class Variable() :
    """ Variable class to insulte from MCVariable becoming obsolete once we move away from trees!"""
    def __init__( self, short_name, long_name, constraint_type = None, limit_value = 0, errors = [] ) :
        if constraint_type is not None :
            assert constraint_type in ["GAUSS", "UL", "LL"], \
                "Unknown constraint type specificed"
            assert len(errors) > 0, "No errors provided for constraint"

            self.errors = errors
            sq_errors = [ error**2 for error in errors ]
            self.error = sqrt( sum(sq_errors) )

        for attr in [ "short_name", "long_name", "constraint_type", "limit_value" ] :
            setattr( self, attr, eval(attr) )

    def getZValue(self, value) :
        return zvalue_function[self.constraint_type]( self, value )

    def getChi2(self, value) :
        return self.getZValue(value)**2

class MCVariable(Variable) :
    def __init__( self, var, offset_relative_to = None, index_offset = 0 ) :

        assert offset_relative_to in [ "SpectrumIndex", "PredictionIndex", None ], \
            "Unkown offset for Variable position"

        self = deepcopy(var) #hopefully provides us with the right functionality
        for attr in [ "offset_relative_to", "index_offset" ] :
            setattr( "self.%s" % attr, eval(attr) )

    def getIndex(self,mcf) :
        offset = getattr( mcf, self.offset_relative_to, None ) if offset_relative_to is not None else 0
        return ( self.index_offset + offset ) if offset is not None else -1
