from math import sqrt
from math import fabs

from copy import deepcopy
from copy import copy

zvalue_functions = { # there might be a better way of doing this... not really sure yet
    None    : lambda o, x : 0,
    "GAUSS" : lambda o, x : fabs(o.limit_value - x)/o.error,
    "UL"    : lambda o, x : fabs(x - o.limit_value)/o.error if x > o.limit_value else 0.,
    "LL"    : lambda o, x : fabs(o.limit_value - x)/o.error if x < o.limit_value else 0.,
}

class Variable(object) :
    """ Variable class to insulte from MCVariable becoming obsolete once we move away from trees!"""
    def __init__( self, short_name, long_name ) :

        self.short_name = short_name
        self.long_name = long_name

    def __str__( self ) :
        return self.short_name

  

class MCVariable(Variable, object) :
    def __init__( self, var, offset_relative_to = None, index_offset = 0 ) :

        assert offset_relative_to in [ "SpectrumIndex", "PredictionIndex", None ], \
            "Unkown offset for Variable position"

        self.__dict__ = var.__dict__.copy()
        self.offset_relative_to = offset_relative_to
        self.index_offset = index_offset

    def __str__( self ) :
        return self.short_name

    def __repr__( self ) :
        r_f = "%s [%s] %0.4f +- %0.4f ( %s + %d )" 
        return  "%s ( %s + %d )"  % (super(MCVariable, self).__repr__(), self.offset_relative_to, self.index_offset )

    def getIndex(self,mcf) :
        offset = getattr( mcf, self.offset_relative_to, None ) if (self.offset_relative_to is not None) else 0
        return ( self.index_offset + offset ) if offset is not None else -1

class Constraint(object ):
    def __init__( self, short_name, constraint_type = None, limit_value = 0, errors = [],info=None ) :
        assert constraint_type in ["GAUSS", "UL", "LL"], \
            "Unknown constraint type specificed"
        assert len(errors) > 0, "No errors provided for constraint"

        self.errors = errors
        sq_errors = [ error**2 for error in errors ]
        self.error = sqrt( sum(sq_errors) )

        self.short_name = short_name # FIXME: assert it is in the base list.. not sure if this is the right place!
        self.constraint_type = constraint_type
        self.limit_value = limit_value
        self.info = info    # We can store where we got the limit from and stuff

    def __str__( self ) :
        return self.short_name

    def __repr__( self ) :
        r_f = "%s                            [%s] %0.4f +- %0.4f" 
        return r_f % ( self.short_name, self.constraint_type, self.limit_value, getattr(self,"error",0.) )

    def getZValue(self, value) :
        return zvalue_functions[self.constraint_type]( self, value )

    def getChi2(self, value) :
        return self.getZValue(value)**2

    def getShortName(self):
        return self.short_name
