#! /usr/bin/env python

import sys

from optparse import OptionParser
from config import file_dict as fd
from modules import recalculate as recalc

############################################
def opts():
    parser = OptionParser("usage: %prog [options]")
#    parser.add_option( "-o", "--output", action="store", dest="output",
#                       default="recalc_out.root", help="name for output file" )
    options,args = parser.parse_args()
    return options, args
############################################

def main( argv=None ) :
#    options,args = opts()
    file_dict = fd.recalc_files() :
    for outputfile, opts in file_dict.iteritems() :
        recalc.go( opts["InputFiles"], outputfile )

if __name__ == "__main__":
    main()
