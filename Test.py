#! /usr/bin/env python
import ROOT as r
from optparse import OptionParser
from modules import tests


############################################
def opts():
    parser = OptionParser("usage: %prog [options] [args]")
    parser.add_option( "-c", "--constraint", action="store", dest="constraint"  ,
                       default=None , help="test a constraint for an input value" )
    parser.add_option( "-l", "--likelihood", action="store", dest="likelihood",
                       default=None , help="print info for specified likelihood" )
    options,args = parser.parse_args()
    return options, args
############################################

    

def main( argv=None ) :
    options, args = opts()  
    
    args = [ eval(a) for a in args ]
    if options.likelihood is not None :
        tests.runLikelihood( options.likelihood, [args] )
    elif options.constraint is not None :
        tests.runConstraint( options.constraint, args )



if __name__ == "__main__":
    main()
