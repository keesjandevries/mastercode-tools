#! /usr/bin/env python
from config import plot_list as pl
from config import file_dict as fd
from modules import histogramProcessing as hfuncs

def main( argv=None ) :
    files = fd.files()

    for file in files.keys() :
        single_vars, spaces = pl.get_plots( files[file]["PredictionIndex"], files[file]["SpectrumIndex"] )

        space_hists = hfuncs.get_entry_hist_list( file, files[file], spaces )
        single_hists = hfuncs.get_entry_hist_list( file, files[file], single_vars )

        hists = { "pval" : [], "chi2" : [], "dchi" : [] }

        hfuncs.fill_all_data_hists( file, files[file], space_hists, hists )
        #hfuncs.fill_all_data_hists_1d( file, files[file], singel_hists, hists )

        for hl in hists.values() :
            hfuncs.save_hlist_to_root_file( space_hists, file, files[file]["DataDirectory"])

if __name__ == "__main__":
    main()
