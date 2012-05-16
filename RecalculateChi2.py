#! /usr/bin/env python

import sys

from optparse import OptionParser
from config import files as fd
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
    file_collection = fd.recalc_files()
    recalc.go( file_collection )

if __name__ == "__main__":
    main()
