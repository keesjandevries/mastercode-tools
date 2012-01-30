#! /usr/bin/env python
import sys
sys.path.append( "./modules/" )

import plot_list as pl
import histogramProcessing as hfuncs
import file_dict as fd

def main( argv=None ) :
    files = fd.files()


    for file in files.keys() :
        spaces = pl.get_list( files[file]["PredictionIndex"], files[file]["SpectrumIndex"] )

        hl = hfuncs.get_hist_list( file, files[file], spaces )

        hists = hfuncs.get_data_hists( file, files[file], hl )
        hfuncs.save_hlist_to_root_file( hists, file, files[file]["DataDirectory"])

if __name__ == "__main__":
    main()
