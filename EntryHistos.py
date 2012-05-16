#! /usr/bin/env python
import ROOT as r

from modules import MCChain as MCC
from modules import histogramProcessing as hists

from config import files
from modules import plots

def print_spaces( p, s ) :
    border = "=" * len(s)
    print "%s\n%s\n%s" % (border, s, border )
    for plot in p :
        print plot.name
    

def main( argv=None ) :
    mcfile_list = files.histo_files()
    for mcf in mcfile_list :
        spaces = plots.get_plots()

        # bit of output
        print_spaces( spaces, "Plots to make" )
       
        chain = MCC.MCChain( mcf )
        complete_histos =  hists.calculate_entry_histograms( spaces, chain )

        hists.save_hlist_to_root_file( complete_histos, mcf.FileName, mcf.EntryDirectory )

if __name__ == "__main__":
    main()
