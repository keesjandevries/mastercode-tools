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
    files = fd.histo_files()
    for mcf in files :
        plots = pl.get_plots( mcf.PredictionIndex, mcf.SpectrumIndex )

        # bit of output
        print_spaces( plots, "Plots to make" )
       
        chain = MCC.MCchain( mcf )
        complete_histos =  hists.calculate_entry_histograms( plots, chain )

        hists.save_hlist_to_root_file( complete_histos, mcf.FileName, mcf.EntryDirectory )

if __name__ == "__main__":
    main()
