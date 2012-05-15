from math import sqrt
from math import fabs

class MCVariable() :
    def __init__( self, short_name, long_name, constraint_type, limit_value, 
                  errors = [], offset_relative_to = None, mc_tree_offset = 0, 
                  plot_range = (None,None) ) :
        


        assert offset_relative_to in [ "SpectrumIndex", "PredictionIndex", None ], \
            "Unkown offset for Variable position" 

        if constraint_type is not None : 
            assert constraint_type in ["GAUSS", "UL", "LL"], \
                "Unknown constraint type specificed"
            assert len(errors) > 0, "No errors provided for constraint"

            self.errors = errors
            sq_errors = [ error**2 for error in errors ]
            self.error sqrt( sum(sq_errors) )

            self.zvalue_function = { # there might be a better way of doing this... not really sure yet
                "GAUSS" : lambda x : fabs(self.limit_value - x)/self.error
                "UL"    : lambda x : fabs(x - self.limit_value)/self.error if x > self.limit_value else 0. 
                "LL"    : lambda x : fabs(self.limit_value - x)/self.error if x < self.limit_value else 0. 
            }

        for attr in [ "short_name", "long_name", "constraint_type", 
                      "limit_value", "offset_relative_to", "mc_tree_offset",
                      "plot_range" ] :
            setattr( "self.%s" % attr, eval(attr) )

    def getIndex(self,mcf) :
        offset = getattr( mcf, self.offset_relative_to ) if offset_relative_to is not None else 0
        return self.mc_tree_offset + offset

    def getZValue(self, value) :
        return self.zvalue_function( value )

    def getChi2(self, value) :
        return self.getZValue(value)**2
