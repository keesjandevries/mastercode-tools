#! /usr/bin/env python
import ROOT as r

from optparse import OptionParser
from modules import MCchain as MCC
from modules import point as pt
#from modules import histogramProcessing as hists

from config import file_dict as fd
#from config import plot_list as pl

############################################
def opts():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option( "-c", "--coordinates", action="store_true", dest="use_coor",
                       default= False , help="specify coordinates, e.g. \"m0= 500\" \"m12 = 1000\"" )
    options,args = parser.parse_args()
    return options, args
############################################

    

def main( argv=None ) :
    # retrieve file
    mcf = fd.point_files()[0]

    #Get options
    options, args = opts()  

    if options.use_coor :
        vars=pt.getVars(args)
        print "Searching for ", vars, " in " , mcf.FileName
        n=pt.getCoorEntry(vars,mcf)
        pt.printInfo(n,mcf)


if __name__ == "__main__":
    main()
