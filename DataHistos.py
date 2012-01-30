#! /usr/bin/env python
import sys
sys.path.append( "./modules/" )
sys.path.append( "./config/" )

import plot_list as pl
import histogramProcessing as hfuncs
import file_dict as fd

def main( argv=None ) :
    files = fd.files()


    for file in files.keys() :
        spaces = pl.get_list( files[file]["PredictionIndex"], files[file]["SpectrumIndex"] )

        hl = hfuncs.get_entry_hist_list( file, files[file], spaces )

        hists = hfuncs.make_all_data_hists( file, files[file], hl )
        # hists is now a list of list of histograms
        hfuncs.set_hist_properties("chi2",hists[0])
        hfuncs.set_hist_properties("pval",hists[1])
        hfuncs.set_hist_properties("dchi",hists[2])

        hfuncs.save_hlist_to_root_file( hists[0], file, files[file]["DataDirectory"])
        hfuncs.save_hlist_to_root_file( hists[1], file, files[file]["DataDirectory"])
        hfuncs.save_hlist_to_root_file( hists[2], file, files[file]["DataDirectory"])

if __name__ == "__main__":
    main()
