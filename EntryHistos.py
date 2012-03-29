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
        if hasattr(plot,"xaxis") :
            print plot.xaxis, plot.yaxis
        else :
            print plot.name
    

def main( argv=None ) :
    files = fd.files()

    # some nice formatted output

    # add in our file list 
    for file in files.keys() :
        single_vars, spaces = pl.get_plots( files[file]["PredictionIndex"], files[file]["SpectrumIndex"] )

        # bit of output
        print_spaces( spaces, "Spaces to make" )
        print_spaces( single_vars, "1d plots to make" )

        chain = MCC.MCchain(file, files[file])
        complete_histos =  hists.calculate_entry_histograms( spaces, single_vars, chain )

        hists.save_hlist_to_root_file( complete_histos, file, files[file]["EntryDirectory"] )

if __name__ == "__main__":
    main()
