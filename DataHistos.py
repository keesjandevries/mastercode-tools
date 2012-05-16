#! /usr/bin/env python
from modules import plots
from config import files as fd
from modules import histogramProcessing as hfuncs

def main( argv=None ) :
    files = fd.histo_files()

    for mcf in files :
        plot_vars = plots.get_plots( mcf )
        contrib_vars = plots.get_contribs( mcf )

        plot_hists = hfuncs.get_entry_hist_list( mcf, plot_vars )

        hists = { "pval" : [], "chi2" : [], "dchi" : [] }

        chists = { }
        for c in contrib_vars : chists[c.short_name] = [] #initialize

        hfuncs.fill_all_data_hists( mcf, plot_hists, contrib_vars, hists, chists )

        for hl in hists.values() :
            hfuncs.save_hlist_to_root_file( hl, mcf.FileName, mcf.DataDirectory)
        for cl in chists.values() :
            hfuncs.save_hlist_to_root_file( cl, mcf.FileName, mcf.DataDirectory)

if __name__ == "__main__":
    main()
