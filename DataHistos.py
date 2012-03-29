#! /usr/bin/env python
from config import plot_list as pl
from config import file_dict as fd
from modules import histogramProcessing as hfuncs

def main( argv=None ) :
    files = fd.files()

    for file in files.keys() :
        single_vars, spaces = pl.get_plots( files[file]["PredictionIndex"], files[file]["SpectrumIndex"] )

        hl = hfuncs.get_entry_hist_list( file, files[file], spaces )

        hists = { "pval" : [], "chi2" : [], "dchi" : [] }

        hfuncs.fill_all_data_hists( file, files[file], hl, hists )
        # hists is now a list of list of histograms
        hfuncs.set_hist_properties(hists)

        for hl in hists.values() :
            hfuncs.save_hlist_to_root_file( hl, file, files[file]["DataDirectory"])

if __name__ == "__main__":
    main()
