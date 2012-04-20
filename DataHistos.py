#! /usr/bin/env python
from config import plot_list as pl
from config import file_dict as fd
from modules import histogramProcessing as hfuncs

def main( argv=None ) :
    from commands import getoutput 
    domainname = getoutput('hostname -d')
    files = fd.files(domainname)

    for filename, opts  in files.iteritems() :
        plot_vars = pl.get_plots( opts["PredictionIndex"], opts["SpectrumIndex"] )

        plot_hists = hfuncs.get_entry_hist_list( filename, opts, plot_vars )

        hists = { "pval" : [], "chi2" : [], "dchi" : [] }
        hfuncs.fill_all_data_hists( filename, opts, plot_hists, hists )

        for hl in hists.values() :
            hfuncs.save_hlist_to_root_file( hl, filename, opts["DataDirectory"])

if __name__ == "__main__":
    main()
