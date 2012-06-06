#! /usr/bin/env python
import ROOT as r

from optparse import OptionParser

from modules import point as pt
from config import files as fd

############################################
def opts():
    parser = OptionParser("usage: %prog [options] [args]")
    parser.add_option( "-b", "--bestfitpoint", action="store_true", dest="bf_mode"  ,
                       default= False , help="print info of best fit point" )
    parser.add_option( "-c", "--coordinates", action="store_true", dest="coor_mode",
                       default= False , help="print info for specified coordinates, e.g. \"m0= 500\" \"m12 = 1000\"" )
    parser.add_option( "-n", "--entrynumber", action="store", dest="entry_nr", type="int",
                       default= -1 , help="print info for entry number " )
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
            vars=pt.get_vars(args)
            n=pt.get_coor_entry(vars,mcf)
            pt.print_info(n,mcf)

        if options.bf_mode :
            print "\nSearch for best it point in ", mcf.FileName
            n=pt.get_best_fit_entry(mcf)
            pt.print_info(n,mcf)

        if options.entry_nr >= 0 :
            n=options.entry_nr
            print "\nSearch entry number %d point in %s" % (n, mcf.FileName)
            pt.print_info(n,mcf)


if __name__ == "__main__":
    main()
