#! /usr/bin/env python
import ROOT as r

from modules import MCchain as MCC
from modules import histogramProcessing as hists

from config import file_dict as fd
from config import plot_list as pl

def print_spaces( p, s ) :
    border = "=" * len(s)
    print "%s\n%s\n%s" % (border, s, border )
    for plot in p :
        print plot.name
    

def main( argv=None ) :
    from commands import getoutput 
    domainname = getoutput('hostname -d')
    files = fd.files(domainname)

    # add in our file list 
    for filename, opts  in files.iteritems() :
        plots = pl.get_plots( opts["PredictionIndex"], opts["SpectrumIndex"] )

        # bit of output
        print_spaces( plots, "Plots to make" )
        
        opts.update( InputFiles = [ filename ], Chi2TreeName = [ opts["Chi2TreeName"] ], 
                   ContribTreeName = [ opts["ContribTreeName"] ] )
        chain = MCC.MCchain( opts )
        complete_histos =  hists.calculate_entry_histograms( plots, chain )

        hists.save_hlist_to_root_file( complete_histos, filename, opts["EntryDirectory"] )

if __name__ == "__main__":
    main()
