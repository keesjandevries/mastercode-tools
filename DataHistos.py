#! /usr/bin/env python
from config import plot_list as pl
from config import file_dict as fd
from modules import histogramProcessing as hfuncs

def main( argv=None ) :
    files = fd.histo_files()

    for mcf in files :
        plot_vars = pl.get_plots( mcf.PredictionIndex, mcf.SpectrumIndex )

        plot_hists = hfuncs.get_entry_hist_list( mcf, plot_vars )

        hists = { "pval" : [], "chi2" : [], "dchi" : [], "contrib" : [] }
        hfuncs.fill_all_data_hists( mcf, plot_hists, hists )

        for hl in hists.values() :
            hfuncs.save_hlist_to_root_file( hl, mcf.FileName, mcf.DataDirectory)

if __name__ == "__main__":
    main()
