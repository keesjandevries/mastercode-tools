#! /usr/bin/env python
import ROOT as r
import sys

from config import file_dict as fd
from config import plot_list as VarList
from modules import MCchain as MCC
from modules import histogramProcessing as hists


def print_spaces( p, s ) :
    border = "=" * len(s)
    print "%s\n%s\n%s" % (border, s, border )
    for plot in p :
        print plot.xaxis, plot.yaxis
    

def main( argv=None ) :
    files = fd.files()

    # some nice formatted output

    # add in our file list 
    for file in files.keys() :
        spaces = VarList.get_list( files[file]["PredictionIndex"], files[file]["SpectrumIndex"] )

        # bit of output
        print file
        print_spaces( spaces, "Spaces to make" )

        chain = MCC.MCchain(file, files[file])
        complete_histos =  hists.calculate_entry_histograms( spaces, chain )

        hists.save_hlist_to_root_file( complete_histos, file, files[file]["EntryDirectory"] )

if __name__ == "__main__":
    main()
