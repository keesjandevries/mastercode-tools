#! /usr/bin/env python
import ROOT as r

from modules.mcchain import MCAnalysisChain
from modules import histogramProcessing

from config import files
from modules import plots

def print_spaces( p, s ) :
    border = "=" * len(s)
    print "%s\n%s\n%s" % (border, s, border )
    for plot in p :
        print plot


def main( argv=None ) :
    mcfile_list = files.histo_files()
    for mcf in mcfile_list :
        spaces = plots.get_plots(mcf)

        # bit of output
        print_spaces( spaces, "Plots to make" )

        chain = MCAnalysisChain( mcf )
        complete_histos =  histogramProcessing.calculate_entry_histograms( spaces, chain )

        histogramProcessing.save_hlist_to_root_file( complete_histos, mcf.FileName, mcf.EntryDirectory )

if __name__ == "__main__":
    main()
