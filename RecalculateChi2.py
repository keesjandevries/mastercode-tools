#! /usr/bin/env python

import sys
sys.path.append( "./modules/" )
sys.path.append( "./config/" )

import file_dict as fd
import recalculate as recalc

from optparse import OptionParser

############################################
def opts():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option( "-o", "--output", action="store", dest="output",
        default="recalc_out.root", 
        help = "name for output file" )
    options,args = parser.parse_args()
    return options, args
############################################

def main( argv=None ) :
    options,args = opts()
    files = fd.recalc_files()
    recalc.go( files, options.output )




if __name__ == "__main__":
    main()
