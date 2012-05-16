#! /usr/bin/env python
import ROOT as r

from modules import MCChain as MCC
from modules import point as pt
#from modules import histogramProcessing as hists

from config import file_dict as fd
#from config import plot_list as pl


    

def main( argv=None ) :
    from sys import argv
    files = fd.point_files()
    # get the 
    vars=pt.getVars(argv[1:])


    for mcf in files :
        print "Searching for ", vars, " in " , mcf.FileName
        n=pt.getEntry(vars,mcf)
        pt.printInfo(n,mcf)


if __name__ == "__main__":
    main()
