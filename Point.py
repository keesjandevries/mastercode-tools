#! /usr/bin/env python
import ROOT as r

from optparse import OptionParser

from modules import MCChain as MCC
from modules import point as pt

from config import files as fd

############################################
def opts():
    parser = OptionParser("usage: %prog [options] [args]")
    parser.add_option( "-b", "--bestfitpoint", action="store_true", dest="bf_mode"  ,
                       default= False , help="print info of best fit point" )
    parser.add_option( "-c", "--coordinates", action="store_true", dest="coor_mode",
                       default= False , help="print info for specified coordinates, e.g. \"m0= 500\" \"m12 = 1000\"" )
    options,args = parser.parse_args()
    return options, args
############################################

    

def main( argv=None ) :
    # retrieve file
    files = fd.point_files()

    #Get options
    options, args = opts()  
    
    for mcf in files:
        if options.coor_mode :
            print "\nSearch for coordinates", args, " in " , mcf.FileName
            vars=pt.getVars(args)
            n=pt.getCoorEntry(vars,mcf)
            pt.printInfo(n,mcf)

        if options.bf_mode :
            print "\nSearch for best it point in ", mcf.FileName
            n=pt.getBfEntry(mcf)
            pt.printInfo(n,mcf)


if __name__ == "__main__":
    main()
